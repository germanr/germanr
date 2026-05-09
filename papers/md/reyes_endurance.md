# Cognitive Endurance, Talent Selection, and the Labor Market Returns to Human Capital

*Germán Reyes*  
*May 2026*

**Abstract.** Cognitive endurance—the capacity to sustain performance on a cognitively-demanding task over time—is thought to be a crucial productivity determinant. However, a lack of data on this variable has limited researchers' ability to understand its role for success in college and the labor market. This paper uses college-admission-exam records from 15 million Brazilian high-school students to measure cognitive endurance based on changes in performance during the exam. By exploiting exogenous variation in the order of exam questions, I first show that students are significantly more likely to correctly answer a given question when it appears at the beginning of the test versus the end. Motivated by this fact, I develop a method to decompose test scores into fatigue-adjusted ability and cognitive endurance. I then link these measures to college and employment records to quantify the association between endurance and long-run outcomes. I find that cognitive endurance has a significant wage return. Controlling for fatigue-adjusted ability and other student characteristics, an increase of one standard deviation in endurance predicts a 5.4 percent wage increase. This wage return is equivalent to a third of the wage return to fatigue-adjusted ability. I also document positive associations between endurance and college attendance, college graduation, firm quality, and other outcomes. Finally, I show that the "muddling" of endurance and ability in test score impacts income-based test-score gaps and the informational content of the exam. I discuss the implications of these findings for designing more informative cognitive assessments to select talent and more effective interventions to build human capital.

# Introduction
The human capital framework posits that individuals' skills and knowledge are a form of capital that improves productivity and, thus, labor earnings (Becker, 1962). The positive relationship between human capital and earnings is one of the most robust findings in the social sciences (Deming, 2022), and is supported by a large body of work (e.g., Mincer, 1958; Griliches, 1977; Card, 1999; Card, 2001). While early studies focused on aggregate measures of human capital—like years of schooling—more recent work has focused on estimating the economic returns to specific skills, such as social skills (Deming, 2017), cognitive skills (Hermo et al., 2022), and strategic thinking skills (Choi, Kim, and Lim, 2025). Identifying which skills foster productivity is crucial for the design of effective education and labor-market policies (Almlund et al., 2011; Kautz et al., 2014).

In this paper, I study one skill that may be particularly important for the productivity of knowledge workers: *cognitive endurance*, that is, the ability to sustain performance on a cognitively-demanding task for an extended duration (Brown et al., 2024). Psychologists have long hypothesized that cognitive endurance is an important productivity determinant. This hypothesis is reinforced by research on the nature of expertise—popularized in influential books like *Focus* (Goleman, 2013) or *Deep Work* (Newport, 2016)—which often identifies this skill as a key driver of performance on cognitive tasks. Relatedly, biographers of extraordinary achievers often ascribe their accomplishments to unusually-high endurance (Lykken, 2005). Consistent with this, a vast literature has documented the negative consequences of limited endurance for task performance in many settings.[^1] The hypothesized link between endurance and productivity is also consistent with the large markets for endurance enhancers like coffee or nootropics.

These observations suggest that cognitive endurance and productivity are intimately linked. Yet, despite this popular perception, empirical economists have had little to say about the role of endurance in the labor market, possibly because of a lack of data on this variable. I address this problem by using data from the national college admission exam in Brazil (called "ENEM") to create an individual-level measure of endurance that is based on performance declines throughout the exam (Borghans and Schils, 2018; Brown et al., 2024).

The ENEM is an attractive setting to study cognitive endurance for several reasons. First, the exam is administered under uniform conditions, and the scoring is standardized—two crucial properties for generating measures that are comparable across individuals (Almlund et al., 2011). Second, it is a high-stakes environment. Test scores largely determine college options for millions of high school students who take the ENEM every year. Since test-takers have incentives to exert maximal effort, limits to cognitive endurance are more likely to drive systematic declines in performance rather than low motivation (Duckworth et al., 2011; Gneezy et al., 2019). Third, the exam is grueling. The ENEM is ten hours long and is conducted over two consecutive days of testing. Thus, we might expect cognitive endurance to be an especially valuable skill in this setting and cross-person differences in endurance to be reflected in test performance.

My analysis takes advantage of three features of the ENEM. First, the dataset contains students' responses to each exam question, which enables me to measure student performance throughout the exam. Second, students are randomly assigned different test booklets. Each booklet has the same set of questions but in a different order, which enables me to study how students perform on a given question when they are relatively "fresh" versus mentally fatigued. Third, the ENEM can be linked to other administrative datasets to measure students' long-run outcomes. I link the ENEM records to a census of all Brazilian college students and an employee-employer matched dataset that covers the universe of formal-sector workers in Brazil. In my main sample, I use data from 15 million high-school students and 2.7 billion question responses.

I measure cognitive endurance as the impact of a one-position increase in the order of a given question on the likelihood of correctly answering the question. A potential-outcomes framework reveals that this measure captures the combined impact of two structural parameters: how cognitively fatigued an individual becomes throughout the exam and how an increase in cognitive fatigue affects test performance. These two parameters, and thus, my endurance measure, likely capture a variety of psychological mechanisms, such as grit and attention capacity.

Applying this framework, I first estimate *average* cognitive endurance using two empirical strategies. The first research design compares average student performance *on a given question* as a function of its position on each booklet. This approach provides the more credible estimates of average cognitive endurance; however, since each student only receives one exam booklet, it cannot be used to estimate *individual-level* endurance. Thus, I also use a second research design that can be used to identify both average and individual-level endurance. The second approach consists of creating a position-adjusted measure of question difficulty, and then using this measure as a control variable. Both strategies deliver a similar-sized estimate of average cognitive endurance. A one-position increase in the order of a given question decreases the likelihood of correctly answering the question by 0.08 percentage points. Scaled by the number of questions per testing day, this estimate implies that daily performance decreases by 7.1 percentage points due to limited endurance (relative to a sample mean of 34.3 percent).

Next, I estimate the difficulty-adjusted regression separately for each individual. This allows me to decompose an individual's test score into a measure of cognitive endurance and a measure of fatigue-adjusted academic ability. The measure of cognitive endurance follows the same definition as the average measure described above, but is now estimated separately for each individual student. The measure of fatigue-adjusted ability is the residual of an individual's test score after subtracting from it the component explained by cognitive endurance. To validate the reliability of the endurance measure, I calculate the test-retest reliability using a sample of students who took the exam multiple times. I find that endurance has a test-retest reliability comparable to that of other commonly used variables like teacher value-added (Chetty et al., 2014).

I first use the measures generated by the decomposition to investigate the importance of cognitive endurance for success in college and the labor market. I find that, holding fixed fatigue-adjusted ability and other student characteristics, individuals with more cognitive endurance are more likely to attend college, enroll in higher-quality colleges, are more likely to graduate, earn higher wages, and work for higher-paying firms. The magnitudes of these associations are sizable. For example, ceteris paribus, a one standard-deviation (SD) increase in cognitive endurance predicts a 5.4 percent increase in early-career wages. The corresponding prediction for a one SD increase in fatigue-adjusted ability equals 15.4 percent. Hence, the wage return to endurance is about a third of the size of the return to fatigue-adjusted ability. Instrumental variable regressions show that the association between endurance and wages is larger after accounting for measurement error (on the order of 70 percent the size of the return to ability) and also reveal that the predicted effect is not driven by a mechanical relationship between endurance and test scores.

Then, I assess whether the wage return of endurance varies across jobs by estimating the wage return to ability and to endurance across occupations. The wage returns to ability and endurance exhibit substantial heterogeneity across occupations. On average, occupations that pay higher wages also offer a higher wage return to endurance, revealing a novel type of assortative matching between high-endurance workers and high-paying jobs. Furthermore, occupations with a high wage return to endurance also tend to have a high wage return to ability, suggesting that these two skills are complements in production. Among the occupations with the highest wage return to endurance are those where lapses in sustained attention can have significant production costs, such as professionals in the aviation industry. This pattern suggests that the capacity to sustain focus on a task for extended periods may be a key psychological mechanism contributing to the reduced-form measure of cognitive endurance.

These findings on the varying returns to ability and endurance across occupations and college degrees highlight the importance of distinguishing between ability and endurance for selecting talent. However, when ability and endurance are combined into a single index (the test score) the market faces muddled information (Frankel and Kartik, 2019; Frankel and Kartik, 2022). Even though admission officers or employers would want to assess candidates primarily based on the skills most crucial for success, the information about this skill is "contaminated" by less-relevant information about the other skill.

An important question is whether this skill muddling makes the exam more or less informative for predicting students' future success. Test scores function as signals about student quality. More informative signals enable better student-college matches and enhance the efficiency of college markets. I measure the information content of the exam using the correlation between question responses and long-run outcomes, or "predictive validity," for short (Rothstein, 2004). For identification, I exploit variation in when students encounter a given question across exam booklets, which changes the skill composition reflected by their responses. Intuitively, performance differences when a given question appears at the exam's beginning primarily reflect ability differences (as most students are "fresh"), while differences towards the end increasingly reflect differences in endurance as well.

Skill muddling reduces the predictive validity of exam questions. I find that a given question becomes less predictive of long-run outcomes the later it appears in the exam. This result is driven by the fact that performance differences at the beginning of the exam mainly reflect differences in ability, which are highly predictive of long-run outcomes. In contrast, performance differences towards the end of the exam also reflect the noise associated with mental fatigue, which reduces the information content of test responses.

My findings yield three broad lessons. First, cognitive endurance matters for success in college and the labor market. Thus, investing in the development of this skill, possibly during early ages, may have significant societal returns. Second, distinguishing between endurance and ability can improve how talent is selected and trained. Since the value of endurance varies among college majors, the student-major match may improve if majors where high endurance is required to succeed screen applicants partly based on this skill. Third, seemingly neutral exam design decisions that influence the importance of endurance for test performance—such as number of breaks or the length of the exam —can have important consequences for predictive validity and, likely, the student-college match quality.

This paper contributes to a growing literature documenting the importance of different dimensions of human capital for long-run outcomes. A large body of work shows that cognitive skills are valuable in the labor market (e.g., Hanushek and Woessmann, 2008; Hanushek and Woessmann, 2012; Fé, Gill, and Prowse, 2022; Hermo et al., 2022). This work often uses test scores as a measure of cognitive skills. I show that, even in a high-stakes setting, test scores partly capture cognitive endurance and provide methods to decompose test scores into fatigue-adjusted ability and endurance. Relatedly, a growing body of work shows that noncognitive skills are also important predictors of long-run outcomes (Bowles, Gintis, and Osborne, 2001; Heckman, Stixrud, and Urzua, 2006; Borghans et al., 2008; Almlund et al., 2011; Lindqvist and Vestman, 2011; Deming, 2017; Edin et al., 2022; Buser, Niederle, and Oosterbeek, 2024). I document the strong predictive power of one noncognitive skill (endurance) for long-run outcomes and study how it relates to a measure of cognitive skills (fatigued-adjusted ability) in the labor market.

This paper also contributes to the literature that studies cognitive endurance and fatigue effects in field settings. The consequences of limited endurance have been documented in a wide variety of environments (see footnote 1). Recent experimental evidence shows that children's cognitive endurance can be trained, which leads to less pronounced performance declines over time (Brown et al., 2024). I contribute by linking individual-level endurance to long-run outcomes and establishing a novel set of associations. I do this in a high-stakes exam, which complements previous studies documenting performance declines in the low-stakes PISA test (e.g., Debeer et al., 2014; Borghans and Schils, 2018; Zamarro et al., 2018; Balart and Oosterveen, 2019). My findings provide a micro perspective on the results of Balart, Oosterveen, and Webbink (2018), who show that the average performance decline in the PISA test among a country's test-takers has a sizable predictive power in cross-country growth regressions.

Finally, this paper contributes to the literature on the design of college admission exams (Rothstein, 2004; Ackerman and Kanfer, 2009; Bettinger, Evans, and Pope, 2013; Hoxby, Turner, and others, 2013; Bulman, 2015; Goodman, 2016; Goodman, Gurantz, and Smith, 2020; Riehl, 2023). These exams are designed to rank a large number of applicants. This requires discerning small ability differences, and as a consequence, they tend to be long and arduous. I show that performance on college admission exams measures not only academic preparedness but also the capacity to endure mental fatigue. Hence, there is a limit to how much information an exam can extract about student academic achievement. A lengthier exam may not lead to more precise measures of ability but rather to a selection mechanism that puts more weight on endurance. This may be desirable for programs where endurance is crucial to succeed, but it may come at the cost of screening out high-ability low-endurance students.

The rest of the paper is structured as follows. Section 2 describes the context and data. Section 3 presents a statistical framework and describes my research design. Section 4 presents estimates of average cognitive endurance. Section 5 decomposes test scores into fatigue-adjusted ability and cognitive endurance. Section 6 examines the relationship between cognitive endurance and long-run outcomes. Section 7 studies how skill muddling affects exam information. Section 8 concludes.

# Institutional Context and Data
## The ENEM exam
The High School Assessment Exam (*Exame Nacional do Ensino Médio*, or ENEM) is a high-stakes achievement exam used by most universities in Brazil to admit students (Machado and Szerman, 2021). During the years of my analysis (2009–2016), the ENEM consisted of 180 multiple-choice questions equally divided across four subject tests (language arts, math, natural sciences, and social sciences) and an essay. The testing agency uses item response theory (IRT) to calculate a score for each exam subject.

During my analysis years, the exam took place over two consecutive weekend days, with two subjects tested per day, plus the essay on the second day. Test-takers had four and a half hours to complete the test on the first day and five and a half hours on the second day, with no allocated breaks. To combat cheating, test-takers randomly received one of four different booklets each day. While the order of the subjects and the set of questions was constant across booklets, the order of questions within each subject was randomized.

The exam is simultaneously administered across the country once a year, typically in November. Between 2009 and 2016, over 50 million individuals signed up to take the ENEM, making it the second-largest college admission exam globally during this time frame. Appendix 11 compares the ENEM as it existed during this period to the SAT and ACT exams in the United States and explains how ENEM scores were used in the higher-education system beyond college admissions.

## Data
I combine three administrative databases from Brazil. The base dataset consists of ENEM exam records from 2009–2016. This dataset contains both student- and question-level information. The student-level data includes self-reported demographic and socioeconomic status (SES) measures, such as sex, race, high-school type (public/private), parental education, and family income. The question-level data includes each student's responses to each exam question, the position of the question, and the skill tested.

To study individuals' trajectories through college and the labor market, I link the ENEM records to two other datasets. To measure college outcomes, I use Brazil's higher-education census from 2010–2019. This dataset includes information on all college enrollees' major, university, year of enrollment, number of credits, and year of graduation. To measure labor-market outcomes, I use an administrative employee-employer matched dataset called RAIS from 2016–2018. The RAIS covers the universe of formal-sector workers in Brazil and contains both worker-level and firm-level information. Worker-level data includes educational attainment, occupation, and earnings, while firm-level data includes the number of employees, industry, and geographical location.

## Samples and Summary Statistics
Using the administrative data, I construct my main analysis sample and two additional samples for supplementary analyses.

*High-school-students sample.* To construct this main sample, I impose several sample restrictions. First, I only consider individuals who take the ENEM as high-school students. This restriction excludes individuals who take the exam after dropping out or graduating from high school. Second, I only include individuals with a non-zero non-missing score on each subject test. This restriction excludes, for example, students who missed one of the days of testing. I also exclude a small fraction of students with special accommodations, usually due to a disability. After these restrictions, the high-school-students sample contains information on approximately 15 million students who took the ENEM from 2009–2016.

*Long-run outcomes sample.* To examine students' long-run outcomes, I focus on a subset of the high-school-students sample: 1.9 million high-school seniors from the first two cohorts in my data (2009–2010). For these individuals, I observe college and labor-market outcomes for up to nine years after taking the exam. Specifically, I measure college outcomes using data from 2010–2019 and labor-market outcomes using employment data from 2016–2018. This means that, for the 2009 cohort, I measure employment outcomes 7–9 years after taking the ENEM, and for the 2010 cohort, 6–8 years after taking the ENEM. I account for this variation by controlling for an individual's potential years of experience throughout the analysis.[^2]

*Retakers sample.* To assess the temporal stability of my measure of cognitive endurance, I identify students who take the ENEM more than once, typically as high-school juniors for practice and again in their senior year to apply for college. Approximately 16 percent of test-takers in the high-school-students sample take the exam more than once.[^3] I only include students with a non-zero non-missing score in all years they attempted the test. The retakers sample contains information on 1.5 million students and 3.1 million student-years.

*Summary Statistics.* Table 1 shows summary statistics on the samples. In the high-school-students sample (column 1), the average student is 18.2 years old, 59.8 percent are female, 47.6 percent are white, and 22.2 percent attended a private high school. Over half of students (53.4 percent) have a high-school-educated mother, and 38.8 percent live in a household that earns an income above twice the minimum wage. On average, students correctly respond to 34.3 percent of exam questions. High-school seniors from the 2009–2010 cohorts (column 2) are older, more likely to be female, and more likely to be white. Students in the retakers sample (column 3) are slightly younger, tend to have higher parental incomes, and perform better on the exam. Student characteristics are almost identical across booklet colors (Appendix Table 9).

## Definition of Main Outcomes
This subsection provides definitions of the key outcome variables used in the analysis.

*Test score.* I define a student's exam score as the fraction of correct responses across all four academic subjects. The advantage of this measure is that it is intuitive and consistent with the existing literature (e.g., Zamarro, Hitt, and Mendez, 2019). However, this measure differs from how the Brazilian testing agency calculates the ENEM score, which is based on IRT (see Appendix 11.4). Reassuringly, the correlation between the fraction of correct responses and the IRT-based score is above 0.90 (Appendix Table 26).

*College enrollment.* I define college enrollment as an indicator for appearing in the higher-education census one year after taking the ENEM. The rest of the college outcomes are defined conditional on college enrollment.

*College quality.* I construct an earnings-based index of college quality. To do this, I group all college-educated workers in the RAIS (not just the workers in my sample) based on the university they attended and compute the average earnings of the graduates from each university.[^4]

*College degree quality*. I create an index of college degree (or major) quality using the average earnings of the graduates of each college degree. To allow for international comparisons, I classify majors based on the International Standard Classification of Education (UNESCO, 2012).

*Degree progress.* I calculate the ratio of credits completed to total credits required for graduation, measured annually at the end of each academic year. This measure provides a percentage of degree completion, allowing for comparison across programs with different credit requirements. Data for this variable became available starting with the 2015 higher-education census. Consequently, I use student data from the cohort enrolled in 2015 to measure this outcome, which provides up to five years of degree progress for each student (2015-2019).

*Likelihood of graduating.* I define an indicator for graduating one to six years after enrolling in college. Most students who ever graduate do so within the first six years (Appendix Figure 5). As robustness, I define a measure of on-time graduation based on expected degree length. The higher-education census contains information on how long a student in good standing should take to graduate from each program. I use this information to define an indicator for graduating within the expected number of years.

*Formal-sector employment.* I define formal-sector employment as an indicator for appearing in the employee-employer matched dataset in any year in any year within my sample period. This variable is defined for all test-takers. The rest of the labor-market outcomes are defined conditional on formal employment. If an individual has multiple jobs, I use the data from the job with the highest number of hours. I use the job monthly earnings as a tiebreaker.

*Monthly earnings.* This variable represents the average salary of a worker across all months in a given year. To report this variable, firms have to calculate the worker's total earnings for the year and divide them by the number of months the firm employed the worker. If a worker appears in multiple years in the RAIS, I calculate the inflation-adjusted average monthly earnings across all years. I adjust earnings for inflation using the consumer price index.

*Hourly wage.* I calculate the hourly rate of each worker as the ratio between a worker's inflation-adjusted monthly earnings and the hours worked per month.[^5] If a worker appears in multiple years in the RAIS, I calculate the average hourly wage across all years.

*Firm, industry, and occupation mean wage.* I calculate the average hourly wage at each firm, industry, and occupation. I use leave-one-out measures so that an individual's own employment outcomes do not affect the mean wage. I define firms using the 14-digit CNPJ,[^6] industries using the Brazilian National Classification of Economic Activities (CNAE), and occupations using the Brazilian Occupational Code Classification (CBO). I calculate the wage indices separately for each year and use the average value across years.

# Empirical Framework
This section describes the empirical approach used to measure cognitive endurance. I begin by presenting a potential-outcomes framework that links cognitive fatigue to test performance. I use the framework to formally define cognitive endurance in terms of empirical estimands and to clarify the identification assumptions. Then, I describe two research designs that I use to identify cognitive endurance.

## Statistical Model
Let $C_{ij}$ be the probability of individual $i$ correctly answering question $j$. I model $C_{ij}$ as a function of the student's level of cognitive fatigue, $f_{ij}$. Fatigue affects performance by impairing cognitive functions such as attention, memory, or reasoning (Ackerman, 2011). The effects can manifest in many ways, including students forgetting a crucial formula, making a computation mistake, misinterpreting or ignoring an important aspect of a question, and filling in the wrong bubble in the multiple-choice sheet.

To build intuition, first consider an environment in which fatigue is binary: individuals can be either mentally "fresh" ($f_{ij} = 0$) or "fatigued" ($f_{ij} = 1$). Let $C_{ij}(0)$ be the probability of individual $i$ correctly answering question $j$ if she is fresh and $C_{ij}(1)$ the likelihood if she is fatigued. These two probabilities denote potential outcomes for different fatigue levels, but only one of the two outcomes can be observed. Actual performance, $C_{ij}(f_{ij})$, can be written in terms of these potential outcomes as

$$\begin{align}
 C_{ij}(f_{ij}) = C_{ij}(0) + \underbrace{\Big( C_{ij}(1) -  C_{ij}(0) \Big)}_{\text{``Fatigue effect'' } (\kappa_i)} f_{ij},
\end{align}$$

where $C_{ij}(1) -  C_{ij}(0) \equiv \kappa_i$ measures the effect of cognitive fatigue on $C_{ij}$, or "fatigue effect," for short. I allow the fatigue effect to be heterogeneous across individuals, although for simplicity I assume that it is constant across types of questions.

Suppose for the moment that we observed whether individuals were fresh or fatigued when they answered each exam question. One could then compare an individual's average performance in questions answered while fatigued ($\mathop{\mathrm{\mathbb{E}}}[C_{ij} | f_{ij} = 1]$) to their average performance in questions answered while rested ($\mathop{\mathrm{\mathbb{E}}}[C_{ij} | f_{ij} = 0]$). This can be written as

$$\begin{align*}
    \mathop{\mathrm{\mathbb{E}}}[C_{ij} | f_{ij} = 1] - \mathop{\mathrm{\mathbb{E}}}[C_{ij} | f_{ij} = 0] &= \underbrace{\left(\mathop{\mathrm{\mathbb{E}}}[C_{ij}(1) | f_{ij} = 1] -  \mathop{\mathrm{\mathbb{E}}}[C_{ij}(0) | f_{ij} = 1]\right)}_{\text{Term 1: Fatigue effect }}  &+ \underbrace{\left(\mathop{\mathrm{\mathbb{E}}}[C_{ij}(0) | f_{ij} = 1] -  \mathop{\mathrm{\mathbb{E}}}[C_{ij}(0) | f_{ij} = 0]\right)}_{\text{Term 2: Selection bias}}.
\end{align*}$$

This expression shows that a comparison of average performance yields the sum of two terms. The first term represents the fatigue effect for questions answered while fatigued. The second term represents a selection bias that arises when comparing performance across different questions. For example, a selection bias might arise if individuals become fatigued over time and questions become increasingly difficult over the course of the exam. In this case, an individual's average performance would deteriorate even if they had not experienced fatigue.

In practice, cognitive fatigue is not binary; rather, an individual can experience different gradations of cognitive fatigue. In what follows, I assume $f_{ij}$ is continuous and interpret $\kappa_i$ as the impact of a unit change in cognitive fatigue on performance. Because cognitive fatigue cannot be directly observed, estimating $\kappa_i$ is not feasible. In the empirical analysis, I use the position of question $j$ on the booklet randomly assigned to $i$ ($\text{Position}_{ij}$), under the reasoning that students become increasingly fatigued as the exam progresses. This approach is supported by research showing that time-on-task is a significant determinant of cognitive fatigue (e.g., Ackerman and Kanfer, 2009).

To understand how cognitive fatigue relates to question position, consider a hypothetical linear projection of $f_{ij}$ on $\text{Position}_{ij}$:

$$\begin{align}
 f_{ij} = \omega_i + \pi_i \text{Position}_{ij} + \eta_{ij}.
\end{align}$$

In this projection, the intercept $\omega_i$ represents $i$'s cognitive fatigue at the beginning of the test. The slope $\pi_i$ measures the change in cognitive fatigue due to a one-position increase in the order of a given question. The term $\eta_{ij}$ represents a mean-zero projection error, uncorrelated with $\text{Position}_{ij}$ by definition. If student $i$ answers the exam in chronological order and finds the exam mentally taxing, we would expect $\pi_{i} > 0$, indicating a positive relationship between question position and cognitive fatigue.

Using equation eq:pot-projection, we can rewrite equation eq:pot-out as a regression equation that can be estimated using observational data:

$$\begin{align}
 C_{ij} = \alpha_i + \beta_i \text{Position}_{ij} + \varepsilon_{ij}.
\end{align}$$

The intercept of the regression, $\alpha_i \equiv \mathop{\mathrm{\mathbb{E}}}[C_{ij}(0)] + \kappa_i \omega_i$, measures $i$'s expected performance on the test if they were fresh ($\mathop{\mathrm{\mathbb{E}}}[C_{ij}(0)]$), plus the impact of their initial level of fatigue on performance ($\kappa_i \omega_i$). Henceforth, I interpret $\alpha_i$ as a measure of $i$'s academic ability. The slope of the regression, $\beta_i \equiv \kappa_i \pi_i$, is the product of two structural parameters, $\kappa_i$ and $\pi_i$, which are likely determined by several psychological mechanisms. For instance, some individuals' performance may be less impaired by cognitive fatigue (captured by a low $\kappa_i$) due to high intrinsic motivation or grit. Similarly, some students may becomes fatigued more slowly throughout the exam (captured by a low $\pi_i$) due to high conscientiousness—which may lead to diligent test preparation and better test-taking strategies—or high attention capacity.

In what follows, I interpret $\beta_i$ as $i$'s cognitive endurance. This framework provides a link between the literature on cognitive fatigue (Ackerman, 2011) and the literature on cognitive endurance (Brown et al., 2024). In particular, it shows that cognitive endurance can be partially understood as a skill that allows individuals to cope with mental fatigue. Yet, a limitation of the analysis is my inability to distinguish between the different mechanisms underlying cognitive endurance.

One approach to measure cognitive endurance with observational data is to calculate the change in performance throughout the exam. However, comparing a student's performance across exam questions yields the sum of cognitive endurance plus a selection bias:

$$\begin{align*}
    \mathop{\mathrm{\mathbb{E}}}[C_{ij} | \text{Pos}_{ij} = p ] - \mathop{\mathrm{\mathbb{E}}}[C_{ij} | \text{Pos}_{ij} = p - 1] = \beta_i + \underbrace{\mathop{\mathrm{\mathbb{E}}}[C_{ij}(0) | \text{Pos}_{ij} = p] - \mathop{\mathrm{\mathbb{E}}}[C_{ij}(0) | \text{Pos}_{ij} = p-1] }_{\text{Selection bias}}.
\end{align*}$$

Next, I describe the two research designs that I use to deal with the selection bias.

## Identifying Cognitive Endurance
In the empirical analysis, I first estimate the average cognitive endurance across all students, $\beta \equiv \mathop{\mathrm{\mathbb{E}}}[\beta_i]$. This parameter represents the causal effect of increasing a question's position on average student performance, $\bar{C}_j \equiv \mathop{\mathrm{\mathbb{E}}}[C_{ij}]$. Rejecting the null hypothesis of $\beta = 0$ would demonstrate that test scores reflect not only reflect students' academic preparedness but also their capacity to endure mental fatigue (i.e., this would show that $\kappa_i \pi_i \neq 0$ for some students).

To identify $\beta$, I use two research designs. The first design consists of assessing how average student performance *on a given question* varies as a function of the question's position. This approach leverages the fact that a given question is located in different positions across booklets. To illustrate this approach, Appendix Figure 15 displays student performance in a natural science question (the text of which is shown in Appendix Figure 11). This question appears as early as position 46 in the gray booklet and as late as position 87 in the blue booklet. Correspondingly, the fraction of correct responses declines from 40.8 percent in the gray booklet to 29.9 percent in the blue booklet. Comparing student performance across these two booklets reveals that an increase of 41 positions reduces performance on this question by 10.9 percentage points. Analogous pairwise comparisons can be made for any two booklets.[^7] I exploit this information in the following fixed effects specification:

$$\begin{align}
 \bar{C}_{jb} = \alpha_j + \beta \text{Position}_{jb} + \xi_{jb},
\end{align}$$

where $\bar{C}_{jb}$ is the fraction of students who correctly answered question $j$ in booklet $b$, and $\alpha_j$ are question fixed effects.

The advantage of this approach is that it relies on a weak identification assumption—the random allocation of booklets across students. However, since each student only receives one exam booklet, I cannot compare a student's performance across different booklets to identify individual-level cognitive endurance, $\beta_i$. Thus, I also use a second empirical strategy that can be used to identify both $\beta$ and $\beta_i$.

The second approach consists of controlling for question difficulty ($\text{Difficulty}_{j}$) in equation eq:reg-spec-fe instead of the question fixed effects. To estimate $\beta$, I assess how average student performance changes throughout the exam in regressions of the form:

$$\begin{align}
 \bar{C}_{jb} = \alpha + \beta \text{Position}_{jb} + \delta \text{Difficulty}_{j} + \mu_{jb}.
\end{align}$$

