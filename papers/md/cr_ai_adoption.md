# Generative AI in Higher Education: Evidence from an Elite College

*Zara Contractor, Germán Reyes*  
*May 2026*

**Abstract.** Generative AI is transforming higher education, yet systematic evidence on student adoption, usage patterns, and perceived learning impacts remains scarce. Using survey data from a selective U.S. college, we document rapid generative-AI adoption, reaching over 80 percent within two years of ChatGPT's release. Adoption varies sharply across disciplines, demographics, and achievement levels. Students use AI both to augment their learning—by obtaining explanations and feedback—and to automate coursework by generating final outputs, with augmentation more common than automation. Students generally perceive AI as benefiting their learning, and these beliefs are strongly correlated with adoption. Institutional policies shape usage but have uneven effects, in part because awareness and compliance vary across student groups. These findings suggest that effective AI policies must distinguish between uses that enhance learning and those that substitute for it.

# Introduction
ChatGPT and similar generative artificial intelligence (AI) tools can perform tasks central to academic assessment and learning—write essays, solve problems, and explain concepts—instantly and at near-zero marginal cost. Yet systematic evidence on how this new technology is reshaping student learning remains scarce. How widespread is AI adoption among students, and what factors drive it? Do students primarily use AI to augment their learning or to automate coursework, potentially harming human capital development? Could disparities in access to paid AI resources amplify existing educational inequalities? These questions are central to ongoing debates about AI in education, yet the evidence base remains thin.

In this paper, we examine generative AI adoption, usage patterns, beliefs, and policy responses among students at Middlebury College, a selective liberal arts college in Vermont with about 2,800 undergraduates across 49 majors. Our survey ran from December 2024 to February 2025 and yielded 739 responses (a 26.8 percent response rate). To address sample selection, we construct poststratification weights from the major distribution in administrative records. Main findings are robust to alternative weighting schemes and to unweighted estimates.

We present five main descriptive findings. First, AI adoption is rapid and approaching universality. Over 80 percent of students use AI for academic purposes, up from less than 10 percent before Spring 2023. This rate far exceeds the 40 percent among U.S. workers (Bick, Blandin, and Deming, 2026) and the 34 percent among all U.S. adults (McClain, 2025). Our rate is in line with the upper end of estimates from other universities (Nam, 2023; Hirabayashi et al., 2024; Stöhr, Ou, and Malmström, 2024; Flaherty, 2025; Freeman, 2025; Ravšelj et al., 2025).

Second, AI adoption is unequal across academic disciplines and demographic groups. Field of study is the strongest predictor of adoption, likely reflecting AI's usefulness for each field's tasks. Adoption ranges from over 90 percent in Natural Sciences majors (including mathematics and computer science) to less than 50 percent in Literature. Adoption also varies across demographic groups. Males adopt AI at higher rates than females (88.7 versus 78.4 percent), consistent with gender gaps in AI adoption documented elsewhere (Otis et al., 2024). Lower-achieving students also adopt AI at higher rates than their higher-achieving peers (87.1 versus 80.3 percent); thus, AI could narrow achievement gaps if it enhances learning, or widen them if it undermines skill development.

Third, AI is reshaping students' learning production function through two channels: augmentation, in which AI works *with* the student, and automation, in which AI does the work *for* the student. To classify each task into one of these two categories, we conducted a supplementary Prolific survey in which undergraduates and college instructors classified each task as one where AI primarily "works with" the student or "does the work for" them. We then apply these classifications to our main sample to measure how much students rely on each. Among AI users, the average usage rate across augmentation tasks is 56.0 percent, compared to 45.4 percent across automation tasks. Qualitative evidence reinforces these patterns: students describe AI as an "on-demand tutor" for augmentation, particularly when traditional resources like office hours are unavailable, and turn to automation to save time during periods of high workload. These patterns align with actual usage data from Claude conversation logs (Handa et al., 2025) and ChatGPT interaction logs at another U.S. university (Ammari et al., 2025).

Fourth, institutional policies can influence AI adoption, though information gaps undermine their effectiveness. Explicit prohibitions reduce self-reported intended use by 39 percentage points (pp). The size of this effect and intended usage under prohibition vary by student characteristics like gender, race, and field of study, suggesting that uniform policies may have uneven effects. Information gaps compound these challenges: 19.2 percent of students misunderstand their institution's AI rules, only 10.0 percent know about the college's premium AI resources, and just 31.3 percent know how to cite AI properly.

Fifth, students hold positive beliefs about AI's learning impact, and these beliefs are strongly correlated with adoption. Most students believe that AI improves their understanding of course materials (68.5 percent) and learning ability (57.6 percent), though fewer believe it improves grades (37.6 percent). Students who believe AI improves academic outcomes are more likely to adopt: a 10-pp increase in the share of students who believe AI improves learning is associated with a 4.9 pp increase in adoption.

Our analysis is descriptive, documenting stylized facts to inform future causal work. Yet several patterns carry direct policy relevance. The information gaps we document—in permitted uses and available resources—suggest straightforward opportunities for intervention. Heterogeneity across disciplines and student groups, however, means uniform policies risk unintended consequences. Blanket prohibitions risk disproportionately harming students who would benefit most from AI as a learning aid—if perceived benefits translate into actual learning gains—while unrestricted use may encourage automation that hinders skill development.

Although our findings are specific to a liberal arts college, the setting offers insights into AI's broader societal impact. Rapid AI adoption in higher education may reflect a generalizable principle: adoption is fastest when AI consolidates fragmented tools into a unified platform. Students have long had access to various tools for the tasks AI now handles.[^1] AI delivers all these services through a single interface at near-zero marginal cost. This consolidation may partly explain students' positive perception of AI's learning benefits. If the interpretation holds, the principle extends beyond education: industries with fragmented, specialized tools could adopt AI just as quickly, even if AI does not introduce new capabilities.

Our findings contribute to a rapidly growing literature on the adoption and impacts of generative AI. Recent work has examined AI's effects on worker productivity (Dell'Acqua et al., 2023; Noy and Zhang, 2023; Peng et al., 2023; Cui et al., 2024; Brynjolfsson, Li, and Raymond, 2025; Cruces et al., 2026) and its potential to transform occupations (Felten, Raj, and Seamans, 2021; Felten, Raj, and Seamans, 2023; Eloundou et al., 2024). Several papers document AI adoption in workplace settings (Humlum and Vestergaard, 2025; Bick, Blandin, and Deming, 2026; Hartley et al., 2026) and at the firm level (McElheran et al., 2023; Bonney et al., 2024; Kharazian, 2025). We examine adoption in higher education—a setting in which future high-skilled workers develop human capital.

We add to an emerging and concurrent literature on generative AI in education. Some studies examine AI's learning impacts and find mixed results across settings (e.g., Bastani et al., 2025; Contractor and Reyes, 2025; De Simone et al., 2025; Kestin et al., 2025; Kim et al., 2025; Lehmann, Cornelius, and Sting, 2025; Lira et al., 2025). A complementary strand documents adoption across diverse educational contexts, including Australian (Kelly, Sullivan, and Strampel, 2023), Ghanaian (Bonsu and Baffour-Koduah, 2023), Norwegian (Carvajal, Franco, and Isaksson, 2024), Swedish (Stöhr, Ou, and Malmström, 2024), U.S. (Hirabayashi et al., 2024; Arum et al., 2025; Flaherty, 2025), U.K. (Freeman, 2025), and multi-country (Ravšelj et al., 2025) universities. A few studies analyze AI interaction logs rather than self-reports (Ammari et al., 2025; Chatterji et al., 2025; Handa et al., 2025; Handa et al., 2025).

Our paper contributes in three ways. First, unlike most studies that rely on convenience samples with unclear selection, we survey a well-defined population and address representativeness through poststratification weighting. Second, we examine adoption, usage, beliefs, and policy responses together within the same sample, whereas existing work typically focuses on one dimension at a time. Third, we distinguish between AI uses that *augment* student effort and those that *automate* academic tasks (Brynjolfsson and Mitchell, 2017; Acemoglu and Restrepo, 2019)—a framework that, to our knowledge, has not been systematically applied in higher education.

Finally, our findings speak to the literature on technology diffusion. Unlike the S-shaped adoption curves documented for most technologies (Griliches, 1957; Rogers, 1962), we observe 80 percent AI adoption within two years of ChatGPT's release. This pattern contrasts with historical general purpose technologies like electricity, which required decades to reach widespread use (David, 1990; Bresnahan and Trajtenberg, 1995). It aligns, though, with evidence that newer technologies diffuse faster than older ones (Comin and Hobijn, 2010; Comin and Hobijn, 2010). Two factors may explain this speed. First, unlike electricity or steam power, generative AI requires minimal physical infrastructure—students access it through existing devices—and is available at no cost, eliminating the financial barriers that typically slow adoption. Second, AI consolidates multiple specialized tools into a single platform, making its benefits immediately apparent without specialized training or organizational restructuring (Brynjolfsson and Hitt, 2000).

# Data: Student Survey
## Recruitment and Structure

We conducted the survey from December 2024 to February 2025. We contacted all students by email and sent two follow-up reminders. To encourage participation, we entered respondents into a lottery for Amazon gift cards ($50–$500).

The survey has three main sections (see Appendix Figure 7 for the flow and Appendix app:survey for the full survey instrument). First, we gather demographic and academic information: gender, race/ethnicity, high school type (private or public), current academic year, and declared or intended major.[^2] We also collect self-reported weekly study hours and first-year GPA.[^3]

Second, we measure students' experience with generative AI tools. We ask whether students have ever used tools like ChatGPT or Claude and, for users, collect usage frequency, specific models, payment for AI services, and how they use AI across academic tasks (e.g., writing assistance, learning support, coding).

The final part elicits students' beliefs about generative AI's academic impacts and diffusion. We ask students to evaluate AI's effects on their academic experience across four dimensions—learning, grades, time management, and understanding of course material—and how different policy environments influence their likelihood of using AI. We also elicit beliefs about peer AI use, including estimates of the share of Middlebury students who use AI for schoolwork and leisure. The survey concludes with two open-ended questions inviting students to share their experiences with AI and to comment on institutional policies and support services.

## Sample and Summary Statistics

Of Middlebury's 2760 enrolled students, 739 began the survey (a 26.8 percent response rate). This response rate is in line with the U.S. institutional average (National Survey of Student Engagement, 2020) and exceeds those at institutions like Harvard (Hirabayashi et al., 2024). We exclude 105 respondents who left before reaching the generative AI usage module, leaving an analysis sample of 634 students. To make the sample more representative, we construct poststratification weights from the distribution of declared majors in administrative records.[^4] We weight observations by the ratio of each major's share in the student population to its share in our responses.[^5]

Table 1 presents summary statistics. Column 1 reports unweighted survey averages, column 2 shows poststratification-weighted averages, and column 3 provides administrative-record benchmarks where available. Our unweighted sample is 44.6 percent male and 50.8 percent female. The racial/ethnic composition is 61.8 percent white, 15.5 percent Asian, 9.9 percent Hispanic, and 3.6 percent Black. Most students (54.3 percent) attended public school; 42.0 percent attended private school. The sample spans 43 majors across seven fields, with 3.5 percent of students not yet having declared a major. We group undeclared students by their intended field of study as reported in the survey.

Comparing the unweighted sample to administrative records reveals differences. The sample overrepresents white (61.8 versus 53.8 percent) and Asian (15.5 versus 7.3 percent) students, and underrepresents Black (3.6 versus 5.2 percent) and Hispanic (9.9 versus 12.4 percent) students. First-year students are overrepresented (31.1 versus 25.5 percent) and seniors underrepresented (21.3 versus 28.7 percent). Our weighting partially addresses these differences—weighted figures closely match administrative records for academic fields—but some demographic gaps persist. Appendix 9.1 shows that our main results hold under alternative weighting schemes (by gender and cohort, or by race) and under unweighted estimates.

# Generative AI Usage Patterns Among Students
## Adoption of Generative AI

Generative AI is widely adopted at Middlebury. Figure 1 shows the distribution of AI usage frequency during the academic semester across four levels: "Rarely" (a few times per semester), "Occasionally" (a few times per month), "Frequently" (a few times per week), and "Very Frequently" (daily or almost daily). Overall, 82.5 percent of students report using generative AI for academic purposes, with substantial variation in intensity: 23.5 percent use it rarely, 22.2 percent occasionally, 26.2 percent frequently, and 10.6 percent very frequently.

An independent survey at Middlebury corroborates our adoption estimate. The student-led Zeitgeist 7.0 survey, conducted by *The Middlebury Campus* in Spring 2025 with 1026 respondents (37 percent of the student body), asked "How often do you use A.I. in your classes at Middlebury?". 85.2 percent reported some level of AI use, compared with 82.5 percent in our sample (The Middlebury Campus, 2025). The close correspondence across surveys with different response rates and sampling periods suggests that selection bias is unlikely to substantially inflate our adoption rates.

Middlebury's adoption rate aligns with patterns at other institutions. As of spring 2024, 87.5 percent of Harvard undergraduates used AI (Hirabayashi et al., 2024), and a 2025 *Inside Higher Ed* survey found that 85 percent of U.S. college students had used AI for coursework in the past year (Flaherty, 2025)—both close to our 82.5 percent. In the U.K., 88 percent of undergraduates had used AI for assessments (Freeman, 2025). Earlier surveys show correspondingly lower rates. A fall 2023 *BestColleges* survey found that 56 percent of U.S. students had used AI on assignments or exams (Nam, 2023), against about 39 percent at Middlebury by the same period. International data are similar: 71.4 percent of higher-education students globally had ever used ChatGPT by late 2023–early 2024 (Ravšelj et al., 2025); 63 percent of Swedish students had used ChatGPT by spring 2023 (Stöhr, Ou, and Malmström, 2024); and 68.9 percent of Norwegian students used AI at least occasionally (Carvajal, Franco, and Isaksson, 2024). The convergence across these samples suggests that near-universal AI adoption among university students is not specific to our context.

These adoption rates far exceed those in the general population and workforce. Pew Research finds that 34 percent of U.S. adults have ever used ChatGPT as of early 2025 (McClain, 2025), and Gallup reports that 45 percent of U.S. employees used AI at work at least a few times a year by mid-2025, with daily use at only 10 percent (Gallup, 2025). ChatGPT consumer logs show the platform had reached about 10 percent of the world's adult population by mid-2025 (Chatterji et al., 2025). Bick, Blandin, and Deming (2026) and Hartley et al. (2026) estimate that 36–45 percent of the U.S. working-age population used generative AI for work in late 2024 and 2025. Both document substantial industry heterogeneity, with information services and technology at the top at 56–76 percent—still well below 80 percent at Middlebury. Even among workers in AI-exposed occupations, Humlum and Vestergaard (2025) find adoption rates of only 41 percent.[^6]

## Adoption by Student Characteristics and Field of Study

AI adoption varies considerably across demographic groups and academic disciplines (Figure 1 and Appendix Table 5). Males report higher usage than females (88.7 versus 78.4 percent). Usage differs by race and ethnicity: Black (92.3 percent) and Asian (91.3 percent) students have the highest adoption rates, while white (80.2 percent) and Hispanic (77.9 percent) students report lower usage. Students from private high schools use AI more than those from public schools (84.1 versus 80.4 percent). Students with below-median GPAs report higher usage than their higher-achieving peers (87.1 versus 80.3 percent). Adoption varies most sharply by field of study: Natural Sciences leads at 87.4 percent and Social Sciences follows at 84.5 percent, while Languages (59.5 percent) and Literature (53.8 percent) show considerably lower adoption rates.

To examine how student characteristics jointly relate to adoption, we estimate OLS regressions that include them all as covariates.[^7] Table 2 reports estimates for four usage thresholds. Each column is the probability of meeting a progressively higher frequency threshold: any AI use (column 1), at least monthly use (column 2), at least weekly use (column 3), and daily use (column 4).

The regression results confirm these descriptive patterns. Holding other characteristics constant, males are 10.3 pp more likely than females to use AI (column 1, $p < 0.05$), with this gender gap widening at higher usage frequencies (columns 2–4, all $p < 0.01$). Black and Asian students adopt AI at higher rates than white students, at 13.6 and 11.4 pp respectively (column 1, both $p < 0.01$). Students from public high schools are 4.1 pp less likely to use AI than those from private schools, but this difference is not statistically significant. Field of study is the strongest predictor of adoption. Compared to Natural Sciences majors, students in Literature, Languages, and Humanities all use AI at lower rates, with differences reaching statistical significance at high usage frequencies (columns 3 and 4). Arts majors also show lower adoption on average, but the differences are not statistically significant. Social Sciences majors exhibit adoption rates similar to Natural Sciences majors across all frequency thresholds.

These heterogeneity patterns align with evidence from other settings. The gender gap at Middlebury—10.3 pp higher for males—is consistent with a meta-analysis of 18 studies by Otis et al. (2024), who find that males are 10–20 pp more likely to use generative AI than females. The same gap shows up across educational studies of AI adoption (Nam, 2023; Carvajal, Franco, and Isaksson, 2024; Stöhr, Ou, and Malmström, 2024; Ravšelj et al., 2025). Our finding that students with below-median GPAs adopt AI at higher rates aligns with Carvajal, Franco, and Isaksson (2024), who document higher adoption among students with lower admission grades. Whether greater adoption among lower-achieving students narrows or widens achievement gaps depends on whether AI enhances skill development or erodes it.

Disciplinary differences at Middlebury mirror patterns documented elsewhere. Stöhr, Ou, and Malmström (2024) find that technology and engineering students use ChatGPT more than humanities students. Nam (2023) report that 62 percent of business majors and 59 percent of STEM majors have used AI tools for coursework, versus 52 percent of humanities majors. Ravšelj et al. (2025) document comparable differences, with applied sciences students showing higher usage than arts and humanities students.

These disciplinary differences persist into the workforce. Bick, Blandin, and Deming (2026) find stark variation by college major: STEM graduates have the highest AI adoption rates (46.0 percent), followed by Business/Economics graduates (40.0 percent); Liberal Arts graduates show much lower rates (22.4 percent). Humlum and Vestergaard (2025) document similar patterns by occupation: roles requiring strong writing and technical skills—such as marketing specialists and journalists—have the highest adoption rates. Consistency across educational and professional contexts suggests that field-specific factors—particularly AI's applicability to different tasks—systematically shape adoption.

## Timing of Generative AI Adoption

The speed of technology diffusion is a critical determinant of its economic and social impact (David, 1990; Hall and Khan, 2003; Stokey, 2021). In educational contexts, rapid adoption can create or exacerbate inequalities between early and late adopters, particularly if the technology confers learning advantages (World Bank, 2016). To track adoption timing, we asked students when they first began using generative AI for academic purposes, with options ranging from "This semester (Fall 2024)" to "Before Spring 2023" (ChatGPT launched publicly in November 2022).

Students adopted generative AI at an extraordinary pace. Figure 2 shows that cumulative adoption grew from less than 10 percent before Spring 2023 to over 80 percent by Fall 2024. Adoption accelerated over time, consistent with improvements in AI capabilities: among current users, 31.2 percent adopted in Fall 2024 alone, 24.1 percent in Spring 2024, and 19.8 percent in Fall 2023.

This pace far exceeds that observed in other populations. Bick, Blandin, and Deming (2026) show that computers took over 20 years to reach 80 percent adoption among U.S. working-age adults, and the internet took about 15 years. Generative AI adoption in the broader population has also been slower: Pew Research found that just 23 percent of U.S. adults had ever used ChatGPT as of February 2024, up from 18 percent in July 2023 (McClain, 2024). Students reached 80 percent adoption in under two years, suggesting that academic settings accelerate AI diffusion more than other settings.

To identify early versus late adopters, we examine how adoption timing varies across student characteristics (Table 3 and Appendix Figure fig:ai_cdf_dem). Male students led adoption, with an 8.7 pp higher probability of using AI before Spring 2023 than females (column 1, $p < 0.01$)—a gap that persists across all periods (columns 2–5). Black and Asian students also adopted earlier than white students, though these differences reach statistical significance only in later periods (columns 4–5). Field of study is a strong predictor of adoption timing: Languages majors consistently lagged behind Natural and Social Sciences majors, with significantly lower adoption rates across nearly all periods.

