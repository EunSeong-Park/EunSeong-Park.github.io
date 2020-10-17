---
title:  "[Statistics 5] Statistical Hypothesis"
tags: Statistics
toc: true
---

# Intro
흠

# Statistical Hypothesis
__Statistical hypothesis__ 란, population parameter에 대한 추측(conjecture)이다. 일단은 가설이기 때문에, 추측은 맞을 수도 있고 틀릴 수도 있다.

Statistical hypothesis는 크게 두 종류로 나누어 볼 수 있다. 한국어로 귀무가설(__null hypothesis__)과 대립가설(__alternative hypothesis__)이라고 하는 것 같다. 

- Null hypothesis($H_0$): 기각을 위해 세우는 가설. Parameter와 어떤 값에 유의미한 차이가 없다고 추측한다.
- Alternative hypothesis($H_1$): null hypothesis에 대립되는 가설. Parameter와 어떤 값, 혹은 두 parameter간 유의미한 차이가 있다고 추측한다.

우리는 귀무가설을 먼저 세우고 검증하지만, 보통 실제로 입증하고자 하는 가설은 대립가설이다. 우리가 해야 하는 일은 간단하다. 어떤 parameter에 대하여, $H_0$을 기각(reject)하고, $H_1$을 채택(accept)할 수 있는지 확인하는 것이다.

## Example
각 상황에서 $H_0$과 $H_1$이 무엇인지 각각 확인해보자.

> A researcher thinks that if expectant mothers use vitamin pills, the birth weight of the babies will increase. The average birth weight of the population is 8.6 pounds.

- $H_0$: $\mu = 8.6$
- $H_1$: $\mu > 8.6$

> An engineer hypothesizes that the mean number of defects can be decreased in a manufacturing process of USB drives by using robots instead of humans for certain tasks. The mean number of defective drives per 1000 is 18.

- $H_0$: $\mu = 18$
- $H_1$: $\mu < 18$

> A psychologist feels that playing soft music during a test will change the results of the test. The psychologist is not sure whether the grades will be higher or lower. In the past, the mean of the scores was 73.

- $H_0$: $\mu = 73$
- $H_1$: $\mu \ne 73$

## Level of Significance
### Statistical Error
가설을 세우고 검증하는 과정에서, 통계적 오류(statistical error)가 발생할 수 있다.

- Type I error: false-positive. 실제로 $H_0$이 참이지만, 이를 기각한 경우.
- Type II error: false-negative. 실제로 $H_0$이 거짓이지만, 이를 채택한 경우.

### Level of Significance
유의 수준(level of significance)은 귀무가설, 참인 $H_0$을 기각할 오류를 범할 최대 확률을 의미한다. 즉, type I error가 발생할 확률이다. 이 값을 $\alpha$로 나타내도록 하자.

이제 critical region과 noncritical region에 대해 알아보자. 전자의 경우, 검사하려는 값이 안에 있을 경우 $H_0$이 기각되도록 하는 영역이고, 후자의 경우, 안에 있을 경우 $H_0$이 기각되지 않도록 하는 영역이다. 또, 그 두 영역의 경계를 CV(Critical Value)라고 한다.

우리가 해야 할 일은, test value가 있는 영역이 critical인지 noncritical인지 확인하고, 그에 따라 $H_0$의 채택/기각 여부를 결정하는 것이다.

## Hypothesis Test
이제, 우리는 population mean에 대한 추측이 옳은지 아닌지를 검증해볼 것이다. Population은 normal하다고 가정할 것이다.

물론 아래의 방법들은 대부분 population mean에만 국한된 방법이 아니다. Population mean에 대한 가설을 검증하면서, 가설 검증을 위한 여러 기법을 살펴보도록 하자.

### z-test
z-test는 population mean에 대한 statistical test다. 이는 population standard deviation($\sigma$)이 알려져 있을 때 사용할 수 있다.

$Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}}$

위 standard normal RV가 $z_{\alpha}$에 의해 주어질 critical region 내에 들어가는지의 여부를 판단하고, $H_0$의 기각 여부를 결정한다.

#### Example

