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
__Sample mean__ , $\bar(x)$는 다음과 같이 정의된다.

$$\bar{x} = \frac{\sum_{k=1}^{n} x_k}{n}$$ $$= \frac{x_1 + x_2 + ... + x_n}{n}$$

말 그대로 표본의 평균이다.

### Deviations
__Deviation__ 은 sample mean과 특정 값 사이의 차이로 정의된다.

$$x_i - x$$

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

(나중에 계속)