## Choice of Generative AI Models
Major AI companies operate on a freemium model: free versions coexist with premium subscriptions offering higher usage limits and more advanced models. This tiered structure creates potential for a new form of educational inequality—if paid versions confer academic advantages, students who cannot afford subscriptions may be systematically disadvantaged. We presented respondents with a list of free and paid versions of popular models and collected monthly subscription expenditures, with options ranging from no active subscription to more than $40 per month (ChatGPT Plus cost $20 per month at the time of our survey).

OpenAI's ChatGPT dominates AI usage among Middlebury students. Figure 3 shows that 88.0 percent of AI users rely on the free version, far more than any alternative. Google Gemini (13.5 percent) and Microsoft Copilot (7.7 percent) are distant competitors; other platforms each capture less than 5 percent of users. This dominance mirrors patterns at other selective institutions: Hirabayashi et al. (2024) find that over 95 percent of Harvard AI users report using ChatGPT. Similar patterns appear in other academic settings (Stöhr, Ou, and Malmström, 2024) and in the broader workforce (Bick, Blandin, and Deming, 2026).[^8]

Despite near-universal AI adoption, only 11.4 percent of AI users pay for any AI service.[^9] The rate is similar to the 8 percent in Ravšelj et al. (2025)'s multi-country survey but lower than the 29.7 percent at Harvard (Hirabayashi et al., 2024). The low payment rate suggests that for most students, the premium features—mainly higher usage limits and more advanced models—do not justify the cost. Payment patterns reveal disparities: males and Asian students are more likely to purchase AI subscriptions (Appendix Table 6 and Appendix Figure 8), possibly reflecting differences in usage intensity.

# Generative AI and the Production of Learning
## The Use of Generative AI across Academic Tasks

How is generative AI reshaping the traditional inputs to student learning? The educational production function includes time spent studying (e.g., Stinebrickner and Stinebrickner, 2008), faculty instruction (e.g., Fairlie, Hoffmann, and Oreopoulos, 2014), peer interactions (e.g., Sacerdote, 2001), and academic support services (e.g., Angrist, Lang, and Oreopoulos, 2009). AI tools can complement or substitute for these and other inputs: asking AI to explain a concept may substitute for faculty office hours, and using it for proofreading may reduce the need for academic support services.

To understand AI's role in the learning production function, we collected AI usage across ten academic tasks: proofreading, generating ideas, writing essays, editing drafts, coding assistance, creating images, explaining concepts, composing emails, summarizing materials, and finding information. For each task, students reported usage frequency on a five-point scale from never to daily. We supplement these data with open-ended responses.

Students use generative AI across a wide range of academic tasks, with learning support and text processing showing the highest adoption. Figure fig:ai_use_purpose, Panel A shows that explaining concepts is the most common use case (80.3 percent of AI users), followed by summarizing texts (74.0 percent), finding information (63.1 percent), and generating ideas (61.9 percent). Writing assistance tasks—proofreading and editing essays—are also common (54.1 and 47.3 percent, respectively). 34.4 percent of AI users use it for coding help—a sizable share given that many degrees involve no programming. Only 23.5 percent report using AI to write essays, suggesting reluctance to outsource the writing itself. The lowest adoption is for creating images (20.4 percent), likely reflecting fewer academic use cases for this capability.

An important limitation is that our survey relies on self-reported usage, which may introduce non-classical measurement error (Ling, Kale, and Imas, 2025)—students might underreport uses they perceive as academically inappropriate. To assess validity, we compare our findings against two studies that analyze AI interaction logs: Handa et al. (2025), who examine Claude usage among users with university email addresses, and Ammari et al. (2025), who analyze ChatGPT logs from undergraduates at another U.S. university. Neither comparison is perfect: Handa et al.'s data are conversation-level rather than student-level, and most students in our sample use ChatGPT rather than Claude (Section 3.4); Ammari et al.'s data rely on students voluntarily sharing their logs. Both still offer useful benchmarks.

Our results are broadly consistent with Anthropic's data on Claude usage. Handa et al. (2025) report that the second-largest use case (33.5 percent of conversations) involves "technical explanations or solutions for academic assignments," while we find that 80.3 percent of AI users use it for explaining concepts—a difference likely attributable to our student-level versus their conversation-level measurement. The most common Claude usage category involves "designing practice questions, editing essays, or summarizing academic material" (39.3 percent of conversations), consistent with our finding that 74.0 percent of AI users summarize texts and 47.3 percent edit essays. Disciplinary patterns also converge: Handa et al. (2025) find that computer science, natural sciences, and mathematics conversations are overrepresented, mirroring our finding that Natural Science majors show the highest AI adoption rates (Figure 1).

Further validation comes from Ammari et al. (2025), who analyze ChatGPT logs from undergraduates. Although they use a different classification scheme—information seeking, content generation, language refinement, meta-cognitive engagement, and conversational repair—their findings align closely with ours. "Concept explanation" is the most common information-seeking behavior, consistent with our finding that explaining concepts is the most frequent use case. Information seeking and language refinement dominate over pure content generation, paralleling our results. Convergence across self-reported survey data, Anthropic's conversation logs, and Ammari et al.'s ChatGPT logs—each using different measurement approaches and classification schemes—suggests that our results capture real patterns of student AI engagement rather than social desirability bias.

## Automation versus Augmentation

Are students using generative AI primarily to *augment* their learning or to *automate* their coursework? This distinction matters for understanding AI's impact on human capital. Augmentation may enhance students' learning while maintaining active engagement; automation produces outputs that could be submitted with minimal student input, potentially undermining skill development.

Our main survey records AI use across ten academic tasks but does not classify them as augmentation or automation. To make this distinction, we conducted a supplementary survey of 56 undergraduates and 51 college instructors recruited through Prolific (see Appendix 10). For each task, respondents classified whether AI acts more as a collaborator (works *with* the student) or automates the task (does the work *for* the student). We apply the combined modal classification to categorize tasks. Figure fig:ai_use_purpose, Panel B reports the share of AI users who use each category at various frequencies.

Students use generative AI for both augmentation and automation, but augmentation is more common. Among AI users, the average usage rate across augmentation tasks is 56.0 percent, compared to 45.4 percent across automation tasks—a 10.6 pp gap that suggests students find augmentation more valuable for day-to-day academic work. The pattern is consistent with AI conversation logs: Handa et al. (2025) analyze workplace conversations with Claude and find that 57 percent involve augmentation and 43 percent involve automation.

Qualitative evidence from open-ended responses reinforces the augmentation-automation framework (see Appendix 11 for additional results). For augmentation, many characterize AI as an "on-demand tutor," especially valuable when traditional resources like office hours are unavailable. Non-native English speakers frequently mention using AI for proofreading to overcome language barriers; students in technical majors describe using it to debug code and understand error messages. Students automate mainly to save time: 33.9 percent of open-ended responses mention efficiency benefits (Appendix Figure 11). Students describe turning to AI during periods of overwhelming workload or looming deadlines, using it to generate initial drafts or complete routine assignments.[^10]

The preference for augmentation over automation extends beyond Middlebury. In Appendix Figure fig:chatgpt_use_ravselj, we re-analyze data from Ravšelj et al. (2025)—a multi-country survey of higher education students—to examine how this balance varies by institutional quality.[^11] We classify universities into quintiles based on their *Times Higher Education* World University Rankings. Worldwide, students who use AI show similar rates for augmentation (64.7 percent) and automation (63.2 percent) tasks—a much smaller gap than at Middlebury (Panel A). This aggregate pattern masks heterogeneity by institutional quality (Panel B). Top-quintile students show a slight preference for automation over augmentation; this gap closes through the middle quintiles, then reverses sharply at the bottom quintile, where augmentation reaches roughly 74 percent while automation stays near 65 percent.

## Heterogeneity in Augmentation versus Automation Usage

To assess whether augmentation and automation patterns vary across student populations, we construct four measures: binary indicators for any use of each category, the proportion of tasks used in each category, Likert-scale intensity measures, and the difference between augmentation and automation (capturing relative preference). Table 4 presents regression estimates using these measures as outcomes.

The balance between augmentation and automation varies by student characteristics. Males use AI more in both categories: 8.0 pp more augmentation tasks and 9.5 pp more automation tasks than females (columns 2 and 5, $p < 0.01$). Black students use AI more intensively for both augmentation (0.446 points, $p < 0.10$) and automation (0.477 points, $p < 0.05$), with no significant difference in their relative preference (columns 7–8). Asian students likewise use AI more in both categories than white students. Differences across fields are sizable: humanities, languages, and literature majors use AI less for both augmentation and automation than natural science majors.

# Institutional Policies and AI Adoption
## The Role of Institutional Policies in Shaping Student Behavior

Institutional policies shape technology adoption and diffusion (Acemoglu, 2025).[^12] To examine how policies affect behavior, we asked students to report their likelihood of using AI under scenarios ranging from complete prohibition to unrestricted use—a question made salient by the wide variation in institutional policies across colleges (Nolan, 2023; Xiao, Chen, and Bao, 2023).

Institutional policies shape students' reported likelihood of using AI. Figure 4 shows that under unrestricted use, 52.5 percent of students report being likely or extremely likely to use AI. This share drops modestly when policies require citation (40.9 percent) or when no explicit policy exists (42.2 percent). Explicit prohibition sharply changes intentions: only 13.4 percent say they would be likely or extremely likely to use AI when it is banned, while 72.9 percent say they would be unlikely or extremely unlikely to do so (both figures include current users and non-users).[^13] Institutional policies thus shape usage, though some students report they would use AI even when explicitly prohibited.[^14]

Students do not respond to institutional policies uniformly. In Appendix Table 7, we regress the likelihood of using AI under each policy scenario on student characteristics. Both the effect of prohibition and intended usage under prohibition vary by gender, race, and field of study. Black students reduce their intended use more sharply under a ban than white students, while Arts and Literature majors adjust only modestly—in part because they were less likely to use AI in the first place. Intended usage conditional on prohibition is similarly uneven: males remain substantially more likely than females to report they would still use AI, while Arts and Languages majors are among the least likely. Uniform policies thus produce disparate outcomes across the student body—both in the reductions they induce and in the residual usage they fail to deter.

## Understanding of Institutional Policies and Resources

Information gaps and inattention can affect technology adoption decisions (Duflo, Kremer, and Robinson, 2011; Hanna, Mullainathan, and Schwartzstein, 2014). Imperfect information about rules, available resources, or proper usage guidelines could lead to underadoption of beneficial technologies or inadvertent policy violations. To test for information gaps, we examine three dimensions of policy understanding: whether students find AI policies clear, whether they know about free access to premium AI tools, and whether they know how to cite AI when required.

Most students understand AI policies, but gaps remain. Figure fig:ai_policies, Panel A shows that 79.1 percent of students understand when and where they can use AI in their classes; 19.2 percent find policies unclear. Larger gaps appear elsewhere: only 10.0 percent know they have free access to Microsoft Copilot through the college (Panel B), and just 31.3 percent know how to properly cite AI use (Panel C). Awareness varies by gender and race: females show better policy understanding than males (81.7 versus 75.8 percent), and non-white students show higher awareness than white students across all three dimensions.[^15]

Qualitative evidence from open-ended responses reinforces these frictions and reveals implementation challenges (Appendix 12). Students express frustration with vague guidelines and request specific examples of acceptable versus unacceptable uses. Many advocate for formal training, noting that knowing a policy exists differs from knowing how to integrate AI into their workflow. A recurring theme is blanket prohibitions as both ineffective and unfair, creating a prisoner's dilemma in which compliant students fall behind those who secretly violate the rules. Many responses call for a balanced approach—permitting AI use that supports learning while restricting uses that replace it—though the boundary between the two remains contested.

These findings point to two channels through which institutional interventions may shape AI adoption. Some policies operate through information and norms—clarifying acceptable use or raising awareness of available resources—and shift behavior by changing students' beliefs about appropriateness or their knowledge of options. Others operate through constraints and incentives—explicit prohibitions enforced through academic-integrity sanctions—and may shift behavior even with beliefs fixed, by changing AI use's costs and benefits. The information gaps we document suggest substantial scope for the first type of intervention; our policy-scenario results speak to the potential magnitude of the second.

# Beliefs About AI's Educational Impact and Peer Usage
## Student Beliefs About AI's Impact on Educational Outcomes

Beliefs about potential returns shape technology adoption (Foster and Rosenzweig, 2010). Students' perceptions of how AI affects their learning may influence both whether they adopt AI tools and how they use them. We asked students to evaluate AI's impact across four dimensions—understanding of course materials, overall learning ability, time management, and course grades—on a five-point scale from "significantly reduces" to "significantly improves."

Students generally view generative AI as beneficial, though perceived benefits vary across dimensions. Figure 5 shows that 68.5 percent of students believe AI improves their understanding of course materials, and 57.6 percent report improvements in their ability to grasp concepts, retain information, or learn new skills. A similar 56.4 percent report that AI improves their ability to complete assignments on time. Students are less confident about AI's impact on grades: only 37.6 percent believe it improves their grades, 59.2 percent report no effect, and 3.2 percent report negative effects.[^16] This pattern suggests that students perceive AI as improving their learning process and workflow—through better understanding, skill development, and timely completion of work—but that these perceived benefits do not necessarily translate into better grades.[^17]

Beliefs about AI's benefits are strongly correlated with adoption. Figure fig:ai_adoption_beliefs plots adoption rates against the share of students who believe AI improves a specific outcome, across student subgroups (e.g., males, white students, public-school students). Across all four academic dimensions, the relationship is positive, strong, and statistically significant. The correlation is strongest for beliefs about grades (Panel D): a 10-pp increase in the belief that AI improves grades is associated with a 6.2 pp increase in AI adoption ($p < 0.01$). Similar relationships hold for beliefs about learning ability (4.9 pp, $p < 0.05$), understanding of course materials (5.0 pp, $p < 0.01$), and timely assignment completion (5.4 pp, $p < 0.05$). These group-level correlations suggest that beliefs about AI's academic benefits—whether or not they reflect the actual benefits—shape adoption, though we cannot determine the direction of causation.

These positive beliefs align with findings elsewhere. Ravšelj et al. (2025) report that most students believe ChatGPT improves their general knowledge (68.8 percent) and specific knowledge (62.7 percent)—remarkably similar to our findings on understanding of course materials (68.5 percent) and learning ability (57.6 percent). Similarly, 57.4 percent in Ravšelj et al. (2025)'s sample believe ChatGPT helps meet deadlines, versus 56.4 percent in our data. Stöhr, Ou, and Malmström (2024) find that 47.7 percent of Swedish students believe AI makes them more effective learners, yet only 17.3 percent believe it improves grades—mirroring our finding that perceived learning benefits exceed perceived grade effects.

## Student Beliefs About Peer Use of Generative AI

Students' beliefs about peer AI use may shape adoption through social norms (e.g., Giaccherini et al., 2019), social learning (e.g., Foster and Rosenzweig, 1995; Beaman et al., 2021), peer effects (e.g., Bailey et al., 2022), and competitive pressure (e.g., Goehring, Mezzanotti, and Ravid, 2024). We asked students to estimate the share of peers using generative AI for different purposes and under different policy environments.

On average, students believe that 65.2 percent of peers regularly use generative AI for schoolwork, with wide variation in individual estimates (Appendix Figure fig:ai_beliefs). This average belief exceeds the actual rate of 61.6 percent (defined as use at least occasionally) by 4 pp, implying slight overestimation. Yet this average masks substantial variation across student groups. Figure 6 plots group-level beliefs ($x$-axis) against actual usage ($y$-axis) across demographic and academic groups. First, beliefs vary across groups—from 64 to 69 percent—yet nearly every group exceeds the overall true rate of 61.6 percent, so overestimation is near-universal. The largest overestimates are in lower-adoption groups such as females, white students, and majors in Humanities, Languages, and Literature. Second, beliefs track usage at the group level: groups with higher within-group adoption (ranging from 53 to 81 percent) report higher estimates of peer use, consistent with students inferring norms from their immediate social environment.

Because beliefs track adoption closely, students' overestimation of peer AI use suggests that misperceived social norms may shape technology diffusion. If AI enhances learning, overestimation may accelerate beneficial adoption, and correcting misperceptions could slow it; if AI undermines skill development, the same overestimation may fuel overadoption, and corrections could safeguard against it.

# Discussion
This paper documents generative AI adoption at a selective U.S. college. We find rapid adoption, shifts in the educational production function through augmentation and automation, and a central role for beliefs and institutional policies in shaping AI use. Taken together, these findings point to three implications for institutional policy.

First, we identify low-cost opportunities to make policy more effective by improving student information. The gaps we document in students' understanding of AI policies, citation practices, and available resources suggest that simple interventions—clear guidelines, illustrative examples of acceptable uses, and AI-literacy programs—can reduce unintentional integrity violations and support beneficial AI integration. Qualitative feedback confirms student demand for more explicit guidance.

Second, our evidence challenges narratives that conflate widespread AI adoption with universal academic dishonesty.[^18] Although AI use is near-universal, students primarily use it to enhance learning through augmentation and selectively automate tasks when facing high time opportunity costs, not solely to circumvent academic effort. This distinction matters for policy: normalizing academic dishonesty as inevitable may shift social norms and encourage students who would otherwise use AI responsibly to engage in prohibited behaviors, believing "everyone else is doing it."

Third, our findings caution against policy extremes (Merchant, 2024; McDonald et al., 2025). Blanket prohibitions risk disproportionately harming students who would benefit most from AI as a learning aid—if the perceived learning benefits translate into actual learning gains—while creating uneven compliance that places conscientious students at a disadvantage relative to rule-breakers. Unrestricted use based on revealed preference alone ignores potential market failures in educational settings. We document that students hold positive beliefs about AI's effects on learning and that these beliefs are strongly correlated with adoption. Yet the empirical evidence on AI's actual learning effects is mixed (e.g., Bastani et al., 2025; Contractor and Reyes, 2025; De Simone et al., 2025; Kestin et al., 2025; Kim et al., 2025; Lehmann, Cornelius, and Sting, 2025; Lira et al., 2025). If students' beliefs are more optimistic than the true effects warrant, adoption based on those beliefs may harm learning. Permissive policies also risk creating competitive dynamics in which students feel compelled to adopt AI not for its learning benefits but to avoid falling behind in an educational "arms race" (Goehring, Mezzanotti, and Ravid, 2024).

<div class="singlespace">

# References
<div class="thebibliography">

Acemoglu, D. (2025). Nobel lecture: Institutions, technology, and prosperity. *American Economic Review* *115*(6), 1709–1748.