> In Pennsylvania the average IQ score is 101.5. The variable is normally distributed, and the population standard deviation is 15. A school superintendent claims that the students in her school district have an IQ higher than the average of 101.5. She selects a random sample of 30 students and finds the mean of the test scores is 106.4. Test the claim at α= 0.05.

- $H_0: \mu = 101.5$
- $H_1: \mu > 101.5$ (claim)
- Given: $\alpha = 0.05$, $\bar{X} = 106.4$, $n=30$, $\sigma = 15$

Critical value는 $z_\alpha = z_{0.05} = 1.645$다. Critical region은 $P(Z > z_\alpha) = 100(1-\alpha)$를 만족하는 영역이다. 

$Z = \frac{106.4 - 101.5}{\frac{15}{\sqrt{30}}}$ $= 1.789$이므로, $Z$는 critical region 내에 있다. 즉, $H_0$을 기각하고, $H_1$(claim)을 채택한다.

> The Medical Rehabilitation Education Foundation reports that the average cost of rehabilitation for stroke victims is 24,672 dollars. To see if the average cost of rehabilitation is different at a particular hospital, a researcher selects a random sample of 35 stroke victims at the hospital and finds that the average cost of their rehabilitation is 26,343 dollars. The standard deviation of the population is 3251 dollars. At α= 0.01, can it be concluded that the average cost of stroke rehabilitation at a particular hospital is different from 24,672 dollars?

- $H_0: \mu = 24672$
- $H_0: \mu \ne 24672$ (claim)
- Given: $\alpha = 0.01$, $\bar{X}=26343$, $n=35$, $\sigma = 3251$

$CV = \pm z_{\frac{\alpha}{2}}$다. 왜냐? 그래야 $P(Region) = \alpha$가 나오기 때문이다. 아무튼, 그래서 $z_{\frac{\alpha}{2}} = 2.58$이고, 따라서 CV는 $\pm 2.58$이다. 그에 따라 critical region은 절댓값이 $2.58$보다 큰 영역이다. 이제 test value, $Z$를 계산해보자.

$Z= \frac{26343-24672}{\frac{3251}{\sqrt{35}}} = 3.04$

$Z$는 critical region 내에 있고, 그에 따라 $H_0$을 기각하며 $H_1$을 채택한다.

### P-value Test
P-value(Probability value)는 귀무가설($H_0$)이 참임을 가정하였을 때, sample이 어떤 sample statistic, 혹은 그보다 더 극단적인(extreme) 값이 나올 확률을 의미한다. 여기서 극단적이라 함은 대립가설을 지지하는 방향임을 의미한다.

어떤 ($H_0$을 지지하지 않는) statistic이 관측되었을 때, 이것이 population에서 샘플링을 했을 때 나올 가능성이 높은 statistic이라면 우리는 $H_0$을 잘 받아들일 수 있다. 하지만 그 statistic이 나올 가능성이 희박하다면, 우리는 $H_0$을 의심하게 된다. 예를 들어, 당첨 확률이 $0.001%$인 복권을 100장 샀는데 전부 당첨되었다면, 이게 우연의 일치라고 생각하고 넘기기 보다는, 복권의 시스템이나 당첨 확률 자체를 의심하게 되는 것과 같은 맥락이다.

예를 들어, 평균 100에 표준 편자가 20인 population에서 샘플링을 했더니 sample mean이 99.9998이었다? 이것은 population과 가까운 값이므로 충분히 그럴 수 있다고 느껴진다. 즉, 그 statistic이 등장할 확률이 높다고 본다. 하지만 sample mean이 999999였다? 우리의 선택지는 두 가지다.

- "아, 정말 극악의 확률로 저런 sample mean이 나왔구나!"
- "왜 저렇게 가능성이 낮은 sample mean이 나왔지? 혹시 추측한 population mean(100)이 잘못된건가?"

우리는 여기서 후자와 같이 생각한다. _"관측된 sample mean이 (우리가 세운 가정 하에선) 등장할 확률이 낮으니, 이 귀무가설은 기각되어야 한다"_ 라고 생각하는 것이다. 그리고 그 확률을 우리는 P-value라고 부른다.

