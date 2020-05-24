---
title:  "[Statistics 4] Sampling"
tags: Statistics
toc: true
---

# Intro
샘플링(sampling)은 통계에서 필수불가결한 요소다. 맨 처음에도 언급했지만, 샘플링은 population 전체를 조사하지 않고도 그것에 대한 정보를 얻기 위한 수단이다. 적절한 샘플링이란 무엇을 의미하며, 그러한 샘플링을 위해서라면 어떤 게 필요할까?


# Sample
두 용어를 다시 한 번 짚고 넘어가자.

- Statistic: A numerical quantity whose value is __determined by the sample__.
- Parameter: A numerical quantity who __describing the whole population.__

Sample mean, sample variance 등은 모두 statistic(통계량)에 속한다. 그중에서도, 우리는 sample mean에 주목할 것이다.

## Sample Mean
$X_1, X_2, ..., X_n$ population으로부터 추출한 샘플이라고 하자. 그렇다면 sample mean, $\bar{X}$는 다음과 같다.

$\bar{X} = \sum_{i=1}^n \frac{X_i}{n} $ 

우리는 샘플을 무작위로 추출하는 시행(experiment)에서, 각 sample의 sample mean을 random variable의 일종으로 볼 수 있다. 그렇다면, sample mean의 expectation, variance 등을 구할 수 있을 것이다.

Sample mean의 expectation, $E(\bar{X})$는 population mean, $\mu$와 같다. 그리고 sample mean의 variance, $Var(\bar{X})$는 population의 variance($\sigma^2$)에 샘플 사이즈를 나눈 값과 같다. 정리하면,

- $E(\bar{X}) = \mu$
- $Var(\bar{X}) = \frac{\sigma^2}{n}$
- $SD(\bar{X}) = \frac{\sigma}{\sqrt{n}}$

## Central Limit Theorem
앞서 우리는 sample mean을 random variable의 일종으로 보는 아이디어를 사용하여 그것의 expectation과 variance 등을 생각하였다. 그렇다면 마찬가지로 sample mean에 관한 확률을 계산할 수 있지 않을까?

우리는 central limit theorem을 이용하여, sample mean을 normal random variable로 근사시키는 방법을 사용할 것이다. Central limit theorem은 다음과 같다.

> As the sample size, n increases without limit, the shape of the distribution of the sample means taken with replacement from a population with mean $\mu$ and standarad deviation $\sigma$ will approach a normal distribution. This distribution will have a mean $\mu$ and a standard deviation $\frac{\sigma}{\sqrt{n}}$.

즉, sample mean을 어떤 normal distribution에 근사(approximate)시킬 수 있다. 또, 이것을 standard normal distribution으로 치환하면 Z-table을 이용해 그 값을 구할 수 있을 것이다.

물론, 이러한 근사는 샘플 사이즈가 적당히 커야 잘 근사된다. 보통 그 기준은 $n \ge 30$으로 본다. 하지만 조금 더 낮아도 approxmation이 꽤 유효한데, 심지어 $n$이 5여도 근사가 나름 잘 된다.

### Example

> Frequent fliers of a particular airline fly a random number of miles each year, having mean and standard deviation (in thousands of miles) of 23 and 11, respectively. As a promotional gimmick, the airline has decided to randomly select 20 of these fliers and give them, as a bonus, a check of $10 for each 1000 miles flown. Approximate the probability that the total amount paid out is between $4500 and $5000.

우리가 구하려는 대상은 total pay, $X_1 + X_2 + ... + X_{20}$이 450-500 사이에 있을 확률이다. 즉,

$P(450 \le X_1 + X_2 + ... + X_{20} \le 500)$

식 내부에 각각 $n=20$을 나누어주면 sample의 total pay는 sample mean이 된다.

$P(22.5 \le \bar{X} \le 25)$

이를 standard normal distribution으로 근사하기 위해, 식을 $\frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}}$의 형태로 약간 변형한다. 

$P(\frac{-0.5}{\frac{11}{\sqrt{20}}} \le \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} \le \frac{2}{\frac{11}{\sqrt{20}}})$

