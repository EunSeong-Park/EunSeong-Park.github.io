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
시작 시간과 종료 시간, $s_i < f_i$는 half-open interval($\[s_i, fi)$)이고,