달리 말하면, P-value는 관측된 sample이 귀무가설과 양립하는 정도를 의미한다. 그 값이 작을 수록 둘이 양립하지 못함을 의미하므로, P-value가 어느 수준 이하라면 귀무가설을 기각한다. 우리는 그 기준을 $\alpha$로 정한다.

- $P-value \le \alpha$: Reject $H_0$
- $P-value > \alpha$: Do not reject $H_0$

그리고 P-value는 $P(X > TestValue)$와 같은 방식으로 계산된다. 이것의 계산은 standard normal RV로의 치환을 수반한다. 즉, population standard deviation, $\sigma$의 값을 알고 있어야 한다.

#### Example

> A researcher claims that the average wind speed in a certain city is 8 miles per hour. A sample of 32 days has an average wind speed of 8.2 miles per hour. The standard deviation of the population is 0.6 mile per hour. At α= 0.05, is there enough evidence to reject the claim? Use the P-value method.

- $H_0: \mu = 8$ (claim)
- $H_1: \mu \ne 8$
- Given: $n=32$, $\bar{X}=8.2$, $\alpha = 0.05$, $\sigma = 0.6$

문제를 잘 읽자. 귀무가설이 claim이고, 우리는 이를 기각하기 위한 증거를 찾아야 한다. 그래서 관측된 statistic, sample mean이 주어졌고, 우리는 이게 기각을 위한 증거로 충분한지를 판단하면 된다.

어떻게? Test value(sample mean)로부터 P-value를 계산해, 그것이 alpha보다 큰지 작은지 확인한다.

먼저, Test value를 $z$로 치환한다.

$z = \frac{8.2 - 8}{\frac{0.6}{\sqrt{32}}} = 1.886$

이제, 이를 바탕으로 P-value를 계산한다. Two-tailed test이므로, P-value는 다음과 같다.

$P-value = 2P(Z > 1.886)$ $=0.0588 > \alpha$

즉, $H_0$을 채택하고, 관측된 sample mean은 $H_0$을 기각하기 위한 충분한 증거가 될 수 없다.

### t-Test
위의 두 방법과 달리, t-test는 population variation을 모를 때 사용된다. z-test와 비슷한 방식으로, $t$값이 critical region에 있는지 확인하여 $H_0$의 기각 여부를 결정한다.

알고 있겠지만, $DoF(=n-1)$와 $\alpha$에 따른 $t$값은 t-table을 통해 찾을 수 있다. 이를 통해 test type에 따른 critical t-value를 찾을 수 있다.

$\alpha$ | $n$ | Test type | | DoF | CV
---|---|---|---|---|---
0.05 | 16 | right-tailed | | 15 | $1.753$
0.01 | 23 | left-tailed | | 22 | $-2.508$
0.10 | 19 | two-tailed | | 18 | $\pm 1.734$

Two-tailed test는 $\frac{\alpha}{2}$를 사용함을 알아두자.

#### Example

> A medical investigation claims that the average number of infections per week at a hospital in southwestern Pennsylvania is 16.3. A random sample of 10 weeks had a mean number of 17.7 infections. The sample standard deviation is 1.8. Is there enough evidence to reject the investigator's claim at α= 0.05? Assume the variable is normally distributed.

- $H_0: \mu = 16.3$ (claim)
- $H_1: \mu \ne 16.3$
- Given: $n=10$, $\bar{X}=17.7$, $\alpha = 0.05$$

먼저, critical t-value를 알아보자. DoF가 $9$, two-tailed test이므로 $\frac{\alpha}{2}=0.025$를 사용하면, CV는 $\pm 2.262$가 나온다.

이제 test-value를 $t$로 치환해보자. 

$t = \frac{\bar{X} - \mu}{\frac{S}{\sqrt{n}}}$ $= \frac{17.7-16.3}{\frac{1.8}{\sqrt{10}}} = 2.46$ 

이는 critical region 내부에 있으므로, 우리는 claim, $H_0: \mu = 16.3$을 기각할 수 있다.

