---
title: "[Data Science Programming 7] Statistical Testing"
tags: Data-Science Statistics Python
toc: true
---

# Intro
EDA와 달리, 이제 주어진 샘플을 통해 모집단의 특성을 **추론(inference)**하는 과정을 진행해볼 것이다. 하지만 결국 "추론"이기 때문에 항상 완전히 들어맞지는 않을텐데, 이를 어떻게 확인하고 검증하면 좋을까?


# Statistical Testing
## Hypothesis
**가설(hypothersis)**은 population parameter에 대한 추측이자 가정을 의미한다. 하지만 당연히 아무말이나 내뱉는다고 다 가설이 되는 건 아니고, 보통은 전체 모집단에 대한 무작위 샘플(random sample)을 사용하는 걸 전제로 한다. 최홍만 한명 뽑았다고 대한민국 평균 키가 $217\;cm$는 아니잖아?

아무튼, 이렇게 세운 가설이 타당한지 검증하는 과정이 꼭 필요하다. 말 같지도 않은 소리를 걸러내기 위해.. 이러한 검증 과정을 **Hypothesis testing**이라고 한다.

## Random Sample Basics
**무작위 샘플(random sample)**은 모집단으로부터 뽑아낸 IID 확률 변수의 집합이다. 즉,

- $X_1, X_2, \cdots X_n$는 서로 독립이다.
- 임의의$x \in mathbb R$에 대하여 $p_{X_1}(x) = \cdots = p_{X_n}(x)$

Sample statistic과 population parameter 사이엔 어느 정도 관련이 있다. 

### Sample Mean
**Sample mean**($\bar X$)은 말 그대로 뽑아낸 샘플의 평균이다. 샘플을 무작위로 추출해서 얘도 확률 변수의 일종이다. 즉, mean, variance 등을 구할 수 있는데,

$$ E(\bar X ) = \mu $$

$$ Var(\bar X) = \frac{\sigma^2}{n}$$

증명은 생략한다. 다 배운 내용이니까!

### Sample Variance
**Sample variance**($S^2$)는 자유도를 고려하여 다음과 같이 정의할 수 있다.

$$\sum_{k=1}^n \frac{1}{n-1}(X_k - \bar X)^2$$

적당히 식을 정리해보면, $E(S^2) = \sigma^2$라는 사실을 알 수 있다.

### Central Limit Theorem
**CLT**는 샘플링에서 매우 유용하고 중요한 정리다.

> IID RV의 집합 {$X_1,X_2,\cdots,X_n$}이 $E(X) = \mu$, $Var(X) < \sigma^2 < \infty$를 만족한다고 가정하자. $n \to \infty$인 상황에서 sample mean, $\bar X$는 원래의 분포에 관계없이 $\mathcal{N}(\mu, \frac{\sigma^2}{n})$에 수렴한다.

## Hypothesis Testing
이제 가설 검정을 해볼 수 있겠다! 우선, 두 종류의 가설을 생각해보자.

- **Null hypothesis** ($H_0$): A statement in which no difference or effect is expected from conventional knowledge
- **Alternative hypothesis** ($H_1$): Opposite of $H_0$.

예외가 있지만, 일반적으로 $H_0$은 기각을 위해 세운다. $H_0$을 기각하고 $H_1$을 채택하면서 우리가 의도하는 가설을 입증한다. [예전 글](https://eunseong-park.github.io/2020/04/25/Statistics-5-Statistical-Hypothesis.html)에 대충 정리해놔서 자세한 설명은 생략한다.

러프한 예시를 들어보자. 전 세계 평균 체중이 $62\;kg$라고 하는데, 어떤 연구자가 $1,000,000$명을 샘플링해서 확인해보니 평균 체중이 $95\;kg$이 나왔다. 그렇다면 다음과 같은 가설을 세울 수 있을 것이다.

- $H_0: \mu = 62$
- $H_1: \mu > 62$ (Claim)

직관적으로 보면, 샘플은 $H_0$를 기각하기 위한 strong evidence처럼 보인다. 그런데 여기서, strong하다는 기준이 뭘까? 어떤 증거가 얼마나 strong한 걸까?

### Significance Level
다음과 같은 상황들을 생각해볼 수 있다.

/ | Real $H_0$ | Real $H_1$
---|---|---
**Decision** $H_0$ | Correct | Type II error
**Decision** $H_1$ | Type I error | Correct

여기서 우리가 주목할 곳은 Type I error다. 왜냐? 보통 우리는 $H_1$을 채택하기 위해 가설을 여차저차 세우고, 그 가설이 맞기를 바라는데, 실제로 $H_0$이 맞는 상황은 바람직하지 않기 때문이다. 우리는 **significance level**, $\alpha$를 그러한 Type I error를 발생시킬 확률로 정의할 것이다. 

우리는 어떤 $\alpha$를 기준으로, 그것보다 낮을 경우 $H_0$을 기각하고 $H_1$을 채택할 것이다.

이제 그걸 어떻게 측정하느냐? [여기](https://eunseong-park.github.io/2020/04/25/Statistics-5-Statistical-Hypothesis.html#hypothesis-test)에 정리해놓았다.



