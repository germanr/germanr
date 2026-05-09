"""Convert a paper .tex file to clean markdown for LLM consumption.

Pipeline:
1. pandoc .tex -> .md (preserving citations as `[@key]` syntax)
2. Parse .bib to build {key: (last_names, year)} index
3. Replace `[@key, @key2]` -> `(Last1 Year1; Last2 Year2)` (parenthetical)
4. Replace `@key` -> `Last1 et al. (Year)` (narrative)
5. Strip pandoc cross-reference attributes ({#sec:foo}, [reference-type=ref])
6. Light cleanup: collapse extra blank lines

Usage:
    python _tex2md.py <tex_path> <bib_path|-> <output.md>
"""
import sys
import re
import subprocess
from pathlib import Path


def parse_bib(bib_path: Path) -> dict:
    """Return {key: (display_authors, year)} from a BibTeX file."""
    if not bib_path or not bib_path.exists():
        return {}
    text = bib_path.read_text(encoding='utf-8', errors='replace')
    index = {}
    # Find each entry by scanning for "@type{key,..." then balance braces.
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        kind = m.group(1).lower()
        key = m.group(2).strip()
        if kind in {'comment', 'string', 'preamble'}:
            continue
        # find matching closing brace from the opening at the entry-level
        opening = text.find('{', m.start())
        if opening < 0:
            continue
        depth = 0
        end = opening
        for i in range(opening, len(text)):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i
                    break
        body = text[m.end():end]
        author = _field(body, 'author')
        editor = _field(body, 'editor')
        year = _field(body, 'year') or _field(body, 'date') or ''
        ym = re.match(r'\d{4}', year)
        year = ym.group() if ym else year[:4]
        names = _short_authors(author or editor or '')
        index[key] = (names, year)
    return index


def _field(body: str, name: str) -> str:
    """Extract a BibTeX field value, handling braces."""
    m = re.search(rf'\b{name}\s*=\s*', body, re.IGNORECASE)
    if not m:
        return ''
    rest = body[m.end():]
    # value is enclosed in {...} or "..." possibly nested
    if rest.startswith('{'):
        depth = 0
        for i, c in enumerate(rest):
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return rest[1:i]
    elif rest.startswith('"'):
        m2 = re.match(r'"([^"]*)"', rest)
        if m2:
            return m2.group(1)
    else:
        m2 = re.match(r'(\S+?)(?:\s*[,}]|\s*$)', rest)
        if m2:
            return m2.group(1)
    return ''