One challenge in implementing this approach is measuring question difficulty. An intuitive and often used measure is the fraction of students who correctly answered the question. However, this fraction varies depending on the question's position in the booklet. Consequently, a question might appear more difficult simply because it is located later in the exam on average across booklets. To address this issue, I exploit the within-question position variation to construct a "position-adjusted" measure of question difficulty. This measure represents the projected fraction of correct responses we would expect to observe if question $j$ appeared in the first position of the exam (see Appendix 12 for details). To avoid a spurious correlation, I calculate question difficulty using data from test-takers outside my sample.[^8]

This strategy yields a consistent estimate of $\beta$ under the assumption that unobserved determinants of student performance are conditionally independent of question position. Below, I provide evidence supporting this assumption. Importantly, as I describe in Section 5, this second strategy can also be used to identify the cognitive endurance of *each individual*. In this case, the identification assumption requires any unobserved determinants of $i$'s test performance to be uncorrelated with question position (conditional on question difficulty). I discuss the consequences of potential violations of this assumption in Section 5.2.

In the following two sections, I present estimates of average cognitive endurance (Section 4) and individual-level endurance (Section 5).

# Cognitive Endurance and Test Performance
This section examines the relationship between cognitive endurance and test performance, presenting empirical evidence of how student performance evolves over the course of the ENEM and estimates of average cognitive endurance using two research designs.

## Student Performance over the Course of the ENEM
As a starting point for the analysis, I begin by studying student performance over the duration of the exam without controlling for question difficulty or any other performance determinant. Figure 1 plots the fraction of students who correctly responded to questions at each position in the test ($y$-axis) against the position of the question in the test ($x$-axis). As a benchmark, the red dashed line shows the expected performance if students randomly guessed the answer to each question. Table 2, column 1 presents estimates of a bivariate regression of the fraction of correct responses on question position.

There is strong negative relationship between student performance and question position. Average performance decreases from about 45 percent at the beginning of each testing day to about 24 percent at the end. The regression estimates indicate that average student performance declines by 21.4 percentage points over the course of each testing day ($p < 0.01$). Furthermore, Figure 1 shows performance recovers between testing days. Specifically, average performance *increases* from about 30 percent at the end of the first day to approximately 45 percent at the beginning of the second day.

Limited cognitive endurance can provide a parsimonious explanation of these patterns. As students advance through the exam, their mental resources may become increasingly taxed, making them more prone to committing mistakes. Cognitive resources are replenished after taking a break (Sievertsen, Gino, and Piovesan, 2016) and overnight via sleep (Baumeister, 2002; Lim and Dinges, 2008), which can explain why performance increases between the end of the first day and the beginning of the second day. However, other factors such as question difficulty could contribute to these performance trends.

## Estimates of Average Cognitive Endurance
To identify average cognitive endurance, I next implement the research designs described in Section 3.2. Table 2 presents estimates of $\beta$ from the two research designs. To facilitate the interpretation of the coefficients, I scale $\beta$ so that it can be interpreted as the change in student performance over the course of each testing day.

Average student performance decreases by about five to seven percentage points per day due to limited cognitive endurance. The question-fixed-effects specification (equation eq:reg-spec-fe) yields an average cognitive endurance $\hat{\beta} = -0.072$ ($p < 0.01$, column 2), indicating that daily average performance decreases by 7.2 percentage points due to limited cognitive endurance. The difficulty-adjusted regression specification (equation eq:reg-spec-diff) produces a similar estimate of $\hat{\beta} = -0.058$ ($p < 0.01$, column 3). The similarity between these estimates suggests that controlling for question difficulty adequately accounts for differences in question characteristics. Furthermore, 97 percent of the variation in $\bar{C_{j}}$ is explained by a question's position and difficulty. This high R-squared suggests that there is limited scope for unobservable variables to affect $\bar{C_{j}}$, lending further support for the selection-on-observables assumption (Oster, 2016).

Figures 2 and 3 provide visual evidence on how limited endurance impacts performance. Figure 2 plots average student performance over the course of the exam after removing the influence of question difficulty. To construct this figure, I first regress $\bar{C}_{jb}$, the fraction of students who correctly answered question $j$ in booklet $b$, on question difficulty, $\text{Difficulty}_{j}$, and estimate the residual from this regression, $\bar{C}^{r}_{jb} = \bar{C}_{jb} - \mathop{\mathrm{\mathbb{E}}}[\bar{C}_{jb} | \text{Difficulty}_{j}]$. I then add back the sample mean to $\bar{C}^{r}_{jb}$ to facilitate interpretation of units. Finally, I plot the mean value of $\bar{C}^{r}_{jb}$ across the exam. The figure shows that performance decreases by about 5.2 percentage points each day, a magnitude consistent with the regression estimates. It also reveals that difficulty-adjusted performance tends to decline linearly throughout the exam, providing support for the linear functional form of equation eq:reg-spec-diff.

Figure 3 depicts the percentage-point change in the probability of correctly answering a question ($y$-axis) against the change in question position across booklets ($x$-axis), averaged across all questions. The line represents the predicted value from a linear regression estimated on the micro data. Its intercept is statistically equal to zero, indicating that a given question is, on average, equally likely to be answered correctly if it appears in the same position in two different booklets. The slope indicates that, on average, a given question is $0.08$ percentage points less likely to be correctly answered if it appears one position later in the test ($p < 0.01$). Thus, student performance decreases by about one percentage point roughly every 12 questions (equivalent to 36 minutes if students spend the exam time uniformly across questions). The implied daily change in performance due to limited endurance equals $7.2$ percentage points ($p < 0.01$), an estimate quantitatively identical to that obtained from the question-fixed-effects specification.

The impact of limited cognitive endurance on test performance is substantial. The fixed-effects-specification estimate indicates a 16 percent decrease from the estimated performance at the beginning of the exam (which is 45 percent, as shown in Table 2, column 1). This performance decline is equivalent to approximately 60 percent of the standard deviation of overall test scores (11.6 percentage points). To contextualize this magnitude, the effect is similar to that of a decrease of half a standard deviation in teacher quality (Chetty et al., 2014). It is also comparable to the impact of increasing class size by about 16 pupils (Angrist and Lavy, 1999), or the performance decline observed when taking an exam under conditions that are 66 degrees Fahrenheit hotter (Park, 2020).

## Limited Cognitive Endurance or Time Pressure?
Throughout this section, I have interpreted the causal effect of an increase in question position on performance as a manifestation of limited cognitive endurance. This interpretation is in line with the framework in Section 3. However, an estimate of $\beta < 0$ could potentially result from students running out of time toward the end of the exam. While the testing agency does not record time-stamped information, I evaluate this alternative explanation using several approaches.

Appendix 10.1 presents three indirect pieces of evidence against this alternative interpretation. First, in the data, very few students leave any responses unanswered, suggesting that time constraints are not preventing them from attempting all questions. Second, performance declines are observed even when students are responding to questions in the first half of each testing day, a period during which they are unlikely to be under significant time pressure. Third, students who took a test preparation course—who presumably are better at time management—exhibit performance declines of similar magnitude to students who did not take such a course. This last result also suggests that the performance decline is unlikely to be driven by strategic test-taking behavior.

Data from Brazil's national college exit exam, the ENADE, enables me to directly test the hypothesis that performance declines are driven by time constraints in a different but comparable setting. The ENADE is a field-specific assessment used by the Brazilian government to evaluate higher education programs. Crucially, at the end of the exam, students answer a questionnaire that includes two time-management related questions. The first question asks: *Considering the length of the exam in relation to the total time, do you think the exam was: (1) very long, (2) long, (3) adequate, (4) short, or (5) very short.* The second question asks: *How much time did you spend to complete the exam? (1) Less than an hour, (2) between one and two hours, (3) between two and three hours, (4) between three and four hours, (5) or four hours, and I couldn't finish*. I use these questions to define samples of students for whom time was not a binding constraint (options 3 through 5 for the first question and 1 through 4 for the second question). Intuitively, if the performance decline were due to time constraints, we would expect to see no change in performance for these subsets of students who reported having sufficient time.

Table 3 estimates the performance change throughout the ENADE for all test-takers and for the subset who had enough time to complete the exam. Average student performance in the ENADE decreases by $6.1$ percentage points over the course of the exam (column 1, $p < 0.01$). This magnitude is equivalent to a $13.5$ percent decrease from the estimated performance at the beginning of the exam (which is $45$ percent, column 1). The magnitude of this performance decline is remarkably similar to the one estimated in the ENEM, which provides support for the external validity of the findings. More importantly, columns 2–5 show that the performance of students who completed the exam without time pressure also declines significantly. For example, column 2 shows that students who assess the exam length as adequate suffered a performance decline of $5.1$ percentage points ($p < 0.01$), equivalent to a $11$ percent decrease from the estimated performance at the beginning of the exam. Similarly, columns 3-5 show significant performance declines for students who reported the exam as short or very short ($6.6$ percentage points, $p < 0.01$), and those who completed the exam within the allocated four hours ($4.9$–$6.5$ percentage points, $p < 0.01$).

Taken together, this evidence strongly supports the interpretation of $\hat{\beta} < 0$ as a consequence of limited cognitive endurance rather than time pressure.

# Decomposing Test Scores into Ability and Cognitive Endurance
The results in Section 4 indicate that test scores are influenced by both students' academic preparedness ("ability") and their capacity to maintain performance under mental fatigue ("cognitive endurance"). This section decomposes individuals' test scores into these two skills and examines the test-retest reliability of the generated measures.

## Linear Decomposition

To quantify the relative influence of ability and endurance on a student's test score, I estimate the difficulty-adjusted regression specification separately for each student:

$$\begin{align}
 C_{ij}  = \alpha_i + \beta_i \text{PosNorm}_{ij} + \delta_i \text{Difficulty}_j + \varepsilon_{ij} \quad \text{for } i = 1, ..., N,
\end{align}$$

where $C_{ij}$ equals one if student $i$ answered question $j$ correctly, $\text{PosNorm}_{ij}$ is question position normalized such that the first question of each day equals zero and the last question equals one, and $\text{Difficulty}_j$ is the position-adjusted measure of question difficulty, normalized to have mean zero. In the baseline specification, I estimate equation reg:lpm-ind pooling student responses from both testing days and all academic subjects. I show robustness to including day and subject fixed effects, to estimating the parameters separately by day and subject, and to estimating non-linear models.

The estimates $\hat{\alpha}_i$ and $\hat{\beta}_i$ describe how student $i$'s performance changes throughout the test. The intercept of each regression, $\hat{\alpha}_i$, measures the predicted probability of the student correctly answering a question of average difficulty at the start of the exam. Thus, $\hat{\alpha}_i$ represents $i$'s performance after accounting for the impact of a question's position and difficulty. The slope of each regression, $\hat{\beta}_i$, measures the predicted performance change throughout each testing day after accounting for question difficulty. Importantly, these statistical measures can be linked to underlying student skills by interpreting equation reg:lpm-ind as an observational analog of the model eq:pot-out-reg. Under this model, $\hat{\alpha}_i$ measures $i$'s fatigue-adjusted ability and $\hat{\beta}_i$ measures $i$'s cognitive endurance.[^9]

