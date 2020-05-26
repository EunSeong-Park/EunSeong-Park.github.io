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

## Test of Population Mean
이제, 우리는 population mean에 대한 추측이 옳은지 아닌지를 검증해볼 것이다. Population은 normal하다고 가정할 것이다.

물론 아래의 방법들은 대부분 population mean에만 국한된 방법이 아니다. Population mean에 대한 가설을 검증하면서, 검증을 위한 여러 기법을 살펴보도록 하자.

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

Two-tailed test는 $frac{\alpha}{2}$를 사용함을 알아두자.

#### Example

> A medical investigation claims that the average number of infections per week at a hospital in southwestern Pennsylvania is 16.3. A random sample of 10 weeks had a mean number of 17.7 infections. The sample standard deviation is 1.8. Is there enough evidence to reject the investigator's claim at α= 0.05? Assume the variable is normally distributed.

- $H_0: \mu = 16.3$ (claim)
- $H_1: \mu \ne 16.3$
- Given: $n=10$, $\bar{X}=17.7$, $\alpha = 0.05$$

먼저, critical t-value를 알아보자. DoF가 $9$, two-tailed test이므로 $\frac{\alpha}{2}=0.025$를 사용하면, CV는 $\pm 2.262$가 나온다.

이제 test-value를 $t$로 치환해보자. 

$t = \frac{\bar{X} - \mu}{\frac{S}{\sqrt{n}}}$ $= \frac{17.7-16.3}{\frac{1.8}{\sqrt{10}}} = 2.46$ 

이는 critical region 내부에 있으므로, 우리는 claim, $H_0: \mu = 16.3$을 기각할 수 있다.

## population proportionhogogog