def _clean_name(s: str) -> str:
    """Strip LaTeX commands, braces; convert basic accents."""
    # accent commands with letter argument
    s = re.sub(r'\\[\'\"^`~][\{]?([A-Za-z])[\}]?', _accent, s)
    # \v{X} caron, \u{X} breve, \r{X} ring, \c{X} cedilla, \H{X} hungarian
    s = re.sub(r'\\v\s*\{?(\w)\}?', lambda m: _CARON.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\\u\s*\{?(\w)\}?', lambda m: _BREVE.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\\c\s*\{?(\w)\}?', lambda m: _CEDILLA.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\\H\s*\{?(\w)\}?', lambda m: _HUNGUMLAUT.get(m.group(1), m.group(1)), s)
    # \i and \j (dotless) used inside accent commands like \'\i, \'{\i}, \'\j
    s = re.sub(r"\\'\s*\\i\b", 'í', s)
    s = re.sub(r"\\'\s*\{\\i\}", 'í', s)
    s = re.sub(r'\\"\s*\\i\b', 'ï', s)
    s = re.sub(r'\\([oO])\b', lambda m: 'ø' if m.group(1) == 'o' else 'Ø', s)
    s = re.sub(r'\{\\(aa|AA)\}', lambda m: 'å' if m.group(1) == 'aa' else 'Å', s)
    s = re.sub(r'\\(aa|AA)\b', lambda m: 'å' if m.group(1) == 'aa' else 'Å', s)
    s = re.sub(r'\\([lL])\b', lambda m: 'ł' if m.group(1) == 'l' else 'Ł', s)
    s = re.sub(r'\\(ss)\b', 'ß', s)
    # strip commands BEFORE braces, with optional braced argument
    s = re.sub(r'\\[A-Za-z]+\b', '', s)
    s = s.replace('{', '').replace('}', '')
    return s.strip()


_CARON = {
    'c': 'č', 'C': 'Č', 's': 'š', 'S': 'Š', 'z': 'ž', 'Z': 'Ž',
    'n': 'ň', 'N': 'Ň', 'r': 'ř', 'R': 'Ř', 't': 'ť', 'T': 'Ť',
    'd': 'ď', 'D': 'Ď', 'e': 'ě', 'E': 'Ě',
}
_BREVE = {'a': 'ă', 'A': 'Ă', 'g': 'ğ', 'G': 'Ğ', 'u': 'ŭ', 'U': 'Ŭ'}
_CEDILLA = {'c': 'ç', 'C': 'Ç', 's': 'ş', 'S': 'Ş', 't': 'ţ', 'T': 'Ţ'}
_HUNGUMLAUT = {'o': 'ő', 'O': 'Ő', 'u': 'ű', 'U': 'Ű'}


_ACCENT_MAP = {
    "'a": 'á', "'e": 'é', "'i": 'í', "'o": 'ó', "'u": 'ú', "'n": 'ń',
    '"a': 'ä', '"e': 'ë', '"i': 'ï', '"o': 'ö', '"u': 'ü',
    '^a': 'â', '^e': 'ê', '^i': 'î', '^o': 'ô', '^u': 'û',
    '`a': 'à', '`e': 'è', '`i': 'ì', '`o': 'ò', '`u': 'ù',
    '~a': 'ã', '~n': 'ñ', '~o': 'õ',
    "'A": 'Á', "'E": 'É', "'I": 'Í', "'O": 'Ó', "'U": 'Ú',
    '"A': 'Ä', '"O': 'Ö', '"U': 'Ü',
}


def _accent(m: re.Match) -> str:
    full = m.group(0)
    # extract the accent kind and letter
    cmd = full[1]
    letter = m.group(1)
    return _ACCENT_MAP.get(cmd + letter, letter)


def _short_authors(author_field: str) -> str:
    """Return short citation form: 'Smith', 'Smith and Jones', or 'Smith et al.'"""
    if not author_field:
        return ''
    parts = _split_authors(author_field)
    last_names = []
    for p in parts:
        last_names.append(_extract_last_name(p))
    if not last_names:
        return ''
    if len(last_names) == 1:
        return last_names[0]
    if len(last_names) == 2:
        return f'{last_names[0]} and {last_names[1]}'
    if len(last_names) == 3:
        return f'{last_names[0]}, {last_names[1]}, and {last_names[2]}'
    return f'{last_names[0]} et al.'


def _split_authors(s: str) -> list:
    """Split BibTeX author field on ' and ' respecting brace depth."""
    parts = []
    cur = ''
    depth = 0
    i = 0
    while i < len(s):
        if s[i] == '{':
            depth += 1
            cur += s[i]
        elif s[i] == '}':
            depth -= 1
            cur += s[i]
        elif depth == 0 and s[i:i+5] == ' and ':
            parts.append(cur.strip())
            cur = ''
            i += 5
            continue
        else:
            cur += s[i]
        i += 1
    if cur.strip():
        parts.append(cur.strip())
    return parts


def _extract_last_name(p: str) -> str:
    """Extract the last (family) name from a BibTeX author entry.

    Handles:
    - "{{Cornell University}}"  -> "Cornell University"
    - "Last, First"             -> "Last"
    - "First Middle Last"       -> "Last"
    - "First {de la Last}"      -> "de la Last"
    """
    p = p.strip()
    # Corporate-style double-braced name: take entire braced content
    m = re.match(r'^\{\{(.+)\}\}$', p)
    if m:
        return _clean_name(m.group(1))
    # If "Last, First", take portion before comma
    if ',' in p:
        last = p.split(',')[0].strip()
        # If still braced, strip
        m = re.match(r'^\{(.+)\}$', last)
        if m:
            last = m.group(1)
        return _clean_name(last)
    # "First Middle Last" — but if there's a {Group} at end, use that
    # tokenize respecting braces
    tokens = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}|\S+', p)
    if not tokens:
        return _clean_name(p)
    last_token = tokens[-1]
    # If it's braced, use content
    m = re.match(r'^\{(.+)\}$', last_token)
    if m:
        last = m.group(1)
    else:
        last = last_token
    return _clean_name(last)


# ---- citation replacement ----