그리고 가운데의 $\frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}}$는 central limit theorem에 의해 standard normal random variable, $Z$로 근사될 수 있다. 이는 근사일 뿐, 같지는 않다는 사실을 기억하자.

$P(\frac{-0.5}{\frac{11}{\sqrt{20}}} \le Z \le \frac{2}{\frac{11}{\sqrt{20}}})$

### Binomial Distribution
Binomial distribution을 central limit theorem을 이용해 normal distribution으로 근사해보자. 왜 그런 짓을 하느냐? Binomial RV의 확률 계산을 쉽게 하기 위해서다.

우리는 확률이 $p$인 베르누이 시행들로 구성된 population을 생각해볼 수 있다. 그리고 각각의 베르누이 시행을 성공 확률이 $p$고, 성공 시 1, 실패 시 0의 값을 가지는 indicator random variable, $X_i$로 보자.

$E(X_i) = p고, Var(X_i) = p(1-p)$다. 이는 $n=1$인 binomial RV와 같기 때문이다. 이는 population의 mean과 variance와도 같다.

이제 이 population으로부터 크기가 $n$인 샘플을 추출할 것이다. $X_1, ..., X_n$이라 하자. 샘플에서 성공 횟수, 즉, $X_1 + ... + X_n$이 어떤 값 $x$를 가질 확률은 어떻게 될까?

$P(X_1 + ... + X_n = x)$

결국 이는 $X \sim B(n, p)$인 $X$에 대하여 $P(X = x)$를 구하는 과정과 같다. 그러니 $X_1, ..., X_n$를 그냥 $X$로 놓자. 여기서 우린 $\frac{X}{n}$을 sample mean으로 보아, 여기에 central limit theorem을 적용할 수 있다.

$\frac{\frac{X}{n} - p}{\sqrt{\frac{p(1-p)}{n}}}$ $= \frac{X-np}{\sqrt{np(1-p)}}$

음 조금 주저리주저리 적어놓은 것 같다

#### Correction for Continuity
확률이 density curve 아래의 영역으로 정의되는 continuous RV의 경우, 특정 값을 가질 확률이 0이다. 그래서, binomial RV를 normal RV로 근사할 때, continuity를 고려하여 적절히 확률식을 바꿔주어야 한다.

어떤 정수 $a$에 대한 확률은 interval $(a-0.5, a+0.5)$로 치환한다. 이는 부등식이 사용된 확률에도 동일하게 적용되며, 표로 정리하면 다음과 같다.

Binomial | Normal
---|---
$P(X = a)$ | $P(a-0.5 < X < a+0.5)$
$P(X \ge a)$ | $P(X > a-0.5)$
$P(X > a)$ | $P(X > a+0.5)$
$P(X \le a)$ | $P(X < a+0.5)$
$P(X < a)$ | $P(X < a - 0.5)$


# Estimation
## Estimator
__Estimator__ 는 샘플의 추출에 의존하는 statistic이다. 예를 들어, sample mean은 population으로부터 뽑는 샘플에 따라 그 값이 다를 수 있다. 그리고 __estimate__ 은 추정치의 특정한 값으로, population의 parameter를 예측하는 데 사용된다.

만약 estimator의 expectation이 우리가 추정하려는 population의 parameter와 같다면, 우리는 sample을 통해 parameter를 쉽게 추정할 수 있을 것이다. 이러한 estimator를 unbiased estimator라고 한다.

우리는 estimator를 이용해, population의 unknown parameter의 값을 추정하는 게 목표다. 그 방법으로 크게 point estimation과 interval estimation이 있는데, 우리는 후자를 중심으로 알아볼 것이다.

## Point Estimation
Point estimation이란, population의 특성, 즉 parameter를 어떤 하나의 값으로 추정하는 방법이다.

즉, "이 population의 parameter, a는 x의 값을 갖는다!"라고 추정하는 셈이다.

가장 간단한 예시는 샘플, $X_1, X_2, ..., X_n$으로부터 population의 mean을 추정하는($E(\bar{X}) = \mu$) 경우다. 이 땐, $\bar{X}$가 estimator의 역할을 하며, 이는 unbiased estimator다.

