---
title:  "[Statistics 3] Random Variable"
tags: Statistics
toc: true
---

# Intro
지난 포스트에선 확률(probability)의 개념과 그 특성을 알아보았다. 예제를 전혀 풀지 않아서 빨리 넘어갔던 것 같다. 

이번엔 확률 변수(Random Variable, RV)에 대해 가볍게 알아보자.


# Random Variable (RV)
확률 변수(random variable)은 다음을 의미한다.

> A quantity whose value is determined by the outcome of probability experiment

풀어서 설명하자면, 확률적 시행으로 결정되는 값 정도로 볼 수 있다. 예를 들어, 주사위를 던지는 experiment에서, 주사위의 눈(1, 2, 3, 4, 5, 6)을 RV, $X$로 정의해볼 수 있다. 

RV는 "확률적 시행으로 결정된다"라는 조건만 만족하면 어떻게 정의하든 상관 없다. 주사위 던지기를 다시 생각해보자.

- 두 번 던져 나오는 눈의 합
- 한 번 던져 나오는 눈의 제곱
- 5가 나오면 0, 나머지는 1
- 무조건 0
- 한 번 던져 나오는 눈에 인접한 눈들의 합

모두 RV가 될 수 있다.

RV는 가질 수 있는 값의 성질에 따라 두 종류로 나눌 수 있다. 바로 RV가 이산적인(discrete) 경우와 연속적인(continuous) 경우다.

## Probability Notation
어떤 RV, $X$를 생각해보자. 우린 $X$가 특정한 값, $x_i$를 가질 확률에 관심이 있다. 예를 들어, 주사위의 눈을 $X$라 한다면, $X$가 1이나 3같은 특정한 값을 가질 확률을 구해야 한다. 혹은 특정한 값보다 크거나 작을 확률, 또는 그 값이 아닐 확률에 관심이 있을 수도 있다. 일반적으로 다음과 같은 노테이션을 사용한다.

> $P{X = x_i}$ : Probability that $X = x_i$

이를 변형하여 $P{X < x_i}$ 등의 부등식이나, set-builder notation을 이용하여 $P{X = x_i \vert x_i mod 5 = 3}$과 같은 표기를 할 수도 있다.


# Discrete RV
먼저, 이산적인(discrete) RV를 알아보자. Discrete RV는 이산적이기 때문에 그것의 분포(distribution)을 표로 나타낼 수 있다. 주사위 눈을 다시 생각해보자. 이는 다음과 같이 나타낼 수 있다.

$X$ | 1 | 2 | 3 | 4 | 5 | 6
---|---|---|---|---|---|---
$P(X = x_i)$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$

모든 경우의 확률의 합, 즉 sample space의 확률 $P(S)$는 1임을 기억하자.

## Expectation
Discrete RV, $X$의 기댓값(expectation, expected value)은 다음과 같이 정의된다.

> $E(X) = \sum_{i=1}^n x_iP(X=x_i)$

이것은 확률에 따른 RV의 weighted average로 볼 수 있다. 

Expectation은 이산적이든 연속적이든 대부분의 성질을 공유하므로, 여기서 expectation의 일반적인 성질을 알아볼 것이다.

### Properties
가장 중요한 기댓값의 성질은 선형성(linearity)이다. 우선, 임의의 상수 $c$에 대하여 다음을 만족한다.

- $E(cX) = cE(X)$
- $E(X + c) E(X) + c$

더욱 간단하게 나타내면 다음과 같다. 임의의 상수 $a, b$에 대하여...

$E(aX + b) = aE(X) + b$ 

또, 임의의 RV, $X_1, X_2, ..., X_n$에 대해 다음이 성립한다.

$E(X_1 + ... X_n) = E(X_1) + ... + E(X_n)$

선형성은 기댓값의 계산을 매우 편하게 만들어준다.

### Function of RV
어떤 RV, $X$에 대한 함수, $g(X)$를 생각해보자. $g(X)$의 기댓값은 다음과 같다.

> $E(g(X)) = \sum g(X_i)P(X = x_i)$

함수가 적용되면 확률은 유지된 채로 RV의 값만 달라진다고 생각하면 받아들이기 쉽다.

#### Example
주사위 눈의 제곱의 기댓값을 구해보자.

주사위 눈을 RV, $X$라고 하자. 우리는 눈의 제곱에 관심이 있으므로, $g(X) = X^2$으로 놓는다.

$E(g(X))$ $= \frac{1}{6}(1^2 + 2^2 + ... + 6^2)$ $= \frac{91}{6}$

## Variance
RV의 기댓값을 $\mu$라 하자. RV, $X$의 분산(variance)은 RV의 종류에 상관 없이 다음과 같이 정의된다.

> $Var(X) = E((X-\mu)^2)$

그리고 기댓값의 선형성을 이용하면 다음과 같이 쉽게 계산할 수 있다.

> $Var(X) = E(X^2) - \mu^2$

### Properties
우선, 분산의 정의에 의해 $Var(X) \ge 0$이다. 또, 정의에 의해 다음과 같은 식이 성립한다.

> $Var(aX + b) = a^2Var(X)$

위의 사실은 분산의 정의를 통해 쉽게 유도할 수 있다.

또, 두 RV, $X, Y$에 대해 다음이 성립한다.

> $Var(aX + bY)$ $= a^2Var(X) + b^2Var(Y) + 2abCov(X, Y)$

$Cov(X, Y)$는 $X$와 $Y$의 공분산(covariance)을 나타내고, 두 RV가 independent하다면 0이다. 즉,

> $Var(aX + bY)$ $= a^2Var(X) + b^2Var(Y)$ if $X$ and $Y$ are independent