def replace_citations(text: str, idx: dict) -> str:
    """Replace LaTeX citation commands with rendered (Author Year) text.

    Handles \\citep, \\citet, \\cite, \\citeauthor, \\citealp, \\citealt,
    \\citeyear, \\citeyearpar. Run on .tex source BEFORE pandoc.
    """

    def lookup(key: str) -> tuple:
        k = key.lstrip('@').strip()
        return idx.get(k, (k, ''))

    def render_parenthetical(keys_str, prefix='', suffix=''):
        keys = [k.strip() for k in keys_str.split(',') if k.strip()]
        parts = []
        for k in keys:
            authors, year = lookup(k)
            parts.append(f'{authors}, {year}' if year else authors)
        joined = '; '.join(parts)
        body = joined
        if prefix:
            body = f'{prefix} {body}'
        if suffix:
            body = f'{body}, {suffix}'
        return f'({body})'

    def render_narrative(keys_str):
        keys = [k.strip() for k in keys_str.split(',') if k.strip()]
        parts = []
        for k in keys:
            authors, year = lookup(k)
            parts.append(f'{authors} ({year})' if year else authors)
        if len(parts) == 1:
            return parts[0]
        if len(parts) == 2:
            return f'{parts[0]} and {parts[1]}'
        return '; '.join(parts)

    def render_authors_only(keys_str):
        keys = [k.strip() for k in keys_str.split(',') if k.strip()]
        parts = [lookup(k)[0] for k in keys]
        if len(parts) == 1:
            return parts[0]
        if len(parts) == 2:
            return f'{parts[0]} and {parts[1]}'
        return '; '.join(parts)

    def render_year_only(keys_str):
        keys = [k.strip() for k in keys_str.split(',') if k.strip()]
        parts = [lookup(k)[1] for k in keys]
        return ', '.join(parts)

    def render_alp(keys_str, prefix='', suffix=''):
        # \citealp: "Author, Year" without parens
        keys = [k.strip() for k in keys_str.split(',') if k.strip()]
        parts = []
        for k in keys:
            authors, year = lookup(k)
            parts.append(f'{authors}, {year}' if year else authors)
        joined = '; '.join(parts)
        body = joined
        if prefix:
            body = f'{prefix} {body}'
        if suffix:
            body = f'{body}, {suffix}'
        return body

    # Pattern: \cmd[opt1][opt2]{keys} OR \cmd{keys}
    # Helpers below all use this same opt-arg pattern.
    optargs = r'(?:\[([^\]]*)\])?(?:\[([^\]]*)\])?'

    # \citep[prefix][suffix]{keys}
    text = re.sub(
        r'\\citep' + optargs + r'\{([^}]+)\}',
        lambda m: render_parenthetical(
            m.group(3), (m.group(1) or '').strip(),
            (m.group(2) or '').strip()
        ),
        text,
    )

    # \citeyearpar -> (Year)
    text = re.sub(
        r'\\citeyearpar' + optargs + r'\{([^}]+)\}',
        lambda m: f'({render_year_only(m.group(3))})',
        text,
    )

    # \citeyear -> Year
    text = re.sub(
        r'\\citeyear' + optargs + r'\{([^}]+)\}',
        lambda m: render_year_only(m.group(3)),
        text,
    )

    # \citeauthor -> Author (no year)
    text = re.sub(
        r'\\citeauthor' + optargs + r'\{([^}]+)\}',
        lambda m: render_authors_only(m.group(3)),
        text,
    )

    # \citet[prefix][suffix]{keys} -> Author (Year)
    text = re.sub(
        r'\\citet' + optargs + r'\{([^}]+)\}',
        lambda m: render_narrative(m.group(3)),
        text,
    )

    # \citealp / \citealt -> "Author Year" no parens
    text = re.sub(
        r'\\citealp' + optargs + r'\{([^}]+)\}',
        lambda m: render_alp(
            m.group(3), (m.group(1) or '').strip(),
            (m.group(2) or '').strip()
        ),
        text,
    )
    text = re.sub(
        r'\\citealt' + optargs + r'\{([^}]+)\}',
        lambda m: render_alp(
            m.group(3), (m.group(1) or '').strip(),
            (m.group(2) or '').strip()
        ),
        text,
    )

    # \cite{keys} -> narrative form (most papers use this like \citet)
    text = re.sub(
        r'\\cite' + optargs + r'\{([^}]+)\}',
        lambda m: render_narrative(m.group(3)),
        text,
    )

    return text


def replace_pandoc_citations(md: str, idx: dict) -> str:
    """Resolve any pandoc-style [@key] or @key citations that pandoc emitted."""

    def lookup(key: str) -> tuple:
        k = key.lstrip('@').strip()
        return idx.get(k, (k, ''))

    def render_pandoc_bracket(m):
        body = m.group(1)
        cites = [c.strip() for c in body.split(';')]
        rendered = []
        prefix_text = ''
        for cite in cites:
            mm = re.match(r'^(.*?)@([A-Za-z0-9_.\-:]+)(.*)$', cite)
            if not mm:
                rendered.append(cite)
                continue
            pre = mm.group(1).strip()
            key = mm.group(2)
            suf = mm.group(3).strip().rstrip(',').strip()
            authors, year = lookup(key)
            piece = f'{authors}, {year}' if year else authors
            if pre and not prefix_text:
                prefix_text = pre
            if suf:
                piece = f'{piece}, {suf}'
            rendered.append(piece)
        joined = '; '.join(rendered)
        if prefix_text:
            return f'({prefix_text} {joined})'
        return f'({joined})'

    # match [text@key text] but NOT followed by `(` (which would be a markdown link)
    md = re.sub(r'\[([^\[\]]*?@[A-Za-z0-9_.\-:]+[^\[\]]*?)\](?!\()', render_pandoc_bracket, md)
    md = re.sub(
        r'(?<![A-Za-z0-9])@([A-Za-z][A-Za-z0-9_.\-:]+)',
        lambda m: (
            f'{lookup(m.group(1))[0]} ({lookup(m.group(1))[1]})'
            if lookup(m.group(1))[1] else m.group(0)
        ),
        md
    )
    return md


# ---- pandoc cross-ref cleanup ----

def strip_pandoc_refs(md: str) -> str:
    """Remove pandoc cross-reference attributes from headings and links."""
    # Heading: "# Title {#sec:foo}" -> "# Title"
    md = re.sub(r'\s*\{#[^}]+\}\s*$', '', md, flags=re.MULTILINE)
    # Link with reference attributes: [text](#anchor){reference-type="ref" reference="x"}
    md = re.sub(
        r'\[([^\[\]]+)\]\(#[^)]+\)\{reference-type="[^"]+" reference="[^"]+"\}',
        r'\1', md
    )
    md = re.sub(
        r"\[([^\[\]]+)\]\(#[^)]+\)\{reference-type='[^']+' reference='[^']+'\}",
        r'\1', md
    )
    md = re.sub(r'\{reference-type="[^"]*"\s+reference="[^"]*"\}', '', md)
    md = re.sub(r'\\\[([^\[\]]+?)\\\]', r'\1', md)
    # Plain Markdown link to anchor: [Table tab:foo](#tab:foo) -> Table tab:foo
    md = re.sub(r'\[([^\[\]]+)\]\(#[^\)]+\)', r'\1', md)
    return md


# ---- final cleanup ----