## Population Proportion

$z = \frac{\hat{p}-p}{\frac{p(1-p)}{n}}$

이를 이용해 $\hat{p}$를 적절히 변형하여 사용할 수 있을 것이다. 예제나 풀어보자.

### Example

> A researcher claims that based on the information obtained from the Centers for Disease Control and Prevention, 17% of young people ages 2–19 are obese. To test this claim, she randomly selected 200 people ages 2–19 and found that 42 were obese. At α = 0.05, is there enough evidence to reject the claim?

- $H_0: p = 0.17$ (claim)
- $H_1: p \ne 0.17$
- Given: $n=200$, $\alpha = 0.05$, $\hat{p} = 0.21$

#### Using z-Test

$2P(Z > z_{\frac{\alpha}{2})} = \alpha$

위 식을 만족하는 $z_{\frac{\alpha}{2}}$는 $1.96$이다. 즉 CV는 $\pm 1.96$이다. 이제 test value를 계산해보자.

$z = \frac{\hat{p} - p}{\sqrt{frac{p(1-p)}{n}}} = 1.51$

이는 critical region 밖에 있으므로, 가설을 기각하기 위한 충분한 증거가 될 수 없다.

#### Using P-value Test
P-value를 통해 가설을 검증해보자. Two-tailed test고, test value는 앞서 구했으므로,

$P-value = 2P(Z > test) = 2P(Z > 1.51) = 0.0656$

이는 $\alpha(=0.05)$보다 크므로, 가설을 기각할 수 없다.

## Test Concerning Two Populations
우리는 앞서 하나의 population에 관한 가설만을 세우고, 검증해왔다. 하지만 두 population의 parameter를 비교하는 가설이 필요할 때도 있다.

- "남학생과 여학생의 수학 성적 평균은 같을까?"
- "미국 사람과 러시아 사람의 평균 키는 누가 더 클까?"

...와 같은 예시가 두 population의 parameter를 필요로 하는 케이스다.

우리는 이제부터 두 normal population에 대한 가설에 대해 살펴볼 것이다.

### Equality of Means (1)
다음과 같은 가설을 생각할 수 있다.

- $H_0: \mu_x = \mu_y$
- $H_1: \mu_x \ne \mu_y$

만약 각 population의 sample에 대하여, $\bar{X}$와 $\bar{Y}$가 충분히 멀리 있다면, 가설을 기각해도 될 것처럼 보인다. 즉, 적당한 $c$를 잡아, $\vert \bar{X}-\bar{Y}\vert \ge c$일 때 $H_0$을 기각하고, 그렇지 않다면 기각하지 말자는 아이디어다.

여기서 중요한 점은, population은 normal하다는 가정이다. 즉, 우리는 $\bar{X}-\bar{Y}$에 대해 다음과 같은 특성을 생각해볼 수 있다. $n$은 $x$에 대한 sample size, $m$은 $y$에 대한 sample size다.

- $E(\bar{X}-\bar{Y}) = \mu_x - \mu_y$
- $Var(\bar{X}-\bar{Y}) = \frac{\sigma_x^2}{n} + \frac{\sigma_y^2}{m}$

그럼, 자연스럽게 $\bar{X}-\bar{Y}$를 standardize할 수 있다.

$ \frac{\bar{X}-\bar{Y} - (\mu_x - \mu_y)}{\sqrt{\frac{\sigma_x^2}{n} + \frac{\sigma_y^2}{m}}} $

이럼으로써, 우리는 $ \frac{\bar{X}-\bar{Y}}{\sqrt{\frac{\sigma_x^2}{n} + \frac{\sigma_y^2}{m}}} $이라는 하나의 TS(Test Statistic)만을 생각하면 된다. 물론 이 또한 standard normal distribution을 따를 것이다. 우리는 $\mu_x - \mu_y != 0$을 alternative hypothesis로 세웠으므로, TS에 대한 two-tailed test를 생각해볼 수 있다.

