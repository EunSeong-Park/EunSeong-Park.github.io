---
title: "[Algorithms 7] 동적 계획법"
tags: Algorithms
toc: true
---

# Intro
동적 계획법(dynamic programming)은 어떤 특정한 알고리즘은 아니고, 일종의 테크닉이다. 분할 정복이 알고리즘 자체는 아닌 것과 비슷한 맥락이다. 이번 포스팅에선 동적 계획법이 무엇인지, 그리고 동적 계획법이 활용할 수 있는 문제와 그에 대한 솔루션을 알아볼 것이다.


# Dynamic Programming
동적 계획법은 최적화(optimization) 문제를 해결할 때 주로 사용된다. 예전에 사용된, 혹은 결과로 나온 값을 이후의 연산에 사용하여 전체 연산의 비용을 줄이는 방식이다. 우선 동적 계획법의 절차를 알아보자.

1. Optimal solution의 structure를 characterize한다.
2. Optimal solution의 값을 재귀적으로 정의한다.
3. 상향식(bottom-up), 혹은 하향식(top-down)으로 optimal solution을 계산한다.
4. 계산한 정보를 바탕으로 optimal solution을 세운다.

모르고 보니까 뭔 소린지 모르겠다. 예제를 풀어보고 다시 확인해보자.

## Example: Rod-Cutting Problem

> 어떤 긴 막대기를 하나 팔려고 하는데, 우리는 이걸 일정 길이로 자를 수 있고, 막대기는 길이에 따라 가격이 다르다. 막대기를 적절하게 잘라, 최대의 이익을 얻고자 한다.

![](/imgs/algorithm/algo15.png)

$p(i)$을 길이 $i$를 가지는 막대기의 가격이라고 하자. 처음 길이가 $n$이고, 이를 $k$개의 막대기로 잘랐다면, $n = i_1 + i_2 + ... + i_k$으로 막대 길이를 표현할 수 있고, 총 판매 가격, $r_n$은 다음과 같이 나타낼 수 있다.

$r_n = p(i_1) + p(i_2) + ... + p(i_k)$

우리는 이 $r_n$을 maximize해야 한다.

### Optimal Structure
우선, $n=i_1+i_2+...+i_k$를 $n$-length 막대기의 optimal solution이라 하자. 즉, 우선 최적의 해임을 가정하는 것이다. 여기서, $i_2+i_3+...+i_k$는 $n-i_1$-length 막대기의 optimal solution이 된다! 이 사실은 당연한 듯 보이지만 증명이 필요한데, 단순히 더 나은 최적의 해가 있음을 가정하고 귀류법을 사용하면 된다. 그래서 증명을 따로 적지는 않는다.

아무튼 optimal solution은 이러한 구조를 가지고 있음을 파악하였다.

### Recursive Definition
위의 구조를 통해, optimal solution, $r_n$은 $n-i$에서의 optimal solution, $r_{n-i}$에 $p(i)$를 더한 것과 같다는 사실을 알 수 있다. 

$$ r_n = max(p(i)+ r_{n-i} | i=1,2,...n) $$

충분히 납득할 수 있는 식일 것이다.

### Dynamic Programming
재귀적으로 정의가 잘 된다고 해서 단순히 이걸 재귀적으로 전부 탐색하는 대참사는 일어나선 안된다. 모든 경우를 다 검사하면 exponential한 환장할 complexity를 가질 것이다. 아래는 그렇게 망한 케이스의 수도코드다.

![](/imgs/algorithm/algo16.png)

이러한 방법은 걸러야 마땅한데, 어째서 이런 대참사가 일어났는지 알고 넘어가는 게 좋다. 이유는 간단하다. 동일한 케이스를 너무 많이 비교하게 된다.

![](/imgs/algorithm/algo17.png)

그래서 DP에서는 이미 해결된 subproblem을 저장하고, 이후 같은 subproblem을 만날 때 참조하여 필요한 연산을 줄인다. 이러한 방법으로 exponenital한 running time을 polynomial하게 줄일 수 있다. 이를 위한 두 가지 방법이 있는데, 바로 메모이제이션을 이용한 하향식(top-down) 방법과, 상향식(bottom-up) 방법이다.

#### Top-Down
하향식 방법에선 기존과 같은 방법으로 재귀를 사용한다. 하지만 각각의 결과를 테이블에 저장하고, 매 subproblem의 시작마다 테이블을 확인한다. 테이블에 있으면 바로 그걸 사용하면 되고, 아니면 계산 후 테이블에 집어 넣으면 된다.

![](/imgs/algorithm/algo18.png)

`r`이 subproblem의 결과를 저장할 테이블이다. `r[k]`은 `Cut-Rod(p, k)`의 결과를 저장한다.

#### Bottom-Up
`Cut-Rod(p, n)`을 계산하기 위해, `n`보다 작은 `k`에 대해 `Cut-Rod(p, k)`를 먼저 구하는 방식이다. 

![](/imgs/algorithm/algo19.png)

함수 자체는 재귀 호출을 하지 않고, 대신 doubly-nested-loop의 형태를 띄고 있다. 예를 들어, `Cut-Rod(p, 2)`를 계산하려면 그 전에 `Cut-Rod(p, 1)`의 값이 저장되어 있어야 한다. 마찬가지로, 3의 경우엔 1과 2를, 4의 경우엔 1, 2, 3을 확인한다. 