def cleanup(md: str) -> str:
    md = strip_pandoc_refs(md)
    # pandoc emits "<!-- -->" between adjacent inline elements (e.g., $-$<!-- -->0.5)
    md = re.sub(r'<!--\s*-->', '', md)
    md = re.sub(r'<!–\s*–>', '', md)  # variant with en-dashes
    # span/anchor leftovers from pandoc on labeled headings/captions:
    # <span id="sec:foo" label="sec:foo"></span>
    md = re.sub(
        r'\s*<span\s+(?:id|label)="[^"]*"(?:\s+(?:id|label)="[^"]*")*\s*></span>',
        '', md
    )
    md = re.sub(r"\s*<span\s+(?:id|label)='[^']*'(?:\s+(?:id|label)='[^']*')*\s*></span>", '', md)
    # esttab significance-star artifacts that pandoc emits as math + escaped stars
    # e.g. "\^\*\*\*$^{***}$" or "&\^\*\*\*" -> "***"
    md = re.sub(r'\\\^(\*+)\$\^\{\*+\}\$', r'\1', md)
    md = re.sub(r'\\\^(\*+)', r'\1', md)
    # stray \notag and trailing \\ in equation-aligned blocks
    md = re.sub(r'\\notag\s*\\\\?', '', md)
    md = re.sub(r'\\nonumber\s*\\\\?', '', md)
    # subsubsection that pandoc botched into "<dims> Title"
    # pattern: line starts with a sequence of LaTeX dimensions then heading text
    md = re.sub(
        r'^(?:[+-]?\d*\.?\d+(?:ex|em|pt|in|cm|mm)\s*)+(.+)$',
        r'### \1', md, flags=re.MULTILINE
    )
    # math-mode dollar amounts: $\$6$ -> $6
    md = re.sub(r'\$\\\$([0-9]+(?:\.[0-9]+)?)\$', r'\$\1', md)
    # remaining LaTeX dollar escape -> literal $
    md = re.sub(r'\\\$', '$', md)
    # LaTeX protected space "\ " -> " "
    md = re.sub(r'\\ ', ' ', md)
    # tilde-protected space "U.S.~samples" -> "U.S. samples"
    # (pandoc usually handles ~ but just in case)
    md = re.sub(r'(\w)~(\w)', r'\1 \2', md)
    # \label{...} inside math
    md = re.sub(r'\\label\{[^}]+\}\s*', '', md)
    # em/en dashes — applied per-line, skipping pandoc grid/pipe table rules
    # (lines that look like table separators must keep their literal `-` chars)
    def _dash_line(line: str) -> str:
        s = line.lstrip()
        if s.startswith(('+-', '+:', '|-', '|:', '|=', ':-', '=-')) or set(s) <= set('+-=:| \t'):
            return line
        return line.replace('---', '—').replace('--', '–')
    md = '\n'.join(_dash_line(ln) for ln in md.split('\n'))
    # collapse 3+ newlines to 2
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.replace('\t', '    ')
    return md.strip() + '\n'


# ---- title/abstract extraction ----

def _balanced_braces(s: str, start: int) -> str:
    """Return content of {...} starting at s[start]=='{', with proper nesting."""
    if start >= len(s) or s[start] != '{':
        return ''
    depth = 0
    for i in range(start, len(s)):
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return s[start+1:i]
    return ''


def extract_metadata(tex: str) -> dict:
    """Extract title, authors, abstract from LaTeX source."""
    tex_nc = _strip_tex_comments(tex)

    title = ''
    m = re.search(r'\\title\s*\{', tex_nc)
    if m:
        raw = _balanced_braces(tex_nc, m.end() - 1)
        raw = _strip_balanced(raw, ['thanks', 'footnote'])
        raw = _normalize_tex_layout(raw)
        title = _strip_tex(raw).strip()

    authors = []
    m = re.search(r'\\author\s*\{', tex_nc)
    if m:
        raw = _balanced_braces(tex_nc, m.end() - 1)
        raw = _strip_balanced(raw, ['thanks', 'footnote'])
        raw = _normalize_tex_layout(raw)
        parts = re.split(r'\\and\b|\\\\', raw)
        for p in parts:
            p = _strip_tex(p).strip().strip('*').strip()
            if p and len(p) > 1:
                authors.append(p)

    abstract = ''
    m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex_nc, re.DOTALL)
    if m:
        raw = _normalize_tex_layout(m.group(1))
        abstract = _strip_tex(raw).strip()

    date = ''
    has_date_cmd = False
    m = re.search(r'\\date\s*\{', tex_nc)
    if m:
        has_date_cmd = True
        raw_braces = _balanced_braces(tex_nc, m.end() - 1)
        # Detect macros that should resolve to current month/year before stripping
        needs_today = bool(re.search(
            r'\\today\b|\\MONTH\b|\\the\s*\\year\b|\\year\b|\\month\b',
            raw_braces,
        ))
        raw = _normalize_tex_layout(raw_braces)
        date = _strip_tex(raw).strip()
        if date.lower() in {'', 'today'}:
            date = ''
        if not date and needs_today:
            from datetime import date as _date
            date = _date.today().strftime('%B %Y')
    # No explicit \date{}: if \maketitle is called, LaTeX defaults to \today.
    if not date and not has_date_cmd and re.search(r'\\maketitle\b', tex_nc):
        from datetime import date as _date
        date = _date.today().strftime('%B %Y')

    return {'title': title, 'authors': authors, 'date': date, 'abstract': abstract}


