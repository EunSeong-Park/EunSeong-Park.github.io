---
title:  "[Statistics 1] Intro"
tags: Statistics
toc: true
---

# Intro
이번엔 통계학 기초를 복습하려고 한다! 시간이 남으니 별 걸 다 한다. 초중반의 내용은 고등학교 확률과 통계부터, 이산수학, 확률과 랜덤프로세스 개론까지 몇 번은 우려먹은 내용이다. 하지만 순서는 맞춰야 하니 처음부터 복습해보자. 이참에 혼동하기 쉬웠던 개념들을 확실히 짚고 넘어가면 좋을 듯 하다.

물론 내가 정리하기 싫은 부분은 뺀다.

이번엔 간단하고 넓은 통계 개념을 간단히 짚어보려 한다.

아무튼 통계도 열심히 공부해보자.


# Basic Statistics
## Population & Sample
__모집단(Population)__ 이란, 우리가 어떤 문제나 상황에서 관심을 가지고 있는 사건이나 대상의 집합이다. Population은 그 집단의 특성을 완전히 갖고 있지만, 때론 그 크기가 너무 커 조사 및 분석하는 데 어려움이 있다.

그래서 우리는 __표본(sample)__ . 즉, population의 부분 집합을 가져와 이를 대신 조사한다. 샘플이 의미를 가지려면, 샘플은 어느 정도 population의 특성을 반영해주어야 한다.

예를 들어, 미국인의 재산 수준을 알기 위해 몇 명을 대표로 샘플링(sampling)하여 조사했다고 하자. 그런데 뽑은 사람이 달랑 4명이고, 하필 뽑은 사람이 빌 게이츠, 워런 버핏, 트럼프, 주커버그였다면, 우리는 "미국 사람들은 다 억만장자다!"라고 결론지을 수 있을까? 이런 주장이 터무니없는 것처럼 들리는 이유는, 이렇게 뽑은 샘플은 population을 대표하지 못한다는 사실을 우리가 알고 있기 때문이다.

어떻게 뽑아야 의미 있고, 더 믿을만한지는 나중에 천천히 알아볼 것이다.

## Statistic
__통계량(statistic)__ 이란, (특히 샘플의) 데이터로부터 얻어지는 수치화된 값(numerical value)을 의미한다. 보통 statistic은 sample을, parameter는 population 전체를 설명하는 numeric value로 생각하는 듯하다.

우리는 세 종류의 통계량에 주목할 것이다.

### Sample Mean
__Sample mean__ , $\bar{x}$는 다음과 같이 정의된다.

$$\bar{x} = \frac{\sum_{k=1}^{n} x_k}{n}$$ $$= \frac{x_1 + x_2 + ... + x_n}{n}$$

말 그대로 표본의 평균이다.

### Deviations
__Deviation__ 은 sample mean과 특정 값 사이의 차이로 정의된다.

$x_i - x$

### Sample Median
__Sample median__ 은 샘플을 정렬했을 때 가운데에 위치한 값이다. 샘플 크기가 홀수라면 정확히 가운데를 찾을 수 있지만, 짝수라면 그렇지 않다. 이 때는 나온 두 값의 평균으로 median을 정의한다. $n$은 샘플의 크기고, 번호는 1번부터 시작한다고 하자.

$$
(median) = 
\begin{cases}
x_{\frac{n+1}{2}} & \text{if $n$ is odd} \\
\frac{x_{\frac{n}{2}} + x_{\frac{n+1}{2}}}{2} & \text{if $n$ is even}
\end{cases}
$$

... 이거 수식 치느라 좀 힘들었다.

### Sample Percentiles
이건 조금 생소한 개념일 수도 있다. __Sample 100p percentile__ 이란, $100p%$만큼의 데이터가 자신보다 작거나 같도록 하는 값을 의미한다.

예를 들어, {1, 2, ..., 100}인 샘플에서 95th percentile을 찾는다고 해보자. 1, 2, ... 95(총 $95%$)는 95보다 작거나 같다. 그렇다면 95th percentile은 95가 된다. 샘플 사이즈가 깔끔하지 않다면 헷갈릴 수 있으니 조심하자.

또, 샘플 사이즈가 $n$일 때, $np$가 정수가 아니라면 가장 작은 $np$보다 큰 정수, $k$를 골라, $k$번째로 작은 데이터를 고르면 되고, 만약 정수라면 간단히 $np$번째로 작은 데이터를 고르면 된다.

또, 샘플을 4분할 했을 때의 percentile은 여러모로 유용하게 쓰인다.

- First quartile($Q_1$): sample 25th percentile 
- Second quartile($Q_2$): sample median(50th percentile)
- Third quartile($Q_3$): sample 75th percentile

그리고 __Five-number summary__ 는 최솟값, $Q_1$, 미디안, $Q_3$, 최댓값을 포함한다.

### Sample Mode
__Sample Mode__ 는 샘플에서 가장 출현 빈도가 높은 데이터를 의미한다. 

### Sample Varaiance
이제부턴 조금 중요하다. 당연히 다 알고 있겠지만, 최빈값도 쓴 주제에 이걸 안쓰면 문제가 있으니 정리하자.

__Sample variance__ , $s^2$은 다음과 같이 정의된다.

$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$

Deviation의 제곱의 평균으로 하면 될 것을 왜 $n-1$로 나누냐는 의문은 평생 식지 않는 떡밥이다. 통계학에서의 $0.9999... = 1$과 같은 느낌이다.

