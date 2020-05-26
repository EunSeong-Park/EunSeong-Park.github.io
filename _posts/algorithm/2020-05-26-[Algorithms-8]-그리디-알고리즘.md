---
title: "[Algorithms 8] 그리디 알고리즘"
tags: Algorithms
toc: true
---

# Intro
우리는 지난 포스팅에서 DP와 그것의 예시를 알아보았다. 이번엔 그리디 알고리즘(greedy algorithm)에 대해 알아보자.

그리디 알고리즘은 locally optimal choice를 찾는 방식의 문제 해결법이다. 즉, 항상 완전한 최적해를 제공해주는 건 아니지만, 효율적인 방식으로 그것의 근사적인 해나 휴리스틱(heuristic)을 제공해 줄 수는 있다.


# Activity-Selection Problem
Activity-selection problem은 다음과 같은 상황을 다루는 문제다.

> 어떤 행사엔 여러 액티비티가 있고, 각 액티비티는 각자의 시작 및 종료 시간이 있다. 여기서 할 수 있는 최대의 액티비티 수를 알고 싶다.

![](/imgs/algorithm/algo27.png)

위와 같은 상황이라면, 최대 두 개의 활동을 할 수 있을 것이다. 이를 해결하기 위해, 다음과 같은 상황을 가정한다.

## Problem
$S=\{a_1, a_2, ..., a_n\}$을 액티비티의 집합으로 보고, 각 액티비티 $a_i$에 대하여 시작 시간과 종료 시간, $s_i < f_i$는 half-open interval($\[s_i, fi)$)이라 하자. 이러한 상황에서, "두 활동을 같이 할 수 있다"는 것은 다음을 의미한다.

$\[s_i, f_i) \cup \[s_j, f_j) = \emptyset$

주어지는 input은 종료 시간에 대해 정렬되어 있다고 가정한다. 즉,

$f_1 \le f_2 \le ... \le f_{n-1} \le f_n$

또, 아래와 같은 집합을 생각해보자.

$S_k = \{a_i \in S \vert f_k \le s_i \}$

이는 $a_k$가 종료된 이후 시작할 수 있는, 즉 $a_k$와 compatible하면서 시간적으로 뒤에 있는 $S$의 원소(액티비티)들의 집합을 의미한다.

## Solution
여기서 greedy choice라 함은... 

- 가장 빨리 끝나는 액티비티를 고른다. 동일한 종료 시간의 액티비티가 여러 개 있다면 아무거나 고른다.
- 그에 따라, $S$가 정렬되어 있다면, $a_1$부터 선택한다.

아하! 욕심쟁이라서 가장 눈 앞에 있는 최선의 선택, 즉 locally optimal choice을 하는구나! 라고 생각할 수 있겠다.

아무튼, $a_1$을 먼저 구했으니, 우리는 $S_1$에서 maximum set을 찾고, 이후에 이 과정을 반복하면 된다.

![](/imgs/algorithm/algo28.png)

위의 표를 예시로 하면, 그리디 알고리즘에서 최선의 선택은 아마, $1 \to 4 \to 8 \to 11$일 것이다.

## Implementation
그리디 알고리즘은 보통 하향식(top-down)으로 구현된다. 하향식, 그리고 재귀적 activity selector를 구현해보자.

![](/imgs/algorithm/algo30.png)

$s, f$는 $a_i$의 시작/종료 시간을 나타내는 배열이고, $k, n$은 배열의 시작과 끝 인덱스를 의미한다. 2-3에서 루프를 돌려 마지막 액티비티가 끝난 뒤에 시작하면서 가장 빨리 끝나는(이미 정렬됨을 가정하므로) 다음 액티비티를 찾는다. 그렇게 찾은 액티비티를 집합에 추가하면서 재귀적으로 찾아나간다.

Iterative한 selector를 구현해볼 수도 있다.

![](/imgs/algorithm/algo31.png)

## Cost
Recursive든 iterative든, 각 원소는 단 한 번 탐색된다. 따라서 $\Theta(n)$의 time complexity를 가진다. 다만, 이 알고리즘은 정렬을 필요로 하므로, 정렬되어 있지 않다면 $\Theta(n \log n)$의 비용이 추가로 발생한다.