def _strip_balanced(s: str, command_names: list) -> str:
    """Remove \\name{...} commands with arbitrarily nested braces."""
    out = []
    i = 0
    while i < len(s):
        matched = False
        for name in command_names:
            tok = '\\' + name
            if s[i:i+len(tok)+1] == tok + '{' or (
                s[i:i+len(tok)] == tok
                and i + len(tok) < len(s)
                and s[i + len(tok)] == '{'
            ):
                # find balanced }
                start = i + len(tok)
                content = _balanced_braces(s, start)
                # advance past the entire \name{...}
                i = start + len(content) + 2
                matched = True
                break
            # also handle \name*{...} variant
            tok_star = '\\' + name + '*'
            if s[i:i+len(tok_star)] == tok_star and (
                i + len(tok_star) < len(s) and s[i + len(tok_star)] == '{'
            ):
                start = i + len(tok_star)
                content = _balanced_braces(s, start)
                i = start + len(content) + 2
                matched = True
                break
        if not matched:
            out.append(s[i])
            i += 1
    return ''.join(out)


def _normalize_tex_layout(s: str) -> str:
    """Normalize layout-only LaTeX in title/author for clean display."""
    # discardable layout commands with arg: \vspace{...}, \hspace{...}, \setlength{...}{...}
    s = _strip_balanced(s, ['vspace', 'hspace', 'setlength', 'setstretch',
                            'pdfbookmark', 'phantomsection'])
    # style/font commands wrap content (one-level): \normalsize{X} -> X
    s = re.sub(
        r'\\(?:normalsize|small|tiny|large|Large|huge|Huge|footnotesize|scriptsize|textbf|textit|textrm|textsf|texttt|textsc|emph)\s*\{([^{}]*)\}',
        r'\1', s
    )
    # bare commands w/o args
    s = re.sub(r'\\(?:today|MONTH|the|year|noindent|maketitle|sl|it|bf|tt|sc|rm)\b', '', s)
    return s


def _strip_tex_comments(tex: str) -> str:
    """Strip LaTeX line comments (%...) but keep escaped \\%."""
    out_lines = []
    for line in tex.splitlines():
        # find first unescaped %
        i = 0
        result = ''
        while i < len(line):
            if line[i] == '\\' and i + 1 < len(line) and line[i+1] == '%':
                result += '\\%'
                i += 2
            elif line[i] == '%':
                break
            else:
                result += line[i]
                i += 1
        out_lines.append(result)
    return '\n'.join(out_lines)


def _strip_tex(s: str) -> str:
    """Light TeX-to-text cleanup for metadata."""
    # strip environment markers: \begin{x} ... \end{x} -> ... (just remove begin/end)
    s = re.sub(r'\\begin\{[^}]+\}', '', s)
    s = re.sub(r'\\end\{[^}]+\}', '', s)
    # \href{url}{text} -> text
    s = re.sub(r'\\href\s*\{[^}]*\}\s*\{([^}]*)\}', r'\1', s)
    # specific replacements before stripping commands
    s = s.replace('---', '—').replace('--', '–')
    s = re.sub(r"``", '"', s)
    s = re.sub(r"''", '"', s)
    s = re.sub(r'\\noindent\b\s*', '', s)
    s = re.sub(r'\\\\(?:\[[^\]]*\])?', ' ', s)  # LaTeX line break
    s = re.sub(r'\\ ', ' ', s)  # protected space
    s = re.sub(r'(\w)~(\w)', r'\1 \2', s)  # tilde-space
    # accents and remaining commands
    s = _clean_name(s)
    # collapse newlines/whitespace
    s = re.sub(r'\s+', ' ', s)
    return s


def build_header(meta: dict) -> str:
    parts = []
    if meta.get('title'):
        parts.append(f'# {meta["title"]}')
    byline = []
    if meta.get('authors'):
        byline.append('*' + ', '.join(meta['authors']) + '*')
    if meta.get('date'):
        byline.append(f'*{meta["date"]}*')
    if byline:
        parts.append('  \n'.join(byline))
    if meta.get('abstract'):
        parts.append('**Abstract.** ' + meta['abstract'])
    return '\n\n'.join(parts) + ('\n\n' if parts else '')


# ---- main ----

def expand_inputs(tex_path: Path, max_depth: int = 5) -> str:
    """Recursively inline-expand \\input{...}, \\include{...}, and
    \\ExpandableInput{...} files. Strips line comments first so commented-out
    \\input directives are not expanded.
    """
    text = tex_path.read_text(encoding='utf-8', errors='replace')
    base = tex_path.parent
    return _expand_inputs_text(text, base, max_depth)


def _strip_line_comments(tex: str) -> str:
    """Remove % line comments (preserving \\%)."""
    out = []
    for line in tex.splitlines():
        i = 0
        result = ''
        while i < len(line):
            if line[i] == '\\' and i + 1 < len(line) and line[i+1] == '%':
                result += '\\%'
                i += 2
            elif line[i] == '%':
                break
            else:
                result += line[i]
                i += 1
        out.append(result)
    return '\n'.join(out)


def _expand_inputs_text(text: str, base: Path, depth: int) -> str:
    if depth <= 0:
        return text
    # strip comments BEFORE expanding so commented-out \input{} stays out
    text = _strip_line_comments(text)

    def repl(m):
        name = m.group(2).strip()
        cand = (base / name)
        if not cand.suffix:
            cand = cand.with_suffix('.tex')
        if cand.exists():
            return _expand_inputs_text(
                cand.read_text(encoding='utf-8', errors='replace'),
                cand.parent, depth - 1,
            )
        return m.group(0)

    # \input{file}, \include{file}, \ExpandableInput{file}
    return re.sub(r'\\(input|include|ExpandableInput)\s*\{([^}]+)\}', repl, text)