약식으로 설명하면, "샘플의 크기가 작을 경우, $n$으로 나누면 population의 실제 분산보다 작게 측정하기 때문이다". 그러니까 $n-1$로 나눠서 조금 더 크게, 결과적으론 population variance에 가깝게 추정하려는 시도다...라고 하면 정말 야매같고 없어보이니 이 포스트 뒤쪽에 따로 설명한다.

아무튼 저 식은 계산이 꽤 복잡해 보인다. 하지만 우린 이를 구하기 위한 좋은 공식을 가지고 있는데,

$\sum_{i=1}^{n} (x_i - \bar{x})^2 = \sum_{i=1}^n x_i^2 - n\bar{x}^2$

위 공식을 사용해 보다 편하게 sample variance를 구할 수 있다. 증명은 대충 시그마 풀면 끝나니 생략.

### Sample Standard Deviation
__Sample standard deviation__ , $s$는 sample variance의 square-root로 정의된다.


# Bessel's Correction
이곳에 표본 분산(sample variance)과 표본 표준 편차(sample standard deviation)에서 샘플 사이즈를 n이 아닌 n-1을 사용하는 이유를 정리한다. __베셀 보정(Bessel's correction)__ 을 통해 그 이유를 알 수 있지만, 최대한 풀어서 쓰기 위해 노력했다.

우선, 다시 한 번, sample variance는 다음과 같이 정의된다.

$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$

## Law of Large Numbers
우선, 실제로 저 값이 population의 varaince, $\sigma^2$을 잘 대표해준다는 사실을 보이기 위해, $s^2$의 기댓값(expectation)이 $\sigma^2$임을 보일 것이다.

- $E(s^2) = \frac{1}{n-1} E(\sum_{i=1}^n (x_i - \bar{x})^2) $
- $\qquad \quad = \frac{1}{n-1} E(\sum_{i=1}^n x_i^2 - n\bar{x}^2) $ 
- $\qquad \quad = \frac{1}{n-1} (\sum_{i=1}^n E(x_i^2) - E(\bar{x})^2) $
- $\qquad \quad = \frac{1}{n-1} (\sum_{i=1}^n (Var(x_i) + \mu^2 - Var(\bar{x}) - \mu^2 ) $
- $\qquad \quad = \frac{n}{n-1} (\sigma^2 - Var(\frac{1}{n} \sum_{i-1}^n x_i)) $
- $\qquad \quad = \frac{n}{n-1} (\sigma^2 - \frac{n\sigma^2}{n^2}) = \sigma^2 $

Sample mean의 expectation은 population mean과 같고, independent한 각 $x_i$에 대한, variance의 linearity를 이용하여 증명하였다.

그리고, 큰 수의 법칙(law of large numbers)을 이용하면, $s^2$의 평균이 $\sigma^2$에 수렴함을 알 수 있다.

이렇게 $n-1$로 나눈 추정량(estimator)은 그것의 기댓값이 population parameter(모수?), 즉, population variance와 같고, 이러한 성질을 만족하는 추정량을 불편추정량(unbiased estimator)라고 한다. 

## Degree of Freedom
DoF의 관점에서 이 문제를 볼 수도 있다. DoF는 러프하게 표현하면, 독립적인(자유로운) 변수의 개수로 볼 수 있다. $x + y + z = 9$에서, $x, y$를 임의로 정한다면 $z$는 주어진 조건에 종속된다. 그래서 이 경우 DoF는 2다. 

Sample variance는 어떨까? 정의로부터, 우리는 이를 구하기 위해, sample mean의 값을 필요로 함을 알 수 있다. 그 상태에서, $n-1$개의 데이터는 자유롭게 결정될 수 있지만, 마지막 하나는 나머지 값들에 의존해 결정된다. 그래서 sample variance의 DoF는 $n-1$이다.

"우리는 아직 분산을 모르는데 왜 마지막 데이터가 결정되냐?"라는 의문이 들 수 있다. 하지만 이는 명백히 결정되는데, __편차의 합은 반드시 0이기 때문이다.__ 

마지막으로 "그래서, 왜 DoF로 나누냐?"라는 의문또한 들 수 있다. 아마 이게 직관적으로 납득이 어려운 부분일 것 같다.

이것은 약간은 자의적인 느낌이 있을 수 있는데, 다음 절에 설명한다.

## Bias
샘플 사이즈가 작은 경우, sample variance와 population variance는 어느 정도의 차이를 보인다. 그러한 차이를 bias라고 한다. 또 그렇게, bias를 발생시키는 추정치(estimator, 여기선 sample variance)를 biased estimator라고 한다. 당연하게 느껴지겠지만, 일반적으로 이는 바람직하지 않다.

그런데 $n$ 대신 DoF, $n-1$를 사용함으로써 이러한 estimator를 unbiased하게, 즉 unbiased estimator로 만들 수 있음을 알게 되었고, 그렇게 DoF를 사용하게 된 것이다.

이러한 이유는 꽤 clear하지 않아보인다. "어쩌다 보니 이걸 쓰게 되었다"라는 뉘앙스로 들릴 수 있기 때문인데, 그저 적절한 도구의 도입 정도로 보면 편할 것 같다. 항상 0이 되는 편차의 평균을 대신하여, 데이터의 편차, 그리고 퍼짐의 정도를 표현하기 위해 variance를 도입한 것처럼 말이다.


# 마치며
이제 아주 기본적인 통계 파트가 끝났다. 각종 이상한 도표를 제외하고 나니 진도가 굉장히 빨리 나간다.

다음엔 확률을 비롯한 여러 주제를 다루어보려고 한다.