## Standard Deviation
RV, $X$의 표준 편차(standard deviation)는 다음과 같이 정의된다.

> $SD(X) = \sqrt{Var(X)}$

Variance가 non-negative이므로, $SD(X)$ 또한 non-negative다. 


# Binomial RV
## Bernoulli's Trial
베르누이 시행(Bernoulli's trial)이란, 오직 두 outcome 중 하나를 얻는 시행을 의미한다. 두 사건을 각각 성공, 실패라고 하자.

베르누이 시행은 성공 확률 $p$에 의해 결정될 수 있다. 성공 확률이 $p$라면, 실패 확률은 자연스럽게 $1-p$다. 베르누이 시행의 예는 무엇이 있을까?

- 동전 던지기
- 주사위에서 5를 노리기

## Binomial RV
Binomial(이항) RV는 $n$회의 (일정한 확률의 독립적인) 베르누이 시행의 성공 횟수를 의미하는 discrete random variable이다. 이는 베르누이 시행의 횟수, $n$과 각 베르누이 시행의 확률, $p$에 의해 결정된다.

어떤 RV, $X$가 binomial하다면 $X \sim B(n, p)$와 같이 표현한다.

### Properties
베르누이 시행의 성공 횟수가 $i$일 확률, 즉, $P(X=i)$는 다음과 같다.

> $P(X = i)$ $=C(n, i)p^i(1-p)^{n-i}$

왜냐? 성공 횟수가 $i$면 각 시행은 독립이므로 $i$회 성공할 확률은 $p^i$다. 그에 따라 $n-i$회 실패할 확률은 $(1-p)^{n-i}$다.

또, 성공 횟수가 $i$인 사건은, 총 $C(n, i)$ 경우다($n$개의 시행 시퀀스에서 $i$개를 뽑는 것과 동일하므로). 

기댓값과 분산은 다음과 같다.

- $E(X) = np$
- $Var(X) = npq$

증명은 생략한다.


# Continuous RV
Continuous random variable은 possible value가 interval set에서 정의되는 RV다. 우리는 RV가 어떤 구간에 속할 확률을 continuous RV가 그리는 curve 아래의 면적을 통해 구할 수 있다. 즉,

$P(a \le X \e b)$: Area under curve between a and b.

![](/imgs/stat/s1.png)

## Properties
Axioms of probability에 의해, 해당 curve는 0 밑으로 떨어지지 않는다는 점, 모든 구간($S$)에 속할 확률은 1이므로 정의된 전체 영역에서의 면적은 1임을 알아두자.

Continuous RV도 discrete한 케이스와 거의 같은 성질을 공유한다. 다만 연속적이기 때문에 기댓값의 정의는 약간 수정되어야 한다.

$E(X) = \int_{D} xf(x) dx$

$D$는 해당 distribution이 정의된 영역, $x$는 continuous random variable, $f(x)$는 그것의 probability density function(PDF)다.

나머지 기댓값과 분산에 대한 성질은 이산적인 경우와 동일하다.

## Normal Random Variable
Normal random variable은 continuous RV의 대표적인 예시이자, 통계에서 매우 중요한 RV 중 하나다. Normal RV는 오직 두 parameter에 의해 결정된다. 바로 기댓값($\mu$)과 표준 편차($\sigma$)다. 즉, 다음과 같이 표현할 수 있다.

$X \sim N(\mu, \sigma)$

$\sigma$ 대신 $\sigma^2$, 분산을 사용하는 경우도 많다. 아마 고등학교 교과서에서도 그렇게 사용했을 것이다.

Normal distribution의 density function은 다음과 같이 정의된다.

$f(x) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

그리고 __standard normal random variable__ 은 normal random variable에서 $\mu = 0$이고, $\sigma = 1$인 특별한 경우고, 이는 RV $Z$로 표기한다.

### Properties
Normal RV의 density curve는 보통 모든 실수에서 정의되며 $x = \mu$에 대해 대칭이다. 또, $x=\mu$에서 최댓값을 가지며, 거기에 멀 수록 점점 작아지며 0에 수렴하는 bell-shape 형태를 가진다. 

Density curve는 $\mu$가 커질수록 전반적으로 위로 솟으며, $\sigma$가 커수록 전반적으로 퍼진다. 각 parameter가 의미하는 바를 생각하면 당연한 일이다.

서로 독립인 두 normal RV 사이에서, 기댓값과 분산은 additive property가 성립한다.

- $E(X+Y) = \mu_X + \mu_Y$
- $Var(X+Y) = \sigma_X^2 + \sigma_Y^2$
- $SD(X+Y) = \sqrt{\sigma_X^2 + \sigma_Y^2}$

### Finding Normal Probability
Normal RV의 density function은 식이 꽤 복잡해, 직접 영역을 구하기엔 어려움이 있다. 하지만 우리는 임의의 normal RV를 standard normal RV로 치환하는 방법을 사용할 수 있고, standard normal RV의 확률은 이미 잘 계산된 표(Z-table)가 있어, 이를 참고하여 확률을 구할 수 있다.

Z-table은 어떤 $z$에서의 cumulative probability를 나타낸다. 그림으로 표현하면 아래와 같다.

![](/imgs/stat/s4.png)

![](/imgs/stat/s2.png)

![](/imgs/stat/s3.png)

우리는 z-table과 적절한 계산을 통해 대부분의 normal RV에서의 대부분의 확률을 구할 수 있다.

### Percentiles of Normal RV
어떤 0과 1사이의 $\alpha$에 대하여, $z_{\alpha}$를 다음과 같이 정의한다.

$P(Z > z_{\alpha}) = \alpha$를 만족하는 $z_{\alpha}$

나중에 자주 쓰이니 알아두자.