def inline_bbl(tex_text: str, tex_path: Path, bib_paths: list = None) -> str:
    """If the tex has \\bibliography{...} but no \\thebibliography, inline either
    a sibling .bbl file or a generated minimal bibliography from the .bib(s).
    Also ensures the bibliography section is preceded by a heading.
    """
    if r'\begin{thebibliography}' in tex_text:
        # Already has bibliography inline; just ensure it has a heading.
        if not re.search(r'\\section\*?\s*\{\s*[Rr]eferences?\s*\}', tex_text):
            tex_text = re.sub(
                r'(\\begin\{thebibliography\})',
                r'\\section*{References}\n\n\1',
                tex_text, count=1,
            )
        return tex_text
    bbl = tex_path.with_suffix('.bbl')
    inline_text = ''
    if bbl.exists():
        inline_text = bbl.read_text(encoding='utf-8', errors='replace')
        inline_text = _braced_em_to_textit(inline_text)
    elif bib_paths:
        # Find which keys are actually cited and generate minimal entries
        cited_keys = _find_cited_keys(tex_text)
        inline_text = _generate_bibliography(cited_keys, bib_paths)
    if not inline_text:
        return tex_text
    # replace \bibliography{...} with the bbl/generated content
    if re.search(r'\\bibliography\s*\{[^}]+\}', tex_text):
        tex_text = re.sub(
            r'\\bibliography\s*\{[^}]+\}',
            lambda m: f'\n\\section*{{References}}\n\n{inline_text}\n',
            tex_text, count=1
        )
    else:
        if r'\end{document}' in tex_text:
            tex_text = tex_text.replace(
                r'\end{document}',
                f'\n# References\n\n{inline_text}\n\\end{{document}}'
            )
        else:
            tex_text = tex_text + '\n\n# References\n\n' + inline_text
    return tex_text


def _find_cited_keys(tex_text: str) -> set:
    """Collect all bib keys cited via \\cite-family commands (after my replace_citations,
    these will already be resolved, so look at the original tex too).
    Since this runs BEFORE replace_citations, we can scan tex_text directly."""
    keys = set()
    for m in re.finditer(r'\\cite[a-z]*\s*(?:\[[^\]]*\])?(?:\[[^\]]*\])?\s*\{([^}]+)\}', tex_text):
        for k in m.group(1).split(','):
            keys.add(k.strip())
    return keys


def _generate_bibliography(cited_keys: set, bib_paths: list) -> str:
    """Generate a simple bibliography listing for cited keys from the bib files.

    Each entry: Author(s) (Year). Title. *Journal*, vol(num):pp.
    """
    entries = {}
    for bp in bib_paths:
        if not bp.exists():
            continue
        text = bp.read_text(encoding='utf-8', errors='replace')
        for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
            kind = m.group(1).lower()
            key = m.group(2).strip()
            if kind in {'comment', 'string', 'preamble'}:
                continue
            opening = text.find('{', m.start())
            depth = 0
            end = opening
            for i in range(opening, len(text)):
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                    if depth == 0:
                        end = i
                        break
            body = text[m.end():end]
            entries[key] = (kind, body)

    lines = []
    # Sort by first author last name (using parsed display)
    def sort_key(k):
        kind, body = entries[k]
        author = _field(body, 'author') or _field(body, 'editor') or ''
        names = _short_authors(author) or 'zzz'
        year = _field(body, 'year') or '0000'
        return (names.lower(), year)

    keys_present = sorted([k for k in cited_keys if k in entries], key=sort_key)
    for key in keys_present:
        kind, body = entries[key]
        line = _format_bib_entry(kind, body)
        if line:
            lines.append(line)
    return '\n\n'.join(lines)


def _format_bib_entry(kind: str, body: str) -> str:
    """Format a single bib entry as a one-line plain-text reference."""
    author = _field(body, 'author') or _field(body, 'editor') or ''
    year = _field(body, 'year') or _field(body, 'date') or ''
    ym = re.match(r'\d{4}', year)
    year = ym.group() if ym else year[:4]
    title = _field(body, 'title') or ''
    journal = _field(body, 'journal') or ''
    booktitle = _field(body, 'booktitle') or ''
    publisher = _field(body, 'publisher') or ''
    school = _field(body, 'school') or ''
    institution = _field(body, 'institution') or ''
    volume = _field(body, 'volume') or ''
    number = _field(body, 'number') or ''
    pages = _field(body, 'pages') or ''
    note = _field(body, 'note') or ''
    url = _field(body, 'url') or ''

    # prep author list (full names, not just last)
    authors_str = _format_author_list(author)
    title_str = _clean_name(title)
    parts = []
    if authors_str:
        parts.append(authors_str)
    if year:
        parts.append(f'({year})')
    head = ' '.join(parts) + '.' if parts else ''
    body_parts = []
    if title_str:
        body_parts.append(title_str.rstrip('.'))
    venue = journal or booktitle or institution or school or publisher
    if venue:
        venue_clean = _clean_name(venue)
        v_str = f'\\textit{{{venue_clean}}}'
        if volume:
            v_str += f' {volume}'
            if number:
                v_str += f'({number})'
            if pages:
                v_str += f':{pages.replace("--", "–")}'
        elif pages:
            v_str += f' {pages.replace("--", "–")}'
        body_parts.append(v_str)
    if note:
        body_parts.append(_clean_name(note))

    line = head
    if body_parts:
        line += ' ' + '. '.join(body_parts) + '.'
    return line.strip()


