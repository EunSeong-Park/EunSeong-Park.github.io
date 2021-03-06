---
title: "[Algorithms 6] 순서 통계량"
tags: Algorithms
toc: true
---

# Intro
기나긴 정렬이 끝났다.


# Order Statistic
i-th order statistic이란 배열에서 i-th 정렬 순위를 가지는 원소를 의미한다. Min, max와 같은 값도 결국 1th, n-th order statistic으로 볼 수 있다. 또, n이 홀수라면 median 또한 (n+1)/2에서 유일하게 결정되는 ((n+1)/2)-th order statistic이다. 만약 n이 짝수라면, 우리는 n/2-th를 lower median, n/2+1을 upper median이라고 한다.

## Selection Problems
Selection problem이란, 주어진 배열에 대해 i-th order statistic을 찾는 문제를 말한다. 가장 친숙하고 확실한 방법은, 주어진 배열을 정렬한 뒤 i-th element를 뽑는, sort-then-pick 방식일 것이다. 하지만 우리는 이것보다 더 좋은 방법이 있다.

### Min/Max
최소/최댓값 중 하나를 구하는 건 굉장히 쉽다. 배열을 한 바퀴 순회하면서 최소/최댓값을 갱신하는 방식으로, 배열 크기 n에 대해 n-1회의 연산만 수행하면 된다. 이는 comparison-based selection에선 최선의 방식이다. 토너먼트식도 결국엔 n-1회다. 우승자가 아니면 한 번씩 지기 때문이다.

최대/최솟값을 한 번에 선형 시간으로 찾는 방법도 있다! 물론 최소/최대를 위해 합쳐서 2n-2회 비교를 할 수도 있지만, 첫 비교 후, 승자들 사이에서 최소를, 패자들 사이에서 최대를 찾아 나가면 필요한 연산의 수를 줄일 수 있다. 이러한 방법으로 3\*floor(n/2)의 비교만을 사용할 수 있다.

### Randomized Select
그럼, 임의의 i에 대해 i-th order statistic을 어떻게 찾을까? Quick sort의 변형 스러운 느낌으로 해결해보자.

주어진 배열을 $$A$$, 시작 인덱스를 $$p$$, 끝 인덱스를 $$r$$, 찾으려는 값(i-th order statistics)을 $$i$$라 하자. 단일 배열인 경우($$p == r$$) 즉시 그 원소를 리턴하며, 그렇지 않다면 이를 무작위 분할(pivot이 랜덤인 파티션)한다. Pivot이 i와 같다면 그 값이 우리가 찾는 값이고, 작다면 pivot 왼쪽에서, 크다면 pivot 오른쪽에서 이 과정을 마저 하면 된다. 수도 코드로 나타내면 다음과 같다.

![](/imgs/algorithm/algo13.png)

잊어버렸을까봐 다시 적는데, 참고로 파티션은 다음과 같다. (잊은건 사실 나였다.)

![](/imgs/algorithm/algo14.png)

Randomized selection은 $\Theta(n)$의 expected running time을 가지며, worst-case에선 $\Theta(n^2)$의 시간 복잡도를 가진다. Quick sort와 마찬가지로, pivot이 한쪽에 쏠려서 파티션이 uneven할 수록 시간이 오래 걸린다.

Worst-case는 한 번 시행할 때마다 해결해야 할 배열이 한 칸씩 줄어드는 경우이므로 $\Theta(n^2)$이 직관적으로 납득할 만하다. 그렇다면 expected running time은 어떨까? 

$$X_k$$를 분할된 부분 배열이 $$k$$개의 원소를 가지는 사건에 대한 indicator random variable이라 해보자. 그럼 $P(X_k) = E(X_k) = 1/n$일 것이다. 그렇다면 다음과 같이 표현할 수 있다.

- $$T(n) \le \sum_{k=1}^n X_kT(max(k-1,n-k))+O(n))$$
- $$T(n) \le \sum_{k=1}^n X_kT(max(k-1,n-k)) + O(n)$$
- $$E(T(n)) \le E(\sum_{k=1}^n X_kT(max(k-1,n-k)) + O(n))$$
- $$E(T(n)) \le \sum_{k=1}^n E(X_k)E(T(max(k-1,n-k))) + O(n)$$ (By independence)
- $$E(T(n)) \le \sum_{k=1}^n \frac{1}{n}E(T(max(k-1,n-k))) + O(n) by 

여기서 $max(k-1, n-k)$의 값이 중요한데, 아마 절반보다 크면 $k-1$을, 작으면 $n-k$를 가질 것이다. 좀 더 자세히 보면, $n$이 짝수일 때는 절반부터 $T(n-1)$까지 각 항이 두 번씩 나오고, 홀수일 때는 $T(\lfloor\frac{n}{2}\rfloor)$를 제외하고 한 번씩 나올 것이다. 즉,

$$E(T(n)) \le \frac{2}{n} \sum_{k=\lfloor \frac{n}{2} \rfloor}^{n-1} E(T(k)) + O(n) $$

이고, Substitution으로 $E(T(n)) \le cn$으로 가정하고 풀면 증명이 된다. 디테일은 책보자...

### Deterministic Select
Randomized select와 같은 방식으로 타겟을 찾지만, 다른 방식으로 pivot을 선택해볼 수 있다. 좋은, 즉, median에 가까운 pivot을 찾을 수 있다면, selection의 cost는 크게 줄어들 것이다. 물론, 완벽하게 median을 (퍼포먼스에 지장을 주지 않고) 뽑는 것은 불가능할 것이다. 그 대신, 랜덤보다는 median에 가까운 선택을 해볼 수는 있다.


우선 원소들을 5개 묶음으로 나눈다. (나머지가 있어도 괜찮다.) 이후 각 그룹에서 median을 찾고, 그렇게 구한 median에 대해 재귀적으로 median을 또 구한다. 이런 방식을 median of median(MOM)을 뽑는다고 말한다. 아까도 말했듯이, 이렇게 뽑은 값은 실제 median이 아닐 수 있다.

$$
	\begin{matrix}
	1 & 1 & 9 & 9 & 4 \\
	1 & 1 & 9 & 9 & 2 \\
	7 & 8 & 9 & 9 & 2 \\
	1 & 1 & 9 & 9 & 2 \\
	1 & 1 & 9 & 9 & 2 \\
	\end{matrix}
$$

위와 같은 행렬의 경우 MOM은 2지만, 실제 median은 4다. (아마도) 하지만 이 MOM은 자신의 order statistic이 위-아래 양쪽으로 일정 범위 바운드되어 있음을 보장한다. 자기보다 작은 원소가 최소 $\frac{3n}{10} - 6$개, 큰 원소가 최소 $\frac{3n}{10} - 6$개 만큼 있음을 보장한다. (왜 그런진 책에서 볼 수 있다) 대충 25-75프로 사이에 들어가는 셈이다. 즉, 한 번의 재귀가 수행될 때마다, 해결해야하는 문제는 75%를 넘지 않게 된다. 

$$T(n) \le T(\frac{n}{5}) + T(\frac{3n}{4}) + O(n)$$

이렇게 되면 $O(n)$의 복잡도를 가지게 된다.