## Limitations of Measuring Endurance using Standardized Tests
This approach to measuring cognitive endurance has advantages but also important limitations. The main advantage is that it is based on observed behavior ("revealed preference"). This deals with some of the well-known biases of measures based on self-reports ("stated preferences"). Examples include social-desirability bias (i.e., respondents want to look good in front of the interviewer), reference-group bias (i.e., respondents judge their behavior using different standards), and framing effects (i.e., slightly different ways of asking the same question can cause large changes in respondents' answers). The magnitude of some of these biases has been shown to be quantitatively significant for self-reported grit and self-control, two non-cognitive skills related to cognitive endurance (Lira et al., 2022).

However, this approach has three substantive limitations.

First, estimating individual-level endurance requires one orthogonality condition per student. The identifying assumption is unlikely to hold exactly for *all* students. For example, some students may happen to be unprepared for the questions that appear at the end of the exam. Thus, their decline in performance would partly be driven by lack of preparation, leading to biased estimates of endurance. If the departures from the identification assumption are not systematic (e.g., some students are unprepared for questions at the end, but others are unprepared for questions at the beginning), then this issue is equivalent to measurement error, which would attenuate the effects documented below. Using the retakers sample, I provide evidence consistent with this interpretation. Additionally, I show that the results are similar using several alternative measures of endurance.

Second, the measure of endurance is based on the assumption that the order of the questions in the booklet affects the order in which students answer the exam. While the order of question positions is as-good-as-random, the order in which students actually answer the exam is endogenous. For example, some students may strategically leave the questions they find harder until the end. Consequently, regressing test performance on the actual order in which students answered the exam would show a decline in performance over time simply due to this strategic behavior. Using the order in which questions are positioned on the randomly-assigned booklet as a regressor addresses this problem but may lead to attenuated endurance estimates. Thus, my estimates of endurance should be interpreted as "intention-to-treat" estimates.

Finally, floor or ceiling effects can potentially bias the estimates of endurance. For instance, individuals with extremely low ability or endurance might randomize their responses throughout the entire exam, appearing in the data as having high measured endurance due to their consistently poor but stable performance. While this issue is not unique to this measure of endurance, it may be a concern for the empirical analysis. To address this concern, I show that the results are robust to excluding students in the tails of both the ability and endurance distributions (i.e., students for whom floor and ceiling effects are more likely to be binding).

## Assessing the Reliability of the Cognitive Endurance Measure
Are the measures of fatigue-adjusted ability and cognitive endurance generated by the decomposition reliable? One way to measure the reliability of a construct is by measuring it multiple times and calculating the "temporal stability" or correlation between these measures (Miller, Linn, and Gronlund, 2009). The magnitude of this correlation is a measure of construct reliability; a higher correlation indicates greater reliability.

I compute two measures of test-retest reliability. First, I estimate ability and endurance separately for each testing day and calculate the correlation between consecutive days. The advantage of this approach is that it can be implemented in my main sample, but has the drawback that the academic subjects tested vary each day, which could affect the reliability estimates.[^10] Second, I estimate the temporal stability of ability and endurance between consecutive years. This analysis produces more comparable estimates, but it can only be conducted using the smaller sample of retakers.

The test-retest reliability of academic ability and cognitive endurance are relatively high. Figure fig:temp-stab shows a series of binned scatterplots plotting the average estimate of ability/endurance measured at time $t+1$ as a function of the estimate measured at time $t$. The temporal stability of ability ranges from 0.61 (between consecutive days) to 0.77 (between consecutive years). For cognitive endurance, the temporal stability ranges from 0.14 (between consecutive days) to 0.30 (between consecutive years). These reliability estimates are comparable to those of other often used constructs such as risk aversion or teacher value-added.[^11]

## Summary Statistics on Ability and Cognitive Endurance
Average cognitive endurance is $\hat{\beta} = -0.058$, indicating that, due to limited endurance, the performance of the average student decreases by $5.8$ percentage points over the course of the exam. This estimate aligns with the quasi-experimental results shown in Section 4.

The standard deviation (SD) of $\beta_i$ is $\hat{\sigma}_{\beta} = 0.088$, meaning that an increase of one SD in cognitive endurance predicts an 8.8 percentage point increase in the test score.[^12] The corresponding estimate for fatigue-adjusted ability is $\hat{\sigma}_{\alpha} = 0.132$. Hence, $\hat{\sigma}_{\beta}$ is approximately two-thirds the magnitude of $\hat{\sigma}_{\alpha}$, indicating that ability is more dispersed than endurance across students. These estimates can be translated into percentage effects by dividing by the average test score of 0.343 (as shown in Table 1, Panel D). Under this rescaling, a one SD increase in endurance leads to a 25.6 percent increase in test score (0.088 / 0.343 = 0.256). Similarly, a one SD increase in ability results in a 38.3 percent increase in test score (0.132 / 0.344 = 0.383).

Figure 4 displays the joint distribution of estimated ability ($\hat{\alpha}_i$) and cognitive endurance ($\hat{\beta}_i$). The red diamonds represent a binned scatterplot of mean endurance across 100 equally-sized ability bins, while the gray circles show a scatterplot for one percent of the sample. The figure reveals two important patterns. First, there is substantial variation in individual ability-endurance combinations.[^13] Second, there is a negative relationship between $\hat{\alpha}$ and $\hat{\beta}$. This relationship is largely driven by floor and ceiling effects: low-ability students have a limited margin to decrease their performance throughout the exam because there is a lower bound to how poorly they can perform (i.e., no correct responses). An analogous argument holds for high-ability students. This generates a "missing mass" of students with low-ability low-endurance and high-ability high-endurance, inducing a negative correlation.[^14]

To account for the mechanical relationship between $\hat{\alpha}_i$ and $\hat{\beta}_i$, I always control for both variables in the analysis below. Additionally, I show robustness to excluding individuals in the tails of the ability/endurance distribution.

## Cognitive Endurance and Individual-level Characteristics
What individual-level characteristics correlate with higher fatigue-adjusted ability and cognitive endurance? To address this question, Table 4 presents regressions of each skill on various student characteristics, controlling for the other skill. The coefficients represent the mean skill difference between student groups across five demographic and socioeconomic dimensions: gender (male vs. female students), race (white vs. non-white students, where non-white includes Black, Brown, and Indigenous students), high school type (private vs. public high school), parental education (students with a high-school-educated mother vs. non-high-school-educated mother), and household income (students from households earning more vs. less than twice the minimum wage, representing the top 70 percent vs. bottom 30 percent of the income distribution).

There are substantial differences in both fatigue-adjusted ability and endurance across demographic groups. On average, males exhibit a $3.0$ percentage point higher fatigue-adjusted ability ($p < 0.01$, column 1) and a 3.4 percentage point higher cognitive endurance ($p < 0.01$, column 2) than females. Thus, both differences in ability and endurance contribute to the observed gender-based exam performance gap of $2.6$ percentage points ($p < 0.01$, column 3). Similarly, race and socioeconomic status (SES) are strongly associated with both fatigue-adjusted ability and cognitive endurance. Ability gaps range from $3.4$ percentage points for race to $12.7$ percentage points for private schooling (both $p < 0.01$), while endurance gaps range from $3.1$ percentage points for race to $7.5$ percentage points for private schooling (both $p < 0.01$). As a result, differences in ability and endurance contribute to the SES-based exam performance gaps (column 3).[^15]

In the following two sections, I use the estimates of fatigued-adjusted ability and cognitive endurance to (i) re-examine the relationship between test scores and long-term outcomes through the lens of the ability-endurance decomposition, and (ii) investigate how combining ability and endurance into a single test score impacts the informational content of exams.

# Cognitive Endurance and Student Outcomes in Adulthood
In this section, I use the decomposition to separately quantify the contribution of ability and endurance to the well-known association between test scores and long-run outcomes (e.g., Bishop, 1989; Hanushek and Woessmann, 2008; Hanushek and Woessmann, 2012; Friedman et al., 2025).

## Estimating the Return to Academic Ability and Cognitive Endurance

To assess how test scores and their component skills (ability and endurance) relate to college and labor-market outcomes, I estimate regressions of the form:

$$\begin{align}
    Y_{i} &= \phi         + \lambda X_i  + \psi_T \text{TestScore}_i  + \nu_{i} \\
    Y_{i} &= \tilde{\phi} + \tilde{\lambda} X_i + \psi_A \text{Ability}_i  + \psi_E \text{Endurance}_{i} + \tilde{\nu}_{i}, \end{align}$$

where $Y_i$ is an outcome of student $i$; $\text{Ability}_i$ and $\text{Endurance}_{i}$ are the measures of fatigue-adjusted ability and cognitive endurance estimated in Section 5; and $X_i$ is a vector that contains demographic variables and socioeconomic status (age, race, high-school type, maternal education, family income).[^16] For labor-market outcomes, I additionally control for educational attainment and potential years of experience. Because students can enroll in multiple college degrees, each observation denotes a student–degree combination. I account for the fact that an individual can appear multiple times in the dataset by clustering the standard errors at the individual level.

To compare the magnitude of the predicted effect of endurance on a given outcome ($\hat{\psi}_E$) with the corresponding effect of fatigue-adjusted ability ($\hat{\psi}_A$), I normalize both variables such that their coefficients represent the effect of a one SD increase on a given outcome. As a benchmark of the effect sizes, I compute the ratio between the predicted effect of endurance on an outcome and the predicted effect ability ($\hat{\psi}_E/\hat{\psi}_A$).

## Baseline Estimates

Table 5 presents estimates of equations reg:score-outcomes and reg:endurance-outcomes using as dependent variables college outcomes and labor-market outcomes. Figure fig:binsc-coll-lmkt presents binned scatterplots of a subset of these outcomes against cognitive endurance. To construct each panel, I first regress $Y_i$ and $\text{Endurance}_{i}$ on $X_i$ and ability, and estimate the residuals from these regressions, $Y^r_i$ and $\text{Endurance}^r_{i}$ (adding back the unconditional sample mean to facilitate the interpretation of units). Then, I group individuals into ten deciles based on $\text{Endurance}^r_{i}$ and plot the mean value of $Y^r_i$ for each decile. I first discuss college outcomes and then turn to labor-market outcomes.

*College outcomes.* Test scores positively predict college outcomes (Table 5, Panel A). Students with a one SD higher test score are $8.8$ percentage points more likely to enroll in college (relative to a mean of $24.4$ percent, column 1). Conditional on enrolling in college, the quality of their institution and college major—as measured by the average earnings of previous graduates—is $8.2$ percent to $11.7$ percent higher (columns 2–3), the share of total credits they complete by the end of their first year is $1.4$ percentage points higher (an $8.8$ percent increase relative to the mean of $15.8$ percent, column 4), and they are $6.0$ percentage points more likely to graduate (column 5). Conditional on graduating, they take $0.12$ fewer years to graduate (a $3.1$ percent decrease relative to the mean of $3.4$ years, column 6).[^17]

Both fatigue-adjusted ability and cognitive endurance have an significant predicted impact on college outcomes. The predicted effect of ability on college outcomes is stronger than that of test scores. For example, a one SD increase in ability is associated with a $7.2$ percentage point increase in graduation rate (compared to $6.0$ percentage points for test scores). Cognitive endurance also has a substantial predicted effect on college outcomes. For instance, a one SD increase in endurance predicts a $3.2$ percentage point increase in the likelihood of enrolling in college ($p < 0.01$); a $3.0$ percent increase in the college quality ($p < 0.01$), and a $2.6$ percentage point increase in the six-year graduation rate ($p < 0.01$). The effect of endurance as a percent of the effect of ability ranges from $31.0$ percent to $36.5$ percent, depending on the outcome (third-to-last row, Panel A). Visual evidence further corroborates the strong relationship between endurance and college outcomes (Figure fig:binsc-coll-lmkt, Panels A–C).

These results show that both fatigue-adjusted ability and cognitive endurance are crucial predictors of college success. While the importance of ability has been extensively documented in prior research, the findings suggest that cognitive endurance plays a commensurate role in college outcomes. Moreover, these results reveal that traditional estimates of the impact of test scores—often used as a proxy for cognitive skills—on long-run outcomes partially capture the effect of endurance, rather than solely reflecting academic ability.

*Labor-market outcomes.* Test scores are positively correlated with labor-market outcomes (Table 5, Panel B). On average, students with a one SD higher test score are $0.1$ percentage points more likely to have a formal-sector job (column 1). Conditional on being employed in the formal sector, they have a $12.9$ percent higher hourly wage (column 2), earn a $11.1$ percent higher monthly salary (column 3), are employed by firms that pay $9.2$ percent higher wages (column 4), work in occupations that pay $4.1$ percent higher average wages (column 5), and work in industries that pay $1.3$ percent higher average wages (column 6).

The decomposition of test scores reveals that both fatigue-adjusted ability and cognitive endurance independently predict labor-market outcomes. For example, a one SD increase in endurance predicts a $5.4$ percent increase in hourly wages ($p < 0.01$), a $5.2$ percent increase in monthly earnings ($p < 0.01$), and a $3.6$ percent increase in average firm wage ($p < 0.01$). The strong relationship between cognitive endurance and these three outcomes is illustrated in Figure fig:binsc-coll-lmkt, Panels D–F. These figures show that mean wages and earnings increase roughly linearly with endurance. Depending on the outcome, the predicted effect of cognitive endurance as a percent of the predicted effect of ability ranges from 25.5 percent to 38.7 percent (third-to-last row, Panel B).

These results show that cognitive endurance commands a substantial wage premium in the labor market. Under complete information and frictionless markets, the price of a skill equates to the present value of the future returns it generates (Abraham and Mallatt, 2022). Thus, the significant wage return to endurance suggests that this skill is a key determinant of productivity. The positive wage returns to both ability and endurance are consistent with models where firms pay workers according to their productivity, and output is generated by combining ability with sustained cognitive effort. Cognitive endurance enables workers to maintain effort over extended periods, thereby increasing their total output. Notably, these findings also reveal a novel form of assortative matching in the labor market: workers with high cognitive endurance are more likely to be employed by high-paying firms. This observation is particularly relevant given that worker-firm sorting is a crucial driver of labor-market outcomes (Card et al., 2018).

## Robustness of Baseline Estimates

The results are robust to computing the effects nonparametrically, flexibly controlling for fatigue-adjusted ability, estimating each skill with alternative specifications, and imposing several sample restrictions (see Appendix 10.4 for details).

First, the results are robust to non-parametric estimation methods of the endurance return. In the baseline specification, I estimate linear models of the effect of ability/endurance on outcomes. As a robustness check, I estimate the effect of ability/endurance on outcomes based on the slope of percentile changes (Heckman, Stixrud, and Urzua, 2006). Specifically, I estimate the impact of moving from the bottom to the top decile in the endurance distribution and compare it to an equivalent movement in the ability distribution. Consistent with the baseline estimates, the effect of moving from the bottom to the top decile in the endurance distribution represents 32.6 percent–53.0 percent of the corresponding effect for ability, on the outcome (Appendix Table 14).

Second, the relationship between cognitive endurance and long-run outcomes remains robust when employing more flexible specifications to control for fatigue-adjusted ability. The baseline specification controls for fatigue-adjusted ability linearly, which could potentially mask non-linear relationships between ability and outcomes that might influence the estimated endurance effect. To address this concern, I estimate two alternative specifications: one that includes a seventh-order polynomial of fatigue-adjusted ability, and another that includes fixed effects for each percentile of the ability distribution (Appendix Tables 15 and 16). The estimated effects of cognitive endurance on all outcomes remain substantially unchanged across both specifications, suggesting that the relationship between cognitive endurance and long-run outcomes is not driven by a misspecification of the functional form of ability.

Third, the results are robust to using alternative measures of ability and endurance. In the baseline specification, I estimate each skill by pooling student responses from both testing days and all academic subjects. As a robustness check, I estimate ability/endurance separately for each testing day and/or academic subject, and then use the averaged estimate as regressors in the main model. In addition, I estimate specifications that include day and subject fixed effects, and use an alternative measure of endurance based on the correlation between question position and correct answers. The effects remained consistent across these specifications, with results quantitatively similar to the baseline estimates (Appendix Tables 17 and 18).

Fourth, the results are robust to alternative methods of controlling for question difficulty. In the baseline specification, I compute a position-adjusted measure of question difficulty when estimating ability/endurance. As robustness checks, I also (i) estimate models without controlling for question difficulty, (ii) calculate question difficulty without adjusting for average question position, and (iii) use alternative adjustments for average question position when computing difficulty. The estimates remain remarkably consistent across these specifications, demonstrating that the results are not sensitive to the method of controlling for question difficulty (Appendix Tables 19 and 20).

Finally, the results are also robust to several sample restrictions and corrections for measurement error. I estimate the baseline specification with all students in my sample and without accounting for potential measurement error. As a robustness check, I exclude students in the tails of the ability and endurance distributions to address potential floor and ceiling effects (Appendix Tables 21 and 22). To account for measurement error, I weight observations by the inverse of the standard error of the ability and endurance estimates and also use shrunk estimators that put more weight on measures estimated with higher precision (Appendix Tables 23 and 24). Across all these specifications, the results remain very similar to the baseline estimates.

## Why Is Cognitive Endurance Related to Long-Run Outcomes?

An important question is whether the predicted impact of cognitive endurance on long-run outcomes is due to a mechanical relationship between this variable and the test score. When ability is held constant, an increase in endurance leads to a higher test score. The effects documented above could result from the opportunities created by having a better test score, rather than cognitive endurance being a valuable skill in itself.

To shed light on this issue, I employ a measure of cognitive endurance that is not mechanically related to the test score students use for college applications. ENEM scores are only valid for one year, meaning students cannot use scores from previous years to apply for college. Therefore, I instrument the year $t$ measure of endurance (and ability) with the year $t-1$ measures, using the sample of retakers. Using repeated measures of a skill as an instrument additionally helps to address measurement error (e.g., Grönqvist, Öckert, and Vlachos, 2017; Edin et al., 2022). Appendix Tables 11 and 12 present the results for college outcomes and labor-market outcomes, respectively. Panel A reports OLS estimates using the same specification as in the main analysis but applied to the retakers sample, while Panel B shows the instrumental variables (IV) estimates.

The instrumental variable approach confirms and strengthens the relationship between cognitive endurance and long-run outcomes. The OLS coefficients estimated on the retakers sample are comparable to those estimated on the main sample, while the IV estimates tend to be larger than the OLS estimates. For instance, the OLS estimate of the effect of a one SD increase in endurance on wages is 12.1 percent, while the corresponding IV estimate is 18.8 percent. Similarly, for ability, the OLS estimate is 23.1 percent, compared to the IV estimate of 25.0 percent. Notably, the IV estimates suggest that the wage return to endurance—as a percent of the wage return to ability—is significantly higher, on the order of 75 percent. The difference between the IV and OLS estimates is generally larger for the endurance effects than for the ability effects, consistent with greater measurement error in the endurance measure. These findings indicate that the predicted impact of endurance on long-run outcomes is not due to a mechanical relationship between endurance and test scores.

## Understanding the Channels Through Which Endurance Affects Wages

Cognitive endurance predicts a sizable wage premium in the labor market. This reduced-form impact combines two effects: a direct effect of endurance on earnings (holding human capital accumulation and job characteristics fixed) and an indirect effect through endogenous channels such as educational attainment and job sorting mechanisms. An important question is the extent to which these indirect effects can explain the wage return to endurance.

Establishing causal evidence on this matter is challenging, as it would require an exogenous source of variation for each potential mediating variable. As an alternative, I employ a multivariate regression approach (e.g., Fagereng, Mogstad, and Rønning, 2021; Finkelstein et al., 2024). The starting point is estimating equation reg:endurance-outcomes using log hourly wage as the dependent variable. This regression produces an initial estimate of the wage return to endurance. I then assess how this estimate changes as I sequentially include controls for college attainment, college and major fixed effects, occupation, industry, and firm characteristics. For this analysis, I restrict the sample to individuals for whom data on all mediating variables are available, ensuring comparability across specifications. Appendix Table 13 presents the results. Appendix Figure 7 provides visual evidence in the form of specification curves (Simonsohn, Simmons, and Nelson, 2020), which show how the wage return to endurance (both in absolute terms and as a fraction of the wage return to ability) varies across different combinations of control variables.

The coefficient on endurance declines substantially between the baseline specification (column 1) and the specification that includes the most comprehensive set of controls (column 8). Specifically, the wage return to endurance decreases from 7.7 percent to 2.0 percent, while the wage return to ability decreases from 20.2 percent to 6.0 percent. This suggests that the association between ability/endurance and wages is largely, although not entirely, mediated by college outcomes and job-related factors. The largest declines in the coefficients occurs when controlling for educational attainment (column 3) and college-by-major fixed effects (column 5), suggesting that educational achievement is a particularly important channel through which endurance affects wages. The coefficients further decline when controlling for occupation, industry, and firm fixed effects (columns 6-9), indicating that job-related mechanisms also plays a role in explaining the wage returns to both skills.

These findings suggest that a substantial portion of the wage return to cognitive endurance operates through educational and job-sorting channels, though a direct effect persists even after accounting for these factors. Remarkably, despite the substantial decline in the absolute magnitude of the endurance premium, the relative importance of endurance remains stable—the ratio between the endurance and ability coefficients consistently hovers around one-third across specifications.

## Cognitive Endurance and Earnings Gaps

Understanding the sources of racial and socioeconomic wage disparities is an active area of research in labor economics. While many factors contribute to wage gaps, one potential factor may be systematic skill differences across groups (e.g., Neal and Johnson, 1996; Urzúa, 2008; Bayer and Charles, 2018). Cognitive endurance commands a wage premium in the labor market and, as shown in Section 5.5, it is systematically correlated with race and socioeconomic status (SES). Consequently, differences in cognitive endurance may partially explain observed wage gaps between advantaged and disadvantaged groups.

To quantify the role that cognitive endurance and fatigue-adjusted ability play in explaining wage gaps, I begin by estimating unconditional wage gaps by regressing wages on indicator variables for gender, race, or measures of SES. Table 6, Panel A presents these estimates. Consistent with previous literature, I find substantial unconditional wage gaps across various demographic groups. Males earn 18.9 percent higher wages than females ($p < 0.01$, column 1), whites earn 14.5 percent more than non-whites ($p < 0.01$, column 2), and high-SES workers earn 18.3 percent–27.9 percent more than low-SES workers, depending on the SES measure used (all $p < 0.01$, columns 3-5).

Next, I sequentially control for ability and endurance to examine how these skills contribute to explaining the observed wage disparities. Controlling for fatigue-adjusted ability substantially narrows these gaps (Panel B). For instance, SES wage gaps decrease by 8.4–14.0 percentage points, representing a 31.1 percent–50.0 percent reduction of the unconditional gap. When additionally controlling for endurance, these disparities further diminish (Panel C). The racial wage gap shrinks from 8.9 percent to 6.9 percent (an additional 2.0 percentage point or 13.8 percent reduction). Most notably, the SES wage gaps decrease by up to an additional 4.8 percentage points (or up to a 34.6 percent further reduction beyond what ability alone explains). This implies that cognitive endurance accounts for a meaningful portion of wage gaps even after accounting for differences in cognitive ability.

These findings suggest that cognitive endurance represents a substantial and previously unexamined channel that contributes to earnings gaps in the labor market. The results highlight two important implications. First, traditional measures of cognitive skills may not fully capture the dimensions of human capital that contribute to earnings gaps. Second, this points to the potential for targeted interventions that enhance cognitive endurance among disadvantaged groups as a means to reduce persistent earnings disparities.

## The Return to Endurance Across Occupations

The task-based approach to labor markets highlights that workers produce output by performing job tasks, and tasks differ in their skill requirements (Acemoglu and Autor, 2011; Acemoglu, Kong, and Restrepo, 2024). Consequently, the value of endurance may vary according to the tasks individuals have to accomplish in a given job and the importance of endurance in the production function of those tasks. For example, endurance may be particularly important for some jobs because mistakes due to attentional lapses can dramatically reduce the output value, as in "O-ring" production functions (Kremer, 1993; Demir et al., 2024).

To investigate this, I estimate the wage return to endurance separately for each occupation. Under the assumption that workers are paid in proportion to their productivity, the wage return to endurance should reflect the increase in productivity resulting from an increase in this skill. Thus, a high wage return to endurance in a specific occupation would suggest that this skill is especially valuable in the production function of the tasks required by that occupation.[^18]

The wage returns to ability and endurance exhibit substantial heterogeneity across occupations. Figure fig:endurance-het plots nonparametric Kernel density estimates of the distribution of the wage return to ability (red line) and the wage return to endurance (green line) across 3-digit occupations. For both distributions, the mass is above zero, indicating the two skills are valuable across occupations. The average return to endurance across occupation is 4.9 percent, but there is substantial dispersion. This suggests that cognitive endurance is more valuable for success in some occupations. I also find substantial heterogeneity in wage returns across college degrees and industries.

To make tangible some of the real-world tasks for which endurance may be particularly valuable, Table 7, Panel A list the top-five occupations with the highest wage return to endurance. The list includes occupations where attentional lapses may be extremely costly, such as air navigation professionals (e.g., air-traffic controllers), and occupations in which sustained focus is required to produce valuable output, such as public tax auditors or precision equipment repairers. The top-five college degrees and industries with the highest endurance return includes includes degrees conducive to these occupations (e.g., aeronautics) and related industries (e.g., oil extraction), as shown in Panels B and C. This list provides suggestive evidence that one of the psychological mechanisms behind the reduced-form measure of cognitive endurance is the capacity to sustain attention on a task for a long time.

# Skill Muddling and Exam Informativeness
Admission officers use test scores to screen applicants because they are informative about which applicants will succeed in college. The heterogeneous returns to ability and endurance across occupations and college degrees underscore the importance of disentangling these skills when selecting talent. However, when ability and endurance are combined into a single index (the test score) the market faces muddled information (Frankel and Kartik, 2019; Frankel and Kartik, 2022). While a top score reveals that a student has both high ability and high endurance, an average test score might come from a student with high ability and low cognitive endurance, a student with low ability and high endurance, or a student who is average on both dimensions.

Even though admission officers would want to assess candidates primarily on the skill most critical to success, the information revealed about this skill is obfuscated by the less-relevant information about the other skill. This informational problem could be overcome by reporting separate sub-scores for fatigue-adjusted ability and endurance. However, this may not be feasible due to institutional or other constraints. In this section, I study the consequences of skill muddling for the informativeness of college admissions exams. I focus on identifying how exam information changes when exam questions reveal less information about ability (and more about endurance).

## Measuring Informativeness

The standard approach to measure exam informativeness is to calculate the cross-individual correlation between test scores and a long-run outcome that colleges want to screen their applicants based on (such as first-year college GPA or on-time graduation):

$$\begin{align*}
    \rho^Y  &\equiv \text{Corr}(Y_i, \text{TestScore}_i).
\end{align*}$$

This correlation is known as the *predictive validity* of an exam (Rothstein, 2004). To measure how skill muddling affects predictive validity, ideally one would want to manipulate exam design features—such as exam length or number of breaks—to generate exogenous variation in the relative importance of ability and endurance for performance.

Since this is not feasible in my setting, I instead exploit the variation in question position across exam booklets. As the empirical framework in Section 3 highlights, both ability and endurance are required to correctly answer a question, but the importance of these two skills varies throughout the exam. Loosely speaking, when a question appears at the beginning of the exam, performance differences across students primarily reflect differences in ability since most students are still mentally "fresh." As the exam progresses, questions become affected by skill muddling since differences in performance increasingly reflect differences in cognitive endurance.

This variation allows me to study how the informativeness of exam questions changes when they reveal relatively more about endurance and less about ability. To connect overall exam informativeness to question-level informativeness, notice that the exam's predictive power can be expressed as a weighted average of the informativeness of each exam question $j \in \{1, ..., J\}$:

$$\begin{align}
 \rho^Y = \frac{1}{J} \sum_{j=1}^J  \frac{\sigma_{C_{ij}}}{\sigma_T} \rho^Y_j,
\end{align}$$

where $\rho^Y_j \equiv \text{Corr}(Y_i, C_{ij})$ is the correlation between correctly answering question $j$ and outcome $Y$, $\sigma_{C_{ij}}$ is the standard deviation of correct responses to question $j$, and $\sigma_T$ is the standard deviation of the overall test score. Equation eq:pred-val-decomp shows that, ceteris paribus, an increase in question informativeness $\rho^Y_j$ directly translates to higher exam informativeness.

## Regression Model

I exploit the variation in the position of a given question across booklets in the following fixed effects regression:

$$\begin{align}
 \rho^Y_{jb} &= \alpha_j + \gamma^Y \text{Position}_{jb} + \eta_{jb},
\end{align}$$

where $\rho^Y_{jb}$ is the predictive validity of question $j$ in booklet $b$ for outcome $Y$, $\alpha_j$ are question fixed effects, and $\text{Position}_{jb}$ is the position of question $j$ in booklet $b$.

The coefficient of interest is $\gamma^Y$, which measures the impact of a one-position increase in the order of a given question on the question's predictive validity for outcome $Y$. To facilitate interpretation, I re-scale $\gamma^Y$ so that it represents the change in predictive validity from the beginning to the end of each testing day. Under the framework in Section 3, $\gamma^Y$ can be interpreted as the effect of skill muddling on a question's informativeness.

I examine informativeness for eight outcomes: four college-related outcomes (the fraction of correct exam responses calculated without the contribution of question $j$ to avoid spurious correlation, college enrollment, college quality, and six-year graduation rate) and four labor-market outcomes (hourly wage, monthly earnings, firm mean wage, and wage growth). I cluster standard errors at the question level.

## Informativeness over the Course of the ENEM

I begin by descriptively analyzing the average informativeness of test questions and how it evolves throughout the exam. Table 8, Panel A reports the average predictive validity across all test questions, while Panel B presents estimates from bivariate regressions of question informativeness on question position.

Question responses tend to be informative of long-run outcomes, although the magnitude of the correlations is modest. For example, on average across all questions, correctly responding to a question has a $0.077$ positive correlation with enrolling in college (column 2, $p < 0.01$), a $0.109$ correlation with college quality (column 3, $p < 0.01$), and a $0.092–0.101$ correlation with wages and earnings (columns 6–7, $p < 0.01$). These findings align with the predictive validity literature (e.g., Riehl, 2023; Friedman et al., 2025), though my estimated coefficients are smaller, possibly because I measure informativeness at the individual question level rather than using the overall test score.

Question informativeness declines over the course of the exam, with later questions providing less information about long-run outcomes. For the overall test score, the (re-scaled) coefficient on normalized question position is $-0.184$ ($p<0.01$), indicating that predictive validity decreases by approximately 0.18 from the beginning to the end of the exam. Similar patterns hold for college outcomes, with coefficients of $-0.054$ for college enrollment and $-0.051$ for college quality (both $p<0.01$), and for labor market outcomes, with coefficients of $-0.051$ for hourly wage and $-0.049$ for monthly earnings (both $p<0.01$). Across all outcomes in Table 8, I find a statistically significant negative relationship between question position and informativeness.

This descriptive evidence suggests that skill muddling may reduce the information content of exam questions. However, these patterns could potentially be influenced by other factors such as systematic differences in question characteristics across positions. Next, I address this potential concern by exploiting the variation in a question's position across booklets.

## The Impact of Skill Muddling on Informativeness.

Table 8, Panel C presents estimates of $\gamma^Y$ from equation reg:validity-pos. Figure fig:pred-val-chg-pos shows binned scatterplots plotting how the predictive ability of a question ($y$-axis) changes when the position of the question chances ($x$-axis) for a subset of the outcomes.

Skill muddling reduces the informativeness of exam questions for the majority of outcomes. Increasing a question's position from the beginning to the end of the exam decreases its predictive validity for the overall test score by 0.184 points (column 1, $p<0.01$), for college enrollment by 0.054 points (column 2, $p<0.01$), for college quality by 0.051 points (column 3, $p<0.01$), and for hourly wages and monthly earnings by 0.051 and 0.049 points respectively (columns 5–6, $p<0.01$). Similarly, the predictive validity for graduation rate and firm wage also declines significantly (columns 4 and 7, $p<0.01$), though the magnitude is somewhat smaller for wage growth (column 9, $p<0.01$). These declines in question informativeness are substantial: they represent approximately 40–50 percent reductions relative to the predictive power of questions at the beginning of the exam. In sum, the evidence consistently shows that questions provide less information about long-run success when they appear later in the exam, where performance increasingly reflects differences in cognitive endurance rather than differences in ability.

The decreasing informativeness of questions during the exam helps explain puzzling empirical findings in the literature. Kobrin et al. (2008) study how the predictive validity of the SAT changed after the 2005 revision, which increased the exam's number of questions. Intuitively, more test questions should lead to better measurement of student ability and thus more predictive test scores. Yet, their results showed that the exam's predictive validity remained unchanged. My findings offer a plausible explanation: cognitive fatigue likely eroded the informational content of the additional questions positioned later in the exam, offsetting the expected gains from a longer test. Similarly, Bettinger, Evans, and Pope (2013) document that performance on the ACT's English and Math sections—which appear first in the exam—significantly predict college outcomes, while performance on the Science and Reading sections—which appear last—does not. Rather than indicating that science and reading skills are unimportant for college success, this pattern aligns with my results suggesting that skill muddling diminishes the signal value of questions appearing later in tests, regardless of their content.

## Implications for Exam Design

The findings on skill muddling have important implications for the design of standardized tests. Exam designers face a fundamental tradeoff when designing and interpreting tests in that a longer test measures more endurance at the cost of muddling information on ability.

As noted above, one solution is reporting sub-scores for ability and endurance may. This approach would allow admission officers to measure the two skills and weight them according to their relevance for specific programs or institutions.[^19] In some academic contexts, cognitive endurance may be particularly valuable—for instance, in programs requiring sustained attention to complex problems. In others, raw ability might be more predictive of success. With separate sub-scores, a longer exam would be better as it would provide a better measurement of cognitive endurance. An implementation challenge is that if test-takers may try to game the system once they know they are being tested on endurance.

With a one-dimensional test score, my results suggest that shorter exams may be more informative than longer ones. This aligns with recent trends in standardized testing. For example, in 2023, the Graduate Record Examination (GRE) reduced its duration from nearly 4 hours to just under 2 hours, with the testing agency explicitly noting that "shortening the test will help test-takers stay focused and avoid fatigue" (Educational Testing Service, 2023). Similarly, the College Board launched a digital SAT in 2024 that cuts nearly an hour from the exam, while the ACT announced reductions in the exam duration from three hours to approximately two hours.[^20] These industry-wide shifts toward shorter tests align with my empirical findings on the decreasing informativeness of questions as cognitive fatigue sets in.

My findings also suggest ways to leverage existing exam information to produce more informative test scores. Test scores can be thought of as a method for aggregating individual questions into an index. In typical tests, all questions contribute equally to an individual's score, despite the fact that questions appearing early in the exam are more predictive of long-run outcomes. Testing agencies could improve informativeness by implementing position-based weighting schemes that assign greater importance to responses given earlier in the exam, when cognitive fatigue has less influence.

Finally, my results highlight that seemingly neutral exam design decisions—such as exam length or number of breaks—can significantly influence which students are selected into selective universities. When exam questions are more affected by skill muddling, the exam's capacity to identify students who will succeed in college is reduced. Consequently, the student-college match quality may deteriorate, potentially leading to efficiency losses in the higher education market.

# Conclusion
There is increasing recognition among social scientists and policymakers that skills other than intelligence and technical skills, such as industriousness, perseverance, and self-control, are important predictors of individual-level outcomes (Borghans et al., 2008; Almlund et al., 2011). Just like individuals differ in preferences and personality traits, they also differ in their cognitive endurance. This paper shows that cognitive endurance has a substantial earnings return in the labor market and this return varies across occupations. This insight, coupled with a toolkit to measure endurance, offers a promising avenue for talent selection based on skills that are demonstrably relevant for professional success across diverse occupational contexts.

My findings have implications for investments in different types of human capital. Despite the value of cognitive endurance, a typical school curriculum does not include any material directly aimed at building this skill. Policymakers should consider investing in the development of cognitive endurance, possibly during early ages when neuroplasticity is higher.[^21] An important caveat in my analysis is the lack of exogenous variation in cognitive endurance. While my findings provide evidence of a positive link between endurance and earnings, these estimates may be misleading if the available control variables are inadequate to provide meaningful estimates of the causal effect of this skill on long-run outcomes.

The ability-endurance score decomposition developed in this paper generates directions for future research. Test scores are commonly used in economics research, for example, as measures of cognitive skills (Hanushek and Woessmann, 2008; Hanushek and Woessmann, 2012); as a "surrogate" variable to measure the impact of an intervention on long-run outcomes (Athey et al., 2019); and to measure the effectiveness of educational inputs (Chetty, Looney, and Kroft, 2009; Dobbie and Fryer Jr, 2015; Angrist et al., 2016). The decomposition allows researchers to explore the role of cognitive endurance in these and other applications. For instance, researchers can use conventional value-added methods to identify teachers who might be particularly effective at building cognitive endurance, which would help quantify the multidimensional impacts that teachers can have on students (Jackson, 2018; Petek and Pope, 2023).

# Figures and Tables
<figure id="fig:mean-corr" data-latex-placement="H">
<embed src="../results/mean-corr-question.pdf" />
<p><em>Notes:</em> This figure shows student performance over the course of each testing day in the ENEM. The <span class="math inline"><em>y</em></span>-axis displays the fraction of students who correctly responded to each question, averaged across all years in my sample. The <span class="math inline"><em>x</em></span>-axis displays the position of each question in the exam. The dashed lines are predicted values from a linear regression estimated separately for each testing day. The horizontal red dashed line shows the expected performance if students randomly guessed the answer to each question.</p>
<figcaption>Average student performance over the course of the ENEM</figcaption>
</figure>

<figure id="fig:mean-corr-res" data-latex-placement="H">
<embed src="../results/mean-corr-question-res-subj.pdf" />
<p><em>Notes:</em> This figure shows student performance over the course of each testing day after removing the influence of question difficulty on performance. The <span class="math inline"><em>y</em></span>-axis displays the residuals of a regression of (i) <span class="math inline"><em>C̄</em><sub><em>j</em><em>b</em></sub></span>, the fraction of students who correctly answered question <span class="math inline"><em>j</em></span> in booklet <span class="math inline"><em>b</em></span> on (ii) <span class="math inline">Difficulty<sub><em>j</em></sub></span>, a position-adjusted measure of question difficulty (adding back the sample mean to facilitate interpretation of units). The <span class="math inline"><em>x</em></span>-axis displays the position of each question in the exam. Marker colors denote each academic subject tested. Appendix <a href="#app:difficulty" data-reference-type="ref" data-reference="app:difficulty">12</a> describes how I construct the measure of question difficulty. The dashed lines are predicted values from a linear regression estimated separately for each academic subject. The horizontal red dashed line shows the expected performance if students randomly guessed the answer to each question.</p>
<figcaption>Performance residuals after controlling for question difficulty</figcaption>
</figure>

<figure id="fig:chg-pos" data-latex-placement="htpb!">
<embed src="../results/chg-pos-pct-corr.pdf" />
<p><em>Notes:</em> This figure shows estimates of the impact of an increase in the order of a given question on the fraction of students who correcly answer the question.</p>
<p>The <span class="math inline"><em>y</em></span>-axis plots the average change (in percentage points) in the fraction of students who correctly respond to a question. The <span class="math inline"><em>x</em></span>-axis displays changes in a question position between each possible booklet pair. See Appendix Figure <a href="#fig:hist-chg-pos" data-reference-type="ref" data-reference="fig:hist-chg-pos">[fig:hist-chg-pos]</a>, Panel A for a histogram of the values in the <span class="math inline"><em>x</em></span>-axis. To construct this figure, I first compute the change in student performance and the distance in a question’s position between each possible booklet pair. Then, I calculate the average change in performance for each observed distance.</p>
<p>The solid line denotes predicted values from a linear regression estimated on the plotted points, using as weights the number of questions used to estimate each point. The vertical dashed lines denote 95% confidence intervals, estimated with heteroskedasticity-robust standard errors.</p>
<figcaption>The effect of an increase in the order of a given question on student performance</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/time-stab-alpha-day.pdf" />
<figcaption>Panel A. Ability in day <span class="math inline"><em>d</em></span> and day <span class="math inline"><em>d</em> + 1</span></figcaption>
</figure>
<figure>
<embed src="../results/time-stab-beta-day.pdf" />
<figcaption>Panel B. Endurance in day <span class="math inline"><em>d</em></span> and day <span class="math inline"><em>d</em> + 1</span></figcaption>
</figure>
<figure>
<embed src="../results/time-stab-alpha-1yr.pdf" />
<figcaption>Panel C. Ability in year <span class="math inline"><em>t</em></span> and year <span class="math inline"><em>t</em> + 1</span></figcaption>
</figure>
<figure>
<embed src="../results/time-stab-beta-1yr.pdf" />
<figcaption>Panel D. Endurance in year <span class="math inline"><em>t</em></span> and year <span class="math inline"><em>t</em> + 1</span></figcaption>
</figure>
<figure>
<embed src="../results/time-stab-alpha-2yr.pdf" />
<figcaption>Panel E. Ability in year <span class="math inline"><em>t</em></span> and year <span class="math inline"><em>t</em> + 2</span></figcaption>
</figure>
<figure>
<embed src="../results/time-stab-beta-2yr.pdf" />
<figcaption>Panel F. Endurance in year <span class="math inline"><em>t</em></span> and year <span class="math inline"><em>t</em> + 2</span></figcaption>
</figure>
<p><em>Notes:</em> This figure shows the correlation between the measures of academic ability and cognitive endurance measured at two different points in time. Each panel shows a binned scatterplot plotting the estimates of ability/endurance at two different times. To construct this figure, I first divide students into 100 equally-sized bins based on their ability/endurance at time <span class="math inline"><em>t</em></span>. Then, I calculate the average ability/endurance at time <span class="math inline"><em>t</em><sup>′</sup> &gt; <em>t</em></span> for students in each bin. The panel title indicates the two time periods in which I measure ability and endurance.</p>
<figcaption>Panel F. Endurance in year <span class="math inline"><em>t</em></span> and year <span class="math inline"><em>t</em> + 2</span></figcaption>
</figure>

<figure id="fig:corr-alpha-beta" data-latex-placement="H">
<img src="../results/binsc-alpha-beta.jpg" />
<p><em>Notes:</em> This figure shows estimates of the relationship between fatigue-adjusted academic ability and cognitive endurance. Gray circles display a scatterplot of <span class="math inline"><em>β̂</em><sub><em>i</em></sub></span> against <span class="math inline"><em>α̂</em><sub><em>i</em></sub></span> for a randomly-selected one percent of my sample. The red diamonds show a binned scatterplot of average endurance as a function of ability. To construct the binned scatterplot, I first divide students into 100 equally-sized bins based on their ability. Then, I calculate the average endurance for students in each bin. Finally, I plot average endurance against ability in each bin.</p>
<figcaption>Joint distribution of ability and endurance estimates</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/binsc-beta-censo_1yr.pdf" />
<figcaption>Panel A. College enrollment</figcaption>
</figure>
<figure>
<embed src="../results/binsc-beta-coll_wage.pdf" />
<figcaption>Panel B. College quality</figcaption>
</figure>
<figure>
<embed src="../results/binsc-beta-grad_6yr.pdf" />
<figcaption>Panel C. Six-year graduation rate</figcaption>
</figure>
<figure>
<embed src="../results/binsc-beta-wage.pdf" />
<figcaption>Panel D. Log hourly wage</figcaption>
</figure>
<figure>
<embed src="../results/binsc-beta-earn_mean.pdf" />
<figcaption>Panel E. Log monthly earnings</figcaption>
</figure>
<figure>
<embed src="../results/binsc-beta-firm_wage.pdf" />
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the relationship between cognitive endurance and selected college and labor-market outcomes. Each panel shows a binned scatterplot plotting the average value of the outcome (<span class="math inline"><em>y</em></span>-axis) against cognitive endurance (<span class="math inline"><em>x</em></span>-axis). To construct this figure, I first residualize cognitive endurance and each outcome on student-level characteristics and academic ability. I add back the unconditional sample mean to facilitate interpretation. Then, I divide students into 10 equally-sized bins (deciles) based on their residualized endurance and plot the average outcome for students of each bin. The red dashed lines are predicted values from a linear regression on the plotted points. Each panel shows the results for the outcome listed in the panel title. See Section <a href="#sub:var-def" data-reference-type="ref" data-reference="sub:var-def">2.4</a> for variable definitions.</p>
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/deg_dist.pdf" />
<figcaption>Panel A. Distribution of wage returns across college degrees</figcaption>
</figure>
<figure>
<embed src="../results/deg_scatter.pdf" />
<figcaption>Panel B. Return to ability/endurance vs. average wage across college degrees</figcaption>
</figure>
<p><em>Notes:</em> Panel A shows nonparametric estimates of the distribution of the wage return to ability (red line) and the wage return to endurance (green line) across occupations. The wage return to ability and endurance are the coefficients <span class="math inline"><em>ψ</em><sub><em>A</em></sub></span> and <span class="math inline"><em>ψ</em><sub><em>E</em></sub></span> in equation <a href="#reg:endurance-outcomes" data-reference-type="eqref" data-reference="reg:endurance-outcomes">[reg:endurance-outcomes]</a> using log hourly wage as outcome, estimated separately for each three-digit occupation for which at least X observations are available (<span class="math inline"><em>N</em> = <em>X</em></span>). The figure excludes outliers (i.e., estimates of the returns below -0.05 or above 0.25).</p>
<p>Panel B display a binned scatterplot of the wage return to ability/endurance (<span class="math inline"><em>y</em></span>-axis) against the mean hourly wage in bins (<span class="math inline"><em>x</em></span>-axis). To construct this figure, I first divide occupations into ten equally-sized bins based on their mean wage. Then, I estimate the average return to ability/endurance in each bin. Finally, I plot the average return to ability/endurance against the mean wage in each bin.</p>
<figcaption>Panel B. Return to ability/endurance vs. average wage across college degrees</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/scat_end_ret_deg.pdf" />
<figcaption>Panel A. Across college degrees</figcaption>
</figure>
<figure>
<embed src="../results/scat_end_ret_occ.pdf" />
<figcaption>Panel B. Across occupations</figcaption>
</figure>
<figure>
<embed src="../results/scat_end_ret_ind.pdf" />
<figcaption>Panel C. Across industries</figcaption>
</figure>
<figure>
<embed src="../results/binsc_wage_returns.pdf" />
<figcaption>Panel D. Binned scatterplot</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the relationship between the wage return to ability (<span class="math inline"><em>y</em></span>-axis) against the wage return to endurance (<span class="math inline"><em>x</em></span>-axis). Panels A–C show scatterplots of the wage return to ability in a given college degree (Panel A), occupation (Panel B), and industry (Panel C), against the wage return to endurance. The scatterplots exclude outliers (wage returns in the bottom 5% or top 5% of the distribution). The solid lines denote predicted values from linear regressions estimated on the microdata (including all observations).</p>
<p>Panel D shows a binned scatterplot plotting the mean wage return to ability against the wage return to endurance. To construct this figure, I first divide degrees (blue circles), occupations (red triangles), and industries (green diamonds) into 10 equally-sized bins based on their wage return to endurance. Then, I calculate the average wage return to ability in each bin, using the number of individuals in each bin as weights. The solid lines denote predicted values from linear regressions estimated on the plotted points.</p>
<figcaption>Panel D. Binned scatterplot</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/chg_pos_indq_pct_corr.pdf" />
<figcaption>Panel A. Test score (leave-question-out)</figcaption>
</figure>
<figure>
<embed src="../results/chg_pos_indq_censo_1yr.pdf" />
<figcaption>Panel B. College enrollment</figcaption>
</figure>
<figure>
<embed src="../results/chg_pos_indq_coll_wage.pdf" />
<figcaption>Panel C. College quality</figcaption>
</figure>
<figure>
<embed src="../results/chg_pos_indq_wage.pdf" />
<figcaption>Panel D. Hourly wage</figcaption>
</figure>
<figure>
<embed src="../results/chg_pos_indq_earn_mean.pdf" />
<figcaption>Panel E. Monthly earnings</figcaption>
</figure>
<figure>
<embed src="../results/chg_pos_indq_firm_wage.pdf" />
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>
<p><em>Notes:</em> This figure displays estimates of the effect of an increase in the order of a given question on the question’s predictive validity. Each panel shows a binned scatterplot plotting the average change in the predictive validity of a test question on a given outcome (<span class="math inline"><em>y</em></span>-axis) against the change in the position of the question on the exam (<span class="math inline"><em>x</em></span>-axis). Each panel shows the results for the outcome listed in the panel title. See Section <a href="#sub:var-def" data-reference-type="ref" data-reference="sub:var-def">2.4</a> for variable definitions. The red dashed lines are predicted values from a linear regression on the microdata. See Appendix Figure <a href="#fig:hist-chg-pos" data-reference-type="ref" data-reference="fig:hist-chg-pos">[fig:hist-chg-pos]</a>, Panel B for a histogram of the values in the <span class="math inline"><em>x</em></span>-axis.</p>
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>

<div class="centering">

<div id="tab:summ-enem">

+-----------------------------+---------------------------------+---------------+-----------------+
|                             | High-school-students sample     |               | Retakers sample |
+:============================+:==============:+:==============:+:=============:+:===============:+
| 2-3                         | All            | 2009-2010      |               | All             |
+-----------------------------+----------------+----------------+---------------+-----------------+
|                             | \(1\)          | \(2\)          |               | \(3\)           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| **Panel A. Demographic characteristics and race**                                               |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Age                         | 18.204         | 19.151         |               | 18.062          |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Female                      | 0.598          | 0.611          |               | 0.618           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| White                       | 0.476          | 0.510          |               | 0.504           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Black/Brown                 | 0.505          | 0.450          |               | 0.483           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| **Panel B. SES and household characteristics**                                                  |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Attends a private HS        | 0.222          | 0.222          |               | 0.342           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Mom completed high school   | 0.534          | 0.506          |               | 0.606           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Mom completed college       | 0.205          | 0.186          |               | 0.270           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Family earns above 2x M.W.  | 0.388          | 0.379          |               | 0.432           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Family earns above 5x M.W.  | 0.062          | 0.071          |               | 0.087           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| **Panel C. Exam preparation**                                                                   |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Took a foreign lang. course | 0.241          | 0.269          |               | 0.263           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Took a test prep course     | 0.119          | 0.167          |               | 0.160           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| **Panel D. Fraction of correct responses**                                                      |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Natural Science             | 0.283          | 0.333          |               | 0.317           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Social Science              | 0.398          | 0.388          |               | 0.446           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Language                    | 0.408          | 0.449          |               | 0.468           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Math                        | 0.283          | 0.287          |               | 0.320           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Average                     | 0.343          | 0.364          |               | 0.388           |
+-----------------------------+----------------+----------------+---------------+-----------------+
| Number of test-takers       | 14,941,156     | 1,910,502      |               | 1,519,842       |
+-----------------------------+----------------+----------------+---------------+-----------------+
|                             |                |                |               |                 |
+-----------------------------+----------------+----------------+---------------+-----------------+

: Summary statistics of the samples

</div>

</div>

<div class="singlespace">

*Notes*: This table shows summary statistics on all test-takers in the high-school-students sample (column 1), those who took the exam in 2009–2010 as high-school seniors (column 2), and students in the retakers sample (column 3). For students who took the exam multiple times, I compute the summary statistics using data from the last year in which I observe them in my sample. See Section 2.3 for sample definitions.

</div>

<div class="center">

<div id="tab:perf-pos">

+----------------------------------+---+--------------------------------------------------------------------------------------------------+
|                                  |   | Outcome: Correctly responded the question                                                        |
+:=================================+:==+=================:+:============+=================:+:============+=================:+:===========:+
| 3-8                              |   | \(1\)            |             | \(2\)            |             | \(3\)            |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| Question position (normalized)   |   | $-$0.214 | $^{***}$    | $-$0.071 | $^{***}$    | $-$0.058 | $^{***}$    |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
|                                  |   | (0.013           | )           | (0.004           | )           | (0.002           | )           |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| Constant                         |   | 0.450            | $^{***}$    |                  |             |                  |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
|                                  |   | (0.008           | )           |                  |             |                  |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| $N$ (Item$-$Booklets)            |   | 5,896            |             | 5,896            |             | 5,896            |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| $N$ (Students)                   |   | 14,940,464       |             | 14,940,464       |             | 14,940,464       |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| $N$ (Question responses)         |   | 2,689,345,707    |             | 2,689,345,707    |             | 2,689,345,707    |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| R$-$squared                      |   | 0.85             |             | 0.99             |             | 0.97             |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| Question fixed effects           |   | No               |             | Yes              |             | No               |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+
| Controls for question difficulty |   | No               |             | No               |             | Yes              |             |
+----------------------------------+---+------------------+-------------+------------------+-------------+------------------+-------------+

: The effect of question position on student performance on the ENEM

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the effect of a question position on the likelihood of correctly answering the question.

Each column displays an estimate from a different specification. Column 1 presents estimates from a bivariate regression of average student performance on question position. Column 2 presents estimates from equation eq:reg-spec-fe, which includes question fixed effects. Column 3 presents estimates from equation eq:reg-spec-diff, which controls for question difficulty. I normalize question position such that the first question in each testing day is equal to zero and the last question is equal to one.

Heteroskedasticity-robust standard errors clustered at the question level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

<div class="center">

<div id="tab:enade">

+------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |   | Outcome: Correctly responded the question                                                                                                              |
+:=======================+:==+=================:+:=========+=================:+:=========+====================:+:========:+=================:+:=========+=================:+:========:+
| 3-12                   |   |                  |          | Exam length was:                                             | Time spent on exam:                                       |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| 5-7                    |   | All students     |          | Adequate         |          | Short or very short |          | 0–2 hours       |          | 2–4 hours       |          |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
|                        |   | \(1\)            |          | \(2\)            |          | \(3\)               |          | \(4\)            |          | \(5\)            |          |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| Question pos.          |   | $-$0.058 | $^{***}$ | $-$0.051 | $^{***}$ | $-$0.066    | $^{***}$ | $-$0.065 | $^{***}$ | $-$0.049 | $^{***}$ |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
|                        |   | (0.000           | )        | (0.000           | )        | (0.001              | )        | (0.000           | )        | (0.000           | )        |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| Constant               |   | 0.447            | $^{***}$ | 0.452            | $^{***}$ | 0.450               | $^{***}$ | 0.418            | $^{***}$ | 0.463            | $^{***}$ |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
|                        |   | (0.000           | )        | (0.000           | )        | (0.000              | )        | (0.000           | )        | (0.000           | )        |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| $N$ (Items$-$Booklets) |   | 9,392            |          | 9,392            |          | 9,392               |          | 9,392            |          | 9,392            |          |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| $N$ (Students)         |   | 5,356,208        |          | 2,646,472        |          | 301,059             |          | 1,310,334        |          | 3,273,377        |          |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+
| $N$ (Responses)        |   | 117,111,928      |          | 57,352,134       |          | 6,764,895           |          | 28,346,835       |          | 71,258,745       |          |
+------------------------+---+------------------+----------+------------------+----------+---------------------+----------+------------------+----------+------------------+----------+

: The effect of question position on student performance on the ENADE

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the effect of a question position on the likelihood of correctly answering the question using data from Brazil's national college exit exam, the National Student Performance Exam (Exame Nacional de Desempenho dos Estudantes, or ENADE for short), for the years 2004–2018.

Each column displays an estimate for a different sample of students. Column 1 shows results for all students. Columns 2-3 show results for students who reported the exam length as adequate and short/very short, respectively. Columns 4-5 show results for students who spent 0-2 hours or 2-4 hours on the exam, respectively. I normalize question position such that the first question in each testing day is equal to zero and the last question is equal to one. All specifications include student fixed effects.

Heteroskedasticity-robust standard errors clustered at the question level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

<div class="center">

<div id="tab:corr-endurance">

+---------------------+---+--------------------------------------------------------------------------------------------------------------+---+---+
|                     |   | Dependent variable:                                                                                          |   |   |
+:====================+:==+===========================:+:=========+============================:+:=========+=================:+:========:+==:+:==+
| 3-8                 |   | Ability ($\hat{\alpha}_i$) |          | Endurance ($\hat{\beta}_i$) |          | Fraction correct |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | \(1\)                      |          | \(2\)                       |          | \(3\)            |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Male                |   | 0.030                      | $^{***}$ | 0.034                       | $^{***}$ | 0.026            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Constant            |   | 0.360                      | $^{***}$ | -0.071                      | $^{***}$ | 0.333            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| $N$                 |   | 14,941,097                 |          | 14,941,097                  |          | 14,941,097       |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| White               |   | 0.056                      | $^{***}$ | 0.031                       | $^{***}$ | 0.057            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Constant            |   | 0.346                      | $^{***}$ | -0.073                      | $^{***}$ | 0.316            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| $N$                 |   | 14,565,550                 |          | 14,565,550                  |          | 14,565,550       |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Private school      |   | 0.127                      | $^{***}$ | 0.075                       | $^{***}$ | 0.130            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Constant            |   | 0.349                      | $^{***}$ | -0.074                      | $^{***}$ | 0.319            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| $N$                 |   | 9,924,652                  |          | 9,924,652                   |          | 9,924,652        |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Mom comp. HS        |   | 0.071                      | $^{***}$ | 0.034                       | $^{***}$ | 0.074            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Constant            |   | 0.337                      | $^{***}$ | -0.076                      | $^{***}$ | 0.306            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| $N$                 |   | 14,290,759                 |          | 14,290,759                  |          | 14,290,759       |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| HH income \> 2 M.W. |   | 0.092                      | $^{***}$ | 0.050                       | $^{***}$ | 0.095            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| Constant            |   | 0.337                      | $^{***}$ | -0.077                      | $^{***}$ | 0.306            | $^{***}$ |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   | (0.000                     | )        | (0.000                      | )        | (0.000           | )        |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
| $N$                 |   | 14,825,013                 |          | 14,825,013                  |          | 14,825,013       |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+
|                     |   |                            |          |                             |          |                  |          |   |   |
+---------------------+---+----------------------------+----------+-----------------------------+----------+------------------+----------+---+---+

: The correlates of fatigue-adjusted ability and cognitive endurance

</div>

</div>

<div class="singlespace">

*Notes:* This table presents the relationship between student characteristics and fatigue-adjusted ability, cognitive endurance, and the fraction of correct responses.

Each column shows the results for a different outcome (fatigue-adjusted ability, cognitive endurance, and fraction of correct responses) from separate regressions on the characteristics shown in each panel. The regressions that have ability/endurance as an outcome (columns 1 and 2) control for the other skill normalized to have mean zero so that the constant can be interpreted as the mean value of the outcome for the omitted category.

Each panel displays coefficients for a different student characteristic. The characteristics examined are: gender (male vs. female students), race (white vs. non-white students, where non-white includes Black, Brown, and Indigenous students), high school type (private vs. public high school), parental education (students with a high-school-educated mother vs. non-high-school-educated mother), and household income (students from households earning more vs. less than twice the minimum wage, representing the top 70 percent vs. bottom 30 percent of the income distribution). Sample sizes differ across covariates depending on missing data.

Heteroskedasticity-robust standard errors clustered at the student level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

<div class="center">

<div id="tab:reg-coll-lmkt">

+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+:============+:========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+=================:+:=========+
|             | Dependent variable                                                                                                                            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14        |         | Enrolled  |          | College   |          | Degree    |          | 1st-year  |          | Grad.     |          | Time to          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | college   |          | quality   |          | quality   |          | credits   |          | rate      |          | grad.            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Test score  |         | 0.088     | $^{***}$ | 0.082     | $^{***}$ | 0.117     | $^{***}$ | 0.014     | $^{***}$ | 0.060     | $^{***}$ | $-$0.119 | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.001    | )        | (0.002           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance   |         | 0.032     | $^{***}$ | 0.030     | $^{***}$ | 0.051     | $^{***}$ | 0.006     | $^{***}$ | 0.026     | $^{***}$ | $-$0.048 | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.001           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ability     |         | 0.102     | $^{***}$ | 0.095     | $^{***}$ | 0.140     | $^{***}$ | 0.016     | $^{***}$ | 0.072     | $^{***}$ | $-$0.140 | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.001    | )        | (0.002           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ratio coef. |         | 0.310     | $^{***}$ | 0.319     | $^{***}$ | 0.365     | $^{***}$ | 0.358     | $^{***}$ | 0.361     | $^{***}$ | 0.342            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.002    | )        | (0.001    | )        | (0.001    | )        | (0.004    | )        | (0.003    | )        | (0.005           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV     |         | 0.244     |          | 3.326     |          | 3.244     |          | 0.158     |          | 0.418     |          | 3.817            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$         |         | 2,501,519 |          | 1,800,546 |          | 1,768,707 |          | 1,124,972 |          | 1,472,916 |          | 793,822          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             | Dependent variable                                                                                                                            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14        |         | Formal    |          | Hourly    |          | Monthly   |          | Firm      |          | Occup.    |          | Industry         |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | sector    |          | wage      |          | earnings  |          | wage      |          | wage      |          | wage             |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Test score  |         | 0.001     | $^{***}$ | 0.129     | $^{***}$ | 0.111     | $^{***}$ | 0.092     | $^{***}$ | 0.041     | $^{***}$ | 0.013            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.001    | )        | (0.001    | )        | (0.001    | )        | (0.001    | )        | (0.000           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance   |         | 0.000     | $^{***}$ | 0.054     | $^{***}$ | 0.052     | $^{***}$ | 0.036     | $^{***}$ | 0.017     | $^{***}$ | 0.004            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.001    | )        | (0.001    | )        | (0.001    | )        | (0.000    | )        | (0.000           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ability     |         | 0.002     | $^{***}$ | 0.154     | $^{***}$ | 0.135     | $^{***}$ | 0.108     | $^{***}$ | 0.049     | $^{***}$ | 0.014            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.001    | )        | (0.001    | )        | (0.001    | )        | (0.001    | )        | (0.000           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ratio coef. |         | 0.276     | $^{***}$ | 0.351     | $^{***}$ | 0.387     | $^{***}$ | 0.330     | $^{***}$ | 0.346     | $^{***}$ | 0.255            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.015    | )        | (0.003    | )        | (0.003    | )        | (0.004    | )        | (0.006    | )        | (0.010           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV     |         | 0.326     |          | 3.865     |          | 7.551     |          | 3.885     |          | 3.886     |          | 3.858            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$         |         | 2,523,029 |          | 818,590   |          | 818,590   |          | 692,880   |          | 818,374   |          | 818,590          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+

: The effect of academic ability and cognitive endurance on long-run outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between ability/endurance and college outcomes (Panel A) and labor market-outcomes (Panel B).

The first row of each panel shows estimates of the association between test scores and the outcome listed in the column header (coefficient $\psi_T$ in equation reg:score-outcomes). The following rows show estimates of the association between ability and cognitive endurance and a given outcome (coefficients $\psi_A$ and $\psi_E$ in equation reg:endurance-outcomes). All regressions control for age, gender, race, high school type, parental income, cohort fixed effects, and municipality fixed effects. In addition to the baseline controls, the regressions in Panel A, columns 4–6, include college-degree fixed effects to remove the influence of a student's program choice, while the regressions in Panel B control for potential years of experience and years of education. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. See Section 2.4 for outcome definitions.

The third-to-last row in each panel shows the ratio between the predicted effect of academic ability and the effect of cognitive endurance on a given outcome. Standard errors estimated through the delta method in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels.

</div>

<div class="center">

<div id="tab:gaps-endurance">

+-----------------+---+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                 |   | Wage gap between                                                                                                                                    |
+:================+:==+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:========:+
| 2-12            |   | Male /           |          | White /          |          | Priv HS /        |          | Mom HS /         |          | High-inc /       |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | Female           |          | Non-white        |          | Public HS        |          | No HS            |          | Low-inc          |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | \(1\)            |          | \(2\)            |          | \(3\)            |          | \(4\)            |          | \(5\)            |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   |                  |          |                  |          |                  |          |                  |          |                  |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Wage gap        |   | 0.189            | $^{***}$ | 0.145            | $^{***}$ | 0.183            | $^{***}$ | 0.279            | $^{***}$ | 0.269            | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.002           | )        | (0.002           | )        | (0.002           | )        | (0.003           | )        | (0.002           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   |                  |          |                  |          |                  |          |                  |          |                  |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Wage gap        |   | 0.169            | $^{***}$ | 0.089            | $^{***}$ | 0.096            | $^{***}$ | 0.139            | $^{***}$ | 0.185            | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.002           | )        | (0.002           | )        | (0.002           | )        | (0.003           | )        | (0.002           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| P.p. change gap |   | $-$0.019 | $^{***}$ | $-$0.056 | $^{***}$ | $-$0.087 | $^{***}$ | $-$0.140 | $^{***}$ | $-$0.084 | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.001           | )        | (0.001           | )        | (0.001           | )        | (0.001           | )        | (0.001           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Pct. change gap |   | $-$0.101 | $^{***}$ | $-$0.388 | $^{***}$ | $-$0.476 | $^{***}$ | $-$0.500 | $^{***}$ | $-$0.311 | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.003           | )        | (0.006           | )        | (0.006           | )        | (0.006           | )        | (0.003           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   |                  |          |                  |          |                  |          |                  |          |                  |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Wage gap        |   | 0.145            | $^{***}$ | 0.069            | $^{***}$ | 0.072            | $^{***}$ | 0.091            | $^{***}$ | 0.162            | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.002           | )        | (0.002           | )        | (0.002           | )        | (0.003           | )        | (0.002           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| P.p. change gap |   | $-$0.025 | $^{***}$ | $-$0.020 | $^{***}$ | $-$0.024 | $^{***}$ | $-$0.048 | $^{***}$ | $-$0.024 | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.000           | )        | (0.000           | )        | (0.000           | )        | (0.001           | )        | (0.000           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Pct. change gap |   | $-$0.145 | $^{***}$ | $-$0.219 | $^{***}$ | $-$0.250 | $^{***}$ | $-$0.346 | $^{***}$ | $-$0.127 | $^{***}$ |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   | (0.003           | )        | (0.006           | )        | (0.006           | )        | (0.008           | )        | (0.002           | )        |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| $N$             |   | 821,794          |          | 771,496          |          | 765,842          |          | 821,745          |          | 779,597          |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                 |   |                  |          |                  |          |                  |          |                  |          |                  |          |
+-----------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+

: The contribution of gaps in ability and endurance to wage gaps

</div>

</div>

<div class="singlespace">

*Notes:* This table shows wage gaps in the labor market and the contribution of differences in ability and endurance to those gaps.

Each column shows the result for a different group of workers. Column 1 shows gaps between male and female workers. Column 2 shows gaps between white and non-white (Black, Brown, and Indigenous) workers. Column 3 shows gaps between workers who went to a private high school and a public high school. Column 4 shows gaps between workers with a high-school-educated mother and non-high-school-educated mother. Column 5 shows gaps between workers whose households arned above two minimum wages and below two minimum wages at the time of taking the ENEM.

Panel A shows unadjusted wage gaps, Panel B show wage gaps after controlling for fatigue-adjusted ability, and Panel C show wage gaps after controlling for fatigue-adjusted ability and cognitive endurance. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses.

$^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels.

</div>

<div class="center">

<div id="tab:reg-rank-return">

+:---------------------------------------+:----------+----------:+:----------+----------:+:----------+----------:+:----------+-------:+:--+-------:+:--+
|                                        |           | Return    |           | Return    |           | Ratio     |           | Wage   |   | Sample |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | ability   |           | endur.    |           | returns   |           | pctil. |   | size   |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | \(1\)     |           | \(2\)     |           | \(3\)     |           | \(4\)  |   | \(5\)  |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| **Panel A. Top five occupations**                                                                                          |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| . Public tax auditors                  |           | 0.454     |           | 0.168     |           | 0.369     |           | 49.2   |   | 255    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.106    | )         | (0.057    | )         | (0.084    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 2\. Professionals in air               |           | 0.278     |           | 0.114     |           | 0.412     |           | 88.3   |   | 347    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  navigation, sea and fluvial           |           | (0.049    | )         | (0.028    | )         | (0.072    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 3\. Technicians in operation of radio, |           | 0.200     |           | 0.112     |           | 0.558     |           | 66.3   |   | 658    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  TV systems and video producers        |           | (0.047    | )         | (0.027    | )         | (0.091    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 4\. Plant operators in chemical,       |           | 0.267     |           | 0.109     |           | 0.409     |           | 62.8   |   | 1,221  |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  petrochemical and related occup.      |           | (0.031    | )         | (0.020    | )         | (0.057    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 5\. Instrument and precision           |           | 0.180     |           | 0.092     |           | 0.511     |           | 70.8   |   | 203    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  equipment repairers                   |           | (0.068    | )         | (0.040    | )         | (0.194    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| **Panel B. Top five college degrees**                                                                                      |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| . Aeronautics and related degrees      |           | 0.173     |           | 0.106     |           | 0.613     |           | 69.7   |   | 670    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.026    | )         | (0.015    | )         | (0.077    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 2\. Music and performing arts          |           | 0.221     |           | 0.093     |           | 0.420     |           | 59.3   |   | 502    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.060    | )         | (0.035    | )         | (0.110    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 3\. Religious studies                  |           | 0.186     |           | 0.088     |           | 0.471     |           | 49.0   |   | 356    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.047    | )         | (0.031    | )         | (0.097    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 4\. History and archeology             |           | 0.211     |           | 0.087     |           | 0.414     |           | 60.0   |   | 988    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.043    | )         | (0.022    | )         | (0.064    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 5\. Forestry engineering               |           | 0.154     |           | 0.084     |           | 0.543     |           | 52.3   |   | 397    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.045    | )         | (0.024    | )         | (0.115    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| **Panel D. Top five industries**                                                                                           |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| . Oil extraction and                   |           | 0.276     |           | 0.135     |           | 0.488     |           | 91.5   |   | 948    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  related services                      |           | (0.034    | )         | (0.021    | )         | (0.052    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 2\. Financial intermediation and       |           | 0.215     |           | 0.087     |           | 0.402     |           | 54.7   |   | 6,177  |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|  and insurance (aux. services)         |           | (0.013    | )         | (0.007    | )         | (0.024    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 3\. Research and development           |           | 0.198     |           | 0.084     |           | 0.426     |           | 73.7   |   | 1,323  |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.024    | )         | (0.015    | )         | (0.052    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 4\. Electricity, gas and hot water     |           | 0.223     |           | 0.083     |           | 0.373     |           | 78.1   |   | 1,966  |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.020    | )         | (0.011    | )         | (0.036    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
| 5\. Manufacture of office machinery    |           | 0.132     |           | 0.073     |           | 0.553     |           | 54.7   |   | 920    |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+
|                                        |           | (0.033    | )         | (0.019    | )         | (0.095    | )         |        |   |        |   |
+----------------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+--------+---+--------+---+

: Degrees, occupations, and industries with the largest wage return to endurance

</div>

</div>

<div class="singlespace">

*Notes:* This table lists the top five 3-digit academic degrees (Panel A), 3-digit occupations (Panel B), and 2-digit industries (Panel C) with the highest wage return to cognitive endurance (column 2).

Column 1 shows the wage return to ability. Column 3 shows the ratio between the wage return to endurance and the wage return to ability. Column 4 shows the average wage percentile of workers in each degree, occupation, or industry. Column 5 shows the sample size used to estimate each wage return.

The wage return to ability and endurance are the coefficients $\psi_A$ and $\psi_E$ in equation reg:endurance-outcomes using as outcome log hourly wage, estimated separately for each degree, occupation, and industry.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses.

</div>

<div class="landscape">

<div class="center">

<div id="tab:val-pos">

+---------------------------+---+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                           |   | Outcome: Predictive validity of question $j$ for                                                                                                                                                                                              |
+:==========================+:==+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:=========+=================:+:========:+
| 3-18                      |   | Test             |          | College          |          | College          |          | Grad.            |          | Hourly           |          | Monthly          |          | Firm             |          | Wage             |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | score            |          | enrol.           |          | quality          |          | rate             |          | wage             |          | earnings         |          | wage             |          | Growth           |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | \(1\)            |          | \(2\)            |          | \(3\)            |          | \(4\)            |          | \(5\)            |          | \(6\)            |          | \(7\)            |          | \(9\)            |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Constant (Mean Inform.)   |   | 0.165            | $^{***}$ | 0.077            | $^{***}$ | 0.109            | $^{***}$ | 0.015            | $^{***}$ | 0.092            | $^{***}$ | 0.101            | $^{***}$ | 0.080            | $^{***}$ | 0.016            | $^{***}$ |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | (0.007           | )        | (0.002           | )        | (0.003           | )        | (0.001           | )        | (0.003           | )        | (0.003           | )        | (0.002           | )        | (0.001           | )        |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Question Position (norm.) |   | $-$0.184 | $^{***}$ | $-$0.054 | $^{***}$ | $-$0.051 | $^{***}$ | $-$0.022 | $^{***}$ | $-$0.051 | $^{***}$ | $-$0.049 | $^{***}$ | $-$0.044 | $^{***}$ | $-$0.008 | $^{***}$ |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | (0.020           | )        | (0.008           | )        | (0.011           | )        | (0.003           | )        | (0.009           | )        | (0.010           | )        | (0.008           | )        | (0.002           | )        |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Constant                  |   | 0.258            | $^{***}$ | 0.104            | $^{***}$ | 0.135            | $^{***}$ | 0.027            | $^{***}$ | 0.118            | $^{***}$ | 0.126            | $^{***}$ | 0.102            | $^{***}$ | 0.020            | $^{***}$ |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | (0.013           | )        | (0.004           | )        | (0.006           | )        | (0.002           | )        | (0.005           | )        | (0.006           | )        | (0.004           | )        | (0.001           | )        |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |                  |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Question Position (norm.) |   | $-$0.014 |          | $-$0.036 | $^{***}$ | $-$0.050 | $^{***}$ | $-$0.000 |          | $-$0.037 | $^{**}$  | $-$0.038 | $^{**}$  | $-$0.035 | $^{**}$  | $-$0.022 | $^{**}$  |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | (0.030           | )        | (0.011           | )        | (0.016           | )        | (0.007           | )        | (0.016           | )        | (0.016           | )        | (0.015           | )        | (0.009           | )        |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| Chg. Inform./Mean Inform. |   | $-$0.085 |          | $-$0.467 | $^{***}$ | $-$0.455 | $^{***}$ | $-$0.014 |          | $-$0.405 | $^{***}$ | $-$0.379 | $^{***}$ | $-$0.440 | $^{***}$ | $-$1.374 | $^{**}$  |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
|                           |   | (0.101           | )        | (0.075           | )        | (0.072           | )        | (0.354           | )        | (0.105           | )        | (0.097           | )        | (0.124           | )        | (0.619           | )        |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+
| $N$ (Item$-$Booklets)     |   | 1,416            |          | 1,416            |          | 1,416            |          | 1,416            |          | 1,416            |          | 1,416            |          | 1,416            |          | 1,416            |          |
+---------------------------+---+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+------------------+----------+

: The effect of skill muddling on exam informativeness

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of equation.

Each column displays the estimates of equation reg:validity-pos for a different outcome. In Panel A, the regression only includes a constant and thus can be interpreted as mean informativeness. In Panel B, the regression includes question fixed effects. I normalize question position so that the coefficients can be interpreted as the change in informativeness throughout the entire exam. See Section 2.4 for outcome definitions.

Heteroskedasticity-robust standard errors clustered at the question level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

</div>

<div class="singlespace">

# References
Abraham, Katharine G., and Mallatt, Justine (2022). Measuring Human Capital. *Journal of Economic Perspectives* 36(3):103–130.

Acemoglu, Daron, and Autor, David (2011). Skills, Tasks and Technologies: Implications for Employment and Earnings. *Handbook of Labor Economics* 4:1043–1171.

Acemoglu, Daron, Kong, Fredric, and Restrepo, Pascual (2024). Tasks at Work: Comparative Advantage, Technology and Labor Demand. *National Bureau of Economic Research*.

Ackerman, Phillip L. (2011). Cognitive Fatigue: Multidisciplinary Perspectives on Current Research and Future Applications. *American Psychological Association* xviii, 333.

Ackerman, Phillip L., and Kanfer, Ruth (2009). Test Length and Cognitive Fatigue: An Empirical Examination of Effects on Performance and Test-Taker Reactions. *Journal of Experimental Psychology: Applied* 15(2):163–181.

Almlund, Mathilde, Duckworth, Angela Lee, Heckman, James, and Kautz, Tim (2011). Chapter 1 - Personality Psychology and Economics. *Handbook of the Economics of Education* 4:1–181.

Angrist, Joshua D., and Lavy, Victor (1999). Using Maimonides' Rule to Estimate the Effect of Class Size on Scholastic Achievement. *The Quarterly Journal of Economics* 114(2):533–575.

Angrist, Joshua D, Cohodes, Sarah R, Dynarski, Susan M, Pathak, Parag A, and Walters, Christopher R (2016). Stand and deliver: Effects of Boston's charter high schools on college preparation, entry, and choice. *Journal of Labor Economics,* 34(2):275–318.

Angrist, Joshua D., Hull, Peter D., Pathak, Parag A., and Walters, Christopher R. (2017). Leveraging Lotteries for School Value-Added: Testing and Estimation. *The Quarterly Journal of Economics* 132(2):871–919.

Anusic, Ivana, and Schimmack, Ulrich (2016). Stability and change of personality traits, self-esteem, and well-being: Introducing the meta-analytic stability and change model of retest correlations. *Journal of Personality and Social Psychology,* 110(5):766.

Archsmith, James, Heyes, Anthony, Neidell, Matthew, and Sampat, Bhaven (2023). The Dynamics of Inattention in the (Baseball) Field. National Bureau of Economic Research.

Athey, Susan, Chetty, Raj, Imbens, Guido W, and Kang, Hyunseung (2019). The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely. *National Bureau of Economic Research*.

Balart, Pau, and Oosterveen, Matthijs (2019). Females Show More Sustained Performance During Test-Taking than Males. *Nature Communications* 10.

Balart, Pau, Oosterveen, Matthijs, and Webbink, Dinand (2018). Test Scores, Noncognitive Skills and Economic Growth. *Economics of Education Review* 63:134–153.

Baumeister, Roy F. (2002). Ego Depletion and Self-Control Failure: An Energy Model of the Self's Executive Function. *Self and Identity* 1(2):129–136.

Bayer, Patrick, and Charles, Kerwin Kofi (2018). Divergent paths: A new perspective on earnings differences between black and white men since 1940. *The Quarterly Journal of Economics* 133(3):1459–1501.

Becker, Gary S. (1962). Irrational Behavior and Economic Theory. *Journal of Political Economy* 70(1):1–13.

Bettinger, Eric P., Evans, Brent J., and Pope, Devin G. (2013). Improving College Performance and Retention the Easy Way: Unpacking the ACT Exam. *American Economic Journal: Economic Policy* 5(2):26–52.

Bishop, John H (1989). Is the test score decline responsible for the productivity growth decline?. *The American Economic Review,* 178–197.

Borghans, Lex, and Schils, Trudie (2018). Decomposing Achievement Test Scores into Measures of Cognitive and Noncognitive Skills. *Social Science Research Network*.

Borghans, Lex, Duckworth, Angela Lee, Heckman, James J., and ter Weel, Bas (2008). The Economics and Psychology of Personality Traits. *Journal of Human Resources* 43(4):972–1059.

Bowles, Samuel, Gintis, Herbert, and Osborne, Melissa (2001). The Determinants of Earnings: A Behavioral Approach. *Journal of Economic Literature* 39(4):1137–1176.

Brown, Christina, Kaur, Supreet, Kingdon, Greeta, and Schofield, Heather (2024). Cognitive Endurance as Human Capital. *Quarterly Journal of Economics (forthcoming),*. Working Paper.

Bulman, George (2015). The Effect of Access to College Assessments on Enrollment and Attainment. *American Economic Journal: Applied Economics* 7(4):1–36.

Buser, Thomas, Niederle, Muriel, and Oosterbeek, Hessel (2024). Can competitiveness predict education and labor market outcomes? Evidence from incentivized choice and survey measures. *Review of Economics and Statistics (forthcoming)*. DOI: 10.3386/w28916.

Card, David (1999). Chapter 30 - the Causal Effect of Education on Earnings. *Handbook of Labor Economics* 3:1801–1863.

Card, David (2001). Estimating the Return to Schooling: Progress on Some Persistent Econometric Problems. *Econometrica* 69(5):1127–1160.

Card, David, Cardoso, Ana Rute, Heining, Joerg, and Kline, Patrick (2018). Firms and Labor Market Inequality: Evidence and Some Theory. *Journal of Labor Economics* 36(S1):S13-S70.

Chetty, Raj, Friedman, John N., Hilger, Nathaniel, Saez, Emmanuel, Schanzenbach, Diane Whitmore, and Yagan, Danny (2011). How Does Your Kindergarten Classroom Affect Your Earnings? Evidence from Project Star. *The Quarterly Journal of Economics* 126(4):1593–1660.

Chetty, Raj, Hendren, Nathaniel, Kline, Patrick, Saez, Emmanuel, and Turner, Nicholas (2014). Is the United States Still a Land of Opportunity? Recent Trends in Intergenerational Mobility. *American Economic Review* 104(5):141–147.

Chetty, Raj, Friedman, John N., and Rockoff, Jonah E. (2014). Measuring the Impacts of Teachers I: Evaluating Bias in Teacher Value-Added Estimates. *American Economic Review* 104(9):2593–2632.

Chetty, Raj, Looney, Adam, and Kroft, Kory (2009). Salience and Taxation: Theory and Evidence. *American Economic Review* 99(4):1145–1177.

Choi, Syngjoo, Kim, Seonghoon, and Lim, Wooyoung (2025). Strategic thinking skills: a key to collective economic success. *American Economic Journal: Microeconomics* 17(2):214–240.

Dai, Hengchen, Milkman, Katherine L., Hofmann, David A., and Staats, Bradley R. (2015). The Impact of Time at Work and Time Off from Work on Rule Compliance: The Case of Hand Hygiene in Health Care. *The Journal of Applied Psychology* 100(3):846–862.

Debeer, Dries, and Janssen, Rianne (2013). Modeling item-position effects within an IRT framework. *Journal of Educational Measurement,* 50(2):164–185.

Debeer, Dries, Buchholz, Janine, Hartig, Johannes, and Janssen, Rianne (2014). Student, School, and Country Differences in Sustained Test-Taking Effort in the 2009 PISA Reading Assessment. *Journal of Educational and Behavioral Statistics* 39(6):502–523.

Deming, David J. (2017). The Growing Importance of Social Skills in the Labor Market. *The Quarterly Journal of Economics* 132(4):1593–1640.

Deming, David J. (2022). Four Facts About Human Capital. *Journal of Economic Perspectives* 36(3):75–102.

Demir, Banu, Fieler, Ana Cecília, Xu, Daniel Yi, and Yang, Kelly Kaili (2024). O-Ring Production Networks. *Journal of Political Economy* 132(1):200–247.

Dobbie, Will, and Fryer Jr, Roland G (2015). The medium-term impacts of high-achieving charter schools. *Journal of Political Economy,* 123(5):985–1037.

Duckworth, Angela Lee, Quinn, Patrick D., Lynam, Donald R., Loeber, Rolf, and Stouthamer-Loeber, Magda (2011). Role of Test Motivation in Intelligence Testing. *Proceedings of the National Academy of Sciences* 108(19):7716–7720.

Edin, Per-Anders, Fredriksson, Peter, Nybom, Martin, and Öckert, Björn (2022). The Rising Return to Noncognitive Skill. *American Economic Journal: Applied Economics* 14(2):78–100.

Educational Testing Service (2023). GRE General Test Enhancements: FAQs for Test Takers. Accessed: 2025-03-12.

Enkavi, A. Zeynep, Eisenberg, Ian W., Bissett, Patrick G., Mazza, Gina L., MacKinnon, David P., Marsch, Lisa A., and Poldrack, Russell A. (2019). Large-Scale Analysis of Test– Retest Reliabilities of Self-Regulation Measures. *Proceedings of the National Academy of Sciences* 116(12):5472–5477.

Fagereng, Andreas, Mogstad, Magne, and Rønning, Marte (2021). Why Do Wealthy Parents Have Wealthy Children?. *Journal of Political Economy* 129(3):703–756.

Finkelstein, Amy, Notowidigdo, Matthew J., Schilbach, Frank, and Zhang, Jonathan (2024). Lives vs. Livelihoods: The Impact of the Great Recession on Mortality and Welfare. *SSRN Electronic Journal*.

Frankel, Alex, and Kartik, Navin (2019). Muddled Information. *Journal of Political Economy* 127(4):1739–1776.

Frankel, Alex, and Kartik, Navin (2022). Improving Information from Manipulable Data. *Journal of the European Economic Association* 20(1):79–115.

Friedman, John N., Sacerdote, Bruce, Staiger, Douglas O., and Tine, Michele (2025). Standardized Test Scores and Academic Performance at Ivy-Plus Colleges. *SSRN Electronic Journal*.

Fé, Eduardo, Gill, David, and Prowse, Victoria (2022). Cognitive Skills, Strategic Sophistication, and Life Outcomes. *Journal of Political Economy* 130(10):2643–2704.

Gneezy, Uri, List, John A., Livingston, Jeffrey A., Qin, Xiangdong, Sadoff, Sally, and Xu, Yang (2019). Measuring Success in Education: The Role of Effort on the Test Itself. *American Economic Review: Insights* 1(3):291–308.

Goleman, Daniel (2013). Focus: The Hidden Driver of Excellence. *A&C Black*.

Goleman, Daniel, and Davidson, Richard J (2017). Altered traits: Science reveals how meditation changes your mind, brain, and body. *Penguin*.

Goodman, Sarena (2016). Learning from the Test: Raising Selective College Enrollment by Providing Information. *The Review of Economics and Statistics* 98(4):671–684.

Goodman, Joshua, Gurantz, Oded, and Smith, Jonathan (2020). Take Two! SAT Retaking and College Enrollment Gaps. *American Economic Journal: Economic Policy* 12(2):115–158.

Griliches, Zvi (1977). Estimating the Returns to Schooling: Some Econometric Problems. *Econometrica* 45(1):1–22.

Grönqvist, Erik, Öckert, Björn, and Vlachos, Jonas (2017). The Intergenerational Transmission of Cognitive and Noncognitive Abilities. *Journal of Human Resources* 52(4):887–918.

Hanushek, Eric A., and Woessmann, Ludger (2008). The Role of Cognitive Skills in Economic Development. *Journal of Economic Literature* 46(3):607–668.

Hanushek, Eric A, and Woessmann, Ludger (2008). The role of cognitive skills in economic development. *Journal of Economic Literature,* 46(3):607–68.

Hanushek, Eric A., and Woessmann, Ludger (2012). Do Better Schools Lead to More Growth? Cognitive Skills, Economic Outcomes, and Causation. *Journal of Economic Growth* 17(4):267–321.

Hanushek, Eric A, and Woessmann, Ludger (2012). Do better schools lead to more growth? Cognitive skills, economic outcomes, and causation. *Journal of Economic Growth,* 17(4):267–321.

Heckman, James J., Stixrud, Jora, and Urzua, Sergio (2006). The Effects of Cognitive and Noncognitive Abilities on Labor Market Outcomes and Social Behavior. *Journal of Labor Economics* 24(3):411–482.

Hermo, Santiago, Päällysaho, Miika, Seim, David, and Shapiro, Jesse M (2022). Labor Market Returns and the Evolution of Cognitive Skills: Theory and Evidence. *The Quarterly Journal of Economics* 137(4):2309–2361.

Hirshleifer, David, Levi, Yaron, Lourie, Ben, and Teoh, Siew Hong (2019). Decision Fatigue and Heuristic Analyst Forecasts. *Journal of Financial Economics* 133(1):83–98.

Hopkins, Kenneth D, and Bracht, Glenn H (1975). Ten-year stability of verbal and nonverbal IQ scores. *American Educational Research Journal,* 12(4):469–477.

Hoxby, Caroline, Turner, Sarah, and others (2013). Expanding college opportunities for high-achieving, low income students. *Stanford Institute for Economic Policy Research Discussion Paper,* 12(014):7.

Jackson, C. Kirabo (2018). What Do Test Scores Miss? The Importance of Teacher Effects on Non– Test Score Outcomes. *Journal of Political Economy* 126(5):2072–2107.

Kautz, Tim, Heckman, James J, Diris, Ron, Ter Weel, Bas, and Borghans, Lex (2014). Fostering and measuring skills: Improving cognitive and non-cognitive skills to promote lifetime success. National Bureau of Economic Research.

Kim, Rebecca H., Day, Susan C., Small, Dylan S., Snider, Christopher K., Rareshide, Charles A. L., and Patel, Mitesh S. (2018). Variations in Influenza Vaccination by Clinic Appointment Time and an Active Choice Intervention in the Electronic Health Record to Increase Influenza Vaccination. *JAMA Network Open* 1(5):e181770.

Kobrin, Jennifer L, Patterson, Brian F, Shaw, Emily J, Mattern, Krista D, and Barbuti, Sandra M (2008). Validity of the SAT for Predicting First-Year College Grade Point Average. Research Report No. 2008-5. *College Board*.

Kremer, Michael (1993). The O-Ring Theory of Economic Development. *The Quarterly Journal of Economics* 108(3):551–575.

Levy, David M, Wobbrock, Jacob O, Kaszniak, Alfred W, and Ostergren, Marilyn (2012). The effects of mindfulness meditation training on multitasking in a high-stress information environment. *Proceedings of Graphics Interface 2012* 45–52.

Lim, Julian, and Dinges, David F. (2008). Sleep Deprivation and Vigilant Attention. *Annals of the New York Academy of Sciences* 1129:305–322.

Linder, Jeffrey A., Doctor, Jason N., Friedberg, Mark W., Reyes Nieva, Harry, Birks, Caroline, Meeker, Daniella, and Fox, Craig R. (2014). Time of Day and the Decision to Prescribe Antibiotics. *JAMA Internal Medicine* 174(12):2029–2031.

Lindqvist, Erik, and Vestman, Roine (2011). The Labor Market Returns to Cognitive and Noncognitive Ability: Evidence from the Swedish Enlistment. *American Economic Journal: Applied Economics* 3(1):101–128.

Lira, Benjamin, O'Brien, Joseph M., Peña, Pablo A., Galla, Brian M., D'Mello, Sidney, Yeager, David S., Defnet, Amy, Kautz, Tim, Munkacsy, Kate, and Duckworth, Angela L. (2022). Large Studies Reveal How Reference Bias Limits Policy Applications of Self-Report Measures. *Scientific Reports* 12(1):19189.

Lykken, David T. (2005). Mental Energy. *Intelligence* 33(4):331–335.

Machado, Cecilia, and Szerman, Christiane (2021). Centralized College Admissions and Student Composition. *Economics of Education Review* 85:102184.

Mata, Rui, Frey, Renato, Richter, David, Schupp, Jürgen, and Hertwig, Ralph (2018). Risk Preference: A View from Psychology. *Journal of Economic Perspectives* 32(2):155–172.

Meier, Stephan, and Sprenger, Charles D. (2015). Temporal Stability of Time Preferences. *The Review of Economics and Statistics* 97(2):273–286.

Miller, M. David, Linn, Robert L., and Gronlund, Norman Edward (2009). Measurement and Assessment in Teaching. *Merrill/Pearson*. Google-Books-ID: pMJTPgAACAAJ.

Mincer, Jacob (1958). Investment in Human Capital and Personal Income Distribution. *Journal of Political Economy* 66(4):281–302.

Neal, Derek A, and Johnson, William R (1996). The role of premarket factors in black-white wage differences. *Journal of Political Economy* 104(5):869–895.

Newport, Cal (2016). Deep work: Rules for focused success in a distracted world. *Hachette UK*.

Oster, Emily (2016). Unobservable Selection and Coefficient Stability: Theory and Evidence. *Journal of Business & Economic Statistics* 1–18.

Park, R. Jisung (2020). Hot Temperature and High Stakes Performance. *Journal of Human Resources*.

Petek, Nathan, and Pope, Nolan G (2023). The multidimensional impact of teachers on students. *Journal of Political Economy* 131(4):1057–1107.

Riehl, Evan (2023). Do Less Informative College Admission Exams Reduce Earnings Inequality? Evidence from Colombia. *Journal of Labor Economics* 000–000.

Rothstein, Jesse M. (2004). College Performance Predictions and the SAT. *Journal of Econometrics* 121(1):297–317.

Sadoff, Sally, Samek, Anya, and Sprenger, Charles (2020). Dynamic Inconsistency in Food Choice: Experimental Evidence from Two Food Deserts. *The Review of Economic Studies* 87(4):1954–1988.

Schuerger, James M, and Witt, Anita C (1989). The temporal stability of individually tested intelligence. *Journal of Clinical Psychology,* 45(2):294–302.

Shachtman, Noah (2013). In Silicon Valley, meditation is no fad. It could make your career. *Wired, June,* 18.

Sievertsen, Hans Henrik, Gino, Francesca, and Piovesan, Marco (2016). Cognitive Fatigue Influences Students' Performance on Standardized Tests. *Proceedings of the National Academy of Sciences* 113(10):2621–2624.

Simonsohn, Uri, Simmons, Joseph P., and Nelson, Leif D. (2020). Specification Curve Analysis. *Nature Human Behaviour* 4(11):1208–1214.

Soares, Joseph A (2015). SAT wars: The case for test-optional college admissions. *Teachers College Press*.

Stango, Victor, and Zinman, Jonathan (2020). Behavioral biases are temporally stable. *National Bureau of Economic Research*.

Steiny Wellsjo, Alex (2023). Simple Actions, Complex Habits: Lessons from Hospital Hand Hygiene. Working Paper.

Thornton, Bill, Faires, Alyson, Robbins, Maija, and Rollins, Eric (2014). The mere presence of a cell phone may be distracting: Implications for attention and task performance. *Social Psychology,* 45(6):479.

UNESCO (2012). International standard classification of education: ISCED 2011. *Comparative Social Research,* 30.

Urzúa, Sergio (2008). Racial Labor Market Gaps the Role of Abilities and Schooling Choices. *Journal of Human Resources* 43(4):919–971.

Wooden, M (2012). The stability of personality traits. *R. Wilkins and D. Warren, Families, Incomes and Jobs,* 7.

Zamarro, Gema, Cheng, Albert, Shakeel, M. Danish, and Hitt, Collin (2018). Comparing and Validating Measures of Non-Cognitive Traits: Performance Task Measures and Self-Reports from a Nationally Representative Internet Panel. *Journal of Behavioral and Experimental Economics* 72:51–60.

Zamarro, Gema, Hitt, Collin, and Mendez, Ildefonso (2019). When Students Don't Care: Reexamining International Differences in Achievement and Student Effort. *Journal of Human Capital* 13(4):519–552.

</div>

<div class="center">

</div>

# Appendix Figures and Tables

<figure id="fig:cdf-grad" data-latex-placement="H">
<embed src="../results/cdf_grad.pdf" />
<p><em>Notes:</em> This figure displays the cumulative distribution function of college graduation rates for individuals in the high-school-students sample. The <span class="math inline"><em>x</em></span>-axis shows the number of years since initial college enrollment, ranging from 0 to 9 years. The <span class="math inline"><em>y</em></span>-axis represents the fraction of enrolled students who have graduated by each year.</p>
<figcaption>Fraction of students who graduate from college by years since enrollment</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/hist-chg-pos.pdf" />
<figcaption>Panel A. All years (2009–2016)</figcaption>
</figure>
<figure>
<embed src="../results/hist-chg-pos-2010.pdf" />
<figcaption>Panel B. First two cohorts (2009–2010)</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the amount of variation available in a given question’s position between different exam booklets. To construct this figure, I first calculate the difference (in absolute value) in a question’s position in two exam booklets. This difference ranges from zero (if a question is in the same position in two different booklets) to 44 (if a question is in the first position of a section in one booklet and the last position of a section in another booklet). I repeat this process for each question and each possible booklet pair. The figure plots the resulting histogram of position differences.</p>
<figcaption>Panel B. First two cohorts (2009–2010)</figcaption>
</figure>

<figure id="fig:hist-item-effect" data-latex-placement="H">
<embed src="../results/hist-item-effect.pdf" />
<p><em>Notes:</em> This figure plots the distribution of item-level position effects. To construct this figure, I estimate the impact of an increase in the position of a given question on student performance separately for each question. The figure displays the distribution of estimated <span class="math inline"><em>β</em></span>’s (one for each item). The figure excludes outliers (i.e., questions for which the effect is below -0.50 or above 0.50 percentage points).</p>
<figcaption>Histogram of question-level position effects</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/hist-cons-lpm.pdf" />
<figcaption>Panel A. Academic ability (<span class="math inline"><em>α</em><sub><em>i</em></sub></span>)</figcaption>
</figure>
<figure>
<embed src="../results/hist-slope-lpm.pdf" />
<figcaption>Panel B. Cognitive endurance (<span class="math inline"><em>β</em><sub><em>i</em></sub></span>)</figcaption>
</figure>
<figure>
<embed src="../results/hist-cons-lpm-shrink.pdf" />
<figcaption>Panel C. Academic ability shrunk (<span class="math inline"><em>α</em><sub><em>i</em></sub><sup><em>s</em></sup></span>)</figcaption>
</figure>
<figure>
<embed src="../results/hist-slope-lpm-shrink.pdf" />
<figcaption>Panel D. Cognitive endurance shrunk (<span class="math inline"><em>β</em><sub><em>i</em></sub><sup><em>s</em></sup></span>)</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the distribution of my estimates of academic ability (Panel A) and cognitive endurance (Panel B) among individuals in the high-school-students sample. The measure of an individual’s ability is the estimated intercept (<span class="math inline"><em>α</em><sub><em>i</em></sub></span>) in equation <a href="#reg:lpm-ind" data-reference-type="eqref" data-reference="reg:lpm-ind">[reg:lpm-ind]</a>. The measure of an individual’s cognitive endurance is the estimated slope (<span class="math inline"><em>β</em><sub><em>i</em></sub></span>) in equation <a href="#reg:lpm-ind" data-reference-type="eqref" data-reference="reg:lpm-ind">[reg:lpm-ind]</a>.</p>
<figcaption>Panel D. Cognitive endurance shrunk (<span class="math inline"><em>β</em><sub><em>i</em></sub><sup><em>s</em></sup></span>)</figcaption>
</figure>

<figure id="fig:speccurve_wage_shr" data-latex-placement="htpb">
<embed src="../results/speccurve_wage_shr.pdf" />
<p><em>Notes:</em> This figure presents a specification curve analysis (Simonsohn, Simmons, and Nelson, 2020) of the wage returns to cognitive endurance. The top panel shows the estimated wage return to a one standard deviation increase in endurance across multiple specifications, with the baseline specification reported in Table <a href="#tab:reg-coll-lmk" data-reference-type="ref" data-reference="tab:reg-coll-lmk">[tab:reg-coll-lmk]</a> highlighted in red. Each black dot represents an alternative specification with different combinations of control variables. The middle panel indicates which controls are included in each specification (filled circles) or excluded (empty circles), with rows representing demographic controls (Demog), college fixed effects (Coll FE), college major fixed effects (Prog FE), occupation fixed effects (Occ FE), industry fixed effects (Ind FE), and firm fixed effects (Firm FE). The bottom panel displays the ratio of the wage return to endurance relative to the wage return to ability for each specification, with 90 percent and 95 percent confidence intervals shown in gray.</p>
<figcaption>Wage returns to cognitive endurance across specifications</figcaption>
</figure>

<figure data-latex-placement="H">
<figure>
<embed src="../results/indq_pct_corr.pdf" />
<figcaption>Panel A. Test score (leave-question-out)</figcaption>
</figure>
<figure>
<embed src="../results/indq_censo_1yr.pdf" />
<figcaption>Panel B. College enrollment</figcaption>
</figure>
<figure>
<embed src="../results/indq_coll_wage.pdf" />
<figcaption>Panel C. College quality</figcaption>
</figure>
<figure>
<embed src="../results/indq_cred_1yr.pdf" />
<figcaption>Panel D. Degree progress</figcaption>
</figure>
<figure>
<embed src="../results/indq_wage.pdf" />
<figcaption>Panel E. Hourly wage</figcaption>
</figure>
<figure>
<embed src="../results/indq_firm_wage.pdf" />
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>
<p><em>Notes:</em> This figure shows the relationship between (i) the predictive validity of an exam question for a given outcome and (ii) the position of the question on the exam. The <span class="math inline"><em>y</em></span>-axis plots the correlation between correctly responding to the question in position <span class="math inline"><em>j</em></span> and a given outcome <span class="math inline"><em>Y</em></span>. The <span class="math inline"><em>x</em></span>-axis show the position of the question on the exam. Each plot shows the results for the outcome listed in the panel title. See Section <a href="#sub:var-def" data-reference-type="ref" data-reference="sub:var-def">2.4</a> for outcome definitions. The red dashed lines are predicted values from a linear regression on the plotted points.</p>
<figcaption>Panel F. Firm mean wage (leave-one-out)</figcaption>
</figure>

<div class="centering">

<div id="tab:summ-enem-book">

+-----------------------------+------------+-----------+-----------------------------------------------+
|                             |            |           | Day 1 booklet color                           |
+:============================+:==========:+:=========:+:=========:+:=========:+:=========:+:=========:+
| 3-7                         | All        |           | Yellow    | Blue      | Pink      | White     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
|                             | \(1\)      |           | \(2\)     | \(3\)     | \(4\)     | \(5\)     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| **Panel A. Demographic characteristics and race**                                        |           |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Age                         | 18.204     |           | 18.201    | 18.210    | 18.209    | 18.196    |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Female                      | 0.598      |           | 0.595     | 0.600     | 0.595     | 0.599     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| White                       | 0.476      |           | 0.478     | 0.476     | 0.476     | 0.474     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Black/Brown                 | 0.505      |           | 0.503     | 0.505     | 0.505     | 0.507     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| **Panel B. Household characteristics**                                                   |           |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Attends a private HS        | 0.222      |           | 0.225     | 0.220     | 0.223     | 0.220     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Mom completed high school   | 0.534      |           | 0.538     | 0.532     | 0.535     | 0.531     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Mom completed college       | 0.205      |           | 0.208     | 0.203     | 0.207     | 0.203     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Family earns above 2x M.W.  | 0.388      |           | 0.392     | 0.386     | 0.390     | 0.385     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Family earns above 5x M.W.  | 0.062      |           | 0.064     | 0.061     | 0.063     | 0.061     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| **Panel C. Exam preparation**                                                            |           |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Took a foreign lang. course | 0.241      |           | 0.241     | 0.241     | 0.240     | 0.241     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Took a test prep course     | 0.119      |           | 0.121     | 0.119     | 0.119     | 0.118     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| **Panel D. Fraction of correct responses**                                               |           |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Natural Science             | 0.283      |           | 0.284     | 0.283     | 0.283     | 0.283     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Social Science              | 0.398      |           | 0.398     | 0.398     | 0.398     | 0.398     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Language                    | 0.408      |           | 0.410     | 0.408     | 0.408     | 0.407     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Math                        | 0.283      |           | 0.284     | 0.283     | 0.283     | 0.282     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Average                     | 0.343      |           | 0.344     | 0.343     | 0.343     | 0.343     |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
| Number of test-takers       | 14,941,156 |           | 3,655,807 | 3,903,653 | 3,590,977 | 3,790,719 |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+
|                             |            |           |           |           |           |           |
+-----------------------------+------------+-----------+-----------+-----------+-----------+-----------+

: Summary statistics of the high-school-student sample by booklet color

</div>

</div>

<div class="singlespace">

*Notes:* This table presents summary statistics for the high-school-student sample, categorized by the booklet color received on the first day of testing. Column 1 shows statistics for the entire sample, while columns 2-5 provide data for each booklet color (Yellow, Blue, Pink, and White) respectively. Panel A displays demographic characteristics and race. Panel B shows household characteristics, including school type and parental education. Panel C presents exam preparation indicators. Panel D reports the fraction of correct responses by subject area. The bottom row indicates the number of test-takers in each category.

</div>

<div class="center">

<div id="tab:reliability">

  ----------------------------------- ----------------------- ------------------------------------
               Construct               Reliability estimate                Reference
                 \(1\)                         \(2\)                         \(3\)
                  IQ                           0.80                Schuerger and Witt (1989)
             Risk aversion                  0.20–0.40                 Mata et al. (2018)
       Big 5 personality traits             0.60–0.73                   Wooden (2012)
             Present bias                      0.36                Meier and Sprenger (2015)
         Dynamic inconsistency              0.20–0.33         Sadoff, Samek, and Sprenger (2020)
             Loss aversion                     0.88                 Stango and Zinman (2020)
          Teacher value added               0.23–0.47                Chetty et al. (2014)
            Self-regulation            $-$0.09–0.66          Enkavi et al. (2019)
           Life satisfaction                   0.67               Anusic and Schimmack (2016)
              Self-esteem                      0.71               Anusic and Schimmack (2016)
   Fatigue-adjusted academic ability        0.61–0.77                     This paper
          Cognitive endurance               0.14–0.30                     This paper
  ----------------------------------- ----------------------- ------------------------------------

  : Examples of reliability estimates in economics and psychology

</div>

</div>

<div class="singlespace">

*Notes:* Notes: This table presents reliability estimates for various measures from the economics and psychology literature. Reliability estimates typically range from 0 to 1, with higher values indicating greater consistency of the measure. The reliability estimates shown reflect either findings from different studies or results from different specifications within studies. For self-regulation measures, the estimates are based on behavioral tasks, and the range reported represents the interquartile range of estimate reported in (Enkavi et al., 2019). The last two rows display the test-retest reliability of the fatigue-adjusted academic ability and cognitive endurance measures estimated in Section 5 of this study.

</div>

<div class="center">

<div id="tab:reg-rob-coll-iv">

+-------------+---------------------------------------------------------------------------------------------------------------------------------------+----------+
|             | Dependent variable                                                                                                                    |          |
+:============+:========+=========:+:=========+========:+:=========+========:+:=========+=========:+:=========+========:+:=========+=================:+:=========+
| 3-14        |         | Enrolled |          | College |          | Degree  |          | 1st-year |          | Grad.   |          | Time to          |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | college  |          | quality |          | quality |          | credits  |          | on time |          | grad.            |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | \(1\)    |          | \(2\)   |          | \(3\)   |          | \(4\)    |          | \(5\)   |          | \(6\)            |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         |          |          |         |          |         |          |          |          |         |          |                  |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Endurance   |         | 0.048    | $^{***}$ | 0.057   | $^{***}$ | 0.110   | $^{***}$ | 0.010    | $^{***}$ | 0.026   | $^{***}$ | $-$0.082 | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.001   | )        | (0.001  | )        | (0.002  | )        | (0.000   | )        | (0.002  | )        | (0.006           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Ability     |         | 0.110    | $^{***}$ | 0.129   | $^{***}$ | 0.217   | $^{***}$ | 0.018    | $^{***}$ | 0.049   | $^{***}$ | $-$0.154 | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.002   | )        | (0.001  | )        | (0.002  | )        | (0.000   | )        | (0.003  | )        | (0.009           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Ratio coef. |         | 0.441    | $^{***}$ | 0.443   | $^{***}$ | 0.509   | $^{***}$ | 0.571    | $^{***}$ | 0.543   | $^{***}$ | 0.533            | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.011   | )        | (0.006  | )        | (0.007  | )        | (0.008   | )        | (0.037  | )        | (0.032           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Mean DV     |         | 0.367    |          | 3.420   |          | 3.390   |          | 0.146    |          | 0.808   |          | 4.191            |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| $N$         |         | 132,634  |          | 111,409 |          | 109,390 |          | 339,727  |          | 51,066  |          | 51,066           |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         |          |          |         |          |         |          |          |          |         |          |                  |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Endurance   |         | 0.046    | $^{***}$ | 0.067   | $^{***}$ | 0.141   | $^{***}$ | 0.016    | $^{***}$ | 0.041   | $^{***}$ | $-$0.120 | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.006   | )        | (0.004  | )        | (0.007  | )        | (0.001   | )        | (0.010  | )        | (0.028           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Ability     |         | 0.107    | $^{***}$ | 0.140   | $^{***}$ | 0.239   | $^{***}$ | 0.022    | $^{***}$ | 0.057   | $^{***}$ | $-$0.169 | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.002   | )        | (0.001  | )        | (0.003  | )        | (0.000   | )        | (0.005  | )        | (0.013           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Ratio coef. |         | 0.430    | $^{***}$ | 0.479   | $^{***}$ | 0.590   | $^{***}$ | 0.738    | $^{***}$ | 0.722   | $^{***}$ | 0.711            | $^{***}$ |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         | (0.053   | )        | (0.025  | )        | (0.028  | )        | (0.026   | )        | (0.156  | )        | (0.145           | )        |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| Mean DV     |         | 0.367    |          | 3.420   |          | 3.390   |          | 0.146    |          | 0.808   |          | 4.191            |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
| $N$         |         | 132,614  |          | 111,394 |          | 109,375 |          | 339,725  |          | 51,056  |          | 51,056           |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+
|             |         |          |          |         |          |         |          |          |          |         |          |                  |          |
+-------------+---------+----------+----------+---------+----------+---------+----------+----------+----------+---------+----------+------------------+----------+

: IV estimates of the relationship between ability/endurance and college outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays OLS and IV estimates of the relationship between ability/endurance and college outcomes.

The OLS estimates are analogous to Table 5 but estimated on the sample of retakers. See notes to Table 5 for details. The IV estimates instrument the year $t$ measure of ability and cognitive endurance with the $t-1$ measures of these skills.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

<div class="center">

<div id="tab:reg-rob-lmkt-iv">

+-------------+------------------------------------------------------------------------------------------------------------------------------+----------+
|             | Dependent variable                                                                                                           |          |
+:============+:========+========:+:=========+========:+:=========+=========:+:=========+========:+:=========+========:+:=========+=========:+:=========+
| 3-14        |         | Formal  |          | Hourly  |          | Monthly  |          | Firm    |          | Occup.  |          | Industry |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | sector  |          | wage    |          | earnings |          | wage    |          | wage    |          | wage     |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | \(1\)   |          | \(2\)   |          | \(3\)    |          | \(4\)   |          | \(5\)   |          | \(6\)    |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         |         |          |         |          |          |          |         |          |         |          |          |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Endurance   |         | 0.001   | $^{***}$ | 0.121   | $^{***}$ | 0.124    | $^{***}$ | 0.081   | $^{***}$ | 0.030   | $^{***}$ | 0.008    | $^{***}$ |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.000  | )        | (0.005  | )        | (0.005   | )        | (0.005  | )        | (0.003  | )        | (0.001   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Ability     |         | 0.002   | $^{***}$ | 0.231   | $^{***}$ | 0.201    | $^{***}$ | 0.163   | $^{***}$ | 0.057   | $^{***}$ | 0.018    | $^{***}$ |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.000  | )        | (0.006  | )        | (0.006   | )        | (0.005  | )        | (0.003  | )        | (0.002   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Ratio coef. |         | 0.518   | $^{***}$ | 0.525   | $^{***}$ | 0.615    | $^{***}$ | 0.496   | $^{***}$ | 0.518   | $^{***}$ | 0.413    | $^{***}$ |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.072  | )        | (0.018  | )        | (0.020   | )        | (0.024  | )        | (0.040  | )        | (0.057   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Mean DV     |         | 0.286   |          | 4.049   |          | 7.702    |          | 4.014   |          | 3.992   |          | 3.875    |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| $N$         |         | 133,904 |          | 37,814  |          | 37,814   |          | 32,908  |          | 37,798  |          | 37,814   |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         |         |          |         |          |          |          |         |          |         |          |          |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Endurance   |         | 0.003   | $^{***}$ | 0.188   | $^{***}$ | 0.232    | $^{***}$ | 0.120   | $^{***}$ | 0.052   | $^{***}$ | 0.001    |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.001  | )        | (0.018  | )        | (0.017   | )        | (0.015  | )        | (0.009  | )        | (0.004   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Ability     |         | 0.002   | $^{***}$ | 0.250   | $^{***}$ | 0.215    | $^{***}$ | 0.180   | $^{***}$ | 0.061   | $^{***}$ | 0.018    | $^{***}$ |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.000  | )        | (0.008  | )        | (0.007   | )        | (0.007  | )        | (0.004  | )        | (0.002   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Ratio coef. |         | 1.171   | $^{***}$ | 0.753   | $^{***}$ | 1.077    | $^{***}$ | 0.670   | $^{***}$ | 0.845   | $^{***}$ | 0.050    |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|             |         | (0.323  | )        | (0.069  | )        | (0.079   | )        | (0.081  | )        | (0.150  | )        | (0.241   | )        |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Mean DV     |         | 0.286   |          | 4.049   |          | 7.702    |          | 4.014   |          | 3.992   |          | 3.875    |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| $N$         |         | 133,884 |          | 37,801  |          | 37,801   |          | 32,902  |          | 37,785  |          | 37,801   |          |
+-------------+---------+---------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+

: IV estimates of the relationship between ability/endurance and labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays OLS and IV estimates of the relationship between ability/endurance and labor-market outcomes.

The OLS estimates are analogous to Table 5 but estimated on the sample of retakers. See notes to Table 5 for details. The IV estimates instrument the year $t$ measure of ability and cognitive endurance with the $t-1$ measures of these skills.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

<div class="landscape">

<div class="center">

<div id="tab:reg-earn-ctrl">

+---------------------------+---+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---+---+
|                           |   | Dependent variable: Log hourly wage                                                                                                                                   |   |   |
+:==========================+:==+========:+:=========+========:+:=========+========:+:=========+========:+:=========+========:+:=========+========:+:=========+========:+:=========+========:+:========:+==:+:==+
| 3-18                      |   | \(1\)   |          | \(2\)   |          | \(3\)   |          | \(4\)   |          | \(5\)   |          | \(6\)   |          | \(7\)   |          | \(8\)   |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Test score                |   | 0.168   | $^{***}$ | 0.161   | $^{***}$ | 0.130   | $^{***}$ | 0.119   | $^{***}$ | 0.099   | $^{***}$ | 0.083   | $^{***}$ | 0.077   | $^{***}$ | 0.050   | $^{***}$ |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
|                           |   | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.001  | )        |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Endurance                 |   | 0.071   | $^{***}$ | 0.069   | $^{***}$ | 0.058   | $^{***}$ | 0.053   | $^{***}$ | 0.039   | $^{***}$ | 0.033   | $^{***}$ | 0.030   | $^{***}$ | 0.021   | $^{***}$ |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
|                           |   | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.001  | )        | (0.001  | )        |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Ability                   |   | 0.202   | $^{***}$ | 0.193   | $^{***}$ | 0.158   | $^{***}$ | 0.145   | $^{***}$ | 0.117   | $^{***}$ | 0.099   | $^{***}$ | 0.091   | $^{***}$ | 0.060   | $^{***}$ |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
|                           |   | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        | (0.002  | )        |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Ratio coef.               |   | 0.354   | $^{***}$ | 0.355   | $^{***}$ | 0.369   | $^{***}$ | 0.368   | $^{***}$ | 0.333   | $^{***}$ | 0.329   | $^{***}$ | 0.328   | $^{***}$ | 0.353   | $^{***}$ |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
|                           |   | (0.004  | )        | (0.004  | )        | (0.005  | )        | (0.005  | )        | (0.007  | )        | (0.008  | )        | (0.008  | )        | (0.011  | )        |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| $N$                       |   | 339,134 |          | 339,134 |          | 339,127 |          | 339,122 |          | 339,126 |          | 339,126 |          | 339,126 |          | 339,123 |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| R$-$squared               |   | 0.17    |          | 0.17    |          | 0.26    |          | 0.27    |          | 0.35    |          | 0.41    |          | 0.45    |          | 0.72    |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
|                           |   |         |          |         |          |         |          |         |          |         |          |         |          |         |          |         |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Demographic variables     |   | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| College enrollment        |   | No      |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Educational attainment    |   | No      |          | No      |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| College fixed effects     |   | No      |          | No      |          | No      |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| College $\times$ major FE |   | No      |          | No      |          | No      |          | No      |          | Yes     |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Occupation fixed effects  |   | No      |          | No      |          | No      |          | No      |          | No      |          | Yes     |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Industry fixed effects    |   | No      |          | No      |          | No      |          | No      |          | No      |          | No      |          | Yes     |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+
| Firm fixed effects        |   | No      |          | No      |          | No      |          | No      |          | No      |          | No      |          | No      |          | Yes     |          |   |   |
+---------------------------+---+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---------+----------+---+---+

: The relationship between cognitive endurance and earnings under various set of controls

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the wage return to ability and endurance across different specifications. The estimating sample includes only individuals for whom data on all mediating variables are available. Each column presents estimates from a regression with a different set of controls. Column 1 presents the baseline specification, which includes only controls for demographic characteristics (age, gender, race, high-school type, parental income), municipality of residence, exam year. Column 2 adds an indicator for college enrollment. Column 3 adds controls for years educational attainment (years of schooling and six-year college graduation dummy) and potential years of experience. Column 4 adds college fixed effects. Column 5 includes college-by-major fixed effects. Column 6 adds two-digit occupation fixed effects. Column 7 adds two-digit industry fixed effects. Column 8 adds firm fixed effects. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

</div>

# Empirical Appendix
## Limited Cognitive Endurance and Time Pressure
Is the causal effect of an increase in question position on student performance a manifestation of limited cognitive endurance or is it driven by students running out of time? Three pieces of evidence suggest that time pressure cannot explain the estimated $\beta < 0$.

First, very few students leave responses unanswered. Appendix Figure 8 plots the fraction of students who left a question unanswered (possibly because they ran out of time) against the question position. Questions that appear later in the test are more likely to be left unanswered. However, only a small fraction of students leave *any* questions unanswered. Thus, missing responses cannot account for the large performance decline observed throughout the exam.[^22]

<figure id="fig:miss-quest" data-latex-placement="H">
<embed src="../results/mean-missing-question.pdf" />
<p><em>Notes:</em> This figure shows the fraction of students who left questions unanswered over the course of each testing day. The <span class="math inline"><em>y</em></span>-axis displays the fraction of students who did not select any of the multiple-choice answers to a given question. The <span class="math inline"><em>x</em></span>-axis displays the position of each question in the exam. The dashed lines are predicted values from a linear regression estimated separately for each testing day.</p>
<figcaption>Fraction of students who did not answer exam questions throughout the ENEM</figcaption>
</figure>

Second, student performance declines even in questions that students answer when they are likely not time-pressured. Appendix Figure fig:chg-pos-firsthalf shows the fatigue effect separately for questions that appear in the first half (Panel A) and the second half of each testing day (Panel B). Presumably, students should have plenty of time to answer the first half of the exam. Yet, I still find fatigue effects that are quantitatively similar—or even larger—to those estimated on the second half of each day or with all questions. This result is consistent with visual evidence in Figure 2, which shows that student performance tends to decline shortly after the exam starts and with the declines in performance exhibited by the example questions that appear at the beginning of the exam in Appendix Figure 16.

<figure data-latex-placement="H">
<figure>
<embed src="../results/chg-pos-firsthalf.pdf" />
<figcaption>Panel A. First half of each testing day</figcaption>
</figure>
<figure>
<embed src="../results/chg-pos-secondhalf.pdf" />
<figcaption>Panel B. Second half of each testing day</figcaption>
</figure>
<p><em>Notes:</em> This figure shows heterogeneity in the effect of limited endurance on performance by question position. Panels A and B are analogous to Figure <a href="#fig:chg-pos" data-reference-type="ref" data-reference="fig:chg-pos">3</a>, but the effect is estimated separately for questions that appear on the first half of each testing day (Panel A) or the second half of each testing day (Panel B). The <span class="math inline"><em>y</em></span>-axis shows the average change (in percentage points) in the fraction of students correctly responding to a question. The <span class="math inline"><em>x</em></span>-axis plots the difference in the question position between each possible booklet pair. The dashed line denotes predicted values from a linear regression estimated on the plotted points, using the number of questions used to estimate each point as weights.</p>
<figcaption>Panel B. Second half of each testing day</figcaption>
</figure>

Third, students who took a test preparation course—who presumably should be better at time management—exhibit performance declines of similar magnitude to those who did not take such a course. Appendix Figure fig:chg-pos-prep presents the fatigue effect separately for students who reported taking a test preparation course (Panel A) and those who did not (Panel B).[^23] If time pressure were driving the performance decline, we would muted effects for students with test prep experience, as these students are typically taught strategies to optimize time allocation during exams and have more experience taking tests. However, the estimated slopes are remarkably similar across both groups ($-$6.49 percentage points for those with test prep versus $-$7.48 percentage points for those without). This similarity suggests that limited cognitive endurance, rather than time mismanagement, is the more likely explanation for the observed performance decline. Furthermore, this result indicates that the performance decline is unlikely to be driven by strategic test-taking behavior, as such strategies would likely differ between students with and without formal test preparation.

<figure data-latex-placement="H">
<figure>
<embed src="../results/chg-pos-vest.pdf" />
<figcaption>Panel A. Took a test prep course</figcaption>
</figure>
<figure>
<embed src="../results/chg-pos-novest.pdf" />
<figcaption>Panel B. Did not take a test prep course</figcaption>
</figure>
<p><em>Notes:</em> This figure shows heterogeneity in the effect of limited endurance on performance by test preparation activity. Panels A and B are analogous to Figure <a href="#fig:chg-pos" data-reference-type="ref" data-reference="fig:chg-pos">3</a>, but the effect is estimated separately for students who reported taking a test preparation course (Panel A) or not taking such a course (Panel B). The <span class="math inline"><em>y</em></span>-axis shows the average change (in percentage points) in the fraction of students correctly responding to a question. The <span class="math inline"><em>x</em></span>-axis plots the difference in the question position between each possible booklet pair. The dashed line denotes predicted values from a linear regression estimated on the plotted points, using the number of questions used to estimate each point as weights.</p>
<figcaption>Panel B. Did not take a test prep course</figcaption>
</figure>

## OLS Formulas of Academic Ability and Cognitive Endurance
My measure of cognitive endurance is $\beta_i$ in equation reg:lpm-ind. Ignoring controls for question difficulty, the OLS estimator of $\beta_i$ is

$$\begin{align}
 \hat{\beta}_i &= \frac{\sum_{j}(\text{Pos}_{ij} - \overline{\text{Pos}})(C_{ij}-\bar{C_i})}{\sum_{j}(\text{Pos}_{ij} - \overline{\text{Pos}})^2} 
    &= \sum_{j} \underbrace{w_{j}}_{\substack{\text{Weight of} \ \text{question $j$}}} \times \underbrace{(C_{ij}-\bar{C_i}),}_{\substack{\text{Performance on} \ \text{question $j$ relative to} \ \text{$i$'s average performance}}}
\end{align}$$

where $\bar{C}_i$ is the fraction of questions correctly answered by student $i$, $\overline{\text{Pos}}$ is the average question position (which is constant across test-takers), and $w_{j} \equiv \frac{\text{Pos}_{j} - \overline{\text{Pos}}}{\sum_{j}(\text{Pos}_{j} - \overline{\text{Pos}})^2}$ is the weight of question $j$.

Equation eq:lpm-slope shows that $\hat{\beta}_i$ is a weighted average of deviations from $i$'s average score. The weight of each question depends on the location of the question on the test. Appendix Figure 9 plots the weight OLS places on each question. The questions with the largest weights (in absolute value) are the ones at the beginning and the end of the test.

<figure id="fig:ols-wt" data-latex-placement="H">
<embed src="../results/weights_ols.pdf" />
<p><em>Notes:</em> This figure displays the weight put by the ordinary least squares (OLS) estimator of <span class="math inline"><em>β</em><sub><em>i</em></sub></span> (equation <a href="#reg:lpm-ind" data-reference-type="eqref" data-reference="reg:lpm-ind">[reg:lpm-ind]</a>) on each question of the test.</p>
<figcaption>Weight of each question in a test with 90 questions</figcaption>
</figure>

My measure of academic ability is $\alpha_i$ in equation reg:lpm-ind. The OLS estimator of $\alpha_i$ is

$$\begin{align}
 \hat{\alpha}_i &= \bar{C_i} - \hat{\beta_i}\overline{\text{Pos}} \\
    &= \bar{C_i} - \sum_{j} w_j C_{ij} \overline{\text{Pos}}.
\end{align}$$

Equation eq:lpm-cons shows that $\alpha_i$ can be estimated by the difference between $i$'s test score ($\bar{C_i}$) and the part of her test score that is explained by limited endurance, $\hat{\beta_i}\overline{\text{Pos}}$.

## Estimating the Standard Deviation of Ability and Endurance
The estimate of cognitive endurance, $\hat{\beta}_i$, can be decomposed into latent cognitive endurance, $\beta_i$, and a sampling error $e_i$ independent of $\beta_i$ and with variance $\sigma^2_e$:

$$\begin{align}
 \hat{\beta}_i = \beta_i + e_i
\end{align}$$

Calculating the variance on each side of equation eq:latent-error yields:

$$\begin{align*}
    \sigma^2_{\hat{\beta}} = \sigma^2_\beta + \sigma^2_e,
\end{align*}$$

where $\sigma^2_{\hat{\beta}}$ and $\sigma^2_\beta$ are the variances of $\hat{\beta}$ and $\beta$, respectively. Equation eq:latent-variance shows that the raw standard deviation of $\hat{\beta}$ overstates the variability of $\beta$ since it includes variability in the sampling error. Let $\text{SE}_{\hat{\beta}}$ be the standard error of $\hat{\beta}$. The variance of the sampling error can be estimated as $\sigma^2_e = \mathop{\mathrm{\mathbb{E}}}[\text{SE}^2_{\hat{\beta}}]$. Thus, an estimate of the variance of $\beta$ is given by

$$\begin{align*}
    \hat{\sigma}^2_\beta = \sigma^2_{\hat{\beta}} - \mathop{\mathrm{\mathbb{E}}}[\text{SE}^2_{\hat{\beta}}].
\end{align*}$$

I use an analogous derivation to estimate the variance of latent ability, $\sigma^2_\alpha$.

## Robustness of the Relationship between Endurance and Outcomes
Appendix Table 14 shows non-parametric estimates of the effect of ability and endurance on each outcome based on the slope of percentile changes on outcomes (Heckman, Stixrud, and Urzua, 2006). I estimate how a movement from the bottom decile to the top decile in the endurance distribution affects a given outcome:

$$\begin{align}
 \mathop{\mathrm{\mathbb{E}}}[Y_i | i \in \text{Top decile Endurance}] - \mathop{\mathrm{\mathbb{E}}}[Y_i | i \in \text{Bottom decile Endurance}].
\end{align}$$

As a benchmark, I compare the size of a decile movement in the endurance distribution to an equivalent decile movement in the ability distribution. I compute these effects in a regression framework by estimating equations of the form:

$$\begin{align}
    Y_{i} &= \phi + \lambda X_i + \sum_{d=2}^{10} \mathbbm{1}\{i \in \text{TestScore decile $d$}\} +  \zeta_i  \\
    Y_{i} &=  \tilde{\phi}_1 + \tilde{\lambda}_1 X_i  + \sum_{d=2}^{10} \mathbbm{1}\{i \in \text{Ability decile $d$}\} + \sum_{d=2}^{10} \mathbbm{1}\{i \in \text{Endurance decile $d$}\} + \tilde{\zeta}_i, \end{align}$$

where the omitted category is the bottom decile. The first row of each panel shows that moving higher in the distribution of test scores tends to improve college and labor-market outcomes. Subsequent rows show that both cognitive endurance and ability contribute to this effect. Depending on the outcome, the predicted effect of a movement from decile 1 to decile 10 in the endurance distribution represents 32.6 percent to 53.0 percent of the corresponding effect of a movement in the ability distribution.

Appendix Tables 15 and 16 show that the results are robust to flexibly controlling for fatigue-adjusted ability. In the baseline specification, I control linearly for fatigue-adjusted ability, which could potentially mask non-linear relationships between ability and outcomes that might influence the estimated endurance effect. To address this concern, I estimate two alternative specifications. First, I include a seventh-degree polynomial of fatigue-adjusted ability, which allows for a highly flexible relationship between ability and outcomes. Second, I include fixed effects for 100 percentile bins of the ability distribution, effectively comparing students with nearly identical levels of ability but different levels of endurance. Both specifications yield estimated effects of endurance that are remarkably similar to the baseline results across all college and labor market outcomes, confirming that the relationship between endurance and long-run outcomes is not driven by a misspecification of the ability-outcome relationship.

Appendix Tables 17 and 18 show that the results are robust to estimating ability and endurance with alternative specifications. First, I compute the estimates of ability/endurance separately for each testing day and for each academic subject, and use the average estimate across days/subjects as regressors in equation reg:endurance-outcomes. Second, I compute the estimates of endurance controlling for day fixed effects and subject fixed effects; thus accounting for possible differences in preparation across subjects. Finally, I use the correlation between question position and a dummy for correctly answering a question as an alternative measure of endurance. Across specifications, I find effects that are quantitatively similar and qualitatively identical to those of the baseline specification.

Appendix Tables 19 and 20 show that the results are robust to controlling for question difficulty in alternative ways when estimating ability and endurance. First, I compute the estimates of ability and endurance in equation reg:lpm-ind without controlling for question difficulty. Second, I calculate question difficulty without adjusting for the average position of the question across booklets. Finally, I compute question difficulty adjusting for average question position in several alternative ways (see Appendix 12). Consistent with the baseline results, I find that the estimates are remarkably robust across specifications.

Appendix Tables 21 and 22 shows that the results are robust to different sample restrictions. Specifically, I estimate the baseline specification excluding students in the tails of the ability and the endurance distributions. These are students for whom floor and ceiling effects may be binding and, thus, for whom estimates may be biased. I also exclude students with a positive estimate of endurance. These are students who, for example, may have answered the exam in reverse order. I find little impact of these sample restrictions on the estimates.

Appendix Tables 23 and 24 show robustness of the baseline regressions to accounting for measurement error. First, I weight each observation by the inverse of the standard error of the ability and endurance estimates, thus giving more weight to students for which I estimate more precise measures. Second, I estimate the baseline regressions using shrunk estimates of ability and endurance. The shrunk estimators of ability and endurance put more weight on measures estimated with more precision, as measured by a low standard error. The results are very similar to the baseline results.

<div class="center">

<div id="tab:pctil-coll-lmkt">

+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+:============+:========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+=================:+:=========+
|             | Dependent variable                                                                                                                            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14        |         | Enrolled  |          | College   |          | Degree    |          | 1st-year  |          | Grad.     |          | Time to          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | college   |          | quality   |          | quality   |          | credits   |          | on time   |          | grad.            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance   |         | 0.136     | $^{***}$ | 0.139     | $^{***}$ | 0.232     | $^{***}$ | 0.030     | $^{***}$ | 0.132     | $^{***}$ | $-$0.224 | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.002    | )        | (0.001    | )        | (0.002    | )        | (0.001    | )        | (0.002    | )        | (0.007           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ability     |         | 0.319     | $^{***}$ | 0.338     | $^{***}$ | 0.488     | $^{***}$ | 0.057     | $^{***}$ | 0.272     | $^{***}$ | $-$0.486 | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.002    | )        | (0.001    | )        | (0.002    | )        | (0.001    | )        | (0.003    | )        | (0.009           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ratio coef. |         | 0.426     | $^{***}$ | 0.412     | $^{***}$ | 0.474     | $^{***}$ | 0.530     | $^{***}$ | 0.485     | $^{***}$ | 0.462            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.005    | )        | (0.003    | )        | (0.003    | )        | (0.009    | )        | (0.007    | )        | (0.012           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV     |         | 0.329     |          | 3.327     |          | 3.244     |          | 0.158     |          | 0.418     |          | 3.842            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$         |         | 1,850,938 |          | 1,711,475 |          | 1,681,214 |          | 1,124,972 |          | 1,471,569 |          | 786,391          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             | Dependent variable                                                                                                                            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14        |         | Formal    |          | Hourly    |          | Monthly   |          | Firm      |          | Occup.    |          | Industry         |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | sector    |          | wage      |          | earnings  |          | wage      |          | wage      |          | wage             |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance   |         | 0.002     | $^{***}$ | 0.241     | $^{***}$ | 0.240     | $^{***}$ | 0.159     | $^{***}$ | 0.084     | $^{***}$ | 0.018            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.005    | )        | (0.004    | )        | (0.004    | )        | (0.003    | )        | (0.001           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ability     |         | 0.006     | $^{***}$ | 0.543     | $^{***}$ | 0.475     | $^{***}$ | 0.387     | $^{***}$ | 0.177     | $^{***}$ | 0.055            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.000    | )        | (0.005    | )        | (0.005    | )        | (0.005    | )        | (0.003    | )        | (0.001           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Ratio coef. |         | 0.337     | $^{***}$ | 0.443     | $^{***}$ | 0.506     | $^{***}$ | 0.410     | $^{***}$ | 0.472     | $^{***}$ | 0.326            | $^{***}$ |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|             |         | (0.034    | )        | (0.007    | )        | (0.007    | )        | (0.009    | )        | (0.012    | )        | (0.020           | )        |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV     |         | 0.326     |          | 3.865     |          | 7.551     |          | 3.885     |          | 3.886     |          | 3.858            |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$         |         | 2,523,032 |          | 818,590   |          | 818,590   |          | 692,880   |          | 818,374   |          | 818,590          |          |
+-------------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+

: The effect of a movement from decile 1 to decile 10 in the ability/endurance distribution on long-run outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between ability/endurance and college outcomes (Panel A) and labor-market outcomes (Panel B).

The first row of each panel shows estimates of the mean outcome difference between individuals in the tenth and first decile of the test score distribution (the coefficient on the decile ten dummy in equation reg:score-pctil). The following rows show estimates of the mean outcome difference between individuals in the tenth and first decile of the ability/endurance distribution (the coefficients on the decile ten dummies in equation reg:endurance-pctil). See Section 5 for a description of the measures of ability and endurance. See Section 2.4 for outcome definitions. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses.

The third-to-last row in each panel shows the ratio between the effect of ability and endurance on a given outcome. Standard errors estimated through the delta method in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:reg-coll-poly">

+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+:==========+:========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+==========:+:=========+=================:+:=========+
|           | Dependent variable                                                                                                                            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14      |         | Enrolled  |          | College   |          | Degree    |          | 1st-year  |          | Grad.     |          | Time to          |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | college   |          | quality   |          | quality   |          | credits   |          | rate      |          | grad.            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance |         | 0.031     | $^{***}$ | 0.029     | $^{***}$ | 0.049     | $^{***}$ | 0.006     | $^{***}$ | 0.026     | $^{***}$ | $-$0.048 | $^{***}$ |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.001           | )        |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV   |         | 0.244     |          | 3.326     |          | 3.244     |          | 0.158     |          | 0.418     |          | 3.817            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$       |         | 2,501,519 |          | 1,800,546 |          | 1,768,707 |          | 1,124,972 |          | 1,472,916 |          | 793,822          |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         |           |          |           |          |           |          |           |          |           |          |                  |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           | Dependent variable                                                                                                                            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| 3-14      |         | Enrolled  |          | College   |          | Degree    |          | 1st-year  |          | Grad.     |          | Time to          |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | college   |          | quality   |          | quality   |          | credits   |          | rate      |          | grad.            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | \(1\)     |          | \(2\)     |          | \(3\)     |          | \(4\)     |          | \(5\)     |          | \(6\)            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Endurance |         | 0.031     | $^{***}$ | 0.029     | $^{***}$ | 0.049     | $^{***}$ | 0.006     | $^{***}$ | 0.026     | $^{***}$ | $-$0.048 | $^{***}$ |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
|           |         | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.000    | )        | (0.001           | )        |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| Mean DV   |         | 0.244     |          | 3.326     |          | 3.244     |          | 0.158     |          | 0.418     |          | 3.817            |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+
| $N$       |         | 2,501,519 |          | 1,800,546 |          | 1,768,707 |          | 1,124,972 |          | 1,472,916 |          | 793,822          |          |
+-----------+---------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+-----------+----------+------------------+----------+

: Robustness of the baseline regressions to flexibly controlling fatigue-adjusted ability: College outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between endurance and college outcomes controlling for a seventh-order polynomial of fatigue-adjusted ability (Panel A) and ability fixed effects (Panel B). All regressions additionally control for age, gender, race, high school type, parental income, cohort fixed effects, and municipality fixed effects. In addition to the baseline controls, the regressions in columns 4–6 include college-degree fixed effects to remove the influence of a student's program choice.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels.

</div>

<div class="center">

<div id="tab:reg-lmkt-poly">

+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         |           |          |         |          |          |          |         |          |         |          |          |          |
+:==========+:========+==========:+:=========+========:+:=========+=========:+:=========+========:+:=========+========:+:=========+=========:+:=========+
|           | Dependent variable                                                                                                             |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| 3-14      |         | Formal    |          | Hourly  |          | Monthly  |          | Firm    |          | Occup.  |          | Industry |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | sector    |          | wage    |          | earnings |          | wage    |          | wage    |          | wage     |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | \(1\)     |          | \(2\)   |          | \(3\)    |          | \(4\)   |          | \(5\)   |          | \(6\)    |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Endurance |         | 0.000     | $^{***}$ | 0.050   | $^{***}$ | 0.052    | $^{***}$ | 0.034   | $^{***}$ | 0.017   | $^{***}$ | 0.004    | $^{***}$ |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | (0.000    | )        | (0.001  | )        | (0.001   | )        | (0.001  | )        | (0.000  | )        | (0.000   | )        |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Mean DV   |         | 0.326     |          | 3.865   |          | 7.551    |          | 3.885   |          | 3.886   |          | 3.858    |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| $N$       |         | 2,523,029 |          | 818,590 |          | 818,590  |          | 692,880 |          | 818,374 |          | 818,590  |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         |           |          |         |          |          |          |         |          |         |          |          |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           | Dependent variable                                                                                                             |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| 3-14      |         | Formal    |          | Hourly  |          | Monthly  |          | Firm    |          | Occup.  |          | Industry |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | sector    |          | wage    |          | earnings |          | wage    |          | wage    |          | wage     |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | \(1\)     |          | \(2\)   |          | \(3\)    |          | \(4\)   |          | \(5\)   |          | \(6\)    |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Endurance |         | 0.000     | $^{***}$ | 0.050   | $^{***}$ | 0.052    | $^{***}$ | 0.034   | $^{***}$ | 0.017   | $^{***}$ | 0.004    | $^{***}$ |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
|           |         | (0.000    | )        | (0.001  | )        | (0.001   | )        | (0.001  | )        | (0.000  | )        | (0.000   | )        |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| Mean DV   |         | 0.326     |          | 3.865   |          | 7.551    |          | 3.885   |          | 3.886   |          | 3.858    |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+
| $N$       |         | 2,523,029 |          | 818,590 |          | 818,590  |          | 692,880 |          | 818,374 |          | 818,590  |          |
+-----------+---------+-----------+----------+---------+----------+----------+----------+---------+----------+---------+----------+----------+----------+

: Robustness of the baseline regressions to flexibly controlling fatigue-adjusted ability: Labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between endurance and labor-market outcomes controlling for a seventh-order polynomial of fatigue-adjusted ability (Panel A) and ability fixed effects (Panel B). All regressions additionally control for age, gender, race, high school type, parental income, cohort fixed effects, municipality fixed effects, potential years of experience, and years of education.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels.

</div>

<div class="center">

<div id="tab:rob-meas-coll">

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
|                  | Dependent variable:                                                                                                                                                                                                               |                  |
+:=================+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+
| 3-14             |                  | Enrolled         |                  | College          |                  | Degree           |                  | 1st-year         |                  | Grad.            |                  | Time to          |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | college          |                  | quality          |                  | quality          |                  | credits          |                  | on time          |                  | grad.            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | \(1\)            |                  | \(2\)            |                  | \(3\)            |                  | \(4\)            |                  | \(5\)            |                  | \(6\)            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel A. Estimating ability/endurance separately by day and using the average**                                                                                                                                                                                       |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.053            | $^{***}$         | 0.050            | $^{***}$         | 0.084            | $^{***}$         | 0.010            | $^{***}$         | 0.043            | $^{***}$         | $-$0.079 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.114            | $^{***}$         | 0.107            | $^{***}$         | 0.157            | $^{***}$         | 0.018            | $^{***}$         | 0.081            | $^{***}$         | $-$0.158 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel B. Estimating ability/endurance separately by subject and using the average**                                                                                                                                                                                   |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.060            | $^{***}$         | 0.055            | $^{***}$         | 0.080            | $^{***}$         | 0.009            | $^{***}$         | 0.043            | $^{***}$         | $-$0.079 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.103            | $^{***}$         | 0.097            | $^{***}$         | 0.140            | $^{***}$         | 0.016            | $^{***}$         | 0.067            | $^{***}$         | $-$0.130 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel C. Including day fixed effects**                                                                                                                                                                                                                                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.031            | $^{***}$         | 0.030            | $^{***}$         | 0.050            | $^{***}$         | 0.006            | $^{***}$         | 0.025            | $^{***}$         | $-$0.047 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.110            | $^{***}$         | 0.104            | $^{***}$         | 0.152            | $^{***}$         | 0.018            | $^{***}$         | 0.077            | $^{***}$         | $-$0.151 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel D. Including subject fixed effects**                                                                                                                                                                                                                            |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.019            | $^{***}$         | 0.018            | $^{***}$         | 0.026            | $^{***}$         | 0.003            | $^{***}$         | 0.014            | $^{***}$         | $-$0.025 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.097            | $^{***}$         | 0.092            | $^{***}$         | 0.133            | $^{***}$         | 0.015            | $^{***}$         | 0.062            | $^{***}$         | $-$0.119 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel E. Using linear correlation as an alternative measure of endurance**                                                                                                                                                                                            |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.030            | $^{***}$         | 0.030            | $^{***}$         | 0.049            | $^{***}$         | 0.006            | $^{***}$         | 0.025            | $^{***}$         | $-$0.047 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.101            | $^{***}$         | 0.095            | $^{***}$         | 0.138            | $^{***}$         | 0.016            | $^{***}$         | 0.072            | $^{***}$         | $-$0.139 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Mean DV          |                  | 0.244            |                  | 3.326            |                  | 3.244            |                  | 0.158            |                  | 0.418            |                  | 3.817            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| $N$              |                  | 2,501,519        |                  | 1,800,546        |                  | 1,768,707        |                  | 1,124,972        |                  | 1,472,916        |                  | 793,822          |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+

: Robustness of baseline regressions to alternative ways of measuring ability and endurance: College outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and college outcomes using alternative specifications to estimate ability and endurance.

Each column shows the result for a different dependent variable. Each panel shows the result from estimating ability and endurance with a different specification. In Panels A–B, I estimate a student's ability/endurance separately for each testing day (Panel A) and academic subject (Panel B) and then average the estimates across days or subjects. In Panels C–D, I estimate endurance in a regression that controls for day fixed effects (Panel C) or subject fixed effects (Panel D). Finally, in Panel E, I use the correlation between question position and a dummy for correctly answering a question as an alternative measure of endurance.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-meas-lmkt">

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
|                  | Dependent variable:                                                                                                                                                                                                               |                  |
+:=================+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+
| 3-14             |                  | Formal           |                  | Hourly           |                  | Monthly          |                  | Firm             |                  | Occup.           |                  | Industry         |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | sector           |                  | wage             |                  | earnings         |                  | wage             |                  | wage             |                  | wage             |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | \(1\)            |                  | \(2\)            |                  | \(3\)            |                  | \(4\)            |                  | \(5\)            |                  | \(6\)            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel A. Estimating ability/endurance separately by day and using the average**                                                                                                                                                                                       |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.001            | $^{***}$         | 0.088            | $^{***}$         | 0.085            | $^{***}$         | 0.058            | $^{***}$         | 0.028            | $^{***}$         | 0.006            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.172            | $^{***}$         | 0.152            | $^{***}$         | 0.121            | $^{***}$         | 0.055            | $^{***}$         | 0.016            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel B. Estimating ability/endurance separately by subject and using the average**                                                                                                                                                                                   |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.001            | $^{***}$         | 0.088            | $^{***}$         | 0.076            | $^{***}$         | 0.061            | $^{***}$         | 0.026            | $^{***}$         | 0.008            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.156            | $^{***}$         | 0.135            | $^{***}$         | 0.110            | $^{***}$         | 0.048            | $^{***}$         | 0.014            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel C. Including day fixed effects**                                                                                                                                                                                                                                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.053            | $^{***}$         | 0.051            | $^{***}$         | 0.035            | $^{***}$         | 0.017            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.167            | $^{***}$         | 0.147            | $^{***}$         | 0.117            | $^{***}$         | 0.053            | $^{***}$         | 0.016            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel D. Including subject fixed effects**                                                                                                                                                                                                                            |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.029            | $^{***}$         | 0.025            | $^{***}$         | 0.020            | $^{***}$         | 0.008            | $^{***}$         | 0.003            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.147            | $^{***}$         | 0.127            | $^{***}$         | 0.104            | $^{***}$         | 0.045            | $^{***}$         | 0.013            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel E. Using linear correlation as an alternative measure of endurance**                                                                                                                                                                                            |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.052            | $^{***}$         | 0.050            | $^{***}$         | 0.035            | $^{***}$         | 0.016            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.151            | $^{***}$         | 0.132            | $^{***}$         | 0.107            | $^{***}$         | 0.048            | $^{***}$         | 0.014            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Mean DV          |                  | 0.326            |                  | 3.865            |                  | 7.551            |                  | 3.885            |                  | 3.886            |                  | 3.858            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| $N$              |                  | 2,523,029        |                  | 818,590          |                  | 818,590          |                  | 692,880          |                  | 818,374          |                  | 818,590          |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+

: Robustness of baseline regressions to alternative ways of measuring ability and endurance: Labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and labor-market outcomes using alternative specifications to estimate ability and endurance.

Each column shows the result for a different dependent variable. Each panel shows the result from estimating ability and endurance with a different specification. In Panels A–B, I estimate a student's ability/endurance separately for each testing day (Panel A) and academic subject (Panel B) and then average the estimates across days or subjects. In Panels C–D, I estimate endurance in a regression that controls for day fixed effects (Panel C) or subject fixed effects (Panel D). Finally, in Panel E, I use the correlation between question position and a dummy for correctly answering a question as an alternative measure of endurance.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-diff-coll">

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
|                   | Dependent variable:                                                                                                                                                                                                                           |                   |
+:==================+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+
| 3-14              |                   | Enrolled          |                   | College           |                   | Degree            |                   | 1st-year          |                   | Grad.             |                   | Time to           |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | college           |                   | quality           |                   | quality           |                   | credits           |                   | on time           |                   | grad.             |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | \(1\)             |                   | \(2\)             |                   | \(3\)             |                   | \(4\)             |                   | \(5\)             |                   | \(6\)             |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel A. Not controlling for question difficulty**                                                                                                                                                                                                                                  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.040             | $^{***}$          | 0.045             | $^{***}$          | 0.080             | $^{***}$          | 0.007             | $^{***}$          | 0.028             | $^{***}$          | $-$0.061  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.114             | $^{***}$          | 0.112             | $^{***}$          | 0.169             | $^{***}$          | 0.018             | $^{***}$          | 0.079             | $^{***}$          | $-$0.159  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel B. Estimating difficulty without adjusting for average position**                                                                                                                                                                                                             |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.030             | $^{***}$          | 0.028             | $^{***}$          | 0.045             | $^{***}$          | 0.006             | $^{***}$          | 0.026             | $^{***}$          | $-$0.046  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.097             | $^{***}$          | 0.090             | $^{***}$          | 0.130             | $^{***}$          | 0.016             | $^{***}$          | 0.068             | $^{***}$          | $-$0.133  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel C. Estimating difficulty using question-specific position effects**                                                                                                                                                                                                           |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.035             | $^{***}$          | 0.038             | $^{***}$          | 0.065             | $^{***}$          | 0.007             | $^{***}$          | 0.027             | $^{***}$          | $-$0.054  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.106             | $^{***}$          | 0.102             | $^{***}$          | 0.152             | $^{***}$          | 0.017             | $^{***}$          | 0.074             | $^{***}$          | $-$0.147  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel D. Estimating difficulty using shrunk question-specific position effects**                                                                                                                                                                                                    |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.034             | $^{***}$          | 0.035             | $^{***}$          | 0.059             | $^{***}$          | 0.006             | $^{***}$          | 0.026             | $^{***}$          | $-$0.052  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.104             | $^{***}$          | 0.098             | $^{***}$          | 0.146             | $^{***}$          | 0.017             | $^{***}$          | 0.073             | $^{***}$          | $-$0.144  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel E. Estimating position effects separately by fraction of correct responses**                                                                                                                                                                                                  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.031             | $^{***}$          | 0.030             | $^{***}$          | 0.049             | $^{***}$          | 0.006             | $^{***}$          | 0.026             | $^{***}$          | $-$0.047  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.101             | $^{***}$          | 0.094             | $^{***}$          | 0.138             | $^{***}$          | 0.016             | $^{***}$          | 0.071             | $^{***}$          | $-$0.139  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel F. Estimating position effects separately by subject**                                                                                                                                                                                                                        |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.031             | $^{***}$          | 0.029             | $^{***}$          | 0.048             | $^{***}$          | 0.006             | $^{***}$          | 0.026             | $^{***}$          | $-$0.047  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.099             | $^{***}$          | 0.093             | $^{***}$          | 0.135             | $^{***}$          | 0.016             | $^{***}$          | 0.071             | $^{***}$          | $-$0.137  | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.000            | )                 | (0.001            | )                 | (0.002            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Mean DV           |                   | 0.244             |                   | 3.326             |                   | 3.244             |                   | 0.158             |                   | 0.418             |                   | 3.817             |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| $N$               |                   | 2,501,519         |                   | 1,800,546         |                   | 1,768,707         |                   | 1,124,972         |                   | 1,472,916         |                   | 793,822           |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+

: Robustness of the baseline regressions to alternative ways of controlling for question difficulty when estimating ability/endurance: College outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and college outcomes using alternative measures of difficulty in the specification used to estimate ability and endurance.

Each panel shows the result using a different measure of question difficulty in equation reg:lpm-ind. In Panel A, I estimate equation reg:lpm-ind without controlling for question difficulty. In Panel B, I measure question difficulty as the fraction of students who incorrectly answer the question across all booklets. In Panels C–F, I adjust for differences in average position across questions by estimating the position effects with alternative specifications. In column C, I compute question-specific position effects. In Panel D, I compute a shrinkage estimator of the position effects. In Panel E, I compute the position effects separately for questions with a below/above fraction of correct responses. In Panel F, I compute the position effects separately by subject. See Appendix 12 for details on each measure of question difficulty. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-diff-lmkt">

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
|                   | Dependent variable:                                                                                                                                                                                                                           |                   |
+:==================+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+==================:+:==================+
| 3-14              |                   | Formal            |                   | Hourly            |                   | Monthly           |                   | Firm              |                   | Occup.            |                   | Industry          |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | sector            |                   | wage              |                   | earnings          |                   | wage              |                   | wage              |                   | wage              |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | \(1\)             |                   | \(2\)             |                   | \(3\)             |                   | \(4\)             |                   | \(5\)             |                   | \(6\)             |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel A. Not controlling for question difficulty**                                                                                                                                                                                                                                  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.001             | $^{***}$          | 0.080             | $^{***}$          | 0.077             | $^{***}$          | 0.053             | $^{***}$          | 0.022             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.002             | $^{***}$          | 0.183             | $^{***}$          | 0.163             | $^{***}$          | 0.127             | $^{***}$          | 0.056             | $^{***}$          | 0.015             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.002            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel B. Estimating difficulty without adjusting for average position**                                                                                                                                                                                                             |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.000             | $^{***}$          | 0.048             | $^{***}$          | 0.047             | $^{***}$          | 0.032             | $^{***}$          | 0.016             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.001             | $^{***}$          | 0.143             | $^{***}$          | 0.125             | $^{***}$          | 0.101             | $^{***}$          | 0.046             | $^{***}$          | 0.014             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel C. Estimating difficulty using question-specific position effects**                                                                                                                                                                                                           |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.001             | $^{***}$          | 0.066             | $^{***}$          | 0.064             | $^{***}$          | 0.044             | $^{***}$          | 0.019             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.002             | $^{***}$          | 0.165             | $^{***}$          | 0.146             | $^{***}$          | 0.115             | $^{***}$          | 0.051             | $^{***}$          | 0.015             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel D. Estimating difficulty using shrunk question-specific position effects**                                                                                                                                                                                                    |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.000             | $^{***}$          | 0.061             | $^{***}$          | 0.059             | $^{***}$          | 0.040             | $^{***}$          | 0.018             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.002             | $^{***}$          | 0.159             | $^{***}$          | 0.140             | $^{***}$          | 0.111             | $^{***}$          | 0.050             | $^{***}$          | 0.014             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel E. Estimating position effects separately by fraction of correct responses**                                                                                                                                                                                                  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.000             | $^{***}$          | 0.053             | $^{***}$          | 0.051             | $^{***}$          | 0.035             | $^{***}$          | 0.017             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.002             | $^{***}$          | 0.152             | $^{***}$          | 0.133             | $^{***}$          | 0.107             | $^{***}$          | 0.048             | $^{***}$          | 0.014             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| **Panel F. Estimating position effects separately by subject**                                                                                                                                                                                                                        |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Endurance         |                   | 0.000             | $^{***}$          | 0.051             | $^{***}$          | 0.049             | $^{***}$          | 0.034             | $^{***}$          | 0.016             | $^{***}$          | 0.004             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Ability           |                   | 0.002             | $^{***}$          | 0.149             | $^{***}$          | 0.130             | $^{***}$          | 0.105             | $^{***}$          | 0.048             | $^{***}$          | 0.014             | $^{***}$          |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   | (0.000            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.001            | )                 | (0.000            | )                 |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| Mean DV           |                   | 0.326             |                   | 3.865             |                   | 7.551             |                   | 3.885             |                   | 3.886             |                   | 3.858             |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
| $N$               |                   | 2,523,029         |                   | 818,590           |                   | 818,590           |                   | 692,880           |                   | 818,374           |                   | 818,590           |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+

: Robustness of the baseline regressions to alternative ways of controlling for question difficulty when estimating ability/endurance: Labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and labor-market outcomes using alternative measures of difficulty in the specification used to estimate ability and endurance.

Each panel shows the result using a different measure of question difficulty in equation reg:lpm-ind. In Panel A, I estimate equation reg:lpm-ind without controlling for question difficulty. In Panel B, I measure question difficulty as the fraction of students who incorrectly answer the question across all booklets. In Panels C–F, I adjust for differences in average position across questions by estimating the position effects with alternative specifications. In column C, I compute question-specific position effects. In Panel D, I compute a shrinkage estimator of the position effects. In Panel E, I compute the position effects separately for questions with a below/above fraction of correct responses. In Panel F, I compute the position effects separately by subject. See Appendix 12 for details on each measure of question difficulty. Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-samp-coll">

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
|                  | Dependent variable:                                                                                                                                                                                                               |                  |
+:=================+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+
| 3-14             |                  | Enrolled         |                  | College          |                  | Degree           |                  | 1st-year         |                  | Grad.            |                  | Time to          |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | college          |                  | quality          |                  | quality          |                  | credits          |                  | on time          |                  | grad.            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | \(1\)            |                  | \(2\)            |                  | \(3\)            |                  | \(4\)            |                  | \(5\)            |                  | \(6\)            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel A. Excluding students in the bottom or top 10 percent of the ability distribution**                                                                                                                                                                             |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.032            | $^{***}$         | 0.027            | $^{***}$         | 0.039            | $^{***}$         | 0.007            | $^{***}$         | 0.030            | $^{***}$         | $-$0.047 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.102            | $^{***}$         | 0.085            | $^{***}$         | 0.107            | $^{***}$         | 0.019            | $^{***}$         | 0.087            | $^{***}$         | $-$0.146 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.003           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel B. Excluding students in the bottom or top 10 percent of the endurance distribution**                                                                                                                                                                           |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.030            | $^{***}$         | 0.030            | $^{***}$         | 0.050            | $^{***}$         | 0.006            | $^{***}$         | 0.025            | $^{***}$         | $-$0.044 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.100            | $^{***}$         | 0.093            | $^{***}$         | 0.135            | $^{***}$         | 0.016            | $^{***}$         | 0.075            | $^{***}$         | $-$0.138 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel C. Excluding students in the bottom or top 10 percent of either distribution**                                                                                                                                                                                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.031            | $^{***}$         | 0.026            | $^{***}$         | 0.037            | $^{***}$         | 0.007            | $^{***}$         | 0.030            | $^{***}$         | $-$0.046 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.102            | $^{***}$         | 0.083            | $^{***}$         | 0.102            | $^{***}$         | 0.020            | $^{***}$         | 0.089            | $^{***}$         | $-$0.146 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.003           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel D. Excluding students in the bottom or top 20 percent of either distribution**                                                                                                                                                                                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.030            | $^{***}$         | 0.023            | $^{***}$         | 0.030            | $^{***}$         | 0.008            | $^{***}$         | 0.034            | $^{***}$         | $-$0.044 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.003           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.099            | $^{***}$         | 0.074            | $^{***}$         | 0.086            | $^{***}$         | 0.022            | $^{***}$         | 0.100            | $^{***}$         | $-$0.152 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.004           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel E. Excluding individuals with positive estimated endurance**                                                                                                                                                                                                    |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.033            | $^{***}$         | 0.028            | $^{***}$         | 0.048            | $^{***}$         | 0.005            | $^{***}$         | 0.026            | $^{***}$         | $-$0.047 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.002           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.107            | $^{***}$         | 0.097            | $^{***}$         | 0.143            | $^{***}$         | 0.016            | $^{***}$         | 0.065            | $^{***}$         | $-$0.133 | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.000           | )                | (0.001           | )                | (0.003           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+

: Robustness of the baseline regressions to sample selection: College outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and college outcomes using alternative sample restrictions.

Each column shows the result for a different dependent variable. Each panel shows the result for a different sample of students. In Panel A, I exclude students in the bottom and top deciles of the ability distribution. In Panel B, I exclude students in the bottom and top deciles of the endurance distribution. In Panel C, I exclude students in the bottom and top deciles of the distribution of either skill. In Panel D, I exclude students in the bottom and top quintiles of the distribution of either skill. In Panel E, I exclude students with a positive estimate of endurance ($\hat{\beta}>0$). I construct the deciles and quintiles using all the students in the high-school-students sample.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-samp-lmkt">

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
|                  | Dependent variable:                                                                                                                                                                                                               |                  |
+:=================+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+=================:+:=================+
| 3-14             |                  | Formal           |                  | Hourly           |                  | Monthly          |                  | Firm             |                  | Occup.           |                  | Industry         |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | sector           |                  | wage             |                  | earnings         |                  | wage             |                  | wage             |                  | wage             |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | \(1\)            |                  | \(2\)            |                  | \(3\)            |                  | \(4\)            |                  | \(5\)            |                  | \(6\)            |                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel A. Excluding students in the bottom or top 10 percent of the ability distribution**                                                                                                                                                                             |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.046            | $^{***}$         | 0.044            | $^{***}$         | 0.031            | $^{***}$         | 0.017            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.001            | $^{***}$         | 0.130            | $^{***}$         | 0.113            | $^{***}$         | 0.092            | $^{***}$         | 0.051            | $^{***}$         | 0.016            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.002           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel B. Excluding students in the bottom or top 10 percent of the endurance distribution**                                                                                                                                                                           |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.053            | $^{***}$         | 0.050            | $^{***}$         | 0.035            | $^{***}$         | 0.016            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.001            | $^{***}$         | 0.149            | $^{***}$         | 0.131            | $^{***}$         | 0.103            | $^{***}$         | 0.049            | $^{***}$         | 0.014            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel C. Excluding students in the bottom or top 10 percent of either distribution**                                                                                                                                                                                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.044            | $^{***}$         | 0.042            | $^{***}$         | 0.029            | $^{***}$         | 0.017            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.001            | $^{***}$         | 0.127            | $^{***}$         | 0.112            | $^{***}$         | 0.089            | $^{***}$         | 0.050            | $^{***}$         | 0.015            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.002           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel D. Excluding students in the bottom or top 20 percent of either distribution**                                                                                                                                                                                  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.000            | $^{***}$         | 0.039            | $^{***}$         | 0.037            | $^{***}$         | 0.025            | $^{***}$         | 0.016            | $^{***}$         | 0.004            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.002           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.001            | $^{***}$         | 0.117            | $^{***}$         | 0.105            | $^{***}$         | 0.083            | $^{***}$         | 0.052            | $^{***}$         | 0.016            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.002           | )                | (0.002           | )                | (0.002           | )                | (0.001           | )                | (0.001           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| **Panel E. Excluding individuals with positive estimated endurance**                                                                                                                                                                                                    |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Endurance        |                  | 0.001            | $^{***}$         | 0.054            | $^{***}$         | 0.055            | $^{***}$         | 0.033            | $^{***}$         | 0.017            | $^{***}$         | 0.003            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Ability          |                  | 0.002            | $^{***}$         | 0.158            | $^{***}$         | 0.137            | $^{***}$         | 0.112            | $^{***}$         | 0.049            | $^{***}$         | 0.014            | $^{***}$         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
|                  |                  | (0.000           | )                | (0.002           | )                | (0.002           | )                | (0.002           | )                | (0.001           | )                | (0.000           | )                |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+------------------+

: Robustness of the baseline regressions to sample selection: Labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table shows estimates of the relationship between ability/endurance and labor-market outcomes using alternative sample restrictions.

Each column shows the result for a different dependent variable. Each panel shows the result for a different sample of students. In Panel A, I exclude students in the bottom and top deciles of the ability distribution. In Panel B, I exclude students in the bottom and top deciles of the endurance distribution. In Panel C, I exclude students in the bottom and top deciles of the distribution of either skill. In Panel D, I exclude students in the bottom and top quintiles of the distribution of either skill. In Panel E, I exclude students with a positive estimate of endurance ($\hat{\beta}>0$). I construct the deciles and quintiles using all the students in the high-school-students sample.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-prec-coll">

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
|                 | Dependent variable                                                                                                                                                                                                     |                 |
+:================+:================+================:+:================+================:+:================+================:+:================+================:+:================+================:+:================+=================:+:================+
| 3-14            |                 | Enrolled        |                 | College         |                 | Degree          |                 | 1st-year        |                 | Grad.           |                 | Time to          |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | college         |                 | quality         |                 | quality         |                 | credits         |                 | on time         |                 | grad.            |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | \(1\)           |                 | \(2\)           |                 | \(3\)           |                 | \(4\)           |                 | \(5\)           |                 | \(6\)            |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| **Panel A. Weighting each observation by its precision**                                                                                                                                                                                                   |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| Endurance       |                 | 0.031           | $^{***}$        | 0.030           | $^{***}$        | 0.051           | $^{***}$        | 0.006           | $^{***}$        | 0.026           | $^{***}$        | $-$0.048 | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.001           | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| Ability         |                 | 0.100           | $^{***}$        | 0.094           | $^{***}$        | 0.139           | $^{***}$        | 0.016           | $^{***}$        | 0.073           | $^{***}$        | $-$0.140 | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.001          | )               | (0.002           | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| **Panel B. Shrunk estimator of ability and endurance**                                                                                                                                                                                                     |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| Endurance       |                 | 0.045           | $^{***}$        | 0.043           | $^{***}$        | 0.073           | $^{***}$        | 0.012           | $^{***}$        | 0.037           | $^{***}$        | $-$0.067 | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.000          | )               | (0.001          | )               | (0.002           | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| Ability         |                 | 0.105           | $^{***}$        | 0.099           | $^{***}$        | 0.145           | $^{***}$        | 0.023           | $^{***}$        | 0.074           | $^{***}$        | $-$0.143 | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 | (0.000          | )               | (0.000          | )               | (0.001          | )               | (0.000          | )               | (0.001          | )               | (0.002           | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| Mean DV         |                 | 0.244           |                 | 3.326           |                 | 3.244           |                 | 0.158           |                 | 0.418           |                 | 3.817            |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
| $N$             |                 | 2,501,519       |                 | 1,800,546       |                 | 1,768,707       |                 | 1,124,972       |                 | 1,472,916       |                 | 793,822          |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+
|                 |                 |                 |                 |                 |                 |                 |                 |                 |                 |                 |                 |                  |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+------------------+-----------------+

: Robustness of the baseline regressions to accounting for measurement error: College outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between ability/endurance and college outcomes accounting for measurement error in the estimates of ability and endurance.

Each column shows the result for a different dependent variable. In Panel A, I weight each observation by the inverse of the standard error of the ability and endurance estimates. Specifically, the weight of each observation is $w = 1/(\text{SE}_{\hat{\alpha}_i}^2 + \text{SE}_{\hat{\beta}_i}^2)$, where $\text{SE}_{\hat{\alpha}_i}$ and $\text{SE}_{\hat{\beta}_i}^2$ are the standard errors of $\hat{\alpha}_i$ and $\hat{\beta}_i$. In Panel B, I estimate the baseline regression using a shrunk estimator of ability and endurance. I compute the shrunk estimator of endurance as $\beta^s_i = \omega_i  \hat{\beta}_i + (1 - \omega_j)\bar{\beta},$ where $\bar{\beta}$ is the average cognitive endurance in my sample. The individual-specific weight is $\omega_i = \frac{\mathop{\mathrm{\mathbb{V}ar}}[\beta_i] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_i}^2]}{\mathop{\mathrm{\mathbb{V}ar}}[\beta_i] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_i}^2] + \text{SE}_{\hat{\beta}_i}^2}.$ The shrunk estimator, $\beta^s_i$, puts more weight on estimates of $\beta_i$ that are more precisely estimated, as measured by a low standard error. I compute the shrunk estimator of ability analogously.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

<div class="center">

<div id="tab:rob-prec-lmkt">

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
|                 | Dependent variable                                                                                                                                                                                                    |                 |
+:================+:================+================:+:================+================:+:================+================:+:================+================:+:================+================:+:================+================:+:================+
| 3-14            |                 | Formal          |                 | Hourly          |                 | Monthly         |                 | Firm            |                 | Occup.          |                 | Industry        |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | sector          |                 | wage            |                 | earnings        |                 | wage            |                 | wage            |                 | wage            |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | \(1\)           |                 | \(2\)           |                 | \(3\)           |                 | \(4\)           |                 | \(5\)           |                 | \(6\)           |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| **Panel A. Weighting each observation by its precision**                                                                                                                                                                                                  |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Endurance       |                 | 0.000           | $^{***}$        | 0.053           | $^{***}$        | 0.051           | $^{***}$        | 0.035           | $^{***}$        | 0.017           | $^{***}$        | 0.004           | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | (0.000          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.000          | )               | (0.000          | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Ability         |                 | 0.001           | $^{***}$        | 0.151           | $^{***}$        | 0.133           | $^{***}$        | 0.107           | $^{***}$        | 0.048           | $^{***}$        | 0.014           | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | (0.000          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.000          | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| **Panel B. Shrunk estimator of ability and endurance**                                                                                                                                                                                                    |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Endurance       |                 | 0.001           | $^{***}$        | 0.076           | $^{***}$        | 0.074           | $^{***}$        | 0.050           | $^{***}$        | 0.024           | $^{***}$        | 0.005           | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | (0.000          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.000          | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Ability         |                 | 0.002           | $^{***}$        | 0.157           | $^{***}$        | 0.138           | $^{***}$        | 0.111           | $^{***}$        | 0.050           | $^{***}$        | 0.015           | $^{***}$        |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 | (0.000          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.001          | )               | (0.000          | )               |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Mean DV         |                 | 0.326           |                 | 3.865           |                 | 7.551           |                 | 3.885           |                 | 3.886           |                 | 3.858           |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| $N$             |                 | 2,523,029       |                 | 818,590         |                 | 818,590         |                 | 692,880         |                 | 818,374         |                 | 818,590         |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+

: Robustness of the baseline regressions to accounting for measurement error: Labor-market outcomes

</div>

</div>

<div class="singlespace">

*Notes:* This table displays estimates of the relationship between ability/endurance and labor-market outcomes accounting for measurement error in the estimates of ability and endurance.

Each column shows the result for a different dependent variable. In Panel A, I weight each observation by the inverse of the standard error of the ability and endurance estimates. Specifically, the weight of each observation is $w = 1/(\text{SE}_{\hat{\alpha}_i}^2 + \text{SE}_{\hat{\beta}_i}^2)$, where $\text{SE}_{\hat{\alpha}_i}$ and $\text{SE}_{\hat{\beta}_i}^2$ are the standard errors of $\hat{\alpha}_i$ and $\hat{\beta}_i$. In Panel B, I estimate the baseline regression using a shrunk estimator of ability and endurance. I compute the shrunk estimator of endurance as $\beta^s_i = \omega_i  \hat{\beta}_i + (1 - \omega_j)\bar{\beta},$ where $\bar{\beta}$ is the average cognitive endurance in my sample. The individual-specific weight is $\omega_i = \frac{\mathop{\mathrm{\mathbb{V}ar}}[\beta_i] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_i}^2]}{\mathop{\mathrm{\mathbb{V}ar}}[\beta_i] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_i}^2] + \text{SE}_{\hat{\beta}_i}^2}.$ The shrunk estimator, $\beta^s_i$, puts more weight on estimates of $\beta_i$ that are more precisely estimated, as measured by a low standard error. I compute the shrunk estimator of ability analogously.

Heteroskedasticity-robust standard errors clustered at the individual level in parentheses. $^{*}$, $^{**}$ and $^{***}$ denote significance at 10 percent, 5 percent and 1 percent levels, respectively.

</div>

## From Question-Level Results to Exam Design

Admission officers use test scores to screen applicants partly because they are informative about which applicants will succeed in college.

The predictive validity of test scores for outcome $Y$, $\rho^Y$, can be written as a weighted average of the predictive validity of each exam question $j \in \{1, ..., J\}$:

$$\begin{align*}
    \rho^Y  &\equiv \text{Corr}(Y_i, \text{TestScore}_i) 
    &= \frac{1}{J} \sum_{j=1}^J  \frac{\sigma_{C_{j}}}{\sigma_T} \rho^Y_j,
\end{align*}$$

where $\sigma_{T}$ and $\sigma_{C_{j}}$ are the standard deviations of test scores and question $j$ responses, and $\rho^Y_j \equiv \text{Corr}(Y_i, C_{ij})$ is the predictive validity of question $j$.

Limited endurance affects a question's informativeness by changing the skill composition of students who correctly answer the question.

# About the ENEM
In this Appendix, I describe the changing role of the ENEM in the higher-education system over time, compare the ENEM to the US SAT and ACT exams, and describe the IRT grading system used by the Ministry of Education to generate ENEM test scores.

## The Role of the ENEM in the Higher-education System
The ENEM was created in 1998 by the National Institute of Educational Studies (INEP), a unit of the Brazilian Ministry of Education, with the goal of evaluating student performance at the end of high school (Appendix Figure 10). The ENEM is an achievement test, that is, it was designed to test for mastery of material individuals should learn by the end of high school.[^24]

The first ENEM contained 63 multiple-choice interdisciplinary questions and was conducted over a five-hour testing block. The test score was calculated as the fraction of correct responses. In its first edition, fewer than 200,000 individuals enrolled to take the ENEM.

<figure id="fig:timeline" data-latex-placement="H">

<figcaption>Timeline of the ENEM</figcaption>
</figure>

In 2004, the government created a college scholarship program for low-income students called ProUni (*Programa Universidade para Todos*). ProUni used ENEM scores to allocate the scholarships to applicants, with program-specific score cutoffs based on the number of seats available in each program. After ProUni was implemented, the number of individuals who signed up to take the ENEM doubled from 1.5 million in 2004 to 3.0 million in 2005.

In 2009, the Ministry of Education reformed the ENEM with the aim of encouraging colleges to use it as an admission exam. The new ENEM consists of 180 multiple-choice questions conducted over two consecutive days of testing during a weekend. The new exam contains questions in four subjects: mathematics, natural sciences (which includes biology, physics, and chemistry questions), social sciences (which includes history, geography, philosophy, and sociology questions), and language arts (which includes questions on Portuguese language, literature, foreign language, arts, physical education, and information and communication technologies). On the first day of testing, individuals had five and a half hours to take the social science test, the natural science test, and the essay. On the second day of testing, individuals had five hours to take math and language arts tests. The new ENEM is graded according to Item Response Theory (IRT), which enables colleges to compare test scores over time (see Appendix 11.4).

In 2010, the Ministry of Education introduced a centralized admission system called SISU (*Sistema de Seleção Unificada*) with the goal of simplifying the college application process for federal universities. The centralized system used ENEM scores to allocate students to participating colleges. All federal universities are part of the system, but other universities (including state and municipal universities) are not mandated to be part of it. Also in 2010, the Government started using ENEM scores to allocate student loans through a program called FIES (*Fundo de Financiamento ao Estudante do Ensino Superior*). In addition, starting in 2010 (and finishing in 2016), ENEM scores could be used to certify the attainment of high-school-level skills (analogously to the GED in the US). By 2010, over 4.6 million individuals enrolled to take the ENEM.

In 2017, INEP changed the schedule of the ENEM. The exam started being conducted over two consecutive Sundays. On the first Sunday, individuals have five and a half hours to answer the language arts test, the social science test, and the essay. On the second Sunday, individuals have five hours to answer the natural science and math tests. The other features of the exam remained constant.

In 2020, individuals had the option to take the ENEM through a computer without internet access. Over 5.7 million individuals enrolled to take the ENEM this year.

## ENEM Sample Questions
Appendix Figures 11–14 present sample questions from the natural science, social science, language arts, and math components of the ENEM. The questions come from the 2016 ENEM. The questions are average in terms of their difficulty.

<figure id="fig:nsci-ex" data-latex-placement="H">
<p><strong>Panel A. Original (in portuguese)</strong></p>
<div class="centering">
<p><br />
 <br />
</p>
</div>
<p><strong>Panel B. Translation</strong></p>
<div class="centering">

</div>
<p><em>Notes:</em> The correct answer is underlined.</p>
<figcaption>Natural Science sample question (item #11898)</figcaption>
</figure>

<figure id="fig:ssci-ex" data-latex-placement="H">
<p><strong>Panel A. Original (in portuguese)</strong></p>
<div class="centering">
<p><br />
 <br />
</p>
</div>
<p><strong>Panel B. Translation</strong></p>
<div class="centering">

</div>
<p><em>Notes:</em> The correct answer is underlined.</p>
<figcaption>Social Science sample question (item #97290)</figcaption>
</figure>

<figure id="fig:lang-ex" data-latex-placement="H">
<p><strong>Panel A. Original (in portuguese)</strong></p>
<div class="centering">
<p><br />
 <br />
</p>
</div>
<p><strong>Panel B. Translation</strong></p>
<div class="centering">

</div>
<p><em>Notes:</em> The correct answer is underlined.</p>
<figcaption>Language Arts sample question (item #86509)</figcaption>
</figure>

<figure id="fig:math-ex" data-latex-placement="H">
<p><strong>Panel A. Original (in portuguese)</strong></p>
<div class="centering">
<p><br />
 <br />
</p>
</div>
<p><strong>Panel B. Translation</strong></p>
<div class="centering">

</div>
<p><em>Notes:</em> The correct answer is underlined.</p>
<figcaption>Math sample question (item #37515)</figcaption>
</figure>

## Comparison of the ENEM to the ACT and SAT exams

Appendix Table 25 compares important features of the SAT, ACT, and ENEM. The SAT contains 154 multiple-choice questions divided into three sections: reading, writing and language, and math, plus an optional essay. Including the essay, individuals have 3 hours and 50 minutes to take the test. On average across sections, test-takers have about 1 minute and 10 seconds to answer each question. Raw scores are converted into scaled scores through a score conversion table.

The ACT contains 215 multiple-choice questions divided into four sections: English, math, reading, and science, plus an optional essay. Including the essay, individuals have 3 hours and 35 minutes to take the test. On average across sections, test-takers have less than 1 minute to answer each question. Raw scores are converted into scaled scores through a score conversion table.

There are some notable differences between the SAT/ACT and the ENEM. First, the ENEM is conducted over two days of testing. Second, individuals in the ENEM have no assigned breaks. Third, the booklet ENEM test-takers receive contains all the questions they have to answer during the testing day. Thus, they may allocate time disproportionally across sections. In contrast, in the SAT and ACT, each section has an assigned amount of time. Finally, in the ENEM, each question is associated with a different text passage or prompt (in some cases, two questions share a prompt or passage). In contrast, in the SAT and ACT, a given passage is associated with multiple questions. This partly explains why the time per question is higher in the ENEM than in the ACT/SAT.

<div class="sidewaystable">

<div class="center">

<div id="tab:sat">

                      SAT                                        ACT                                       ENEM
  ------------------- ------------------------------------------ ----------------------------------------- -----------------------------------
  Cost                $\sim$$60                                 $\sim$$88                                $\sim$$17
  Grading             Score conversion chart using raw scores    Score conversion chart using raw scores   Item Response Theory (IRT)
  Starting time       Between 8:30 and 9am                       Between 8:30 and 9am                      1pm Brasilia time
  Number of items     154 questions                              215 questions                             180 questions
  Total length        3 hours and 50 mins over 1 testing day     3 hours and 35 mins over 1 testing day    10 hours over 2 testing days
  Time per question   1 minute and 10 seconds                    50 seconds                                3 minutes
  Breaks              10 mins break after reading section        10 min break after math section           N/A
                      5 min break between math sections          5 min break before essay                  
                      2 min break before the essay                                                         
  Sections            Reading (65 mins, 52 items)                English (45 mins, 75 items)               Social science (day 1, 45 items)
                      Writing and Language (35 mins, 44 items)   Math (60 mins, 60 items)                  Natural science (day 1, 45 items)
                      Math w/o calculator (25 mins, 20 items)    Reading (35 mins, 40 items)               Language arts (day 2, 45 items)
                      Math w/ calculator (55 mins, 38 items)     Science (35 mins, 40 items)               Math (day 2, 45 items)
                      Optional essay (50 mins)                   Optional essay (40 mins)                  Mandatory essay (day 2)

  : Comparison of the SAT, ACT, and ENEM college admission exams

</div>

</div>

<div class="singlespace">

*Notes:* The SAT refers to the post-2016 version of the SAT, which includes an optional essay. This optional essay was eliminated in 2021. The ENEM refers to the 2009–2016 version of the exam (see Section 11.1 for information on the pre-2009 and post-2016 versions). The exam length was computed excluding breaks and including the essay. The time per question does not account for the essay.

</div>

</div>

## IRT Grading
The Brazilian Testing Agency grades the ENEM exam based on the three-parameter item response theory (IRT). According to IRT, the probability that an individual $i$ with ability $\theta_i$ correctly answers question $j$ is:

$$\begin{align}
\Pr(C_{ij} = 1 | \theta_i) = p_{j}({\theta_i }) = c_{j} + {\frac {1-c_{j}}{1+e^{{-a_{j}({\theta_i }-b_{i})}}}},
\end{align}$$

where $a_j$, $b_j$, and $c_j$ are three question-level parameters that represent, respectively, a question's "discrimination," "difficulty," and "pseudo-guess." A question's discrimination refers to its ability to discriminate between low- and high-ability individuals; the difficulty represents the value of $\theta$ at which $p_{j}({\theta_i})$ has the maximum slope, and the pseudo-guess parameter indicates the likelihood that a student with an infinitely negative ability has to correctly respond to the question. Notice that in equation eq:irt, the probability of correctly answering a question does not depend on its position. Thus, the type of position effects documented above suggests that the IRT estimates of individual-level ability are biased. Modern IRT approaches (e.g., Debeer and Janssen, 2013) include item position into the framework.

Each question's parameters are known from pre-testing. The testing agency estimates the $\theta_i$ that maximizes the empirical likelihood of the entire sequence of responses. They do this separately for each student and academic subject. ENEM scores are normalized to have a mean of 500 and a standard deviation of 100.

Despite its complexity, most of the variation in IRT-estimated ENEM scores is driven by variation in the fraction of correct responses in the exam. A regression of IRT-estimated ENEM scores on the fraction of correct responses yields an R-squared of 0.88 (the rank correlation between the two variables is 0.93). Consistent with this, Appendix Figure fig:irt-pct-corr shows that the relationship between these two variables is linear in both levels (Panel A) and percentiles (Panel B). The strong relationship between IRT-estimated scores and the fraction of correct responses holds not just for the overall score but also for the score in each academic subject (Appendix Table 26).

<figure data-latex-placement="H">
<figure>
<embed src="../results/binsc-score-meancorr.pdf" />
<figcaption>Panel A. In levels</figcaption>
</figure>
<figure>
<embed src="../results/binsc-rankscore-rankcorr.pdf" />
<figcaption>Panel B. In percentiles</figcaption>
</figure>
<p><em>Notes:</em> This figure shows binned scatterplots plotting the average IRT-estimated ENEM score across all four academic subjects (<span class="math inline"><em>y</em></span>-axis) against the fraction of correct responses on the exam (<span class="math inline"><em>x</em></span>-axis). Panel A shows the results in levels and Panel B in percentiles. I first group students into 100 equally-sized bins based on their fraction of correct responses. Then, I calculate the average IRT-estimated ENEM score or score percentile in each bin. The vertical lines denote the 10th and 90th percentiles of the ENEM score distribution. The solid red line shows the predicted values from a linear regression on the plotted points.</p>
<figcaption>Panel B. In percentiles</figcaption>
</figure>

<div class="center">

<div id="tab:irt-pct-corr">

+------------------------+-------------------------------------------------------------------------------------------------------------------------------+---------------+---------------+---------------+---+---+
|                        | Academic subject                                                                                                              |               |               |               |   |   |
+:=======================+:==============+==============:+:==============+==============:+:==============+==============:+:==============+==============:+:==============+==============:+:==============+==:+:==+
| 3-10                   |               | Social        |               | Natural       |               | Language      |               | Math          |               | Average       |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
|                        |               | science       |               | science       |               | arts          |               |               |               | score         |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
|                        |               | \(1\)         |               | \(2\)         |               | \(3\)         |               | \(4\)         |               | \(5\)         |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| **Panel A. Variables measured in levels**                                                                                                                                                              |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| Fraction correct resp. |               | 0.892         | $^{***}$      | 0.880         | $^{***}$      | 0.907         | $^{***}$      | 0.885         | $^{***}$      | 0.937         | $^{***}$      |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
|                        |               | (0.000        | )             | (0.000        | )             | (0.000        | )             | (0.000        | )             | (0.000        | )             |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| $N$                    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| R$-$squared            |               | 0.79          |               | 0.77          |               | 0.82          |               | 0.78          |               | 0.88          |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| **Panel B. Variables measured in percentiles**                                                                                                                                                         |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| Fraction correct resp. |               | 0.904         | $^{***}$      | 0.858         | $^{***}$      | 0.917         | $^{***}$      | 0.845         | $^{***}$      | 0.931         | $^{***}$      |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
|                        |               | (0.000        | )             | (0.000        | )             | (0.000        | )             | (0.000        | )             | (0.000        | )             |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| $N$                    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               | 14,936,699    |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+
| R$-$squared            |               | 0.82          |               | 0.74          |               | 0.84          |               | 0.71          |               | 0.87          |               |   |   |
+------------------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---+---+

: Correlation between IRT-estimated ENEM score and fraction of correct responses on each subject

</div>

</div>

<div class="singlespace">

*Notes:* This table displays the correlation between the IRT-estimated ENEM score and the fraction of correct responses. Columns 1–4 present the correlations separately for each academic subject. Column 5 presents the correlation between the average score across all subjects and the fraction of correct responses in the entire exam. Heteroskedasticity-robust standard errors clustered at the question level in parentheses. $^{***}$, $^{**}$ and $^*$ denote significance at 10%, 5% and 1% levels, respectively.

</div>

# Measuring Fatigue-Adjusted Question Difficulty
In this Appendix, I describe the measures of position-adjusted question difficulty that I use for estimating cognitive endurance. Instead of taking a strong stance on what the right measure of position-adjusted question difficulty is, I show that the results are robust to measuring this variable in several ways.

An intuitive measure of a question's difficulty is the fraction of students who correctly answer the question. This measure is problematic in the presence of limited endurance since a given question has a different fraction of correct responses depending on its location. To illustrate this problem, Appendix Figure 15 plots students' performance on a natural science question in each booklet. The position of this item ranged from position 46 in the gray booklet to position 87 in the blue booklet. Correspondingly, student performance varied from 40.7 percent in the gray booklet to 29.9 percent in the blue booklet.

<figure id="fig:item-11898" data-latex-placement="H">
<embed src="../results/item-11898.pdf" />
<p><em>Notes:</em> This figure shows the fraction of individuals who correctly responded to item #11898 in each of the four booklets. See Appendix Figure <a href="#fig:nsci-ex" data-reference-type="ref" data-reference="fig:nsci-ex">11</a> for the question’s text.</p>
<figcaption>Performance on a natural science question (item #11898)</figcaption>
</figure>

The fact that performance on a question varies according to its position raises an important identification challenge for measuring question difficulty. It becomes difficult to disentangle whether questions that appear later in the exam are less likely to be correctly answered because they test more difficult material or because students are experiencing greater cognitive fatigue by the time they encounter these questions.

To account for limited cognitive endurance, I estimate several measures of question difficulty that represent the estimated fraction of students who would correctly answer a question if the question appeared in the first position of the exam. I estimate this fraction following a three-step process. First, I compute the average position of each question across all booklets. Second, I estimate the effect of a one-position increase of a question position on performance on the question ("position effect"). Third, I multiply the average question position calculated in the first step by the position effect estimated in the second step and subtract this figure from the fraction of correct responses across all booklets. This yields a position-adjusted estimate of question difficulty.

The measures of question difficulty differ in how I estimate the position effect in the second step. My baseline measure of question difficulty uses the position effect estimated by pooling all questions (Table 2, column 3). This measure assumes that the effect of a one-position increase on performance is homogeneous across questions.

The second measure of question difficulty uses a question-specific position effect. I estimate equation eq:pot-out-reg separately for each question and use the intercept from the regression as the measure of difficulty. This does not assume homogeneity in position effects; however, for some questions the position effect is imprecisely estimated. Appendix Figure 16 illustrates this process for seven selected exam questions. Each marker represents the fraction of students who correctly answered a specific question when it appeared at a particular position across the four booklets. Solid lines show the estimated linear relationship between question position and performance for each question. The dashed lines represent the out-of-sample projection of these relationships to the $y$-axis intercept, which corresponds to the estimated performance if the question appeared as the first question on the exam. This $y$-intercept serves as the position-adjusted measure of question difficulty.

<figure id="fig:mean-corr-item" data-latex-placement="H">
<embed src="../results/mean-corr-item-level.pdf" />
<p><em>Notes:</em> This figure plots the fraction of correct responses on seven selected exam questions as a function of their position on the four different exam booklets. Each marker represents the fraction of students who correctly answered a specific question at a given position. Solid lines denote predicted values from linear regressions estimated on the plotted points. Dashed lines show the out-of-sample projection to the <span class="math inline"><em>y</em></span>-axis, where the <span class="math inline"><em>y</em></span>-intercept represents the estimated performance if the question appeared first on the exam (i.e., the position-adjusted measure of question difficulty). The horizontal dashed line at 0.20 indicates the expected performance if students were randomly guessing on a five-option multiple-choice question.</p>
<figcaption>Position-adjusted difficulty for selected exam questions</figcaption>
</figure>

The third measure of question difficulty combines the first two by shrinking the question-specific position effect to the average effect by its signal-to-noise ratio. Specifically, let $\beta_j$ be the position effect estimating using data only from question $j$ and $\bar{\beta}$ be the average position effect across all questions. The shrunk position effect of question $j$, $\beta^s_j$, is a convex combination of $\beta_j$ and $\bar{\beta}$:

$$\begin{align*}
    \beta^s_j = \omega_j  \beta_j + (1 - \omega_j)\bar{\beta},
\end{align*}$$

where the question-specific weight, $\omega_j$, is

$$\begin{align*}
    \omega_j = \frac{\mathop{\mathrm{\mathbb{V}ar}}[\hat{\beta}_j] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_j}^2]}{\mathop{\mathrm{\mathbb{V}ar}}[\hat{\beta}_j] - \mathop{\mathrm{\mathbb{E}}}[\text{SE}_{\hat{\beta}_j}^2] + \text{SE}_{\hat{\beta}_j}^2}.
\end{align*}$$

The shrunk estimator puts more weight on position effects that are more precisely estimated, as measured by a low standard error of $\hat{\beta}_j$, $\text{SE}_{\hat{\beta}_j}^2$.

The fourth measure estimates the position effect separately for questions with a below/above median fraction of correct responses. The fifth measure estimates the effect separately for each academic subject. These measures assume that the effect of a one-position increase on performance is homogeneous within a type of question.

Appendix Table 27 illustrates these steps in calculating the difficulty of item #11898. Appendix Figure 17 shows the cross-question correlation between the measures of question difficulty. Reassuringly, all difficulty measures are highly correlated, with coefficients ranging from 0.77 to 0.99.

<div class="center">

<div id="tab:example-diff">

  ------------------------- ------------------- --------------------------- ------------ --
       Position effect       Average fraction     Position effect (in pp)     Question   
      estimation method      correct responses   $\times$ average position   difficulty  
            \(1\)                  \(2\)                   \(3\)               \(4\)     
            None                   0.36              0 $\times$ 64 = 0          0.36     
      Pooling all items            0.36          -0.08 $\times$ 64 = -5.1       0.41     
    Item-specific effect           0.36          -0.24 $\times$ 64 = -15.3      0.51     
     Shrinkage estimator           0.36          -0.24 $\times$ 64 = -15.3      0.51     
   By fraction corr. resp.         0.36          -0.15 $\times$ 64 = -9.6       0.45     
     By academic subject           0.36          -0.03 $\times$ 64 = -1.6       0.37     
  ------------------------- ------------------- --------------------------- ------------ --

  : Alternative measures of the difficulty of item #11898

</div>

</div>

<div class="singlespace">

*Notes:* This table illustrates how the six measures of question difficulty are calculated. The average fraction of correct responses and the average question position are calculated using the number of students with each booklet as weights.

</div>

<figure id="fig:matrix-diff-measures" data-latex-placement="H">
<embed src="../results/matrix-diff-measures.pdf" />
<p><em>Notes:</em> This figure shows the relationship between the different measures of question difficulty. Each cell shows the cross-question linear correlation between two measures of question difficulty. The sample size is <span class="math inline"><em>N</em> = 1, 842</span> across all cells.</p>
<figcaption>Cross-question correlation matrix of item difficulty measures</figcaption>
</figure>

[^1]: In particular, research shows that individual-level job performance tends to deteriorate over relatively short time spans. For example, over the course of a day: nurses are less likely to wash their hands (Dai et al., 2015; Steiny Wellsjo, 2023); doctors make more diagnostic mistakes (Linder et al., 2014; Kim et al., 2018); financial analysts make less accurate forecasts (Hirshleifer et al., 2019); and umpires make more incorrect calls in baseball games (Archsmith et al., 2023).

[^2]: I define potential experience as the individual's age minus years of schooling minus six. This measure approximates the number of years an individual could have been in the labor force, assuming they started school at age six and began working immediately after completing their education.

[^3]: Some high-school students take the ENEM more than two times in my sample, possibly due to grade repetition. I exclude a small fraction of students who take the ENEM more than three times.

[^4]: This index is analogous to the college quality measure used by Chetty et al. (2011) and Chetty, Friedman, and Rockoff (2014) to study the long-term impacts of kindergarten quality and teachers, respectively.

[^5]: Firms do not record the number of hours individuals actually work each week. Instead, the data on hours indicates the number of hours per week that workers are expected to work based on their contract.

[^6]: The CNPJ is a tax identifier for legally incorporated identities. The first eight digits identify the company. The rest of the digits identify the branch or subsidiary of the company.

[^7]: Not all questions appear in different positions across all booklets. Appendix Figure fig:hist-chg-pos shows the variation in question position across all questions for every pairwise booklet combination.

[^8]: These are mainly individuals who took the ENEM after graduating from high school. The results are very similar if I use my sample to measure question difficulty. The correlation between the measure of question difficulty estimated with test-takers in my sample and outside my sample is 0.98.

[^9]: The OLS formula reveals that $\hat{\beta}_i$ is computed as a weighted average of the deviations between student $i$'s performance on each exam question and $i$'s overall average performance (see Appendix 10.2). Thus, $\hat{\beta}_i$ captures the intuition that a student who consistently performs worse in the latter parts of the exam—relative to their average performance—has low cognitive endurance.

[^10]: For example, students who are proficient in natural science (which is tested on the first day) may not perform as well in language arts (tested on the second day). This variation can lead to an imperfect between-day correlation.

[^11]: Appendix Table 10 includes examples of reliability estimates for some well-known economic and psychological constructs. IQ is the construct with the highest known reliability, with correlations on the order of 0.80 (Hopkins and Bracht, 1975; Schuerger and Witt, 1989). Other commonly used constructs have a much lower temporal stability. For example, reliability estimates of risk aversion range 0.20–0.40 (Mata et al., 2018); big five personality range 0.49–0.70 (Wooden, 2012); self-regulation measures based on behavioral tasks range $-$0.091–0.665 (Enkavi et al., 2019); and teacher value-added range 0.23–0.47 (Chetty et al., 2014).

[^12]: This standard deviation of $\beta_i$ accounts for sampling error to avoid overstating the variability of true cognitive endurance. The standard deviation of the *estimate* of $\beta_i$, is $\sigma_{\hat{\beta}}$ = 14.4 percentage points. Because of sampling error in $\hat{\beta}_i$, this raw standard deviation overstates the variability of true latent $\beta_i$, $\sigma_{\beta}$. Following Angrist et al. (2017), I estimate $\sigma^2_{\beta}$ as $\hat{\sigma}^2_{\beta} =  \sigma^2_{\hat{\beta}} - \mathop{\mathrm{\mathbb{E}}}[\text{SE}^2_{\hat{\beta}}]$, where $\mathop{\mathrm{\mathbb{E}}}[\text{SE}^2_{\hat{\beta}}]$ is the average squared standard error of $\hat{\beta}_i$. I construct an analogous estimate for the standard deviation of latent ability, $\hat{\sigma}_{\alpha}$ (see Appendix 10.3 for details).

[^13]: For example, the estimates of endurance for individuals with $\hat{\alpha}_i \approx 0.50$ range from $\hat{\beta}_i = -0.50$ (a value in the bottom one percent of the endurance distribution) to $\hat{\beta}_i = 0.50$ (a value in the top one percent).

[^14]: For individuals with intermediate values of ability (for whom ceiling and floor effects are less likely to be binding), the correlation is negligible. For example, the correlation between the two measures is $-$0.08 for individuals with estimated ability between $0.50$ and $0.60$.

[^15]: These findings align with Brown et al. (2024), who report steeper performance declines among low-SES students compared to high-SES students (their Figure I, panels E-J), Black and Hispanic students compared to white students (their Figure I, panels A-B), and substantially higher endurance among students in high-quality schools (their Table VII), which in the Brazilian context would correspond to private schools.

[^16]: For students with a missing value for a control variable, I define the missing value as equal to the sample mean value and include a dummy for missing student characteristics in the regressions.

[^17]: These estimates are comparable to those in the literature. For example, Chetty, Friedman, and Rockoff (2014) estimates that a one SD increase in test scores is associated with a $5.5$ percentage point increase in college enrollment at age 20, a $7.8$ percent increase in college quality as measured by the earnings of previous graduates, and an $11.9$ percent increase in earnings at age 28 (see their Appendix Table 3, row 2).

[^18]: Two important caveats should be noted with this approach to measuring the value of endurance. First, individuals may select into occupations partly based on their endurance. Second, an increase in productivity may not necessarily lead to a corresponding increase in wages in some occupations or industries due to institutional factors (e.g., collective bargaining).

[^19]: This is analogous to what some college degrees in Brazil already do with the scores of the four subjects tested in the ENEM. For example, engineering programs tend to put a higher relative weight on the math score of the exam than on the other subjects.

[^20]: For changes in the SAT, see "[No More No. 2 Pencils: The SAT Goes Fully Digital](https://www.nytimes.com/2024/03/08/us/sat-online-digital-test-college.html)," Dana Goldstein, *The New York Times*, March 8, 2024. For changes in the ACT, see "[The ACT Just Announced Major Changes: What You Need to Know](https://www.forbes.com/sites/christopherrim/2024/07/24/the-act-just-announced-major-changes-what-you-need-to-know/)," Christopher Rim, *Forbes*, July 24, 2024.

[^21]: While research in this area is in its infancy, some examples of protocols that build cognitive endurance include mindfulness meditation (Levy et al., 2012; Goleman and Davidson, 2017), spending time engaging in cognitively-effortful activities (Brown et al., 2024), and the restriction of smartphones in learning environments (Thornton et al., 2014). Some of these protocols are already being implemented in the private sector. For example, meditation practices are commonly used among tech companies in Silicon Valley to enhance worker productivity (Shachtman, 2013).

[^22]: There is no penalty for incorrectly answering a question. Therefore, this evidence is only suggestive since leaving a question unanswered is a weakly dominated strategy.

[^23]: The test preparation information comes from the question "Did you attend or are you attending an entrance exam preparation course?" (*Frequentou ou frequenta curso preparatório para vestibular* in Portuguese), which was available in the ENEM questionnaire for the years 2009, 2010, 2011, 2013, and 2014.

[^24]: Researchers often divide standardized tests into two types: reasoning tests and achievement tests. Reasoning tests measure a student's verbal reasoning, critical reading, and skills. Achievement tests measure a student's mastery of specific subjects, like biology or physics. In practice, performance on both types of tests is highly correlated (Soares, 2015).