def _format_author_list(author_field: str) -> str:
    """Render full author list as 'A, B, and C' for bibliography display."""
    if not author_field:
        return ''
    parts = _split_authors(author_field)
    formatted = []
    for p in parts:
        # render as "Last, First M." or just "Name" for corp
        p = p.strip()
        if p.startswith('{{') and p.endswith('}}'):
            formatted.append(_clean_name(p[2:-2]))
            continue
        if ',' in p:
            last, first = p.split(',', 1)
            formatted.append(f'{_clean_name(last)}, {_clean_name(first)}')
        else:
            formatted.append(_clean_name(p))
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f'{formatted[0]}, and {formatted[1]}'
    return ', '.join(formatted[:-1]) + f', and {formatted[-1]}'


def _braced_em_to_textit(s: str) -> str:
    """Convert {\\em X} and {\\bf X} (bare-command-in-braces) into \\textit{X}/\\textbf{X}.

    Handles balanced braces correctly using a stack."""
    out = []
    i = 0
    while i < len(s):
        # detect {\em or {\it or {\bf or {\sl or {\sc with optional space
        m = re.match(r'\{\s*\\(em|it|bf|sl|sc|tt|rm)\b\s*', s[i:])
        if m:
            cmd = m.group(1)
            replacement = {
                'em': 'textit', 'it': 'textit',
                'bf': 'textbf',
                'sl': 'textit', 'sc': 'textsc',
                'tt': 'texttt', 'rm': 'textrm',
            }[cmd]
            # find the matching closing brace
            start = i + m.end()
            depth = 1
            j = start
            while j < len(s) and depth > 0:
                if s[j] == '{':
                    depth += 1
                elif s[j] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            content = s[start:j]
            # recurse into content
            content = _braced_em_to_textit(content)
            out.append(f'\\{replacement}{{{content}}}')
            i = j + 1
        else:
            out.append(s[i])
            i += 1
    return ''.join(out)


def parse_kvstore(csv_path: Path) -> dict:
    """Parse a Stata kvstore CSV (key,value,...) into a dict."""
    if not csv_path or not csv_path.exists():
        return {}
    import csv
    out = {}
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row.get('key') or '').strip()
            val = (row.get('value') or '').strip()
            if key:
                out[key] = val
    return out


def _clean_col_spec(spec: str) -> str:
    """Simplify a tabular column spec to letters pandoc understands.

    Strips array.sty/tabularx/siunitx custom column types, @-separators,
    column qualifiers, etc., reducing to plain l/c/r so pandoc can build
    a real markdown table. Without this, esttab fragments like
    `l@{}lR{1.6cm}@{\\hskip 0.5cm}L{0.5cm}cccc` leak as raw text.
    """
    spec = re.sub(r'\\extracolsep\s*\{[^}]*\}', '', spec)
    for prefix in ['@', '!', '>', '<']:
        prev = None
        while prev != spec:
            prev = spec
            spec = re.sub(re.escape(prefix) + r'\{(?:[^{}]|\{[^}]*\})*\}', '', spec)
    spec = re.sub(r'D\s*\{[^}]*\}\s*\{[^}]*\}\s*\{[^}]*\}', 'r', spec)
    spec = re.sub(r'R\s*\{[^}]*\}', 'r', spec)
    spec = re.sub(r'L\s*\{[^}]*\}', 'l', spec)
    spec = re.sub(r'C\s*\{[^}]*\}', 'c', spec)
    spec = re.sub(r'M\s*\{[^}]*\}', 'c', spec)
    spec = re.sub(r'P\s*\{[^}]*\}', 'l', spec)
    spec = re.sub(r'p\s*\{[^}]*\}', 'l', spec)
    spec = re.sub(r'm\s*\{[^}]*\}', 'c', spec)
    spec = re.sub(r'b\s*\{[^}]*\}', 'l', spec)
    spec = re.sub(r'S\s*\[[^\]]*\]', 'r', spec)

    def expand_star(m):
        try:
            return m.group(2) * int(m.group(1))
        except (ValueError, IndexError):
            return m.group(0)

    spec = re.sub(r'\*\s*\{\s*(\d+)\s*\}\s*\{([^}]*)\}', expand_star, spec)
    spec = spec.replace('|', '')
    spec = re.sub(r'\s+', '', spec)
    return spec


_TABULAR_ENVS_WITH_WIDTH = {'tabular*', 'tabularx', 'tabulary', 'longtabu', 'tabu'}