### Performance
상향식이든 하향식이든, 이들의 running time은 $\Theta(n^2)$이다. 왜냐? 하향식 방법은 각 subproblem이 한 바퀴 루프를 돌려 자신의 subproblem들을 찾기 때문이고, 상향식은 이중 루프 방식으로 배열에 접근하기 때문이다.

Exponential했던 초기에 비하면 굉장한 성과다.

### Extra
우리는 최고 가격을 찾는 데 집중했지만, 최고 가격을 만드는 절단 방법 또한 알 수 있다. 새로운 배열 `s`를 도입하여, 최적의 subproblem이 나온 경우의 길이를 저장하면 된다. `r`과 마찬가지로, `s[k]`는 `Cut-Rod(p, k)`에서의 결과에 대응된다. 

![](/imgs/algorithm/algo20.png)

`s[n]`부터 시작해, 전체 길이를 줄여나가면서 추적하면 된다.

![](/imgs/algorithm/algo22.png)

길이가 8인 막대기가 있고, 다음과 같은 가격표가 주어진다면, 길이를 2와 6으로 나누어 자르면 최적의 해가 나온다. 이 때, 각 테이블은 다음과 같이 구성된다.

![](/imgs/algorithm/algo21.png)

`S[8]`은 2이므로, 그 다음은 `S[6]`을 찾는 방식으로 0이 될 때까지 출력하면 된다.

## Matrix-Chain Multiplication
저번에 배웠듯 가장 단순한 방식의 행렬곱은 $O(n^3)$이다. 좀 더 정확히 말하면, $m * n$ 행렬 $A$와 $n * p$ 행렬 $B$의 곱 $AB$는 $mnp$의 곱셈을 수반한다.

마찬가지로, $A:l * m, B: m * n, C: n * p$라 하면, $(AB)C$는 $lmn + lnp$, $A(BC)$ 는 $mnp+lmp$만큼의 곱셈을 수반한다. 여기서 $l, m, n, p$가 각각 10, 100, 5, 50이라 해보자. 전자의 경우 7500회, 후자의 경우 75000회 곱셈을 수행하게 된다, associative property에 의해 결과는 같은 데도 말이다. 띠용??

알다시피, 행렬 곱은 일반적인 경우엔 commutative property가 성립하지 않는다. 이 상황에서, 괄호를 적당히 박아 최선의 행렬 곱을 이끌어내고 싶다면 어떻게 해야 할까? DP를 이용해 해결해보자.

### Optimal Structure
행렬 $A_1, A_2, ..., A_n$이 있고, $A_i$의 크기는 $p_{i-1} * p_i$다. 이러한 크기를 가져야 행렬 곱이 성립되기 때문이다. 이제 행렬 곱 $A_1A_2A_3...A_n$을 fully parenthesize해서, 최소한의 곱셈 연산으로 그 결과를 구해볼 것이다.

Optimal solution을 다음과 같이 나타내어 보자. 이는 $A_i$부터 $A_j$까지의 행렬 곱의 optimal parenthesis를 포함한다.

$$A_{i...j} = A_iA_{i+1}...A_j$$

여기서 중요한 점은, 전체가 optimal하다면, 이것의 임의의 분할 각각도 optimal해야 한다는 사실이다. 그렇지 않으면 이미 optimal한 solution보다 더 나은 solution이 존재하여 모순이 발생하기 때문이다. Optimal solution (((AB)C)(DE))에서, ((AB)C)는 행렬 곱 ABC의 optimal solution일 것이다.

### Recursive Definition
방법이 정해졌으면 최적 해를 찾는 건 시간 문제다.

$m[i,j]$를 $A_{i...j}$에서의 최소 곱셈 연산 횟수라고 정의한다. $m[i,i]$는 자명하게 0이고, $m[i,j]$는 임의의 분할 지점 $k$를 잡아, $min\{m[i,k]+m[k+1,j]+p_{i-1}p_kp_j\}$와 같이 나타낼 수 있다. 즉, 두 행렬 각각에 수행된 지금까지의 곱셈 연산 수에, 두 행렬 사이의 행렬 곱에 필요한 곱셈 연산 수를 더하는 셈이다.

### Dynamic Programming
마지막으로, $s[i,j]$를 minimum을 이끌어내는 $k$값이라고 하자. 많은 검사 케이스에서, 겹치는 경우가 꽤 많은데, 이를 $s$에 저장함으로써 해결할 수 있다. 예를 들어, ABCDEFGHI에서, ABC에서의 $k$값은 ABCDEF, GHI 분할에서도, ABCD, EFGHI 분할에서도, 혹은 그것의 부분 문제에서도 몇 번이고 필요할 수 있다.

또, chain length, $l$을 $l=j-i+1$과 같이 정의하자. 우리는 임의의 index에서 시작하는 임의의 chain length에서의 최적 해를 상향식으로 모두 구할 것이다.

![](/imgs/algorithm/algo23.png)

$m$과 $s$는 다음과 같은 구성으로 construct될 것이다. 최적 해뿐만 아니라, 최적 해를 이끌어내는 방법 또한 알 수 있는 셈이다. 

![](/imgs/algorithm/algo24.png)

![](/imgs/algorithm/algo25.png)

$s$를 이용해 최적 해를 만드는 parenthesis를 추적할 수 있다. 수도 코드과 같이 재귀적으로 k를 찾아 그에 맞추어 분할하면 된다. 아래 예시와 결과를 비교해보면 이해하기 쉬울 것이다.

![](/imgs/algorithm/algo26.png)

이러한 방법은 $O(n^3)$의 time complexity, $\Theta(n^2)$의 space complexity를 가진다. 

