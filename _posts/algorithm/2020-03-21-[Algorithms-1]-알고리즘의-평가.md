---
title:  "[Algorithms 1] 알고리즘의 평가"
tags: Algorithms
toc: true
key: algo1
---

# Intro
누군가 말하길, 알고리즘은 well-specified된 computational problem의 solution이라고 한다. 알고리즘 전공 도서인 CLRS에서는 알고리즘을 다음과 같이 설명한다. 적절한 정의라고 생각된다. 알고리즘을 이해하고 설계하는 건 input과 output을 명확히 파악하는 것에서 시작하는 게 아닐까 싶다.

> An algorithm is any well-defined computational procedure that takes some value as input and procedures some value as output.

그리고 알고리즘이 사용되는 computational problem은 일종의 함수로 볼 수도 있다. Input에 해당하는 X의 모든 원소 x에 대해, F:X->Y의 매핑이 있고 F(x)는 x에 대한 문제의 정답이다. 이 때, 어떤 알고리즘 A가 있고, 모든 x에 대해 A(x)=F(x)가 성립하면, 그 알고리즘은 correct하다고 볼 수 있다. 이 또한 알고리즘을 설명하기 위한 적절한 방법인 것 같다.

이번엔 정렬 알고리즘을 예시로, 알고리즘을 여러 측면에서 평가 및 검증하는 방법에 대해 배워볼 것이다. 정렬이 메인이 아니므로, insertion sort 하나만 사용할 예정이다.


# Sorting
정렬(sorting)을 위의 설명을 빌려 설명하면,

> Input: n 개의 숫자 배열(a_1, a_2, ... a_n) 

> Output: a_1' <= a_2' <= ... <= a_n'을 만족하는 input의 permutation

## Insertion Sort
간단히 말하면, 정렬되지 않은 원소를 이미 정렬된 부분의 적당한 위치에 삽입하는 방식의 정렬이다. Pseudocode로 나타내어 보자, 그 구현이 명확히 드러날 것이다.

    Insert(A):
    for i = 1 to A.length
      key = A[i]  // A[0]은 이미 정렬되었으므로 A[1]부터
      j = i-1     

      while j >= 0 && A[j] > key // key와 A[j]를 계속 비교해나간다.
        A[j+1] = A[j]
        j -= 1
        // key가 더 작은 경우 계속 한칸씩 밀어낸다.

      A[j+1] = key // 가능한 한 전부 밀어내고 빈 칸에 key를 넣는다.


# Testing Algorithm
이제 이 삽입 정렬을 바탕으로 알고리즘을 평가해보자. 우선 알고리즘이 맞는지(correct) 판단하고, 그 다음에 얼마나 cost가 발생하는지 알아볼 예정이다.

## Correctness - Loop Invariant
우선 다 제쳐놓고, 알고리즘이 정확한 결과를 도출해내야 그 다음의 요소들을 평가하는 게 의미가 있다. 즉, 이 알고리즘의 correctness를 판단해야 하는데, 모든 임의의 원소에서 참임을 직접 보일 수는 없으니, loop invariant를 사용할 것이다. Loop invariant는 단어 그대로, 루프를 돌 동안 항상 참인 (그리고 참이어야 하는) statement다. 또, 이는 correctness를 증명하기 위한 방법으로, (mathematical induction과 비슷한 느낌이다) 아래 세 가지 조건을 만족하면 된다.

1. Initialization : 첫 반복 이전(즉, 루프에 들어가기 전) 그 statement는 참이어야 한다. 
2. Maintenance : 반복 이전에 statement가 참이었다면, 다음 반복도 참이 유지되어야 한다.
3. Termination : 루프가 끝났을 때, 그 statement, 즉 invariant는 우리에게 (문제 해결과 알고리즘 평가에) 유용한 결과를 주어야 한다.

Insertion sort에선, __input A에 대해, j-th iteration에서는 A\[0]부터 A\[j-1]까지 정렬되어 있어야 한다__ 가 loop invariant가 될 것이다. 그럼 이 statement는 위의 세 조건을 만족하는가? 굳이 하나하나 확인해 쓰진 않을 거고, 실제로 저 세 조건을 모두 만족한다.

Loop invariant에 의한 correctness가 중요한 것은 (당연히) 정확한 결과도 있지만, 이렇게 솔루션이 도출되는 알고리즘이 다른 이상한 방법으로 솔루션이 나오는 알고리즘보다 효율적이며 효과적이기 때문일 것이다.