## Interval Estimation
Interval estimation은 어떤 구간에 대하여, 그 구간 내에 parameter가 존재할 확률을 구함으로써 추정하는 방식이다.

그렇게 parameter를 포함할 것으로 예측하는 데 사용하는 구간을 interval estimator of a population parameter라고 한다. 또, 그 구간에 parameter가 존재할 확률을 confidence level이라고 한다.

## Mean of Normal Population
우리의 목표는 어떤 normal population의 population mean, $\mu$를 추정하는 것이다.

### With Population Variance
$100(1-\alpha)$ percent confidence interval estimator는 다음과 같다.

$(\bar{X}-z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}, \bar{X}+z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}})$

즉, population mean을 포함할 확률이 $100(1-\alpha)$가 되도록 하는 구간을 의미한다. 우리는 $\sigma$가 population variance라는 점을 주목해야 한다. 즉, population variance를 알고 있어야 위와 같은 방식으로 confidence interval estimator를 구할 수 있다.

#### Example

> An electric scale gives a reading equal to the true weight plus a random error that is normally distributed with mean 0 and standard deviation σ =0.1 ounces. Suppose that the results of five successive weightings of the same object are as follows: 3.142, 3.163, 3.155, 3.150, 3.141. Determine a 99 percent confidence interval estimate of the true weight.

여기서 confidence level은 $99$%다. 따라서, $z_{\frac{\alpha}{2}} = z_{0.005} = 2.576$이다. 그에 따라 confidence interval estimate는...

$\bar{X} \pm {\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}$ $= 3.1502 \pm 2.56 * \frac{0.1}{\sqrt{5}}$

### Without Population Variance
앞서 언급하였듯, 위의 방법은 population variance를 모른다면 사용할 수 없다. 다른 방법을 찾아보자.

#### t-Distribution
어떤 크기 $n$의 샘플 $X_1, ..., X_n$에 대해, 다음과 같은 RV를 새로 정의한다. Sample mean은 $\bar{X}$, sample standard deviation은 $S$다.

$t_{n-1} = \frac{\bar{X}-\mu}{\frac{S}{\sqrt{n}}}$

이를 t-random variable with $n-1$ degrees of freedom이라고 한다. 좀 뜬금없어 보이지만, 나중에 다른 포스팅에서 알아보도록 하고, t-distribution을 따르는 RV, $T$에 대하여, $t_{DoF, \alpha}$는 다음을 만족하는 값이다.

$P(T > t_{DoF, \alpha}) = \alpha$

$z_{\alpha}$와 달리, 이는 upper-tail probability임을 유의하자. 이 값은 t-table에 잘 정리되어 있다.

![](/imgs/stat/s1.png)

#### Confidence Interval Estimator
이제, 이 값을 이용해 confidence interval estimator를 구할 수 있다.

$(\bar{X} - t_{DoF, \frac{\alpha}{2}} \frac{S}{\sqrt{n}}, \bar{X} + t_{DoF, \frac{\alpha}{2}} \frac{S}{\sqrt{n}})$

계산은 귀찮아서 못하겠다... 예제는 알아서 풀어보자.

## Population Proportion
어떤 population으로부터, 어떤 characteristic을 가지는 요소들의 비율, $p$를 생각해볼 수 있다. 그러한 관점에선, population을 그 characteristic을 가진 요소와 그렇지 않은 요소로 이분할 수 있다.

이번엔, interval estimation으로 population proportion, $p$를 추정해보자.

어떤 크기 $n$의 샘플에 대해, 해당 characteristic을 가진 요소의 수를 $X$라 하고, 샘플 내의 proportion을 $\hat{p}$라 하자. 그렇다면 다음이 성립한다.

- $\hat{p} = \frac{X}{n}$
- $X \sim B(n, p)$
- $E(\hat{p}) = p$
- $SD(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}$

그리고 $n$이 충분히 크다면($np$와 $n(1-p)$가 5보다 크다면), 우리는 normal approximation을 통해, $100(1-\alpha)$ percent confidence interval estimator of $p$를 다음과 같이 구할 수 있다.

$(\hat{p} - z_{\frac{\alpha}{2}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}})$


# 마치며
좀 길었다