$P(\|Z\|\ge z_{\frac{\alpha}{2}} = 2P(Z\ge z_{\frac{\alpha}{2}}) = \alpha$

여기서 $\|TS\| \ge z_{\frac{\alpha}{2}}$면, (귀무)가설을 기각하기에 충분하다고 볼 수 있다. 예제를 통해 연습해보자.

#### Example

> A study using two random samples of 35 people each found that the average amount of time those in the age group of 26–35 years spent per week on leisure activities was 39.6 hours, and those in the age group of 46–55 years spent 35.4 hours. Assume that the population standard deviation for those in the first age group found by previous studies is 6.3 hours, and the population standard deviation of those in the second group found by previous studies was 5.8 hours. At α = 0.05, can it be concluded that there is a significant difference in the average times each group spends on leisure activities?

- $H_0: \mu_x = \mu_y$
- $H_1: \mu_x \ne \mu_y$ (claim)

26-35 그룹과 46-55 그룹, 두 개의 population이 있다. 이들은 각각 다음과 같은 상황이다.

/ | 26-35 | 46-55
---|---|---
$n$ | 35 | 35
$\bar{X}$ | 39.6 | 35.4
$\sigma$ | 6.3 | 5.8

그리고 $\alpha=0.05$다.

Test value가 critical region 내에 있는지 확인해보자. $\frac{\alpha}{2} = 0.025$이므로, $z_{\frac{\alpha}{2}} = 1.96$, 즉, CV는 $\pm 1.96$이다. Test value, $z$는 다음과 같다.

$z = \frac{(39.6-35.4)- (0)}{\sqrt{\frac{(6.3)^2}{35} + \frac{(5.8)^2}{35}}} = 2.9$

즉, 이는 critical region 내부에 있고, 우리는 claim을 채택할 수 있다.

P-value test로도 해보자.

$P-value = 2P(Z > 2.9) = 0.0038 < \alpha$

즉, $H_1$을 채택할 수 있다.

이에 더해, 여기서 $95%$ confidence interval도 구해보자. 이전에 구해왔던 방식과 동일하게 구하면 된다.

$(\bar{X} - \bar{Y}) \pm z_{\frac{\alpha}{2}} \sqrt{\frac{\sigma_x^2}{n} + \frac{\sigma_y^2}{m}}$

이를 계산하면 다음과 같다.

$1.363 < \mu_1 - \mu_2 < 7.037$

우리는 여기서, confidence interval이 0을 포함하는지 여부를 통해 $H_0$의 기각 여부를 판단할 수도 있다. 0이 포함되어 있지 않다면 기각을, 포함되어 있다면 $H_0$을 채택한다.

### Equality of Means (2)
이번엔 두 population의 두 standard deviation($\sigma$)를 모르는 상황을 생각해보자. 우리는 $n_1 \ge 30, n_2 \g2 30$일 때, test value에서 $sigma$를 sample standard deviation, $S$로 치환하여 사용할 수 있다. 즉,

$TestValue = \frac{\bar{X_1} - \bar{X_2}}{\sqrt{\frac{S_1^2}{n_1} + frac{S_2^2 }{m}}}$

#### Example

> To test the effectiveness of a new cholesterol-lowering medication, 100 volunteers were randomly divided into two groups of size 50 each. Members of the first group were given pills containing the new medication, while members of the second, or control, group were given pills containing lovastatin, one of the standard medications for lowering blood cholesterol. All the volunteers were instructed to take a pill every 12 hours for the next 3 months. None of the volunteers knew which group they were in. Suppose that the result of this experiment was an average reduction of 8.2 with a sample variance of 5.4 in the blood cholesterol levels of those taking the old medication, and an average reduction of 8.8 with a sample variance of 4.5 of those taking the newer medication. Do these results prove, at the 5 percent level, that the new medication is more effective than the old one?

- $H_0: \mu_x = \mu_y$
- $H_1: \mu_x > \mu_y$ (claim)

/ | 26-35 | 46-55
---|---|---
$n$ | 50 | 50
$\bar{X}$ | 8.8 | 8.2
$S^2$ | 4.5 | 5.4

$TestValue = \frac{\bar{X_1} - \bar{X_2}}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2 }{m}}} = \frac{8.8 - 8.2}{\sqrt{\frac{4.5}{50} + \frac{5.4}{50}}} = 1.3484$