Acemoglu, D. and P. Restrepo (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives* *33*(2), 3–30.

Ammari, T., M. Chen, S. M. M. Zaman, and K. Garimella (2025). How students (really) use ChatGPT: Uncovering experiences among undergraduate students.

Angrist, J., D. Lang, and P. Oreopoulos (2009). Incentives and services for college achievement: Evidence from a randomized trial. *American Economic Journal: Applied Economics* *1*(1), 136–163.

Arum, R., M. Calderon Leon, X. Li, and J. Lopes (2025). early adoption in higher education: Variation in student usage, instructional support, and educational equity. *AERA Open*.

Bailey, M., D. Johnston, T. Kuchler, J. Stroebel, and A. Wong (2022). Peer effects in product adoption. *American Economic Journal: Applied Economics* *14*(3), 488–526.

Bastani, H., O. Bastani, A. Sungu, H. Ge, Ö. Kabakcı, and R. Mariman (2025, July). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences* *122*(26), e2422633122.

Beaman, L., A. BenYishay, J. Magruder, and A. M. Mobarak (2021). Can network theory-based targeting increase technology adoption? *American Economic Review* *111*(6), 1918–1943.

Bick, A., A. Blandin, and D. J. Deming (2026). The rapid adoption of generative AI. *Management Science*. Published online ahead of print.

Bonney, K., C. Breaux, C. Buffington, E. Dinlersoz, L. S. Foster, N. Goldschlag, J. C. Haltiwanger, Z. Kroff, and K. Savage (2024, April). Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey.

Bonsu, E. M. and D. Baffour-Koduah (2023). From the consumers' side: Determining students' perception and intention to use chatgpt in ghanaian higher education. *Journal of Education, Society & Multiculturalism* *4*(1), 1–29.

Bresnahan, T. F. and M. Trajtenberg (1995). General purpose technologies 'engines of growth'? *Journal of econometrics* *65*(1), 83–108.

Brynjolfsson, E. and L. M. Hitt (2000). Beyond computation: Information technology, organizational transformation and business performance. *Journal of Economic Perspectives* *14*(4), 23–48.

Brynjolfsson, E., D. Li, and L. Raymond (2025, May). Generative AI at Work. *The Quarterly Journal of Economics* *140*(2), 889–942.

Brynjolfsson, E. and T. Mitchell (2017). What can machine learning do? workforce implications. *Science* *358*(6370), 1530–1534.

Carvajal, D., C. Franco, and S. Isaksson (2024). Will artificial intelligence get in the way of achieving gender equality? Discussion Paper 03, NHH Norwegian School of Economics.

Chatterji, A. K., T. Cunningham, D. J. Deming, Z. Hitzig, C. Ong, C. Y. Shan, and K. Wadman (2025). How people use ChatGPT. Working Paper 34255, National Bureau of Economic Research.

Comin, D. and B. Hobijn (2010a). An exploration of technology diffusion. *American Economic Review* *100*(5), 2031–2059.

Comin, D. and B. Hobijn (2010b). *Technology Diffusion and Postwar Growth*, Volume 25, pp. 209–246. University of Chicago Press.

Contractor, Z. and G. Reyes (2025). Experimental evidence on the learning impact of generative AI. Mimeo, Middlebury College.

Cruces, G., D. Fernández Meijide, S. Galiani, R. H. Gálvez, and M. Lombardi (2026). Does generative AI narrow education-based productivity gaps? evidence from a randomized experiment. Working Paper 34851, National Bureau of Economic Research.

Cui, Z. K., M. Demirer, S. Jaffe, L. Musolff, S. Peng, and T. Salz (2024, September). The Effects of Generative AI on High Skilled Work: Evidence from Three Field Experiments with Software Developers.

David, P. A. (1990). The dynamo and the computer: an historical perspective on the modern productivity paradox. *The American economic review* *80*(2), 355–361.

De Simone, M. E., F. H. Tiberti, M. R. Barron Rodriguez, F. A. Manolio, W. Mosuro, and E. J. Dikoru (2025). From chalkboards to chatbots: Evaluating the impact of generative AI on learning outcomes in Nigeria. Policy Research Working Paper 11125, World Bank.

Dell'Acqua, F., E. McFowland, E. R. Mollick, H. Lifshitz-Assaf, K. Kellogg, S. Rajendran, L. Krayer, F. Candelon, and K. R. Lakhani (2023, September). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality.

Duflo, E., M. Kremer, and J. Robinson (2011, October). Nudging Farmers to Use Fertilizer: Theory and Experimental Evidence from Kenya. *American Economic Review* *101*(6), 2350–2390.

Eloundou, T., S. Manning, P. Mishkin, and D. Rock (2024, June). are GPTs: Labor market impact potential of LLMs. *Science* *384*(6702), 1306–1308.

Fairlie, R. W., F. Hoffmann, and P. Oreopoulos (2014). A community college instructor like me: Race and ethnicity interactions in the classroom. *American Economic Review* *104*(8), 2567–2591.

Felten, E. W., M. Raj, and R. Seamans (2021, April). Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and Its Potential Uses.

Felten, E. W., M. Raj, and R. Seamans (2023, March). How will Language Modelers like ChatGPT Affect Occupations and Industries?

Flaherty, C. (2025, August). How AI is changing—not 'killing'—college. *Inside Higher Ed*.

Foster, A. D. and M. R. Rosenzweig (1995). Learning by doing and learning from others: Human capital and technical change in agriculture. *Journal of political Economy* *103*(6), 1176–1209.

Foster, A. D. and M. R. Rosenzweig (2010). Microeconomics of technology adoption. *Annu. Rev. Econ.* *2*(1), 395–424.

Freeman, J. (2025, February). Student generative AI survey 2025. Policy Note 61, Higher Education Policy Institute, Oxford, UK.

Gallup (2025, October). use at work rises. Q3 2025 workforce study, n=23,068, fielded August 5–19, 2025.

Giaccherini, M., D. H. Herberich, D. Jimenez-Gomez, J. A. List, G. Ponti, and M. K. Price (2019). The behavioralist goes door-to-door: Understanding household technological diffusion using a theory-driven natural field experiment. Technical report, National Bureau of Economic Research.

Goehring, G., F. Mezzanotti, and S. A. A. Ravid (2024). Technology adoption and career concerns: Evidence from the adoption of digital technology in motion pictures. Technical report, National Bureau of Economic Research.

Griliches, Z. (1957). Hybrid corn: An exploration in the economics of technological change. *Econometrica* *25*(4), 501–522.

Hall, B. H. and B. Khan (2003). Adoption of new technology.

Handa, K., D. Bent, A. Tamkin, M. McCain, E. Durmus, M. Stern, M. Schiraldi, S. Huang, S. Ritchie, S. Syverud, K. Jagadish, M. Vo, M. Bell, and D. Ganguli (2025). Anthropic education report: How university students use claude.

Handa, K., A. Tamkin, M. McCain, S. Huang, E. Durmus, S. Heck, J. Mueller, J. Hong, S. Ritchie, T. Belonax, et al. (2025). Which economic tasks are performed with AI? Evidence from millions of Claude conversations. *arXiv preprint arXiv:2503.04761*.

Hanna, R., S. Mullainathan, and J. Schwartzstein (2014, August). Learning Through Noticing: Theory and Evidence from a Field Experiment. *The Quarterly Journal of Economics* *129*(3), 1311–1353.

Hartley, J., F. Jolevski, V. Melo, and B. Moore (2026). The labor market effects of generative artificial intelligence. SSRN Scholarly Paper 5136877.

Hirabayashi, S., R. Jain, N. Jurković, and G. Wu (2024). Harvard undergraduate survey on generative AI. *arXiv preprint arXiv:2406.00833*.

Humlum, A. and E. Vestergaard (2025, May). Large Language Models, Small Labor Market Effects.

Hutto, C. and E. Gilbert (2014). Vader: A parsimonious rule-based model for sentiment analysis of social media text. In *Proceedings of the international AAAI conference on web and social media*, Volume 8, pp. 216–225.

Kelly, A., M. Sullivan, and K. Strampel (2023). Generative artificial intelligence: University student awareness, experience, and confidence in use across disciplines. *Journal of University Teaching and Learning Practice* *20*(6), 1–16.

Kestin, G., K. Miller, A. Klales, T. Milbourne, and G. Ponti (2025). tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports* *15*, 17458.

Kharazian, A. (2025). Ramp ai index: Monthly measurement of ai adoption by american businesses. Technical report, Ramp Economics Lab.

Kim, J., H. Lee, J. Park, and K. R. Koedinger (2025). Generative AI can improve performance and engagement without harming learning. Technical report, KAIST.

Lehmann, M., P. B. Cornelius, and F. J. Sting (2025, March). the Classroom: When Do Large Language Models Harm Learning?

Ling, Y., A. Kale, and A. Imas (2025). Underreporting of ai use: The role of social desirability bias. *Available at SSRN 5464215*.

Lira, B., T. Rogers, D. G. Goldstein, L. Ungar, and A. L. Duckworth (2025). Coach not crutch: Evidence that AI can improve writing skill despite reducing effort. Technical report, University of Pennsylvania. arXiv:2502.02880.

Liu, Y. and H. Wang (2024, August). Who on earth is using generative ai? Policy Research Working Paper WPS10870, World Bank Group, Washington, D.C.

McClain, C. (2024, March). Americans' use of ChatGPT is ticking up, but few trust its election information.

McClain, C. (2025, June). of U.S. adults have used ChatGPT, about double the share in 2023. Survey of 5,123 U.S. adults, fielded February 24–March 2, 2025.

McDonald, N., A. Johri, A. Ali, and A. H. Collier (2025, March). Generative artificial intelligence in higher education: Evidence from an analysis of institutional policies and guidelines. *Computers in Human Behavior: Artificial Humans* *3*, 100121.

McElheran, K., J. F. Li, E. Brynjolfsson, Z. Kroff, E. Dinlersoz, L. S. Foster, and N. Zolas (2023, October). in America: Who, What, and Where.

Merchant, B. (2024, February). The new luddites aren't backing down. *The Atlantic*. Accessed: 2025-06-16.

Nam, J. (2023, November). % of college students have used ai on assignments or exams. Technical report. Edited by Lyss Welding. Accessed June 11, 2025.

National Survey of Student Engagement (2020). Nsse 2020 response rates higher despite pandemic. Accessed: 2025-02-08.

Nolan, B. (2023). Here are the schools and colleges that have banned chatgpt. *Business Insider*. Accessed: 2025-01-27.

Noy, S. and W. Zhang (2023, March). Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence.

Otis, N. G., S. Delecourt, K. Cranney, and R. Koning (2024). *Global Evidence on Gender Gaps and Generative AI*. Harvard Business School.

Peng, S., E. Kalliamvakou, P. Cihon, and M. Demirer (2023, February). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot.

Ravšelj, D., D. Keržič, N. Tomaževič, L. Umek, N. Brezovar, et al. (2025, February). Higher education students' perceptions of ChatGPT: A global study of early reactions. *PLOS ONE* *20*(2), e0315011.

Rogers, E. M. (1962). *Diffusion of Innovations*. New York: Free Press.

Sacerdote, B. (2001). Peer Effects with Random Assignment: Results for Dartmouth Roommates. *The Quarterly Journal of Economics* *116*(2), 681–704.

Stinebrickner, R. and T. R. Stinebrickner (2008). The causal effect of studying on academic performance. *The BE Journal of Economic Analysis & Policy* *8*(1).

Stöhr, C., A. W. Ou, and H. Malmström (2024, December). Perceptions and usage of AI chatbots among students in higher education across genders, academic levels and fields of study. *Computers and Education: Artificial Intelligence* *7*, 100259.

Stokey, N. L. (2021). Technology diffusion. *Review of Economic Dynamics* *42*, 15–36.

The Middlebury Campus (2025, May). Zeitgeist 7.0. The Middlebury Campus. <https://www.middleburycampus.com/article/2025/05/zeitgeist-7-0>.

World Bank (2016). *World development report 2016: Digital dividends*. World Bank Publications.

Xiao, P., Y. Chen, and W. Bao (2023). Waiting, banning, and embracing: An empirical analysis of adapting policies for generative ai in higher education. *arXiv preprint arXiv:2305.18617*.

</div>

</div>

# Figures and Tables
<figure id="fig:ai_use" data-latex-placement="H">
<embed src="results/ai_use_demog.pdf" />
<p><em>Notes:</em> This figure shows the fraction of students who report using AI during the academic semester, categorized by demographic characteristics, high school type, academic cohort, GPA, and field of study. Usage frequency is divided into four levels: “Rarely” (a few times a semester), “Occasionally” (a few times a month), “Frequently” (a few times a week), and “Very Frequently” (daily or almost daily).</p>
<p>The category “All students” provides the baseline usage rate for the full sample. Gender categories are based on self-identification, with non-binary responses excluded due to a small sample size. “Private HS” refers to students who attended private high schools, while “Public HS” includes public institutions. “Cohort” denotes the student’s academic year, ranging from first-year (“Freshman”) to fourth-year and beyond (“Senior”). GPA categories (“GPA <span class="math inline">&gt;</span> p50” and “GPA <span class="math inline">&lt;</span> p50”) split students into groups above or below the median first-year GPA, as self-reported on a 4.0 scale. See Appendix <a href="#app:fields" data-reference-type="ref" data-reference="app:fields">9.2</a> for the classification of majors into fields of study.</p>
<figcaption>The Adoption of Generative AI among Middlebury College Students</figcaption>
</figure>

<figure id="fig:ai_use_time" data-latex-placement="H">
<embed src="results/ai_use_time.pdf" />
<p><em>Notes:</em> This figure shows the cumulative percent of students who reported using generative AI tools for academic purposes over time. The data are based on retrospective self-reports collected in our December 2024 survey, where students were asked “When did you first start using any form of Generative AI for academic purposes?” Response options ranged from “Before Spring 2023” to “This semester (Fall 2024).” The <span class="math inline"><em>x</em></span>-axis represents academic semesters, while the <span class="math inline"><em>y</em></span>-axis represents the cumulative adoption rate. Vertical lines represent 95 percent confidence intervals calculated from the standard error of the proportion.</p>
<figcaption>The Evolution of Generative AI Adoption among Middlebury College Students</figcaption>
</figure>

<figure id="fig:ai_models" data-latex-placement="H">
<embed src="results/ai_use_model.pdf" />
<p><em>Notes:</em> This figure shows the adoption rates of various AI models as of Fall 2024. The horizontal axis shows the percent of students who reported using each tool, and the vertical axis lists the tools in descending order of adoption rates.</p>
<figcaption>Adoption of Generative AI Models Among College Students</figcaption>
</figure>

<figure data-latex-placement="H">
<div class="center">
<figure>
<embed src="results/ai_use_purpose.pdf" />
<figcaption>Panel A. Across Common Academic Tasks</figcaption>
</figure>
<figure>
<embed src="results/ai_use_automation.pdf" />
<figcaption>Panel B. Across Tasks that Augment versus Automate Student Effort</figcaption>
</figure>
</div>
<p><em>Notes:</em> This figure shows the percent of AI students who use generative AI for different academic tasks. For each task, usage frequency is divided into four levels: “Rarely” (a few times a semester), “Occasionally” (a few times a month), “Frequently” (a few times a week), and “Very Frequently” (daily or almost daily). The number at the end of each bar represents the total percent of students who use AI for that purpose at any frequency. Tasks are ordered by total usage, from highest to lowest. Results are based on responses to the question: “For academic purposes, which of the following tasks do you typically use generative AI for?” Sample includes all students who reported using AI during the academic semester.</p>
<figcaption>Panel B. Across Tasks that Augment versus Automate Student Effort</figcaption>
</figure>

<figure id="fig:ai_policy" data-latex-placement="H">
<embed src="results/ai_policy_impact.pdf" />
<p><em>Notes:</em> This figure shows the percent of students who report different likelihoods of using AI under various policy scenarios. For each policy, responses are categorized on a five-point scale from “Extremely unlikely to use AI” to “Extremely likely to use AI.” The sample includes all survey respondents. The question asked was: “How likely are you to use generative AI in a class with each of the following AI policies?”</p>
<figcaption>Student Reported Likelihood of Using AI under Different Policies</figcaption>
</figure>

<figure data-latex-placement="H">
<div class="center">
<figure>
<embed src="results/policy_understanding_dem.pdf" />
<figcaption>Panel A. Understanding of AI Policies</figcaption>
</figure>
<figure>
<embed src="results/ai_copilot_dem.pdf" />
<figcaption>Panel B. Awareness of Copilot Access</figcaption>
</figure>
<figure>
<embed src="results/ai_cite_dem.pdf" />
<figcaption>Panel C. Knowledge of Citation Requirements</figcaption>
</figure>
</div>
<p><em>Notes:</em> This figure shows students’ understanding of institutional AI policies and resources. Panel A displays the percent of students who report understanding AI policies in their classes, those who report having no explicit policy, and those who find policies unclear, broken down by demographic characteristics. Panel B shows the percent of students who are aware of their free access to Microsoft Copilot through Middlebury College. Panel C presents the percent of students who report knowing how to properly cite AI use in their academic work when required. For Panels B and C, horizontal lines represent 95 percent confidence intervals. Sample includes all survey respondents.</p>
<figcaption>Panel C. Knowledge of Citation Requirements</figcaption>
</figure>

<figure id="fig:ai_learning" data-latex-placement="H">
<embed src="results/ai_learning_impact.pdf" />
<p><em>Notes:</em> This figure shows the percent of Middlebury students who believe that AI improves, reduces, or has no effect on different aspects of their academic experience. For each outcome, responses are categorized into three groups: “Improves” combines “significantly improves” and “somewhat improves” responses, “Reduces” combines “significantly reduces” and “somewhat reduces” responses, and “No effect” represents neutral responses. Sample includes all survey respondents who answered the question. “Don’t know” responses are excluded.</p>
<figcaption>Student Beliefs about the Impact of AI on their Academic Performance</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="results/ai_beliefs_learn.pdf" />
<figcaption>Panel A. Learning ability</figcaption>
</figure>
<figure>
<embed src="results/ai_beliefs_understand.pdf" />
<figcaption>Panel B. Understanding of course materials</figcaption>
</figure>
<p><br />
 <br />
</p>
<figure>
<embed src="results/ai_beliefs_ontime.pdf" />
<figcaption>Panel C. Complete assignments on time</figcaption>
</figure>
<figure>
<embed src="results/ai_beliefs_grades.pdf" />
<figcaption>Panel D. Course grades</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the relationship between AI adoption rates and beliefs that AI improves various academic outcomes across different student groups. Each panel plots the percentage who believe AI improves a specific outcome (<span class="math inline"><em>x</em></span>-axis) against the percent of students who use AI (<span class="math inline"><em>y</em></span>-axis). Points represent different student groups categorized by demographics (circles), academic characteristics (triangles), and field of study (squares). The dashed line shows the linear fit across all groups. Groups with fewer than ten students are not plotted.</p>
<figcaption>Panel D. Course grades</figcaption>
</figure>

<figure id="fig:beliefs_corr" data-latex-placement="H">
<embed src="results/beliefs_use_corr.pdf" />
<p><em>Notes:</em> This figure shows the relationship between students’ beliefs about AI usage among their peers and actual AI usage rates across different demographic groups. Each point represents a different group of students (by demographics, academic characteristics, or field of study). The <span class="math inline"><em>y</em></span>-axis shows the percent of students in each group who use AI at least occasionally for academic purposes. The <span class="math inline"><em>x</em></span>-axis shows the mean belief within each group about what percent of Middlebury students use AI. The dashed horizontal line shows the overall true rate of AI use at least occasionally (61.6 percent). Sample includes all survey respondents with at least ten observations per group.</p>
<figcaption>Relationship Between Beliefs About AI Usage and Actual AI Usage</figcaption>
</figure>

<div class="center">

<div class="singlespace">

<div id="tab:summ_stats">

+-----------------------------------+-------------------------+---------------+
|                                   | Survey Sample           | Admin records |
+:==================================+:==========:+:==========:+:=============:+
| 2-3                               | Unweighted | Weighted   |               |
+-----------------------------------+------------+------------+---------------+
|                                   | \(1\)      | \(2\)      | \(3\)         |
+-----------------------------------+------------+------------+---------------+
| **Panel A. Demographics**                                                   |
+-----------------------------------+------------+------------+---------------+
| Male                              | 0.446      | 0.433      | 0.463         |
+-----------------------------------+------------+------------+---------------+
| Female                            | 0.508      | 0.516      | 0.533         |
+-----------------------------------+------------+------------+---------------+
| White                             | 0.618      | 0.603      | 0.538         |
+-----------------------------------+------------+------------+---------------+
| Black                             | 0.036      | 0.033      | 0.052         |
+-----------------------------------+------------+------------+---------------+
| Hispanic                          | 0.099      | 0.106      | 0.124         |
+-----------------------------------+------------+------------+---------------+
| Asian                             | 0.155      | 0.162      | 0.073         |
+-----------------------------------+------------+------------+---------------+
| Private high school               | 0.420      | 0.399      | –            |
+-----------------------------------+------------+------------+---------------+
| Public high school                | 0.543      | 0.556      | –            |
+-----------------------------------+------------+------------+---------------+
| **Panel B. Academic Characteristics**                                       |
+-----------------------------------+------------+------------+---------------+
| GPA                               | 3.740      | 3.736      | 3.670         |
+-----------------------------------+------------+------------+---------------+
| Hours spent on academics per week | 17.899     | 17.889     | –            |
+-----------------------------------+------------+------------+---------------+
| Freshman                          | 0.311      | 0.355      | 0.255         |
+-----------------------------------+------------+------------+---------------+
| Sophomore                         | 0.273      | 0.272      | 0.257         |
+-----------------------------------+------------+------------+---------------+
| Junior                            | 0.202      | 0.179      | 0.201         |
+-----------------------------------+------------+------------+---------------+
| Senior                            | 0.213      | 0.194      | 0.287         |
+-----------------------------------+------------+------------+---------------+
| **Panel C. Field of Study**                                                 |
+-----------------------------------+------------+------------+---------------+
| Arts                              | 0.017      | 0.028      | 0.023         |
+-----------------------------------+------------+------------+---------------+
| Humanities                        | 0.071      | 0.091      | 0.073         |
+-----------------------------------+------------+------------+---------------+
| Languages                         | 0.025      | 0.025      | 0.025         |
+-----------------------------------+------------+------------+---------------+
| Literature                        | 0.047      | 0.040      | 0.025         |
+-----------------------------------+------------+------------+---------------+
| Natural Sciences                  | 0.336      | 0.390      | 0.244         |
+-----------------------------------+------------+------------+---------------+
| Social Sciences                   | 0.468      | 0.385      | 0.243         |
+-----------------------------------+------------+------------+---------------+
| Has not declared major            | 0.035      | 0.041      | 0.364         |
+-----------------------------------+------------+------------+---------------+
| N (# degrees)                     | 43         | 43         | 49            |
+-----------------------------------+------------+------------+---------------+
| N (# students)                    | 634        | 2,760      | 2,760         |
+-----------------------------------+------------+------------+---------------+

: Summary Statistics of Survey Participants

</div>

</div>

</div>

<div class="singlespace">

*Notes:* This table presents summary statistics from our survey of college students. Panel A reports demographic characteristics, including the proportion of participants identifying as male, female, white, Black, Hispanic, Asian, or who attended a private or public high school. Panel B provides academic characteristics, such as GPA (only available for non-freshmen), average weekly hours spent on academics, and academic year distribution (Freshman, Sophomore, Junior, and Senior). Note that in column 1–2, GPA refers to self-reported first-year GPA while in column 3 it is the overall GPA during Spring 2024. Panel C summarizes the distribution of participants across different fields of study. Major groups are mutually exclusive.

</div>

<div class="center">

<div id="tab:ai_usage_correlates">

+----------------+---+-----------------------------------------------------------------------------------------------------------------------------------+
|                |   | Outcome: Uses AI during the semester with frequency of at least\...                                                               |
+:===============+:==+=================:+:============+=================:+:============+=================:+:============+=================:+:===========:+
| 3-10           |   | A few times      |             | A few times      |             | A few times      |             | Daily or almost  |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | a semester       |             | a month          |             | a week           |             | daily            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | \(1\)            |             | \(2\)            |             | \(3\)            |             | \(4\)            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Male           |   | 0.103            | $^{***}$    | 0.164            | $^{***}$    | 0.205            | $^{***}$    | 0.092            | $^{***}$    |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.033           | )           | (0.043           | )           | (0.043           | )           | (0.030           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Black          |   | 0.136            | $^{***}$    | 0.222            | $^{**}$     | 0.186            |             | 0.026            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.047           | )           | (0.095           | )           | (0.117           | )           | (0.076           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Latino         |   | $-$0.004 |             | 0.051            |             | $-$0.026 |             | $-$0.023 |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.060           | )           | (0.073           | )           | (0.065           | )           | (0.038           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Asian          |   | 0.114            | $^{***}$    | 0.173            | $^{***}$    | 0.097            |             | 0.052            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.038           | )           | (0.056           | )           | (0.059           | )           | (0.041           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Public HS      |   | $-$0.041 |             | $-$0.060 |             | $-$0.043 |             | $-$0.014 |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.033           | )           | (0.043           | )           | (0.042           | )           | (0.026           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Sophomores     |   | 0.051            |             | 0.056            |             | 0.075            |             | 0.061            | $^{*}$      |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.043           | )           | (0.055           | )           | (0.052           | )           | (0.035           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Juniors        |   | 0.071            |             | 0.119            | $^{**}$     | 0.125            | $^{**}$     | 0.066            | $^{*}$      |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.045           | )           | (0.060           | )           | (0.062           | )           | (0.037           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Seniors        |   | 0.012            |             | 0.054            |             | 0.104            | $^{*}$      | 0.040            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.048           | )           | (0.061           | )           | (0.059           | )           | (0.039           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Arts           |   | $-$0.180 |             | $-$0.177 |             | 0.054            |             | $-$0.078 |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.116           | )           | (0.153           | )           | (0.158           | )           | (0.098           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Humanities     |   | $-$0.121 | $^{*}$      | $-$0.230 | $^{***}$    | $-$0.207 | $^{***}$    | $-$0.112 | $^{***}$    |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.069           | )           | (0.084           | )           | (0.075           | )           | (0.028           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Languages      |   | $-$0.239 | $^{*}$      | $-$0.164 |             | $-$0.245 | $^{***}$    | $-$0.094 | $^{***}$    |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.134           | )           | (0.137           | )           | (0.067           | )           | (0.029           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Literature     |   | $-$0.326 | $^{***}$    | $-$0.177 | $^{*}$      | $-$0.185 | $^{**}$     | $-$0.097 | $^{***}$    |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.095           | )           | (0.101           | )           | (0.083           | )           | (0.023           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Social Sci.    |   | $-$0.036 |             | 0.032            |             | 0.055            |             | 0.028            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
|                |   | (0.036           | )           | (0.047           | )           | (0.048           | )           | (0.033           | )           |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| Mean Dep. Var. |   | 0.825            |             | 0.589            |             | 0.368            |             | 0.106            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| R$-$squared    |   | 0.084            |             | 0.087            |             | 0.106            |             | 0.057            |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+
| $N$ (Students) |   | 616              |             | 616              |             | 616              |             | 616              |             |
+----------------+---+------------------+-------------+------------------+-------------+------------------+-------------+------------------+-------------+

: Student Characteristics Associated with Frequency of Generative AI Use

</div>

</div>

<div class="singlespace">

*Notes:* This table assesses the relationship between AI adoption and student characteristics. We estimate: $$Y_{i} = \alpha + \beta X_i + \varepsilon_{i},$$ where $Y_i$ is a binary indicator of AI usage frequency threshold and $X_i$ is a vector of student characteristics including gender, race/ethnicity, high school type, cohort indicators, and academic division.

Each column uses a different threshold for AI usage frequency, categorized as: "Rarely" (a few times a semester), "Occasionally" (a few times a month), "Frequently" (a few times a week), and "Very Frequently" (daily or almost daily). Column 1 defines usage as any nonzero frequency; column 2 includes at least occasional use; column 3 includes frequent or higher use; and column 4 captures only very frequent use.

The omitted categories are: Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, freshmen for cohort, female for gender, and private high school for school type. Heteroskedasticity-robust standard errors clustered at the student level in parentheses. Observations are weighted to adjust for sampling. \* $p<0.10$, \*\* $p<0.05$, \*\*\* $p<0.01$.

</div>

<div class="center">

<div id="tab:ai_adopt_correlates">

+----------------+---+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                |   | Outcome: Started using generative AI\...                                                                                                            |
+:===============+:==+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:========:+
| 3-12           |   | Before           |          | Spring 2023      |          | Fall 2023        |          | Spring 2024      |          | Fall 2024        |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | Spring 2023      |          | or before        |          | or before        |          | or before        |          | or before        |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | \(1\)            |          | \(2\)            |          | \(3\)            |          | \(4\)            |          | \(5\)            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Male           |   | 0.087            | $^{***}$ | 0.152            | $^{***}$ | 0.220            | $^{***}$ | 0.131            | $^{***}$ | 0.086            | $^{**}$  |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.024           | )        | (0.035           | )        | (0.041           | )        | (0.043           | )        | (0.035           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Black          |   | $-$0.020 |          | 0.033            |          | 0.057            |          | 0.184            | $^{*}$   | 0.157            | $^{***}$ |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.058           | )        | (0.100           | )        | (0.108           | )        | (0.100           | )        | (0.047           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Latino         |   | $-$0.013 |          | 0.032            |          | 0.034            |          | $-$0.044 |          | $-$0.022 |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.037           | )        | (0.054           | )        | (0.063           | )        | (0.070           | )        | (0.063           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Asian          |   | 0.037            |          | 0.024            |          | 0.129            | $^{**}$  | 0.151            | $^{***}$ | 0.136            | $^{***}$ |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.039           | )        | (0.049           | )        | (0.058           | )        | (0.057           | )        | (0.038           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Public HS      |   | $-$0.013 |          | $-$0.056 |          | $-$0.084 | $^{**}$  | $-$0.014 |          | $-$0.068 | $^{**}$  |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.024           | )        | (0.035           | )        | (0.041           | )        | (0.043           | )        | (0.034           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Sophomores     |   | $-$0.056 | $^{*}$   | $-$0.071 | $^{*}$   | 0.029            |          | 0.177            | $^{***}$ | 0.039            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.030           | )        | (0.042           | )        | (0.050           | )        | (0.055           | )        | (0.045           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Juniors        |   | $-$0.051 |          | $-$0.068 |          | 0.074            |          | 0.242            | $^{***}$ | 0.065            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.034           | )        | (0.049           | )        | (0.061           | )        | (0.059           | )        | (0.047           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Seniors        |   | $-$0.063 | $^{*}$   | $-$0.009 |          | 0.070            |          | 0.135            | $^{**}$  | 0.018            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.032           | )        | (0.052           | )        | (0.058           | )        | (0.060           | )        | (0.049           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Arts           |   | 0.023            |          | $-$0.130 |          | 0.138            |          | 0.059            |          | $-$0.161 |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.102           | )        | (0.117           | )        | (0.125           | )        | (0.125           | )        | (0.113           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Humanities     |   | $-$0.019 |          | 0.003            |          | $-$0.079 |          | $-$0.021 |          | $-$0.109 |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.036           | )        | (0.066           | )        | (0.082           | )        | (0.085           | )        | (0.071           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Languages      |   | $-$0.037 | $^{*}$   | $-$0.135 | $^{***}$ | $-$0.324 | $^{***}$ | $-$0.287 | $^{**}$  | $-$0.235 | $^{*}$   |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.020           | )        | (0.037           | )        | (0.051           | )        | (0.124           | )        | (0.133           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Literature     |   | 0.082            |          | 0.084            |          | $-$0.075 |          | $-$0.103 |          | $-$0.300 | $^{***}$ |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.071           | )        | (0.093           | )        | (0.096           | )        | (0.103           | )        | (0.095           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Social Sci.    |   | 0.019            |          | 0.032            |          | $-$0.038 |          | 0.021            |          | $-$0.025 |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.027           | )        | (0.038           | )        | (0.044           | )        | (0.047           | )        | (0.038           | )        |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Mean Dep. Var. |   | 0.089            |          | 0.199            |          | 0.357            |          | 0.551            |          | 0.801            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| R$-$squared    |   | 0.043            |          | 0.061            |          | 0.095            |          | 0.081            |          | 0.075            |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| $N$ (Students) |   | 633              |          | 633              |          | 633              |          | 633              |          | 633              |          |
+----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+

: Student Characteristics Associated with Timing of Generative AI Adoption

</div>

</div>

<div class="singlespace">

*Notes:* This table assesses the relationship between AI adoption and student characteristics. We estimate: $$Y_{i} = \alpha + \beta X_i + \varepsilon_{i},$$ where $Y_i$ is a binary indicator of AI adoption date and $X_i$ is a vector of student characteristics including gender, race/ethnicity, high school type, cohort indicators, and academic division. Each column presents results for a different threshold of AI adoption. Column 1 shows the probability of adopting AI before Spring 2023; column 2 by Spring 2023; column 3 by Fall 2023; column 4 by Spring 2024; and column 5 by Fall 2024. The dependent variable in each regression is a binary indicator equal to one if the student had adopted AI by the specified time period.

The omitted categories are: Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, freshmen for cohort, female for gender, and private high school for school type. Heteroskedasticity-robust standard errors clustered at the student level in parentheses. Observations are weighted to adjust for sampling. \* $p<0.10$, \*\* $p<0.05$, \*\*\* $p<0.01$.

</div>

<div class="landscape">

<div class="center">

<div id="tab:ai_autom_regs">

+----------------+---+----------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|                |   | Augmentation Tasks                                                                     | Automation Tasks                                                                      | Difference: Augm. - Autom.                                |
+:===============+:==+=================:+:========+=================:+:=========+=================:+:========:+=================:+:=======+=================:+:=========+=================:+:========:+=================:+:=========+=================:+:========:+
| 3-7            |   | Any $>0$         |         | Share $>0$       |          | Intensity        |          | Any $>0$         |        | Share $>0$       |          | Intensity        |          | Share            |          | Intensity        |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | \(1\)            |         | \(2\)            |          | \(3\)            |          | \(4\)            |        | \(5\)            |          | \(6\)            |          | \(7\)            |          | \(8\)            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Male           |   | 0.052            | $^{**}$ | 0.080            | $^{***}$ | 0.237            | $^{***}$ | 0.029            |        | 0.095            | $^{***}$ | 0.272            | $^{***}$ | $-$0.016 |          | $-$0.035 |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.026           | )       | (0.028           | )        | (0.076           | )        | (0.027           | )      | (0.024           | )        | (0.059           | )        | (0.023           | )        | (0.055           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Black          |   | $-$0.009 |         | 0.053            |          | 0.446            | $^{**}$  | $-$0.008 |        | 0.109            |          | 0.477            | $^{**}$  | $-$0.056 |          | $-$0.031 |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.080           | )       | (0.068           | )        | (0.220           | )        | (0.083           | )      | (0.069           | )        | (0.199           | )        | (0.052           | )        | (0.155           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Latino         |   | 0.064            | $^{*}$  | 0.074            | $^{*}$   | 0.241            | $^{**}$  | 0.049            |        | 0.088            | $^{**}$  | 0.277            | $^{***}$ | $-$0.014 |          | $-$0.036 |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.034           | )       | (0.042           | )        | (0.118           | )        | (0.035           | )      | (0.043           | )        | (0.104           | )        | (0.041           | )        | (0.091           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Asian          |   | 0.055            | $^{*}$  | 0.066            | $^{*}$   | 0.180            | $^{*}$   | 0.058            | $^{*}$ | 0.050            | $^{*}$   | 0.156            | $^{**}$  | 0.016            |          | 0.025            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.031           | )       | (0.035           | )        | (0.095           | )        | (0.031           | )      | (0.028           | )        | (0.069           | )        | (0.030           | )        | (0.074           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Public HS      |   | $-$0.003 |         | $-$0.028 |          | $-$0.018 |          | $-$0.019 |        | $-$0.005 |          | $-$0.007 |          | $-$0.024 |          | $-$0.011 |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.029           | )       | (0.028           | )        | (0.076           | )        | (0.028           | )      | (0.024           | )        | (0.058           | )        | (0.023           | )        | (0.056           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Sophomores     |   | 0.033            |         | 0.020            |          | 0.059            |          | $-$0.002 |        | 0.003            |          | 0.018            |          | 0.017            |          | 0.041            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.032           | )       | (0.034           | )        | (0.091           | )        | (0.033           | )      | (0.030           | )        | (0.070           | )        | (0.027           | )        | (0.065           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Juniors        |   | 0.049            |         | 0.099            | $^{**}$  | 0.232            | $^{**}$  | $-$0.020 |        | 0.033            |          | 0.119            |          | 0.067            | $^{**}$  | 0.113            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.038           | )       | (0.039           | )        | (0.104           | )        | (0.041           | )      | (0.035           | )        | (0.086           | )        | (0.033           | )        | (0.076           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Seniors        |   | $-$0.013 |         | 0.081            | $^{**}$  | 0.313            | $^{***}$ | 0.017            |        | 0.018            |          | 0.150            | $^{*}$   | 0.063            | $^{*}$   | 0.163            | $^{*}$   |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.042           | )       | (0.040           | )        | (0.115           | )        | (0.031           | )      | (0.030           | )        | (0.081           | )        | (0.033           | )        | (0.083           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Arts           |   | 0.001            |         | $-$0.377 | $^{***}$ | $-$0.840 | $^{***}$ | $-$0.104 |        | $-$0.030 |          | 0.042            |          | $-$0.347 | $^{***}$ | $-$0.882 | $^{***}$ |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.069           | )       | (0.075           | )        | (0.159           | )        | (0.118           | )      | (0.065           | )        | (0.166           | )        | (0.084           | )        | (0.197           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Humanities     |   | $-$0.096 |         | $-$0.199 | $^{***}$ | $-$0.561 | $^{***}$ | 0.025            |        | $-$0.073 | $^{*}$   | $-$0.188 | $^{*}$   | $-$0.126 | $^{***}$ | $-$0.373 | $^{***}$ |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.063           | )       | (0.049           | )        | (0.115           | )        | (0.048           | )      | (0.041           | )        | (0.099           | )        | (0.046           | )        | (0.095           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Languages      |   | $-$0.146 |         | $-$0.279 | $^{***}$ | $-$0.582 | $^{***}$ | $-$0.015 |        | $-$0.045 |          | $-$0.157 |          | $-$0.234 | $^{***}$ | $-$0.424 | $^{***}$ |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.143           | )       | (0.094           | )        | (0.211           | )        | (0.110           | )      | (0.055           | )        | (0.121           | )        | (0.061           | )        | (0.133           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Literature     |   | $-$0.103 |         | $-$0.160 | $^{**}$  | $-$0.474 | $^{***}$ | $-$0.076 |        | $-$0.062 |          | $-$0.097 |          | $-$0.098 | $^{*}$   | $-$0.377 | $^{***}$ |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.094           | )       | (0.079           | )        | (0.164           | )        | (0.100           | )      | (0.058           | )        | (0.144           | )        | (0.056           | )        | (0.121           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Social Sci.    |   | $-$0.001 |         | $-$0.014 |          | 0.054            |          | 0.039            |        | 0.061            | $^{**}$  | 0.233            | $^{***}$ | $-$0.076 | $^{***}$ | $-$0.179 | $^{***}$ |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                |   | (0.029           | )       | (0.030           | )        | (0.086           | )        | (0.029           | )      | (0.027           | )        | (0.066           | )        | (0.024           | )        | (0.059           | )        |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Mean Dep. Var. |   | 0.917            |         | 0.560            |          | 2.159            |          | 0.916            |        | 0.454            |          | 1.885            |          | 0.106            |          | 0.274            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| R$-$squared    |   | 0.041            |         | 0.127            |          | 0.133            |          | 0.026            |        | 0.090            |          | 0.147            |          | 0.098            |          | 0.107            |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| $N$ (Students) |   | 515              |         | 515              |          | 515              |          | 515              |        | 515              |          | 515              |          | 515              |          | 515              |          |
+----------------+---+------------------+---------+------------------+----------+------------------+----------+------------------+--------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+

: Student Characteristics Associated with Task Augmentation and Automation

</div>

</div>

<div class="singlespace">

*Notes:* This table reports estimated associations between student characteristics and their use of generative AI for academic tasks. In columns 1 and 4, the outcome is a dummy that equals one if a student reports using AI with any frequency for at least one augmentation or automation task, respectively. In columns 2 and 5, the outcome is the share of tasks within each category for which the student reports any use. In columns 3 and 6, the outcome is a continuous measure capturing average usage frequency for each task category, based on raw Likert-style responses. In columns 7 and 8, the outcome is the difference in average task share and usage intensity between augmentation and automation, respectively. Regressions are weighted and report robust standard errors clustered at the student level. $^{***}$ $p<0.01$, $^{**}$ $p<0.05$, $^*$ $p<0.10$.

</div>

</div>

<div class="center">

</div>

# Appendix Figures and Tables

<figure id="fig:flow" data-latex-placement="H">
<div class="center">

</div>
<p><span><em>Note:</em> This figure illustrates the structure of the AI usage survey conducted at Middlebury College in December 2024. The survey collected information across three main sections: (1) demographic and academic background, (2) patterns of generative AI usage including adoption timing, frequency, and specific applications, and (3) perceptions of AI’s impact on learning and responses to institutional policies.</span></p>
<figcaption>Generative AI Usage Survey Design Overview</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="results/ai_use_time_gender.pdf" />
<figcaption>Panel A. By Gender</figcaption>
</figure>
<figure>
<embed src="results/ai_use_time_race.pdf" />
<figcaption>Panel B. By Race</figcaption>
</figure>
<figure>
<embed src="results/ai_use_time_hs.pdf" />
<figcaption>Panel C. By High School Type</figcaption>
</figure>
<figure>
<embed src="results/ai_use_time_gpa.pdf" />
<figcaption>Panel D. By Freshman Year GPA</figcaption>
</figure>
<figure>
<embed src="results/ai_use_time_coh.pdf" />
<figcaption>Panel E. By Cohort</figcaption>
</figure>
<figure>
<embed src="results/ai_use_time_field.pdf" />
<figcaption>Panel F. By Field of Study</figcaption>
</figure>
<p><em>Notes:</em> This figure presents cumulative AI use based on different student characteristics. Each panel displays the cumulative distribution of AI use based on a specific characteristic: gender, race, school type, first-year GPA, cohort, or field of study. The cumulative percent of students is plotted against usage categories. The legends and colors correspond to subgroups within each demographic variable.</p>
<figcaption>Panel F. By Field of Study</figcaption>
</figure>

<figure id="fig:ai_pays_dem" data-latex-placement="H">
<embed src="results/ai_pays_dem.pdf" />
<p><em>Notes:</em> This figure shows the percent of AI users who pay for AI tools (through any platform) across different demographic groups. Horizontal lines represent 95 percent confidence intervals calculated with heteroskedasticity-robust standard errors clustered at the student level.</p>
<figcaption>Percent of Students Who Pay for Generative AI Tools</figcaption>
</figure>

<figure data-latex-placement="htbp">
<div class="center">
<figure>
<embed src="results/global_ai_use_automation.pdf" />
<figcaption>Panel A. Across Tasks that Augment versus Automate Student Effort</figcaption>
</figure>
<figure>
<embed src="results/global_ai_quality.pdf" />
<figcaption>Panel B. Across the College Quality Distribution</figcaption>
</figure>
</div>
<p><em>Notes:</em> This figure shows the percent of students who use ChatGPT for different academic tasks based on data from Ravšelj et al. (2025). Panel A displays usage patterns across tasks categorized as augmenting (proofreading, translating, study assistance, research assistance) versus automating (academic writing, professional writing, creative writing, brainstorming, summarizing, calculating, coding assistance, personal assistance) student effort. Panel B shows usage patterns across university quality quintiles based on World University Rankings, with universities ranked in the top 20 percent (top quintile) showing slightly higher rates of augmentation relative to automation compared to bottom quintile institutions. The analysis includes universities with at least 30 student responses and excludes observations with missing usage data.</p>
<figcaption>Panel B. Across the College Quality Distribution</figcaption>
</figure>

<div class="landscape">

<figure data-latex-placement="htpb!">
<div class="center">
<figure>
<embed src="results/beliefs_schoolwork.pdf" />
<figcaption>Panel A. For Schoolwork</figcaption>
</figure>
<figure>
<embed src="results/beliefs_leisure.pdf" />
<figcaption>Panel B. For Leisure</figcaption>
</figure>
<figure>
<embed src="results/beliefs_anypurpose.pdf" />
<figcaption>Panel C. For Any Purpose</figcaption>
</figure>
<figure>
<embed src="results/beliefs_class_nopolicy.pdf" />
<figcaption>Panel D. Classes with No Policy</figcaption>
</figure>
<figure>
<embed src="results/beliefs_class_allows.pdf" />
<figcaption>Panel E. Classes that Allow AI</figcaption>
</figure>
<figure>
<embed src="results/beliefs_class_disallows.pdf" />
<figcaption>Panel F. Classes that Disallow AI</figcaption>
</figure>
</div>
<p><em>Notes:</em> This figure shows the distribution of students’ beliefs about generative AI usage among their peers at Middlebury College. Panels A–C display students’ estimates of the percent of their peers who regularly use AI for schoolwork, leisure activities, and any purpose, respectively. Panels D–F show students’ beliefs about AI usage in classes with different AI policies: those without an explicit policy (Panel D), those that allow AI use (Panel E), and those that prohibit AI use (Panel F). Each panel shows a histogram with bins of width ten percentage points (e.g., responses between 1–10 fall in the 10 bin, 11–20 in the 20 bin, etc.). The red dashed line indicates the mean response. Sample excludes respondents with missing values or who selected the default response for all six categories (which equals zero).</p>
<figcaption>Panel F. Classes that Disallow AI</figcaption>
</figure>

</div>

<div class="center">

<div class="singlespace">

<div id="tab:ai_freq_het">

+------------------+-----------+---------------------------------------------------------+
|                  |           | By Usage Frequency                                      |
+:=================+:=========:+:=========:+:============:+:==========:+:===============:+
| 3-6              | Any use   | Rarely    | Occasionally | Frequently | Very Frequently |
+------------------+-----------+-----------+--------------+------------+-----------------+
|                  | \(1\)     | \(2\)     | \(3\)        | \(4\)      | \(5\)           |
+------------------+-----------+-----------+--------------+------------+-----------------+
| **Panel A. Demographics**                                            |                 |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Male             | 88.7      | 20.2      | 19.1         | 33.4       | 16.1            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Female           | 78.4      | 25.7      | 25.1         | 21.0       | 6.6             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| White            | 80.2      | 25.6      | 19.8         | 24.0       | 10.8            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Black            | 92.3      | 15.1      | 23.5         | 41.4       | 12.3            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Hispanic         | 77.9      | 19.9      | 28.7         | 22.8       | 6.6             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Asian            | 91.3      | 19.5      | 27.0         | 30.1       | 14.8            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Private HS       | 84.1      | 23.7      | 22.2         | 27.2       | 10.9            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Public HS        | 80.4      | 24.7      | 21.4         | 24.4       | 9.9             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| **Panel B. Academic Characteristics**                                |                 |
+------------------+-----------+-----------+--------------+------------+-----------------+
| GPA \> p50       | 80.3      | 26.3      | 17.4         | 23.2       | 13.4            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| GPA \< p50       | 87.1      | 18.7      | 26.3         | 32.2       | 9.9             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Freshman         | 81.3      | 24.3      | 24.1         | 24.7       | 8.1             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Sophomore        | 84.4      | 25.6      | 22.6         | 23.7       | 12.4            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Junior           | 86.2      | 21.6      | 23.1         | 28.6       | 12.8            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Senior           | 78.7      | 21.0      | 17.4         | 29.9       | 10.4            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| **Panel C. Field of Study**                                          |                 |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Arts             | 73.8      | 22.1      | 0.0          | 45.1       | 6.6             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Humanities       | 76.5      | 36.5      | 21.0         | 17.7       | 1.3             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Languages        | 59.5      | 20.8      | 31.0         | 7.7        | 0.0             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Literature       | 53.8      | 10.9      | 25.8         | 17.2       | 0.0             |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Natural Sciences | 87.4      | 25.9      | 23.3         | 26.3       | 11.9            |
+------------------+-----------+-----------+--------------+------------+-----------------+
| Social Sciences  | 84.5      | 18.6      | 21.3         | 29.9       | 14.7            |
+------------------+-----------+-----------+--------------+------------+-----------------+

: Generative AI Usage Frequency by Student Characteristics

</div>

</div>

</div>

<div class="singlespace">

*Notes:* This table presents the percent of students in each demographic group who report using AI at different frequencies during the academic semester. Each cell shows the percent of students within that group. Column 1 reports the total percent who use AI at any frequency. Columns 2 to 5 represent increasing usage frequencies: rarely (1–2 times per semester), occasionally (monthly), frequently (weekly), and very frequently (multiple times per week). Panel A reports percentages by demographic characteristics. Panel B shows percentages by academic characteristics. Panel C presents percentages by field of study.

</div>

<div class="center">

<div id="tab:ai_model_correlates">

+----------------+---+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                |   | Outcome: =1 if student uses                                                                                                                              |
+:===============+:==+=================:+:==========+=================:+:==========+=================:+:==========+=================:+:==========+=================:+:=========:+
| 3-12           |   | OpenAI's         |           | Google's         |           | Microsoft        |           | Other            |           | Pays for         |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | ChatGPT          |           | Gemini           |           | Copilot          |           | Model            |           | GenAI            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | \(1\)            |           | \(2\)            |           | \(3\)            |           | \(4\)            |           | \(5\)            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Male           |   | 0.023            |           | 0.083            | $^{**}$   | 0.011            |           | $-$0.007 |           | 0.103            | $^{***}$  |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.020           | )         | (0.036           | )         | (0.027           | )         | (0.033           | )         | (0.029           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Black          |   | $-$0.017 |           | 0.002            |           | $-$0.012 |           | $-$0.013 |           | $-$0.043 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.055           | )         | (0.095           | )         | (0.061           | )         | (0.076           | )         | (0.050           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Latino         |   | 0.027            |           | $-$0.030 |           | 0.033            |           | $-$0.012 |           | 0.020            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.026           | )         | (0.050           | )         | (0.051           | )         | (0.051           | )         | (0.043           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Asian          |   | 0.029            |           | $-$0.074 | $^{**}$   | $-$0.007 |           | $-$0.065 | $^{**}$   | 0.134            | $^{***}$  |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.019           | )         | (0.035           | )         | (0.033           | )         | (0.032           | )         | (0.044           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Public HS      |   | $-$0.032 | $^{*}$    | 0.004            |           | 0.017            |           | $-$0.010 |           | $-$0.003 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.017           | )         | (0.033           | )         | (0.026           | )         | (0.030           | )         | (0.028           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Sophomores     |   | 0.011            |           | 0.015            |           | $-$0.064 | $^{*}$    | 0.008            |           | 0.025            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.028           | )         | (0.041           | )         | (0.033           | )         | (0.036           | )         | (0.034           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Juniors        |   | 0.044            | $^{**}$   | 0.072            |           | $-$0.065 | $^{*}$    | 0.059            |           | 0.028            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.020           | )         | (0.053           | )         | (0.038           | )         | (0.044           | )         | (0.038           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Seniors        |   | 0.026            |           | 0.058            |           | $-$0.068 | $^{**}$   | 0.054            |           | 0.102            | $^{**}$   |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.026           | )         | (0.050           | )         | (0.034           | )         | (0.045           | )         | (0.045           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Arts           |   | $-$0.082 |           | $-$0.086 |           | 0.002            |           | $-$0.067 | $^{**}$   | 0.342            | $^{*}$    |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.088           | )         | (0.102           | )         | (0.090           | )         | (0.032           | )         | (0.190           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Humanities     |   | $-$0.032 |           | $-$0.101 | $^{*}$    | $-$0.078 | $^{***}$  | 0.015            |           | $-$0.047 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.041           | )         | (0.058           | )         | (0.023           | )         | (0.057           | )         | (0.040           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Languages      |   | 0.041            | $^{*}$    | $-$0.078 |           | $-$0.072 | $^{***}$  | 0.047            |           | $-$0.063 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.022           | )         | (0.071           | )         | (0.023           | )         | (0.137           | )         | (0.039           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Literature     |   | $-$0.026 |           | $-$0.141 | $^{***}$  | $-$0.084 | $^{***}$  | 0.040            |           | $-$0.064 | $^{**}$   |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.058           | )         | (0.031           | )         | (0.023           | )         | (0.080           | )         | (0.029           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Social Sci.    |   | $-$0.006 |           | $-$0.042 |           | $-$0.005 |           | 0.068            | $^{**}$   | 0.084            | $^{***}$  |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.020           | )         | (0.040           | )         | (0.031           | )         | (0.034           | )         | (0.032           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Mean Dep. Var. |   | 0.962            |           | 0.135            |           | 0.077            |           | 0.110            |           | 0.114            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| R$-$squared    |   | 0.026            |           | 0.039            |           | 0.030            |           | 0.029            |           | 0.137            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| $N$ (Students) |   | 516              |           | 516              |           | 516              |           | 516              |           | 516              |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+

: Student Characteristics Associated with Choice of Generative AI Models

</div>

</div>

<div class="singlespace">

*Notes:* This table assesses the relationship between AI model adoption and student characteristics. We estimate: $$Y_{i} = \alpha + \beta X_i + \varepsilon_{i},$$ where $Y_i$ is a binary indicator of AI model usage (columns 1–4) or payment for AI services (column 5), and $X_i$ is a vector of student characteristics including gender, race/ethnicity, high school type, cohort indicators, and academic division.

Each column presents results for a different model or payment outcome. Column 1 shows usage of OpenAI's ChatGPT, column 2 Google Gemini, column 3 Microsoft Copilot, column 4 any other AI model, and column 5 whether the student pays for any generative AI service.

The omitted categories are Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, and freshmen for cohort. Heteroskedasticity-robust standard errors clustered at the student level in parentheses. Observations are weighted to adjust for sampling. \* $p<0.10$, \*\* $p<0.05$, \*\*\* $p<0.01$.

</div>

<div class="center">

<div id="tab:ai_policy_het">

+----------------+---+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                |   | Outcome: Would use generative AI in a given policy scenario\...                                                                                          |
+:===============+:==+=================:+:==========+=================:+:==========+=================:+:==========+=================:+:==========+=================:+:=========:+
| 3-12           |   | AI Use is        |           | No Explicit      |           | AI Allowed       |           | AI Use is        |           | Prohibition      |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | Unrestricted     |           | AI Policy        |           | if Cited         |           | Prohibited       |           | Impact           |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | \(1\)            |           | \(2\)            |           | \(3\)            |           | \(4\)            |           | \(5\)            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Male           |   | 0.134            | $^{***}$  | 0.190            | $^{***}$  | 0.129            | $^{***}$  | 0.107            | $^{***}$  | 0.026            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.045           | )         | (0.045           | )         | (0.045           | )         | (0.033           | )         | (0.045           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Black          |   | 0.261            | $^{***}$  | 0.233            | $^{**}$   | 0.082            |           | 0.020            |           | 0.242            | $^{**}$   |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.097           | )         | (0.114           | )         | (0.119           | )         | (0.083           | )         | (0.116           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Latino         |   | $-$0.039 |           | $-$0.004 |           | $-$0.037 |           | $-$0.056 |           | 0.017            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.074           | )         | (0.072           | )         | (0.072           | )         | (0.042           | )         | (0.072           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Asian          |   | 0.097            |           | 0.091            |           | $-$0.004 |           | 0.022            |           | 0.075            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.060           | )         | (0.059           | )         | (0.059           | )         | (0.044           | )         | (0.059           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Public HS      |   | $-$0.016 |           | $-$0.037 |           | $-$0.065 |           | $-$0.019 |           | 0.002            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.044           | )         | (0.044           | )         | (0.044           | )         | (0.031           | )         | (0.044           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Sophomores     |   | 0.023            |           | 0.062            |           | 0.023            |           | 0.017            |           | 0.006            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.056           | )         | (0.055           | )         | (0.057           | )         | (0.039           | )         | (0.058           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Juniors        |   | 0.011            |           | 0.103            |           | 0.068            |           | 0.035            |           | $-$0.024 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.065           | )         | (0.063           | )         | (0.064           | )         | (0.045           | )         | (0.064           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Seniors        |   | 0.023            |           | 0.042            |           | $-$0.029 |           | $-$0.009 |           | 0.032            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.063           | )         | (0.063           | )         | (0.062           | )         | (0.045           | )         | (0.060           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Arts           |   | $-$0.479 | $^{***}$  | $-$0.384 | $^{**}$   | $-$0.303 | $^{**}$   | 0.011            |           | $-$0.490 | $^{***}$  |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.149           | )         | (0.158           | )         | (0.131           | )         | (0.127           | )         | (0.053           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Humanities     |   | $-$0.079 |           | $-$0.177 | $^{**}$   | $-$0.181 | $^{**}$   | $-$0.068 |           | $-$0.011 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.087           | )         | (0.082           | )         | (0.083           | )         | (0.046           | )         | (0.088           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Languages      |   | $-$0.115 |           | $-$0.256 | $^{**}$   | $-$0.219 | $^{**}$   | 0.004            |           | $-$0.119 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.139           | )         | (0.113           | )         | (0.101           | )         | (0.071           | )         | (0.140           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Literature     |   | $-$0.275 | $^{***}$  | $-$0.220 | $^{***}$  | $-$0.178 | $^{**}$   | $-$0.057 |           | $-$0.219 | $^{**}$   |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.089           | )         | (0.084           | )         | (0.090           | )         | (0.041           | )         | (0.088           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Social Sci.    |   | 0.019            |           | 0.009            |           | 0.042            |           | 0.085            | $^{**}$   | $-$0.067 |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
|                |   | (0.049           | )         | (0.049           | )         | (0.049           | )         | (0.035           | )         | (0.050           | )         |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| Mean Dep. Var. |   | 0.525            |           | 0.422            |           | 0.409            |           | 0.134            |           | 0.391            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| R$-$squared    |   | 0.067            |           | 0.088            |           | 0.064            |           | 0.058            |           | 0.038            |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+
| $N$ (Students) |   | 599              |           | 599              |           | 599              |           | 599              |           | 599              |           |
+----------------+---+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+------------------+-----------+

: Student Characteristics Associated with AI Usage Likelihood Under Different Institutional Policies

</div>

</div>

<div class="singlespace">

*Notes:* This table examines how student characteristics relate to self-reported likelihood of using generative AI under different policy scenarios. Each column presents results for different policy scenarios. In columns 1–4, the dependent variable equals one if the student reports being "likely" or "extremely likely" to use AI under the specified policy, and zero otherwise. Column 5 represents the impact of moving from unrestricted use to complete prohibition.

The omitted categories are: Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, freshmen for cohort, female for gender, and private high school for school type. Heteroskedasticity-robust standard errors clustered at the student level in parentheses. Observations are weighted to adjust for sampling. \* $p<0.10$, \*\* $p<0.05$, \*\*\* $p<0.01$.

</div>

<div class="center">

<div id="tab:ai_learning_het">

+----------------+---+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                |   | Outcome: Believes that generative AI improves\...                                                                                                                            |
+:===============+:==+=================:+:==============+=================:+:==============+=================:+:==============+=================:+:==============+=================:+:=============:+
| 3-12           |   | Learning         |               | Understand       |               | Course           |               | Assignment       |               | Time on          |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | Ability          |               | Materials        |               | Grades           |               | Completion       |               | Academics        |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | \(1\)            |               | \(2\)            |               | \(3\)            |               | \(4\)            |               | \(5\)            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Male           |   | 0.122            | $^{***}$      | 0.101            | $^{**}$       | 0.140            | $^{***}$      | 0.027            |               | 0.181            | $^{***}$      |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.045           | )             | (0.041           | )             | (0.045           | )             | (0.048           | )             | (0.045           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Black          |   | 0.361            | $^{***}$      | 0.244            | $^{***}$      | 0.283            | $^{**}$       | $-$0.056 |               | 0.103            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.065           | )             | (0.055           | )             | (0.129           | )             | (0.128           | )             | (0.110           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Latino         |   | 0.179            | $^{**}$       | 0.069            |               | 0.203            | $^{***}$      | 0.020            |               | 0.076            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.070           | )             | (0.064           | )             | (0.077           | )             | (0.076           | )             | (0.072           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Asian          |   | 0.125            | $^{**}$       | 0.149            | $^{***}$      | 0.060            |               | 0.025            |               | 0.136            | $^{**}$       |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.061           | )             | (0.052           | )             | (0.059           | )             | (0.064           | )             | (0.060           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Public HS      |   | $-$0.067 |               | $-$0.067 | $^{*}$        | 0.014            |               | $-$0.052 |               | $-$0.054 |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.045           | )             | (0.041           | )             | (0.045           | )             | (0.047           | )             | (0.045           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Sophomores     |   | 0.089            |               | 0.026            |               | 0.029            |               | $-$0.133 | $^{**}$       | 0.041            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.055           | )             | (0.050           | )             | (0.057           | )             | (0.059           | )             | (0.058           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Juniors        |   | 0.008            |               | $-$0.027 |               | 0.075            |               | $-$0.148 | $^{**}$       | 0.043            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.067           | )             | (0.059           | )             | (0.066           | )             | (0.067           | )             | (0.065           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Seniors        |   | $-$0.083 |               | $-$0.098 |               | $-$0.106 | $^{*}$        | $-$0.149 | $^{**}$       | $-$0.048 |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.063           | )             | (0.060           | )             | (0.060           | )             | (0.066           | )             | (0.064           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Arts           |   | 0.113            |               | $-$0.084 |               | $-$0.254 | $^{**}$       | 0.128            |               | 0.099            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.152           | )             | (0.146           | )             | (0.118           | )             | (0.208           | )             | (0.128           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Humanities     |   | $-$0.115 |               | $-$0.373 | $^{***}$      | $-$0.149 | $^{*}$        | $-$0.025 |               | $-$0.245 | $^{***}$      |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.090           | )             | (0.083           | )             | (0.078           | )             | (0.089           | )             | (0.086           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Languages      |   | $-$0.186 |               | $-$0.385 | $^{***}$      | $-$0.107 |               | $-$0.143 |               | $-$0.201 | $^{*}$        |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.127           | )             | (0.125           | )             | (0.108           | )             | (0.130           | )             | (0.121           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Literature     |   | $-$0.222 | $^{**}$       | $-$0.224 | $^{**}$       | $-$0.314 | $^{***}$      | $-$0.085 |               | $-$0.138 |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.102           | )             | (0.103           | )             | (0.074           | )             | (0.115           | )             | (0.119           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Social Sci.    |   | 0.015            |               | $-$0.085 | $^{*}$        | 0.030            |               | $-$0.000 |               | $-$0.022 |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
|                |   | (0.049           | )             | (0.044           | )             | (0.051           | )             | (0.051           | )             | (0.050           | )             |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| Mean Dep. Var. |   | 0.576            |               | 0.685            |               | 0.376            |               | 0.489            |               | 0.564            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| R$-$squared    |   | 0.087            |               | 0.120            |               | 0.091            |               | 0.032            |               | 0.082            |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+
| $N$ (Students) |   | 561              |               | 565              |               | 543              |               | 560              |               | 560              |               |
+----------------+---+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+------------------+---------------+

: Student Characteristics Associated with Perceived Learning Benefits

</div>

</div>

<div class="singlespace">

*Notes:* This table assesses the relationship between AI adoption and student characteristics. Each column presents results for beliefs about different academic outcomes: learning ability (e.g., ability to grasp concepts, retain information, or learn new skills) in column 1, understanding of course materials in column 2, course grades in column 3, ability to complete assignments on time in column 4, and time spent on academics in column 5. The dependent variable in each regression equals one if the student believes AI "somewhat improves" or "significantly improves" the outcome, and zero if they believe it has no effect, reduces, or significantly reduces the outcome. "Don't know" responses are excluded.

The omitted categories are: Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, freshmen for cohort, female for gender, and private high school for school type. Heteroskedasticity-robust standard errors clustered at the student level in parentheses. Observations are weighted to adjust for sampling. \* $p<0.10$, \*\* $p<0.05$, \*\*\* $p<0.01$.

</div>

# Empirical Appendix
## Robustness to Alternative Weighting Schemes
This appendix examines how our main findings depend on the choice of poststratification weights. Our benchmark results weight observations by major to match the distribution of fields of study in the student population. We present results using three alternatives: (i) weighting by gender and cohort, (ii) weighting by race, and (iii) unweighted estimates.

The gender-by-cohort weights use 8 cells (two genders $\times$ 4 cohorts). Population cohort totals come from administrative enrollment records. Gender shares within each cohort come from administrative data on expected graduation terms, which give a gender-by-graduation-year cross-tabulation for the classes of 2025, 2026, and 2027. Freshmen (Class of 2028) do not yet have assigned graduation terms; we use the overall gender ratio from the Common Data Set (53.3 percent female). The race weights use 4 cells (white, Black, Hispanic, Asian) with population counts from the Common Data Set. Students outside these four categories or who prefer not to say receive missing weights and are excluded from the race-weighted estimates. All weights are normalized to sum to total enrollment.

Appendix Tables 9–11 show that our main findings are robust across these specifications. The largest variation is for coding assistance under gender-by-cohort weights: the rate shifts from 37.0 percent (benchmark) to 45.3 percent, reflecting the correlation between gender composition and coding-related majors. Small-cell disciplines show wider variation: Arts usage ranges from 57.6 to 73.8 percent across weighting schemes, reflecting the small number of Arts respondents.

<div class="center">

<div class="singlespace">

<div id="tab:weight_adoption">

+-------------------+----------------------------------------------------------+
|                   | Weighting Scheme:                                        |
+:==================+:==========:+:======================:+:=====:+:==========:+
| 2-5               | Benchmark  | Gender $\times$ Cohort | Race  | Unweighted |
+-------------------+------------+------------------------+-------+------------+
|                   | (by major) |                        |       |            |
+-------------------+------------+------------------------+-------+------------+
|                   | \(1\)      | \(2\)                  | \(3\) | \(4\)      |
+-------------------+------------+------------------------+-------+------------+
| Overall           | 82.5       | 84.3                   | 83.6  | 83.8       |
+-------------------+------------+------------------------+-------+------------+
| Male              | 88.7       | 88.9                   | 89.4  | 89.4       |
+-------------------+------------+------------------------+-------+------------+
| Female            | 78.4       | 80.3                   | 80.4  | 80.1       |
+-------------------+------------+------------------------+-------+------------+
| White             | 80.2       | 83.6                   | 82.8  | 82.8       |
+-------------------+------------+------------------------+-------+------------+
| Black             | 92.3       | 95.0                   | 91.3  | 91.3       |
+-------------------+------------+------------------------+-------+------------+
| Hispanic          | 77.9       | 80.4                   | 80.0  | 80.0       |
+-------------------+------------+------------------------+-------+------------+
| Asian             | 91.3       | 90.2                   | 89.8  | 89.8       |
+-------------------+------------+------------------------+-------+------------+
| Private HS        | 84.1       | 86.5                   | 85.8  | 85.6       |
+-------------------+------------+------------------------+-------+------------+
| Public HS         | 80.4       | 82.1                   | 81.2  | 81.8       |
+-------------------+------------+------------------------+-------+------------+
| GPA $\geq$ median | 80.3       | 82.6                   | 82.7  | 82.4       |
+-------------------+------------+------------------------+-------+------------+
| GPA $<$ median    | 87.1       | 88.2                   | 88.7  | 88.0       |
+-------------------+------------+------------------------+-------+------------+
| Natural Sciences  | 87.4       | 86.8                   | 85.6  | 86.4       |
+-------------------+------------+------------------------+-------+------------+
| Social Sciences   | 84.5       | 89.6                   | 89.0  | 89.0       |
+-------------------+------------+------------------------+-------+------------+
| Humanities        | 76.5       | 76.7                   | 79.9  | 77.3       |
+-------------------+------------+------------------------+-------+------------+
| Literature        | 53.8       | 50.5                   | 51.7  | 50.0       |
+-------------------+------------+------------------------+-------+------------+
| Languages         | 59.5       | 52.2                   | 54.0  | 53.3       |
+-------------------+------------+------------------------+-------+------------+
| Arts              | 73.8       | 57.6                   | 58.3  | 63.6       |
+-------------------+------------+------------------------+-------+------------+
| $N$ (Students)    | 616        | 589                    | 560   | 616        |
+-------------------+------------+------------------------+-------+------------+

: Generative AI Adoption Rates by Weighting Scheme

</div>

</div>

</div>

<div class="singlespace">

*Notes:* This table presents the percent of students who report using generative AI for academic purposes during the semester, across different poststratification weighting schemes. Column 1 shows our benchmark estimates using weights based on major. Column 2 uses weights based on the joint distribution of gender and cohort. Column 3 uses weights based on race/ethnicity. Column 4 shows unweighted estimates. The sample in column 3 excludes students who report a race/ethnicity outside the four categories used for weighting (white, Black, Hispanic, Asian) or who prefer not to say.

</div>

<div class="center">

<div class="singlespace">

<div id="tab:weight_tasks">

+------------------------+----------------------------------------------------------+
|                        | Weighting Scheme:                                        |
+:=======================+:==========:+:======================:+:=====:+:==========:+
| 2-5                    | Benchmark  | Gender $\times$ Cohort | Race  | Unweighted |
+------------------------+------------+------------------------+-------+------------+
|                        | (by major) |                        |       |            |
+------------------------+------------+------------------------+-------+------------+
|                        | \(1\)      | \(2\)                  | \(3\) | \(4\)      |
+------------------------+------------+------------------------+-------+------------+
| *Augmentation tasks*                                                              |
+------------------------+------------+------------------------+-------+------------+
| Explaining concepts    | 85.4       | 85.7                   | 86.5  | 85.9       |
+------------------------+------------+------------------------+-------+------------+
| Generating ideas       | 66.0       | 68.8                   | 69.6  | 67.7       |
+------------------------+------------+------------------------+-------+------------+
| Editing essay drafts   | 51.5       | 52.2                   | 52.8  | 52.6       |
+------------------------+------------+------------------------+-------+------------+
| Coding assistance      | 37.0       | 45.3                   | 41.2  | 42.1       |
+------------------------+------------+------------------------+-------+------------+
|                        |            |                        |       |            |
+------------------------+------------+------------------------+-------+------------+
| Summarizing texts      | 79.5       | 80.3                   | 79.9  | 80.3       |
+------------------------+------------+------------------------+-------+------------+
| Finding information    | 67.1       | 68.8                   | 69.6  | 67.9       |
+------------------------+------------+------------------------+-------+------------+
| Proofreading           | 58.5       | 59.3                   | 59.4  | 58.6       |
+------------------------+------------+------------------------+-------+------------+
| Writing emails         | 40.2       | 41.5                   | 41.3  | 41.5       |
+------------------------+------------+------------------------+-------+------------+
| Writing essays         | 26.1       | 27.1                   | 25.4  | 26.9       |
+------------------------+------------+------------------------+-------+------------+
| Creating images        | 21.8       | 21.6                   | 19.2  | 20.6       |
+------------------------+------------+------------------------+-------+------------+
| Augmentation (average) | 59.6       | 62.6                   | 62.1  | 61.6       |
+------------------------+------------+------------------------+-------+------------+
| Automation (average)   | 48.3       | 49.1                   | 48.6  | 48.7       |
+------------------------+------------+------------------------+-------+------------+
| $N$ (Students)         | 510        | 510                    | 510   | 510        |
+------------------------+------------+------------------------+-------+------------+

: Academic Uses of Generative AI by Weighting Scheme

</div>

</div>

</div>

<div class="singlespace">

*Notes:* This table presents the percent of AI users who report using generative AI for each academic task, across different poststratification weighting schemes. Tasks are grouped into augmentation (explaining concepts, generating ideas, editing drafts, and coding assistance) and automation (summarizing texts, finding information, proofreading, writing emails, writing essays, and creating images) based on the combined survey classification described in Appendix 10. The bottom rows show the average usage rate across tasks within each category. Column definitions follow Appendix Table 9. Sample restricted to students who report using AI during the academic semester.

</div>

<div class="center">

<div class="singlespace">

<div id="tab:weight_beliefs">

+-----------------------------------------+----------------------------------------------------------+
|                                         | Weighting Scheme:                                        |
+:========================================+:==========:+:======================:+:=====:+:==========:+
| 2-5                                     | Benchmark  | Gender $\times$ Cohort | Race  | Unweighted |
+-----------------------------------------+------------+------------------------+-------+------------+
|                                         | (by major) |                        |       |            |
+-----------------------------------------+------------+------------------------+-------+------------+
|                                         | \(1\)      | \(2\)                  | \(3\) | \(4\)      |
+-----------------------------------------+------------+------------------------+-------+------------+
| Learning ability                        | 57.6       | 59.2                   | 60.2  | 59.2       |
+-----------------------------------------+------------+------------------------+-------+------------+
| Understanding of course materials       | 68.5       | 68.5                   | 69.2  | 68.7       |
+-----------------------------------------+------------+------------------------+-------+------------+
| Course grades                           | 37.6       | 39.6                   | 41.0  | 40.1       |
+-----------------------------------------+------------+------------------------+-------+------------+
| Ability to complete assignments on time | 56.4       | 57.6                   | 55.9  | 57.3       |
+-----------------------------------------+------------+------------------------+-------+------------+
| Time spent on academics                 | 48.9       | 47.3                   | 47.5  | 48.8       |
+-----------------------------------------+------------+------------------------+-------+------------+
| $N$ (Students)                          | 560        | 537                    | 511   | 560        |
+-----------------------------------------+------------+------------------------+-------+------------+

: Student Beliefs About AI's Academic Impact by Weighting Scheme

</div>

</div>

</div>

<div class="singlespace">

*Notes:* This table presents the percent of students who believe that generative AI "somewhat improves" or "significantly improves" each aspect of their academic experience, across different poststratification weighting schemes. Students who responded "I don't know" are excluded. Column definitions follow Appendix Table 9.

</div>

## Field of Study Classifications
This appendix details the classification of majors into broad fields of study:

- **Natural Sciences:** Includes Biology, Chemistry, Computer Science, Earth and Climate Sciences/Geology, Environmental Studies, Mathematics, Molecular Biology & Biochemistry, Neuroscience, Physics, and Statistics.

- **Social Sciences:** Includes Anthropology, Economics, Education, Geography, International & Global Studies, International Politics & Economics, Political Science, Psychology, and Sociology.

- **Humanities:** Includes American Studies, Architectural Studies, Art History & Museum Studies, Black Studies, Classical Studies, History, History of Art & Architecture, Philosophy, and Religion.

- **Literature:** Includes Comparative Literature, English/English & American Literatures, and Literary Studies.

- **Languages:** Includes Arabic, Chinese, French & Francophone Studies, German, Japanese Studies, Russian, and Spanish.

- **Arts:** Includes Film & Media Culture, Music, Studio Art, and Theatre.

- **Has not declared major:** Students who had not yet declared a major at the time of the survey are grouped by their intended field of study, as reported in the survey.

## Task-Specific Use of Generative AI

The aggregate patterns in Section 4 may mask heterogeneity across student groups. Appendix Table 12 reports regression estimates of how student characteristics predict AI usage for each of our ten academic tasks.

Usage patterns differ by student characteristics. Males show higher adoption across most applications, with the largest gaps for finding information (16.2 pp; $p < 0.01$), summarizing texts (12.0 pp; $p < 0.01$), and creating images (16.3 pp; $p < 0.01$). Black students show 26.5 pp higher usage for finding information than white students ($p < 0.05$) and higher adoption of writing assistance tools (30.2 pp for editing text, $p < 0.05$; 22.2 pp for writing emails, $p < 0.10$). Hispanic students show higher usage for generating ideas (21.4 pp; $p < 0.01$) and writing emails (19.8 pp; $p < 0.01$), while Asian students show higher adoption for writing emails (24.7 pp; $p < 0.01$) and explaining concepts (11.2 pp, $p < 0.05$). Public high school students report lower usage for concept explanation (8.9 pp; $p < 0.10$) and writing emails (7.4 pp; $p < 0.10$), but higher usage for proofreading (9.0 pp; $p < 0.10$).

Field of study is a strong predictor. Arts majors show lower adoption across multiple tasks than Natural Science students, with gaps of 40.9 pp for finding information ($p < 0.05$), 42.4 pp for generating ideas ($p < 0.05$), and 59.2 pp for coding assistance ($p < 0.01$). Humanities majors are 33.3 pp less likely to use AI for generating ideas ($p < 0.01$) and 31.8 pp less likely for coding assistance ($p < 0.01$). Languages majors show the largest differences: 49.7 pp less likely to use AI for summarizing texts ($p < 0.01$), 42.5 pp less likely for generating ideas ($p < 0.01$), and 35.6 pp less likely for coding assistance ($p < 0.01$). Social science students show higher usage for summarizing texts (9.9 pp; $p < 0.05$) but lower usage for coding assistance (17.0 pp; $p < 0.01$).

<div class="landscape">

<div class="center">

<div id="tab:ai_purpose_correlates">

+----------------+---+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+----------+
|                |   | =1 if student uses generative AI with any frequency during the academic semester to\...                                                                                                                                                                                                                                                                                                                   |                  |          |
+:===============+:==+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:====================+====================:+:===================:+=================:+:=========+
| 3-22           |   | Explain             |                     | Summ.               |                     | Find                |                     | Gen.                |                     | Proof-              |                     | Edit                |                     | Write               |                     | Code                |                     | Write               |                     | Create           |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | Cnpts.              |                     | Texts               |                     | Info.               |                     | Ideas               |                     | read                |                     | Text                |                     | Emails              |                     | Assist.             |                     | Essays              |                     | Images           |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | \(1\)               |                     | \(2\)               |                     | \(3\)               |                     | \(4\)               |                     | \(5\)               |                     | \(6\)               |                     | \(7\)               |                     | \(8\)               |                     | \(9\)               |                     | \(10\)           |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Male           |   | 0.076               | $^{**}$             | 0.120               | $^{***}$            | 0.162               | $^{***}$            | 0.049               |                     | 0.042               |                     | 0.097               | $^{**}$             | 0.041               |                     | 0.097               | $^{**}$             | 0.044               |                     | 0.163            | $^{***}$ |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.037              | )                   | (0.042              | )                   | (0.046              | )                   | (0.046              | )                   | (0.050              | )                   | (0.049              | )                   | (0.046              | )                   | (0.043              | )                   | (0.044              | )                   | (0.039           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Black          |   | 0.114               |                     | 0.042               |                     | 0.265               | $^{***}$            | $-$0.113    |                     | 0.148               |                     | 0.302               | $^{***}$            | 0.222               | $^{*}$              | $-$0.091    |                     | 0.093               |                     | $-$0.117 |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.078              | )                   | (0.111              | )                   | (0.101              | )                   | (0.121              | )                   | (0.125              | )                   | (0.117              | )                   | (0.118              | )                   | (0.100              | )                   | (0.122              | )                   | (0.076           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Latino         |   | 0.158               | $^{***}$            | 0.064               |                     | 0.084               |                     | 0.214               | $^{***}$            | 0.072               |                     | 0.079               |                     | 0.198               | $^{**}$             | $-$0.156    | $^{***}$            | $-$0.014    |                     | 0.122            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.050              | )                   | (0.066              | )                   | (0.076              | )                   | (0.064              | )                   | (0.083              | )                   | (0.080              | )                   | (0.083              | )                   | (0.059              | )                   | (0.073              | )                   | (0.075           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Asian          |   | 0.112               | $^{**}$             | 0.034               |                     | 0.014               |                     | 0.038               |                     | 0.080               |                     | 0.061               |                     | 0.247               | $^{***}$            | 0.054               |                     | 0.006               |                     | $-$0.081 | $^{*}$   |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.045              | )                   | (0.056              | )                   | (0.061              | )                   | (0.061              | )                   | (0.064              | )                   | (0.064              | )                   | (0.061              | )                   | (0.058              | )                   | (0.054              | )                   | (0.042           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Public HS      |   | $-$0.089    | $^{**}$             | $-$0.057    |                     | $-$0.007    |                     | $-$0.001    |                     | 0.090               | $^{*}$              | 0.025               |                     | $-$0.074    |                     | $-$0.048    |                     | 0.000               |                     | 0.021            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.038              | )                   | (0.042              | )                   | (0.046              | )                   | (0.046              | )                   | (0.049              | )                   | (0.049              | )                   | (0.045              | )                   | (0.042              | )                   | (0.041              | )                   | (0.038           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Sophomores     |   | 0.040               |                     | 0.066               |                     | 0.040               |                     | 0.024               |                     | 0.027               |                     | $-$0.079    |                     | $-$0.018    |                     | 0.093               | $^{*}$              | $-$0.006    |                     | $-$0.091 | $^{*}$   |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.047              | )                   | (0.054              | )                   | (0.059              | )                   | (0.058              | )                   | (0.062              | )                   | (0.061              | )                   | (0.057              | )                   | (0.052              | )                   | (0.054              | )                   | (0.047           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Juniors        |   | 0.051               |                     | $-$0.009    |                     | 0.063               |                     | 0.085               |                     | 0.075               |                     | $-$0.010    |                     | 0.052               |                     | 0.272               | $^{***}$            | 0.053               |                     | $-$0.036 |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.052              | )                   | (0.060              | )                   | (0.063              | )                   | (0.062              | )                   | (0.069              | )                   | (0.069              | )                   | (0.065              | )                   | (0.061              | )                   | (0.062              | )                   | (0.053           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Seniors        |   | 0.020               |                     | 0.058               |                     | $-$0.022    |                     | 0.060               |                     | 0.046               |                     | $-$0.041    |                     | 0.011               |                     | 0.284               | $^{***}$            | $-$0.039    |                     | 0.057            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.054              | )                   | (0.055              | )                   | (0.065              | )                   | (0.065              | )                   | (0.068              | )                   | (0.067              | )                   | (0.063              | )                   | (0.063              | )                   | (0.055              | )                   | (0.058           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Arts           |   | $-$0.122    |                     | 0.043               |                     | $-$0.409    | $^{**}$             | $-$0.424    | $^{**}$             | 0.188               |                     | $-$0.370    | $^{***}$            | 0.219               |                     | $-$0.592    | $^{***}$            | $-$0.048    |                     | $-$0.176 | $^{*}$   |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.127              | )                   | (0.118              | )                   | (0.169              | )                   | (0.179              | )                   | (0.172              | )                   | (0.130              | )                   | (0.136              | )                   | (0.096              | )                   | (0.117              | )                   | (0.096           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Humanities     |   | $-$0.120    |                     | $-$0.143    |                     | $-$0.138    |                     | $-$0.333    | $^{***}$            | $-$0.044    |                     | $-$0.025    |                     | $-$0.120    |                     | $-$0.318    | $^{***}$            | $-$0.060    |                     | 0.069            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.078              | )                   | (0.091              | )                   | (0.087              | )                   | (0.087              | )                   | (0.096              | )                   | (0.091              | )                   | (0.077              | )                   | (0.072              | )                   | (0.072              | )                   | (0.079           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Languages      |   | $-$0.377    | $^{**}$             | $-$0.497    | $^{***}$            | 0.010               |                     | $-$0.425    | $^{***}$            | 0.072               |                     | 0.043               |                     | $-$0.036    |                     | $-$0.356    | $^{***}$            | $-$0.055    |                     | 0.239            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.160              | )                   | (0.131              | )                   | (0.174              | )                   | (0.144              | )                   | (0.185              | )                   | (0.187              | )                   | (0.166              | )                   | (0.119              | )                   | (0.110              | )                   | (0.176           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Literature     |   | $-$0.159    |                     | 0.029               |                     | $-$0.165    |                     | 0.029               |                     | $-$0.026    |                     | $-$0.191    | $^{*}$              | $-$0.060    |                     | $-$0.319    | $^{***}$            | $-$0.133    | $^{*}$              | $-$0.017 |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.113              | )                   | (0.115              | )                   | (0.122              | )                   | (0.116              | )                   | (0.124              | )                   | (0.109              | )                   | (0.126              | )                   | (0.101              | )                   | (0.080              | )                   | (0.091           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Social Sci.    |   | 0.008               |                     | 0.099               | $^{**}$             | 0.017               |                     | 0.048               |                     | 0.087               | $^{*}$              | 0.057               |                     | 0.089               | $^{*}$              | $-$0.170    | $^{***}$            | 0.110               | $^{**}$             | $-$0.035 |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
|                |   | (0.040              | )                   | (0.045              | )                   | (0.050              | )                   | (0.049              | )                   | (0.053              | )                   | (0.053              | )                   | (0.050              | )                   | (0.047              | )                   | (0.049              | )                   | (0.041           | )        |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| Mean Dep. Var. |   | 0.803               |                     | 0.740               |                     | 0.631               |                     | 0.619               |                     | 0.541               |                     | 0.473               |                     | 0.371               |                     | 0.344               |                     | 0.235               |                     | 0.204            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| R$-$squared    |   | 0.076               |                     | 0.089               |                     | 0.072               |                     | 0.105               |                     | 0.028               |                     | 0.053               |                     | 0.089               |                     | 0.159               |                     | 0.037               |                     | 0.083            |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+
| $N$ (Students) |   | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515                 |                     | 515              |          |
+----------------+---+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+---------------------+------------------+----------+

: Student Characteristics Associated with Task-Specific Use of Generative AI

</div>

</div>

<div class="singlespace">

*Notes:* This table reports estimated associations between student characteristics and use of AI for specific academic tasks. Each column shows the result for a different academic task. The omitted categories are: Natural Sciences (and the small share of students with no declared or intended major) for academic division, white students for race/ethnicity, freshmen for cohort, female for gender, and private high school for school type. Regressions are weighted and use heteroskedasticity-robust standard errors clustered at the student level. $^{***}$, $^{**}$, and $^*$ indicate significance at the 1%, 5%, and 10% levels, respectively.

</div>

</div>

# Supplementary Survey on Task Classification
Our main survey records how frequently students use AI for 10 academic tasks but does not classify these tasks as augmentation or automation. This classification is essential for the analysis in Section 4, in which we examine whether students primarily use AI to complement their own effort or to replace it. To make the distinction, we designed a supplementary survey to elicit independent classifications from undergraduate students and college instructors outside our main sample. This appendix describes the survey design, reports the classification results, and examines their robustness.

## Sample and Recruitment

We recruited respondents through Prolific in February 2026. The student sample has 56 enrolled U.S. undergraduates; the instructor sample has 51 college instructors, including faculty, lecturers, and teaching assistants. We paid respondents $5 for a survey that took about 5 minutes. Respondents had to be U.S.-based and either currently enrolled as an undergraduate or currently teaching at the college level.

## Survey Design

The survey presented respondents with the same ten academic tasks measured in our Middlebury survey: explaining concepts, summarizing texts, finding information, generating ideas, proofreading, editing drafts, composing emails, coding assistance, writing essays, and creating images. We asked respondents to imagine working on a college assignment and to evaluate how using AI would change the nature of each task (see Appendix app:classification_instrument for survey instrument).

We elicited classifications along multiple dimensions, each capturing a different aspect of how AI interacts with student effort and learning. All respondents evaluated three classification dimensions—for/with, effort, and learning. The student sample additionally rated the importance of each task. To mitigate order effects and respondent fatigue, we randomized the order in which dimensions appeared: the three classification dimensions were presented in random order relative to each other, and in the student survey the importance block appeared either before or after them.

The *for/with* dimension is our primary classification variable. For each task, respondents indicated whether AI acts more as a collaborator that "works with" the student (augmentation) or automates the task by "doing it for" the student (automation). This binary classification maps directly onto the augmentation–automation framework in Section 4.

The *effort* dimension asked respondents to assess whether AI use reduces, increases, or has no effect on the cognitive effort required for each task. This three-point scale captures whether AI substitutes for or complements student effort, independent of how that effort maps onto learning.

The *learning* dimension asked whether AI use for each task increases, decreases, or has no effect on student learning. This dimension captures respondents' beliefs about the educational consequences of AI use, which may differ from their beliefs about effort. A task could reduce effort while increasing learning (e.g., AI explains a concept the student would have struggled with alone) or reduce both (e.g., AI writes an essay the student never engages with).

We asked only the student sample to rate the *importance* of each task for their own learning on a 0–100 slider scale, since instructors may weigh task importance differently from students.

Each dimension's block also included a ranking task in which respondents ordered all 10 tasks from one end of the dimension to the other (e.g., from "most works with" to "most does for"). These rankings provide an ordinal measure that complements the categorical classifications. The survey concluded with questions about respondents' own AI usage frequency, both overall and for each of the 10 tasks.

## Main Classification Results

We classify each task using the combined modal response across both samples. For each task, we compute the share of pooled respondents (students and instructors) who classify AI as "working with" versus "doing for" the student, and assign the task to the majority category.

Appendix Table 13 presents the results. The combined classification categorizes 4 tasks as augmentation—explaining concepts, generating ideas, editing essays, and coding help—and 6 tasks as automation—summarizing texts, finding information, proofreading, writing emails, writing essays, and creating images. Students and instructors agree on the classification of 8 out of 10 tasks. The two samples disagree on two tasks: students classify both finding information and editing essays as augmentation, while instructors classify both as automation. In both cases, the combined classification follows the pooled majority.

Appendix Figure 9 plots mean for/with rankings from students against those from instructors. Tasks cluster near the 45-degree line, confirming broad agreement on which tasks are more collaborative versus more automated. The correlation between rankings is high, with explaining concepts and generating ideas consistently ranked as the most "with" tasks and writing essays and creating images as the most "for" tasks.

<div class="center">

<div id="tab:class_forwith">

+--------------------------+------------------+------------------+------------------+----------------+
|                          | Students         | Instructors      | Overall          | Survey         |
+:=========================+:=======:+:======:+:=======:+:======:+:=======:+:======:+:==============:+
| 2-3 (lr)4-5 (lr)6-7 Task | \% With | \% For | \% With | \% For | \% With | \% For | Classification |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Explaining concepts      | 64.3    | 30.4   | 58.8    | 41.2   | 61.5    | 35.8   | AUG            |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Summarizing texts        | 35.7    | 58.9   | 9.8     | 90.2   | 22.8    | 74.5   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Finding information      | 50.0    | 44.6   | 47.1    | 52.9   | 48.5    | 48.8   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Generating ideas         | 60.7    | 33.9   | 52.9    | 47.1   | 56.8    | 40.5   | AUG            |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Proofreading             | 46.4    | 48.2   | 29.4    | 70.6   | 37.9    | 59.4   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Editing essays           | 58.9    | 35.7   | 41.2    | 58.8   | 50.0    | 47.2   | AUG            |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Writing emails           | 37.5    | 57.1   | 35.3    | 64.7   | 36.4    | 60.9   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Coding help              | 58.9    | 35.7   | 64.7    | 35.3   | 61.8    | 35.5   | AUG            |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Writing essays           | 37.5    | 57.1   | 31.4    | 68.6   | 34.5    | 62.8   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+
| Creating images          | 28.6    | 66.1   | 37.3    | 62.7   | 33.0    | 64.4   | AUTO           |
+--------------------------+---------+--------+---------+--------+---------+--------+----------------+

: For/With Classification: Students vs. Instructors

</div>

</div>

<div class="singlespace">

*Notes:* This table shows the percentage of respondents who classify AI as "working with" or "doing for" the student for each academic task. The student sample includes 56 undergraduates and the instructor sample includes 51 instructors at U.S. colleges and universities. The "Survey" column shows the combined modal classification (averaging across both samples).

</div>

<figure id="fig:class_rankings" data-latex-placement="H">
<embed src="results/class_rankings_figure.pdf" />
<p><em>Notes:</em> This scatterplot shows mean for/with rankings from students (<span class="math inline"><em>y</em></span>-axis) and instructors (<span class="math inline"><em>x</em></span>-axis) for each of the ten academic tasks. Rankings range from 1 (most “works with”) to 10 (most “does for”). Circles denote tasks classified as augmentation in the combined survey classification; triangles denote automation tasks. The dashed line is the 45-degree line.</p>
<figcaption>Student vs. Instructor For/With Rankings</figcaption>
</figure>

## Additional Dimensions: Effort, Learning, and Importance

The effort and learning dimensions provide evidence that is broadly consistent with the for/with classification. Appendix Table 14 shows that for most tasks, both students and instructors report that AI reduces cognitive effort. The reduction is largest for tasks classified as automation: large majorities of respondents report that AI reduces the effort required for proofreading, writing emails, and creating images. Among augmentation tasks, the picture is more mixed. Explaining concepts and generating ideas show smaller effort reductions, and a nontrivial share of respondents report that AI increases the effort required for coding help—consistent with the view that debugging and understanding code with AI requires active engagement.

Appendix Table 15 presents results for the learning dimension. Respondents generally view augmentation tasks as more likely to increase learning than automation tasks. Explaining concepts stands out: a majority of both students and instructors report that AI use increases learning for this task. By contrast, respondents most often rate automation tasks—such as writing emails, proofreading, and creating images—as having no effect on learning. Writing essays is the task respondents most often rate as decreasing learning, consistent with the concern that outsourcing core writing undermines skill development.

Appendix Table 16 shows that students rate augmentation tasks as more important to their learning than automation tasks. Explaining concepts, generating ideas, and coding help receive the highest mean importance ratings, while creating images and writing emails receive the lowest. This pattern is consistent with students valuing tasks in which AI complements their effort over those in which AI substitutes for it.

<div class="center">

<div id="tab:class_effort">

+---------------------+----------------+-----------------------------------------------------+-----------------------------------------------------+
|                     |                | Students                                            | Instructors                                         |
+:====================+:===============+:===================:+:=========:+:=================:+:===================:+:=========:+:=================:+
| 3-5 (lr)6-8 Task    | Classification | $\downarrow$ Effort | No effect | $\uparrow$ Effort | $\downarrow$ Effort | No effect | $\uparrow$ Effort |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Explaining concepts | AUG            | 71.4                | 21.4      | 3.6               | 76.5                | 13.7      | 9.8               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Summarizing texts   | AUTO           | 85.7                | 5.4       | 5.4               | 90.2                | 3.9       | 5.9               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Finding information | AUTO           | 76.8                | 12.5      | 7.1               | 82.4                | 11.8      | 5.9               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Generating ideas    | AUG            | 73.2                | 21.4      | 1.8               | 84.3                | 7.8       | 7.8               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Proofreading        | AUTO           | 76.8                | 16.1      | 3.6               | 82.4                | 7.8       | 9.8               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Editing essays      | AUG            | 76.8                | 12.5      | 7.1               | 84.3                | 13.7      | 2.0               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Writing emails      | AUTO           | 69.6                | 23.2      | 3.6               | 86.3                | 13.7      | 0.0               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Coding help         | AUG            | 82.1                | 12.5      | 1.8               | 78.4                | 17.6      | 3.9               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Writing essays      | AUTO           | 87.5                | 5.4       | 3.6               | 80.4                | 9.8       | 9.8               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| Creating images     | AUTO           | 76.8                | 7.1       | 12.5              | 80.4                | 13.7      | 5.9               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| *All tasks*         |                | 77.7                | 13.8      | 5.0               | 82.5                | 11.4      | 6.1               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| *AUG tasks*         |                | 75.9                | 17.0      | 3.6               | 80.9                | 13.2      | 5.9               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+
| *AUTO tasks*        |                | 78.9                | 11.6      | 6.0               | 83.7                | 10.1      | 6.2               |
+---------------------+----------------+---------------------+-----------+-------------------+---------------------+-----------+-------------------+

: Effort Dimension: Students vs. Instructors

</div>

</div>

<div class="singlespace">

*Notes:* This table shows the percentage of respondents who report that AI use for each task reduces, has no effect on, or increases the student's cognitive effort. Classification column reflects the combined survey classification.

</div>

<div class="center">

<div id="tab:class_learning">

+---------------------+--------+---------------------------------------------------------+---------------------------------------------------------+
|                     |        | Students                                                | Instructors                                             |
+:====================+:=======+:=====================:+:=========:+:===================:+:=====================:+:=========:+:===================:+
| 3-5 (lr)6-8 Task    | Class. | $\downarrow$ Learning | No effect | $\uparrow$ Learning | $\downarrow$ Learning | No effect | $\uparrow$ Learning |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Explaining concepts | AUG    | 23.2                  | 7.1       | 64.3                | 35.3                  | 5.9       | 58.8                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Summarizing texts   | AUTO   | 26.8                  | 25.0      | 42.9                | 56.9                  | 15.7      | 27.5                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Finding information | AUTO   | 32.1                  | 23.2      | 39.3                | 49.0                  | 13.7      | 37.3                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Generating ideas    | AUG    | 50.0                  | 19.6      | 25.0                | 52.9                  | 19.6      | 27.5                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Proofreading        | AUTO   | 32.1                  | 23.2      | 39.3                | 39.2                  | 41.2      | 19.6                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Editing essays      | AUG    | 44.6                  | 16.1      | 33.9                | 52.9                  | 31.4      | 15.7                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Writing emails      | AUTO   | 53.6                  | 30.4      | 10.7                | 45.1                  | 33.3      | 21.6                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Coding help         | AUG    | 37.5                  | 16.1      | 41.1                | 35.3                  | 19.6      | 45.1                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Writing essays      | AUTO   | 73.2                  | 7.1       | 14.3                | 84.3                  | 3.9       | 11.8                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| Creating images     | AUTO   | 37.5                  | 46.4      | 10.7                | 31.4                  | 54.9      | 13.7                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| *All tasks*         |        | 41.1                  | 21.4      | 32.1                | 48.2                  | 23.9      | 27.8                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| *AUG tasks*         |        | 38.8                  | 14.7      | 41.1                | 44.1                  | 19.1      | 36.8                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+
| *AUTO tasks*        |        | 42.6                  | 25.9      | 26.2                | 51.0                  | 27.1      | 21.9                |
+---------------------+--------+-----------------------+-----------+---------------------+-----------------------+-----------+---------------------+

: Learning Dimension: Students vs. Instructors

</div>

</div>

<div class="singlespace">

*Notes:* This table shows the percentage of respondents who report that AI use for each task decreases, has no effect on, or increases student learning. Classification column reflects the combined survey classification.

</div>

<div class="center">

<div id="tab:class_importance">

  --------------------- ---------------- ----------------- -----------
  Task                  Classification    Mean importance   Mean rank
                                             (0–100)        (1–10)
  Explaining concepts   AUG                    67.8            3.8
  Finding information   AUTO                   67.6            4.0
  Generating ideas      AUG                    64.9            4.3
  Writing essays        AUTO                   69.5            4.5
  Proofreading          AUTO                   57.5            5.2
  Summarizing texts     AUTO                   54.7            5.6
  Editing essays        AUG                    64.0            5.8
  Coding help           AUG                    45.3            6.8
  Writing emails        AUTO                   51.3            7.0
  Creating images       AUTO                   30.3            8.0
  *All tasks*                                  57.3            5.5
  *AUG tasks*                                  60.5            5.2
  *AUTO tasks*                                 55.2            5.7
  --------------------- ---------------- ----------------- -----------

  : Task Importance: Student Sample

</div>

</div>

<div class="singlespace">

*Notes:* This table shows mean importance ratings (0–100 slider) and mean importance rankings for each academic task, from the student sample only. Tasks are sorted by mean rank. Classification column reflects the combined survey classification. Summary rows show averages across augmentation and automation tasks.

</div>

## Robustness: AI Users Only

Students and instructors who rarely or never use AI may classify tasks differently from those with firsthand experience. Appendix Table 17 restricts the classification sample to respondents who report using AI at least occasionally. This restriction changes only one classification: finding information flips from automation to augmentation, consistent with AI users having a more interactive experience with this task. All other classifications remain unchanged.

<div class="center">

<div id="tab:class_aiusers">

+-------------------------+-------------------+-----------------------+----------------+----------------+
|                         | Overall (full)    | Overall (AI users)    | Full           | AI users       |
+:========================+:=======:+:=======:+:=========:+:=========:+:==============:+:==============:+
| 2-3 (lr)4-5 Task        | \% With | \% For  | \% With   | \% For    | Classification | Classification |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Explaining concepts     | 61.6    | 35.8    | 64.7      | 35.3      | AUG            | AUG            |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Summarizing texts       | 22.8    | 74.6    | 23.6      | 76.4      | AUTO           | AUTO           |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| **Finding information** | 48.5    | 48.8    | 50.5      | 49.5      | AUTO           | **AUG**        |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Generating ideas        | 56.8    | 40.5    | 62.5      | 37.5      | AUG            | AUG            |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Proofreading            | 37.9    | 59.4    | 42.5      | 57.5      | AUTO           | AUTO           |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Editing essays          | 50.1    | 47.3    | 55.7      | 44.3      | AUG            | AUG            |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Writing emails          | 36.4    | 60.9    | 37.3      | 62.7      | AUTO           | AUTO           |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Coding help             | 61.8    | 35.5    | 64.9      | 35.1      | AUG            | AUG            |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Writing essays          | 34.4    | 62.9    | 35.1      | 64.9      | AUTO           | AUTO           |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+
| Creating images         | 32.9    | 64.4    | 33.2      | 66.8      | AUTO           | AUTO           |
+-------------------------+---------+---------+-----------+-----------+----------------+----------------+

: For/With Classification: AI Users Only

</div>

</div>

<div class="singlespace">

*Notes:* This table replicates the classification analysis restricting to respondents who report using AI more than rarely. The first two columns show the overall (student and instructor combined) percentages from the full sample; the next two columns show the corresponding percentages among AI users only. Tasks in bold indicate changes in classification relative to the full sample.

</div>

# Qualitative Evidence on Student Perspectives on AI Use
This section analyzes student responses to an open-ended question about their use of generative AI: "Please describe the factors that have personally influenced your use of generative AI in your academic work. What initially led you to try it, what has motivated you to use it or caused you to hesitate?" 48.7 percent of respondents answered this optional question. Appendix Figure 10 presents a word cloud of the most frequent words in the responses.

## Validating the Open-Ended Response Measure

We first validate our open-ended response measure. We use VADER (Valence Aware Dictionary and sEntiment Reasoner), a lexicon-based sentiment analysis tool (Hutto and Gilbert, 2014), and test whether sentiment scores correlate with actual AI adoption. If the responses capture real attitudes, students with more positive sentiment should adopt AI at higher rates. We test this prediction using two measures: whether students have ever used generative AI, and whether they currently use AI for academic purposes. Appendix Figure fig:vader presents binned scatterplots of AI adoption against standardized sentiment scores.

Sentiment toward generative AI strongly predicts adoption. Students with negative sentiment scores show adoption rates of 83–92 percent for ever using AI and 69–85 percent for academic use, while those with positive scores reach nearly 100 percent for general use and 87–100 percent for academic purposes. The relationship is stronger for academic AI use (Panel B), where $\hat{\beta} = 0.169$ is twice as large as for general adoption.[^19] The open-ended responses thus capture meaningful variation in attitudes that maps to behavior.

## How Students use Generative AI

To analyze these responses systematically, we classified each one using keywords. For example, if a student mentioned saving time, we tagged the response as "time-saver"; if a student expressed concern about learning, we tagged it as "negative learning." We allowed multiple keywords per response. Appendix Figure 11 shows the frequency of keywords. The responses reveal how students use AI, what motivates them, and what causes some to hesitate.

The most common use is as an explanatory tool. Nearly 30 percent of responses mentioned using AI to understand course material, asking it to break down concepts from readings and lectures. One student reported: "I can ask AI to explain concepts to me that I have a hard time grasping. \... I can keep asking 'simplify' or 'break down even more."' Students also use AI to summarize dense readings, which they say helps manage heavy course loads.

Students use AI throughout different stages of the writing process. Some use AI to generate initial drafts that serve as starting points. One student explained: "Helps me get started with a base for most of my essays. It feels easier to edit something already written and make it my own than to write from scratch." Others use AI more narrowly for brainstorming when stuck on specific problems. As one student noted: "I use it if I am feeling stuck to push me to the right direction (whether a mathematical problem or an essay idea)." Many also report using AI as an editing tool to improve grammar, sentence structure, and overall writing flow. This editing use is especially common among non-native English speakers. As one student explained: "English is not my first language and it frustrates me sometimes that I cannot find the best way to phrase a certain idea and AI is a useful tool to have to find alternate expressions."

Students also mentioned task-specific uses. In coding-intensive courses, students use AI for debugging and understanding programming concepts. Others use it for administrative tasks like formatting citations and drafting emails. Many treat AI as an enhanced search engine: "It has significantly reduced the time it takes to conduct research on new topics and ideas, and helps me by giving me a thorough selection of sources to use for projects of any kind."

## Why Students Adopt AI

Saving time was the most cited reason for adoption. Nearly 25 percent of responses mentioned using AI to complete work more efficiently, viewing it as a way to manage demanding course loads. Students particularly embrace AI for mechanical or administrative tasks—one noted using it for "Writing emails quick and creating resume/ cover letter templates." But AI assistance extends beyond grunt work. Some use it to "spend less time doing assignments and homework," especially when they view the work as peripheral: "when I come across work I deem as ineffective, I want to spend as little time as possible doing it."

Having an on-demand tutor was another key motivation. Around 12 percent of responses described using AI as a "tutor" when other resources were unavailable. As one student noted, "I use it as a last resort (if there are no office hours, after looking up videos, etc.) if I need extra help. I'd like to think that the way I use it is similar to going to office hours or TA hours."

Peer influence also drove AI adoption. Some students reported feeling pressure to use AI to remain competitive with their classmates. One student explained: "I noticed others use it, are getting better grades than me, and they say they learn better with the help of AI, so I gave it a try." Others worried about being at a competitive disadvantage: "Other people were using it and told me about it. I felt like I would be at a disadvantage if I wasn't also using it."

## Concerns and Limitations

The most frequent concern was negative impacts on learning. One student who initially used AI extensively reported: "In the past, I have simply plugged and chugged homework assignments into ChatGPT and submitted it. Those assignments feedback from teachers was positive and I was getting good grades, but I definitely felt that my own learning outcomes to be significantly worse." Others viewed AI use as fundamentally incompatible with their educational goals: "my task is as a humanities student is to think, not calculate; why should I let AI do the thinking for me? It would defeat the purpose of pursuing my education."

Many students described ethical uncertainty about where to draw the line. One noted: "I never use it to explicitly write something because that feels like overt cheating, but sometimes I hesitate when it completely solves Econ problems. I understand how it does it, and it helps me to learn, but it still sometimes feels a little morally gray." Another expressed similar ambivalence: "I tend to only use it when it will save me time in a moral way." Closely related was the desire to maintain ownership of their work: "I don't have interest in using generative AI for my academic work because I want my work to reflect my own ideas." Another noted: "It usually would not even occur to me to turn to AI to substitute writing because I want to take credit for my work, and using AI seems to diminish that."

Technical limitations also deterred some students. Concerns about inaccurate outputs ("hallucinations") and poor quality were common, especially for creative or complex analytical work. One student noted: "In my poetry class we were instructed to use it to come up with poems and they were awful, so that kinda turned me away from using it to do my work for me."

## Discussion
Two overarching themes emerge from the responses.

First, students vary substantially in how they incorporate AI into their academic lives, and this heterogeneity depends largely on what they perceive as "appropriate" uses. For tasks they view as core—writing essays, solving problems—many hesitate. One student put it clearly: "Most of my work is writing or reading. If I'm not doing the writing, what is the purpose of me taking the class?" Yet students draw different boundaries between central tasks and grunt work. Some use AI extensively, viewing their role as a manager who provides direction while AI handles implementation. Others restrict it to brainstorming, editing, or drafting emails. Still others avoid AI entirely for academic work, often for ethical reasons. Even among users, adoption patterns reflect individual trade-offs between time savings, learning goals, and integrity concerns.

Second, efficiency and learning are in tension. The time-saving benefits are easy to observe and quantify. But they are unlikely to be a free lunch: some may come at the cost of spending less time with material that requires deeper engagement. As one student noted: "There may be a negative effect in that it eliminates much of the 'struggle' in learning." Yet having an on-demand tutor can also improve learning: "It can explain concepts to me in a way that is tailored to my learning style." This tension suggests that AI's impact on learning depends not on whether students use it—almost all do—but on how they use it.

<figure id="fig:ai_wordcloud_motivation" data-latex-placement="H">
<img src="results/wordcloud_motivation.png" />
<p><em>Notes:</em> Word cloud displaying words that appear at least five times in 309 student responses after removing common English stop words and the word “AI”. Text size is proportional to word frequency. The visualization is based on responses to the question: “Please describe the factors that have personally influenced your use of generative AI in your academic work. What initially led you to try it, what has motivated you to use it or caused you to hesitate?’</p>
<figcaption>Word Cloud of Student Motivations for Generative AI Use</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="results/vader_adopt_ever.pdf" />
<figcaption>Panel A. Ever Used Generative AI</figcaption>
</figure>
<figure>
<embed src="results/vader_adopt_acad.pdf" />
<figcaption>Panel B. Uses AI for Academic Purposes</figcaption>
</figure>
<p><em>Notes:</em> This figure presents the relationship between AI sentiment and AI adoption. Panel A shows the proportion of respondents who have ever used generative AI, while Panel B shows the proportion who use AI for academic purposes. Each point represents the mean adoption rate for respondents within sentiment score bins of width 0.2. Sentiment scores are standardized compound scores computed using Hutto and Gilbert (2014)’s VADER algorithm applied to responses to an open-ended question about generative AI. Positive values indicate positive sentiment and negative values indicate negative sentiment. The dashed lines show OLS best-fit lines estimated on the microdata, with coefficients and standard errors (in parentheses) displayed in the top-left corner of each panel.</p>
<figcaption>Panel B. Uses AI for Academic Purposes</figcaption>
</figure>

<figure id="fig:ai_keywords_motiv" data-latex-placement="H">
<embed src="results/ai_keywords_motiv.pdf" />
<p><em>Notes:</em> The figure shows the share of open-ended responses that mentioned different themes related to AI use. The responses come from the question “Please describe the factors that have personally influenced your use of generative AI in your academic work. What initially led you to try it, what has motivated you to use it or caused you to hesitate?” Color coding indicates the category of each theme. Usage type refers to how students use AI tools. Motivation captures what drove students to try AI. Concerns include mentions of course policies and academic integrity, individual reservations about AI use, worries about AI’s impact on education, and AI’s technical limitations.</p>
<figcaption>Frequency of Keywords in Student Motivations for AI Use</figcaption>
</figure>

# Qualitative Evidence on Student Views of AI Policies
This section analyzes student responses to an open-ended question about Middlebury's AI policies: "Do you have any specific feedback or suggestions about Middlebury's generative AI policies, resources, or support services?" Appendix Figure 12 presents a word cloud of the most frequent words; Appendix Figure 13 shows keyword frequencies.

## Polarized Views on Generative AI Policy Approaches

Students expressed sharply different views about AI policies. Some advocated embracing the technology: "The tool is there, there is supply and there is demand. Don't fight another war on drugs. Don't live in a fake reality." Others called for restrictions, arguing that "the use of generative AI is dishonest and corrosive" and that it "prohibits these organic processes and divorces students from true learning."

The most common position, however, called for a balanced approach. Students distinguished between uses that enhance learning (concept explanation) and those that substitute for it (generating entire essays). One student wrote: "AI also can really be helpful at explaining a textbook problem that doesn't make sense, or guiding slightly with homework, or creating study materials, or editing/tightening up your prose. All of those things are good, and universities should figure out how to maximize AI use for those reasons and to minimize students just feeding their problem sets into ChatGPT."

A recurring theme was the perceived futility of blanket bans. One student noted: "I don't think anyone really cares what the policy of any given class is. If professors want people to not use it, they need to structure assessments in a way that will discourage use." Another compared AI bans to restricting internet use: "AI policies seem to be totally irrelevant. It's like telling people they can't use the internet as a resource for the class." The perceived ineffectiveness of bans creates fairness concerns: "I think if it is banned in a class, that should be enforced (and right now it absolutely is not)\... As with any form of cheating, those who don't cheat are put at a disadvantage."

## Need for Clear Guidelines

Students repeatedly asked for clarity. Many said they did not know what counted as acceptable use in a given course: "I think it should be more clear whether we can use it and how and how to cite it since most professors rarely mention it at all." Beyond knowing the rules, students wanted to understand why they existed: "I think that Professor's should be very specific about what is allowed and their reasoning behind their policy."

A related frustration was inconsistency across courses. As one student put it: "Sometimes its confusing when one class allows it and another doesn't and the other encourages it and so on so if there was a school wide or department wide policy that could help." Others pushed back against uniform rules, noting that AI is more useful in some fields than others: "GenAI is more effective in some classes/majors than others. Making sure professors understand how students use GenAI and how useful GenAI is in their class (given the course structure, nature of assignments/material, etc.) is very important for the class policy."

## Training and Support Services

Many students called for formal training on generative AI use. One proposed "a workshop that teaches you to effectively use GenAI without violating the honor code." Others wanted help distinguishing productive from counterproductive uses: "I think it could be useful to develop some sort of training. How do we use AI in a way that actually benefits our learning? I tried out some things on my own but I feel that I need more guidance." The underlying concern was not whether to use AI, but how to use it well.

Students frequently connected this desire for training to workplace preparedness. One noted that "As the world uses more and more AI, I think it is an important tool that students should know how to leverage." Another framed the issue more bluntly: "The moment us students leave campus, we will be using it in the professional world, and when used in combination with one's own skills, it is merely a tool to maximize efficiency." For many respondents, learning to use AI well is not a nice-to-have but something their college education should prepare them for.

## Discussion
The picture that emerges from these 194 responses is one of unresolved contradictions. Most students have already made AI part of their workflow, using it for brainstorming, editing, and concept clarification. They distinguish that use from having ChatGPT write an essay, and they want policies that reflect the distinction. Blanket bans, in their view, do not. As one student noted, such bans "seem to be totally irrelevant" when enforcement is inconsistent and compliance puts rule-followers at a disadvantage. Students also disagree about who should set the rules. Some want a campus-wide standard so they know what to expect; others argue that an economics professor and a creative writing instructor face such different questions about AI that a uniform rule makes no sense. What nearly everyone agrees on is that the status quo fails students: policies vary by course, often go unstated, and rarely come with any explanation of the reasoning behind them.

<figure id="fig:ai_wordcloud_policy" data-latex-placement="H">
<img src="results/wordcloud_policy.png" />
<p><em>Notes:</em> Word cloud displaying words that appear at least five times in 194 student responses after removing common English stop words and the word “AI”. Text size is proportional to word frequency. The visualization is based on responses to the question: “Do you have any specific feedback or suggestions about Middlebury’s generative AI policies, resources, or support services?”</p>
<figcaption>Word Cloud of Student Feedback on Generative AI Policies</figcaption>
</figure>

<figure id="fig:ai_keywords_policy" data-latex-placement="H">
<embed src="results/ai_keywords_policy.pdf" />
<p><em>Notes:</em> The figure shows the share of open-ended responses that mentioned different themes related to Middlebury’s AI policies. The responses come from the question “Do you have any specific feedback or suggestions about Middlebury’s generative AI policies, resources, or support services?” Color coding indicates the category of each theme. Policy Approach captures suggestions about how AI should be regulated at the college. Adoption Views reflect positions on whether and how AI should be integrated into academic work. Training Needs indicates requests for guidance and support. Other Concerns include issues of workplace relevance and fairness.</p>
<figcaption>Frequency of Keywords in Student Feedback on AI Policies</figcaption>
</figure>

[^1]: Examples include Chegg and Course Hero for homework help and essay writing; Grammarly for proofreading and grammar checking; Khan Academy, Coursera, and YouTube tutorials for concept explanations; faculty office hours for personalized instruction; SparkNotes and CliffsNotes for text summaries; and Stack Overflow for coding assistance.

[^2]: We asked students to report their primary major; some listed two in the open-text box. In those cases, we keep the first. Results are similar if we include each major-student pair in the dataset.

[^3]: We asked about first-year GPA rather than cumulative GPA to measure academic performance at a comparable point in students' college careers, unaffected by grade trajectories across class years.

[^4]: We target representativeness at the field-of-study level given substantial evidence that AI adoption varies systematically across disciplines and occupations, with usage patterns tied to field-specific tasks (Stöhr, Ou, and Malmström, 2024; Humlum and Vestergaard, 2025; Ravšelj et al., 2025; Bick, Blandin, and Deming, 2026).

[^5]: We normalize weights to sum to total enrollment (2760) rather than total declared majors, which differs because some students have multiple majors.

[^6]: The higher adoption rates in higher education may partly reflect demographic composition. Younger and more educated individuals consistently show greater AI adoption: McClain (2025) find that 58 percent of adults under 30 have used ChatGPT compared to 34 percent overall. Bick, Blandin, and Deming (2026) document that workers aged 18–29 are twice as likely to use AI at work as those aged 50–64, and college-educated workers are twice as likely to use AI as those without degrees. Similar age and education gradients appear in Humlum and Vestergaard (2025) and Liu and Wang (2024).

[^7]: We exclude first-year GPA from these regressions because this variable is unavailable for first-year students.

[^8]: ChatGPT's dominance is less pronounced in the general population. Bick, Blandin, and Deming (2026) find that ChatGPT leads with 28.5 percent adoption among U.S. adults, followed by Google Gemini at 16.3 percent—a much smaller gap than we observe at Middlebury.

[^9]: The share of students who report using paid ChatGPT (12.8 percent) is slightly larger than the share who report paying for any AI service (11.4 percent). The gap may arise because some students access paid versions through shared accounts and do not personally pay.

[^10]: This pattern is consistent with anecdotal evidence suggesting that students rely on automation under time pressure, particularly in courses outside their major. See, for example: ["What Happens After A.I. Destroys College Writing?"](https://www.newyorker.com/magazine/2025/07/07/the-end-of-the-english-paper) Hua Hsu, *The New Yorker*, July 7, 2025.

[^11]: While Ravšelj et al. (2025) elicit a different set of academic tasks than our survey, we categorize them similarly. Augmentation tasks are study assistance, brainstorming, and coding assistance; automation tasks are proofreading, translating, summarizing, calculating, research assistance, personal assistance, and writing (academic, professional, and creative).

[^12]: Middlebury has no college-wide AI policy; individual departments and faculty set their own.

[^13]: These policy magnitudes are broadly in line with findings from other contexts. Carvajal, Franco, and Isaksson (2024) estimate that banning AI reduces usage by about 28.9 pp. In our survey, a ban reduces usage by 39.1 pp.

[^14]: An important limitation of our analysis is the sequential nature of the policy questions, which may introduce bias through anchoring or contrast effects. If respondents anchor on their first response or evaluate subsequent scenarios relative to previous ones, the absolute magnitudes of our estimates may be biased. However, if these biases operate similarly across demographic groups, our analysis of between-group differences in policy responses remains informative. We are reassured by the similarity between our self-reported results and those of Carvajal, Franco, and Isaksson (2024), who employ a between-subject vignette experiment in which each respondent is randomly assigned to a single policy scenario, thereby avoiding sequential-response concerns.

[^15]: Similar patterns of limited awareness and confusion surrounding AI policies have been documented in other educational contexts. Stöhr, Ou, and Malmström (2024) find that only 19.1 percent of Swedish students report that their teachers or universities have rules or guidelines on responsible AI use, suggesting widespread policy ambiguity.

[^16]: Perceived benefits vary across student groups (Appendix Table 8). Black students report the most positive perceptions, being 36.1 pp more likely than white students to believe AI improves learning ability. Male students consistently perceive greater benefits than females across most dimensions (2.7-18.1 pp higher). Students in humanities, languages, and literature report less optimistic views than natural sciences majors, with literature majors 31.4 pp less likely to believe AI improves grades.

[^17]: This pattern suggests that many students perceive a low elasticity of grades with respect to learning. While understanding this disconnect is beyond the scope of this paper, several mechanisms could explain it. Grade inflation may create ceiling effects that compress the grade distribution, limiting the scope for learning improvements to translate into higher grades. Alternatively, students may believe that effort and compliance with course requirements matter more for grades than deep understanding of the material—or that these inputs can compensate for gaps in learning.

[^18]: See, for example: ["Everyone Is Cheating Their Way Through College. ChatGPT has unraveled the entire academic project."](https://nymag.com/intelligencer/article/openai-chatgpt-ai-cheating-education-college-students-school.html) John Herrman, *New York Magazine*, May 7, 2025.

[^19]: This stronger association is expected: our open-ended question asked about academic AI use, so sentiment scores are most relevant in that domain.