def clean_tabular_specs(tex: str) -> str:
    """Rewrite \\begin{tabular...}{...spec...} so pandoc can parse it."""
    pattern = re.compile(r'\\begin\s*\{(tabular\*?|tabularx|tabulary|longtable|longtabu|tabu)\}')
    out = []
    i = 0
    for m in pattern.finditer(tex):
        out.append(tex[i:m.start()])
        env = m.group(1)
        pos = m.end()
        head = f'\\begin{{{env}}}'
        if env in _TABULAR_ENVS_WITH_WIDTH:
            # consume optional whitespace then a {width} arg
            while pos < len(tex) and tex[pos].isspace():
                pos += 1
            if pos < len(tex) and tex[pos] == '{':
                width = _balanced_braces(tex, pos)
                head += '{' + width + '}'
                pos += len(width) + 2
        # consume optional [t|b] positioning arg
        while pos < len(tex) and tex[pos].isspace():
            pos += 1
        if pos < len(tex) and tex[pos] == '[':
            j = tex.find(']', pos)
            if j > 0:
                head += tex[pos:j+1]
                pos = j + 1
        while pos < len(tex) and tex[pos].isspace():
            pos += 1
        if pos < len(tex) and tex[pos] == '{':
            spec = _balanced_braces(tex, pos)
            head += '{' + _clean_col_spec(spec) + '}'
            pos += len(spec) + 2
        out.append(head)
        i = pos
    out.append(tex[i:])
    return ''.join(out)


def resolve_getval(tex: str, kv: dict) -> str:
    """Replace \\getval{key} with the value (in the .tex source before pandoc)."""
    if not kv:
        return tex
    return re.sub(
        r'\\getval\s*\{([^}]+)\}',
        lambda m: kv.get(m.group(1).strip(), m.group(0)),
        tex,
    )


def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: python _tex2md.py <tex_path> <bib_path|-> <out.md> [kv_csv|-]")
        sys.exit(1)
    tex_path = Path(sys.argv[1])
    bib_arg = sys.argv[2]
    out_path = Path(sys.argv[3])
    kv_arg = sys.argv[4] if len(sys.argv) >= 5 else None
    # bib_arg may be "-" (none), a single path, or comma-separated list
    if bib_arg == '-':
        bib_paths = []
    else:
        bib_paths = [Path(p.strip()) for p in bib_arg.split(',') if p.strip()]

    # auto-detect kvstore if not provided
    if kv_arg is None:
        candidate = tex_path.parent / 'results' / 'kv_store.csv'
        kv_path = candidate if candidate.exists() else None
    elif kv_arg == '-':
        kv_path = None
    else:
        kv_path = Path(kv_arg)
    kv = parse_kvstore(kv_path) if kv_path else {}

    # 0. read tex; expand \input{} / \ExpandableInput{} so citations
    # and table fragments in sub-files get pulled in
    tex_text = expand_inputs(tex_path)
    # strip \thanks{...} (and orphan \footnote{...} attached to title block)
    # so that pandoc footnote indices start at 1, not 2, and any email-typeset
    # \text{...@...} inside \thanks goes away with it.
    tex_text = _strip_balanced(tex_text, ['thanks'])
    # convert {\em X} / {\bf X} (which pandoc strips) -> \textit{X} / \textbf{X}
    tex_text = _braced_em_to_textit(tex_text)
    # strip \textcolor{color}{content} -> content (keep the content)
    tex_text = re.sub(
        r'\\textcolor\s*\{[^}]*\}\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',
        r'\1', tex_text
    )
    # NOTE: previously stripped \text{X} -> X here. Removed: that mangles
    # \text{Var}_{i} inside math (Var becomes a runaway identifier and adjacent
    # operators like \times\text{Post} collapse to \timesPost). Pandoc handles
    # \text{} fine in both math and text mode, so leave it alone.
    # strip orphan \tikzstyle{...}=[...] definitions
    tex_text = re.sub(r'\\tikzstyle\s*\{[^}]*\}\s*=\s*\[[^\]]*\]', '', tex_text)
    # rewrite tabular column specs so esttab fragments produce real markdown
    # tables instead of leaking column-type macros as raw text
    tex_text = clean_tabular_specs(tex_text)
    # inline bibliography from .bbl, or generate from .bib if no .bbl
    tex_text = inline_bbl(tex_text, tex_path, bib_paths)
    if kv:
        tex_text = resolve_getval(tex_text, kv)

    # 1. parse bib(s) and merge
    idx = {}
    for bp in bib_paths:
        idx.update(parse_bib(bp))

    # 2. resolve citations in .tex BEFORE pandoc (so they survive table cells, footnotes, etc.)
    if idx:
        tex_for_pandoc = replace_citations(tex_text, idx)
    else:
        tex_for_pandoc = tex_text

    # 3. pandoc tex -> md
    cmd = [
        'pandoc',
        '-f', 'latex',
        '--wrap=none',
        '--markdown-headings=atx',
        '-t', 'markdown-citations-raw_attribute-bracketed_spans-fenced_divs',
    ]
    proc = subprocess.run(cmd, input=tex_for_pandoc, capture_output=True, text=True,
                          encoding='utf-8', cwd=tex_path.parent)
    if proc.returncode != 0:
        print('pandoc failed:', proc.stderr, file=sys.stderr)
        sys.exit(1)
    md = proc.stdout

    # 4. handle any pandoc-style citations that snuck through
    if idx:
        md = replace_pandoc_citations(md, idx)

    # 5. extract title/authors/abstract from .tex (with citations resolved) and prepend
    meta = extract_metadata(tex_for_pandoc)
    header = build_header(meta)

    # 6. cleanup body and assemble
    md = cleanup(md)
    final = header + md if header else md

    out_path.write_text(final, encoding='utf-8')
    print(f'Wrote {out_path} ({len(final)} chars)')


if __name__ == '__main__':
    main()