P-value 테스트를 해보자.

$P = P(Z > 1.3484) = 0.085 > 0.05(\alpha)$

즉, $H_0$을 채택하고, $H_1$을 기각한다.

### Equality of Means (3)
Population standard deviation을 모르는 위의 상황에서, 우리는 각각의 샘플 사이즈가 충분히 크다고 가정하고 위의 공식을 사용하였다. 그렇다면 샘플 사이즈가 작다면 어떨까? 두 sample standard deviation에 따라 가능한 두 케이스가 있다.

1. $s_1$, $s_2$의 값이 비슷하다. ($\frac{s_1^2}{s_2^2} < 3$ where $s_1 > s_2$)
2. $s_1$, $s_2$의 값이 비슷하지 않다. ($\frac{s_1^2}{s_2^2} \ge 3$ where $s_1 > s_2$)

1번의 경우를 pooled하다고 하며, population standard deviation을 같다고 가정한다. 그렇다면 다음과 같이 confidence interval과 test statistic을 계산할 수 있다.

$CI: (\bar{X_1} - \bar{X_2}) \pm t_{DoF, \frac{\alpha}{2}} s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$, where $DoF = n_1+n_2 - 2$

$TestValue: t = \frac{\bar{X_1} - \bar{X_2}}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$

$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2-1)s_2^2}{n_1+n+2 -2}}$

2번의 경우는 nonpooled하다고 하며, 다음과 같은 방식으로 CI와 test statistic을 계산한다.

$CI: (\bar{X_1} - \bar{X_2}) \pm t_{DoF, \frac{\alpha}{2}} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$, where $DoF = min(n_1 - 1, n_2 - 1)$

$TestValue: t = \frac{\bar{X_1} - \bar{X_2}}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$

어우 많이 복잡해졌다.. 예제를 풀며 익숙해져보자.

#### Example

> A researcher wishes to see if the average weights of newborn male infants are different from the average weights of newborn female infants. She selects a random sample of 10 male infants and finds the mean weight is 7 pounds 11 ounces and the standard deviation of the sample is 8 ounces. She selects a random sample of 8 female infants and finds that the mean weight is 7 pounds 4 ounces and the standard deviation of the sample is 5 ounces. Can it be concluded at α = 0.05 that the mean weight of the males is different from the mean weight of the females? Assume that the variables are normally distributed.

- $H_0: \mu_x = \mu_y$
- $H_1: \mu_x \ne \mu_y$ (claim)

/ | Male | Female
---|---|---
$n$ | 10 | 8
$\bar{X}$ | 7 lb 11 oz | 7 lb 4 oz
$S$ | 8 oz | 5 oz

$\frac{64}{25} = 2.56 < 3$이므로, pooled하다. Test value가 critical region에 들어가는지 확인해보자.

$\frac{\alpha}{2} = 0.025$, $DoF = 10+8-2 = 16$이므로, $t_{DoF, \frac{\alpha}{2}} = 2.120$이다. Critial region은 $\pm 2.120$ 바깥의 영역이다.

$s_p = \sqrt{\frac{(10-1)8^2 + (8-1)5^2}{10+8-2}} = \sqrt{46.9375}$

$TestValue = \frac{123-116}{\sqrt{46.9375} \sqrt{\frac{1}{10} + \frac{1}{8}}} = 2.1540$

즉, test value는 critical region 내부에 있고, $H_1$, claim을 채택할 수 있다.

간단하게 P-value 테스트로도 해볼까?

$P = 2P(Z > 2.1540) < 0.025$

덤으로 $95$% confidence interval도 구해보자.

$CI: (\bar{X_1} - \bar{X_2}) \pm t_{DoF, \frac{\alpha}{2}} s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$, where $DoF = n_1+n_2 - 2$

이므로, 대입하면 $0.1105 < \mu_1 - \mu_2 < 13.8895$

이는 0을 포함하지 않으므로, $H_0$을 기각할 수 있다고 볼 수 있다.