## Cost
이제 이게 타당한 알고리즘이란 건 확인했다. 이제 알고리즘의 효율성에 대해 생각해보자. 결국 알고리즘에서 효율이란 건, 얼마나 공간과 시간을 잡아먹는지일 것이다. 다만 실제 실행 시간은 머신, 프로그램, 언어 등 많은 변수에 의존하므로, 우리는 다른 방법을 통해 알고리즘의 효율성을 판단한다. (사실 이는 옛날에 다 배운 내용이다)

모두가 알겠지만, 시간적 측면에서의 코스트는 코드 길이로 측정하는 게 아니며, operation의 수만으로도 측정하는 게 아니다. (물론 이 둘이 필요 이상으로 어마어마하게 크면 분명히 조금 더 비효율적이긴 할 것이다) Assembly에서 DIV 연산은 ADD 연산에 비해 코스트가 훨씬 크다는 걸 생각해보자. 또한, 이는 input에도 의존한다. 길이는 물론이고, 그 내용물에 따라서도 cost가 달라질 수 있다.

위의 pseudocode를 다시 보자.

    0:    Insert(A):
    1:    for i = 1 to A.length
    2:      key = A[i] 
    3:      j = i-1     

    4:      while j >= 0 && A[j] > key 
    5:        A[j+1] = A[j]
    6:        j -= 1

    7:      A[j+1] = key

k-line의 operation의 cost를 `c_k`라고 하고, `key`보다 큰 정렬된 원소의 수를 `t_i`라 하자.

    T(n) = c_1 n + c_2 (n-1) + c_3 (n-1) + c_4 sum(t_i + 1) + c_5 sum(t_i) + c_6 sum(t_j) + c_7 (n-1)
    
이 때, best case는 모든 `i`에 대해 `t_i`가 0인, pre-sorted case일 것이다. 이 때는 `n`에 대하여 최고차항이 1인 linear한 시간 복잡도를 가질 것이다. 반대로, 최악의 상황(모든 iteration에서 `t_i` = `j`)이거나 평균적인 케이스일 경우, 이는 quadratic한 시간 복잡도를 가진다. 시간 복잡도를 표현하기 위한 많은 방법이 있지만, 주로 big-O나 theta를 쓰므로, 이를 사용해 표현하면 O(n^2), 또는 theta(n^2)가 되겠다.

우린 당연하게도, 시간 복잡도를 input size, n에 대한 함수로 나타내는데, 이는 실제로 (특히 큰 수에서) 그 사이즈에 크게 의존하기 때문이다. 7중 for문 같은 해괴한 알고리즘을 구현해도 n이 5 정도라면 constant factor 등에 가려져 그 비효율성이 눈에 띄지 않을 것이다. 배열을 사용하는 알고리즘이면 대개 배열의 길이가, multiplication같은 경우엔 비트 길이가 n이 될 것이다.

## Asymptotic Notation
마치기 전에 asymptotic notation에 대해 잠깐 짚고 가자.

모두가 알겠지만, complexity를 완전한 식으로 표현하는 건 불가능하거나 매우 어렵다. 보통은 가장 영향력이 큰 항만을 주목하게 되는데, 우리는 그래서 주어진 complexity를 점근적으로(asymptotically) 나타내는 방법을 사용한다. 그 종류를 적당히 정의해보면,

Big-O

> f(n) = O(g(n)) iff 적당한 상수 c, n_0가 있어, f(n) <= cg(n) for all n >= n_0 

Big-Omega

> f(n) = Omega(g(n)) iff 적당한 상수 c, n_0가 있어, f(n) >= cg(n) for all n >= n_0 

Big-Theta

> f(n) = Theta(g(n)) iff 적당한 상수 c1, c2, n_0가 있어, c1g(n) <= f(n) <= c2g(n) for all n >= n_0 

정리하면, Big-O는 f의 upper bound가 되는 g를 찾고, Big-Omega는 lower bound가 되는 g를 찾으며, Big-Theta는 upper, lower가 모두 될 수 있는 g를 찾으면 된다. Big-O와 Big-Theta를 주로 쓰는데, Big-Omega는 자칫하면 의미없는 g를 찾을 수도 있다. 예를 들어, f가 3차 다항식일 때, g는 n^3일 수도, n^2일 수도, 1일 수도 있다. 하지만 n^3이 아니면 f를 적절히 점근시키지 못하며, 그 notation은 실제론 별 의미 없는 게 되어버린다.

추가로, small-o와 small-omega도 있는데, 이는 등호를 허용하지 않으며, f, g 모두 0 이상이다.

# 마치며
지금까지 sorting을 핑계로 알고리즘의 평가 방법을 알아보았다. 다음은 분할 정복(divide-and-conquer)에 대해 알아보자.




