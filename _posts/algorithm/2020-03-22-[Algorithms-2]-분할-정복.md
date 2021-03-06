---
title:  "[Algorithms 2] 분할 정복"
tags: Algorithms
toc: true
key: algo2
---

# Intro
이제 본격적으로 알고리즘들에 대해 배운다고 할 수 있겠다. 이번엔 분할 정복(divide-and-conquer)에 대해 알아보자.


# Divide-and-Conquer
분할 정복은 주어진 문제를 잘게 나누어 해결한 뒤 합치는 방법이다. 이는 크게 세 단계로 나눌 수 있는데,

1. Divide : 주어진 문제를 작게 분할한다. 단, 분할된 소문제들도 같은 종류의 문제다.
2. Conquer : 분할된 소문제들을 재귀적으로 해결한다. 만약 base case(가장 작은 단위의 소문제)를 만나면 BF(Brute Force)로 해결한다.
3. Combine : 해결된 소문제들을 병합한다.

분할 정복은 그 특성으로 병렬적인 해결이 용이하기도 하고, 그로 인해 여러 알고리즘의 기반이 되기도 한다. 다만 재귀라는 그 특성상 메모리가 크게 낭비될 수도 있고, 함수 호출에 의한 오버헤드도 무시할 수는 없을 것이다.


# Merge Sort
병합 정렬, 또는 합병 정렬(merge sort)은 분할 정복을 기반으로 하는 대표적인 알고리즘이다. 기본적인 정렬 알고리즘들은 모두 알고 있으니 딱히 설명할 필요는 없을 것 같고, 왜 분할 정복 기반인지도 그 이유가 바로 떠오를 것이다. 그래도 일단 병합 정렬을 분할 정복의 세 절차로 나누어 확인해보자.

1. Divide : n-length array를 n/2-length의 두 array로 분할한다.
2. Conquer : 재귀 호출을 통해 각 sub-array를 정렬한다. (base case는 더 분할이 불가능한 경우)
3. Combine : 정렬된 sub-array를 합친다.

이미 알고리즘을 구현하는 방법은 알고 있을테니, pseudocode는 생략한다. 대신, correctness를 loop invariant를 통해 확인해보자.

## Correctness
병합 정렬에서, 매 병합 시마다 각각의 subarray는 정렬되어 있어야 한다. 이게 적절한 loop invariant인지, 그리고 병합 정렬은 이를 만족하는지 알아본다.

1. 첫 병합 전, 각 array는 1-length다. 따라서 모두 정렬되어 있다.
2. 병합 시 정렬을 하므로, 병합된 subarray도 정렬되어 있다.
3. 최종 병합 시 정렬된 n-length array가 된다.

## Cost
첫 병합 시, 크기가 1인 array를 병합하려면, 비교 연산을 두 번 해야 한다. 이걸 n/2회 반복하니 n회의 연산을 하게 된다. 두 번째엔 크기가 2인 array를 병합하기 위해 비교 연산을 네 번 한다. 이걸 n/4회 반복하니 n회의 연산을 한다. log_2 n의 층으로 이루어져 있으니, 비교에는 O(nlogn)의 복잡도가 형성된다. 

비슷한 방식으로, 이동에도 O(nlogn)의 복잡도가 생기니, 결국 병합에는 O(nlogn)의 복잡도가 형성된다.

외부 공간을 사용하지 않으면 (즉, 분할을 인덱스 지정으로만 수행하면) 분할 과정은 무시해도 된다.


# Maximum Subarray Problem
String의 subset은 string이고, array의 subset도 array다. 생각보다 중요한 사실인데, 아무튼 이번엔 분할 정복을 통해 maximum subarray problem을 해결해보자. 간단히 말하면, 양수와 음수를 모두 포함할 수 있는 어떤 배열로부터, 어떤 연속한 구간을 잘라내 부분 배열(subarray)를 만들어 그것의 합이 최대가 되도록 하는 것이다.

![](/imgs/algorithm/algo1.png)

이걸 어떻게 해결할지 논의하기 전, input과 output을 명확하게 확인하고 가자.

- Input : 정수(non-neg + neg)를 포함하는 어떤 n-length array (A\[1...n])
- Output : 모든 A의 subarray 중 그 값들의 합이 최대인 (j-i)-length array (A\[i...j])

사실 이는 BF, DP 등 여러 방법으로 풀 수 있는 문제지만, 이 포스팅은 분할 정복에 대해 다루므로 분할 정복으로 풀어보려 한다. 아무튼, 그럼 분할 정복으로 어떻게 문제를 해결할 수 있을까?

어떤 배열에서, 배열을 자르는 중점(mid)을 하나 잡고 분할하는 걸 생각해보자. 이 때 가능한 부분 배열의 합은 다음과 같다.

1. 중점을 기준으로 왼쪽에 존재한다.
2. 중점을 기준으로 오른쪽에 존재한다.
3. 중점에 걸쳐 존재한다.

이점을 고려하여 분할 정복의 방법을 세워보면,

- Divide : 어떤 부분배열의 중점을 적절히 잡아 (가능한 한 같은 사이즈로) 분할한다.
- Conquer : 왼쪽 부분배열과 오른쪽 부분배열의 최대 부분합을 구한다.
- Combine : 중점에 걸치는 부분배열의 최대 부분합을 구한다. 배열이 단일 원소인 경우 스스로를 리턴한다.

## Implementation
Pseudocode로 구현 해보자. `Find-Max-Subarray`는 배열 `A`, 최소 인덱스 `low`, 최대 인덱스 `high`를 인자로 받아, 최대 합을 만드는 최소 인덱스 `low`, 최대 합을 만드는 최대 인덱스 `high`, 최대 합 `sum`을 리턴한다. `Find-Max-Crossing-Subarray`는 여기에 `mid`를 추가로 받아, 위와 같은 정보를 리턴한다.

    Find-Max-Subarray(A, low, high)
        if (high == low) return (low, high, A[low]) // base case : 단일 원소 배열

        else mid = floor((low + high)/2)
            // 세 케이스를 모두 뽑아내 비교한다.
            (left-low, left-high, left-sum) = Find-Max-Subarray(A, low, mid)
            (right-low, right-high, right-sum) = Find-Max-Subarray(A, mid+1, high)
            (cross-low, cross-high, cross-sum) = Find-Max-Crossing-Subarray(A, low, mid, high)

            // 최댓값을 찾아내 리턴
            max = max(left-sum, right-sum, cross-sum)
            if (max == left-sum) return (left-low, left-high, left-sum)
            elseif (max == right-sum) return (right-low, right-high, right-sum)
            else return (cross-low, cross-high, cross-sum)

    Find-Max-Crossing-Subarray(A, low, mid, high)
        left-sum = INT_MIN // instead of -inf
        sum = 0

        // 중점부터 low까지 왼쪽으로 이동한다.
        for i = mid downto low
            sum += A[i]
            if sum > left-sum
                // max-left 갱신
                left-sum = sum
                max-left = i

        right-sum = INT_MIN
        sum = 0 

        // 중점부터 high까지 오른쪽으로 이동한다
        for j = mid to high
            sum += A[j]
            if sum > right-sum
                // max-right 갱신
                right-sum = sum
                max-right = j

        return (max-left, max-right, left-sum+right-sum)

## Cost
`Find-Max-Crossing-Subarray`와 이것의 호출을 포함하는 `Find-Max-Subarray`는 for 루프에 의해 명백히 O(n)의 시간 복잡도를 가진다. 그리고 n-length에서의 호출은 2번의 (n/2)-length에서의 호출 두 번과 O(n)의 연산 한 번을 포함하므로, 다음과 같이 나타낼 수 있다.

    T(n) = 2xT(n/2) + O(n)

즉, 이를 풀면,

    T(n) = O(nlogn)


# Strassen Algorithm
슈트라센 알고리즘(Strassen algorithm)은 행렬곱(matrix multiplication)을 빠르게 해낼 수 있는 알고리즘이다. 보통의 행렬곱은 O(n^3)의 시간 복잡도를 요구하기 때문에, 행렬의 크기가 커질 수록 그것의 코스트는 답이 없이 커진다. 

슈트라센 알고리즘은 어떻게 구현하며, 이는 어느 정도의 시간 복잡도를 가질까?

기본 아이디어는 이렇다. 어떤 (n)x(n) 행렬에 대해, 일곱 번(not 8이란 사실이 중요하다)의 (n/2)x(n/2) 사이즈 submatrix의 재귀적 행렬 곱을 수행하고, 이후 O(1)의 몇 번의 덧셈을 수행한다. 이렇게 말하면 잘 와닿지 않을 것 같다. 분할 정복의 관점에서 바라보자.

- Divide : 각 행렬을 4개의 (n/2)x(n/2) 사이즈 부분행렬(submatrix)로 나눈다.(O(1)) 이후, 이들끼리의 sum 혹은 difference인 10개의 행렬을 만든다.(O(n^2))
- Conquer : 재귀적으로 일곱 번의 행렬곱을 수행해, (n/2)x(n/2) 사이즈 행렬 7개를 만든다.
- Combine : 이들을 적절히 조작해 최종적으로 행렬을 만든다. (O(n^2))

## Step
따로 pseudocode를 작성하진 않을 예정이다. 어떻게 이루어지나 확인만 해볼 것이다. 행렬 A와 B를 곱하는 상황을 생각해보자. Aij는 A의 쿼터를 나타낸다.

### Divide
행과 열이 각각 절반인 부분행렬 10개를 만드는 것부터 시작한다.

S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10
---|---|---|---|---|---|---|---|---|---
B12 - B22 | A11 + A12 | A21 + A22 | B21 - B11 | A11 + A22 | B11 + B22 | A12 - A22 | B21 + B22 | A11 - A21 | B11 + B12

### Conquer
이제 이것과 A, B의 부분행렬을 적당히 곱해 행렬 7개를 만든다.

P1 | P2 | P3 | P4 | P5 | P6 | P7
---|---|---|---|---|---|---
A11 x S1 | S2 x B22 | S3 x B11 | A22 x S4 | S5 x S6 | S7 x S8 | S9 x S10

### Combine
이들을 행렬 C로 적절히 합쳐보자.

C11 | C12 | C21 | C22
---|---|---|---
P5 + P4 - P2 + P6 | P1 + P2 | P3 + P4 | P5 + P1 - P3 - P7

이 쌩쇼를 다 하면 목표로 하던 행렬곱이 나온다고 한다. 실제로 대입해서 확인하긴 어렵지 않을 것이다. (난 안 할 거지만)

## Cost
키포인트는 행렬곱을 작은 사이즈로, 재귀적으로 수행한다는 점일 것이다. 재귀적으로 나타낸 시간 복잡도는 다음과 같다.

    T(n) = 7T(n/2) + O(n^2)

이를 풀면 

    T(n) = O(n^log_2(7)) ~ O(n^2.8074)

가 나온다. O(n^3)보다 조금 줄었다. 매우 적은 폭만큼 개선된 것 같긴 하지만, 지수가 줄어듦은 꽤 큰 의미가 있을 것이다. 행렬곱의 계산은 다른 알고리즘이 많이 있는데, 지수가 2.37대인 알고리즘도 있다고 한다.


# Solving Recurrences
앞에서 시간 복잡도를 구할 때, 재귀적으로 정의된 식을 어떻게 풀어서 계산했을까? 분할 정복을 통해 문제를 해결하면 보통 (base-case를 제외하고) 아래와 같은 형식이 나온다.

    T(n) = aT(n/b) + D(n) + C(n) (각 항은 divide, conquer, merge에 해당될 것이다)

이를 위한 세 가지 방법이 있다.

## Substitution Method
이 방법은 솔루션을 미리 예측해, 귀납법(mathematical induction)을 사용해 그것이 맞음을 증명하는 방식이다. 굉장히 무식한 방법처럼 보일지 몰라도, 가정을 잘 세웠다면 (또는 잘 유추해냈다면) 꽤 효과적인 방식일 수 있다.

예제 하나를 가져와 봤다.

    T(n) = 8T(n/2) + O(n^2)
    
여기서 T(n) = O(n^3)으로 추측할 것이고, 실제로 그렇다. T(n) <= dn^3으로 놓고, O(n^2) 부분은 cn^2이라 하자.

    T(n)  <= 8d(n/2)^3 + cn^2
          = dn^3 + cn^2
          ...?

여기서 문제가 생겼다. 적절한 d를 찾을 수 없다. 이럴 땐 우린 조금 전략을 틀어 생각해볼 수 있다. 가정에서, T(n)에 lower-term을 빼주어 새로 풀어보자. T(n) <= dn^3 - d'n^2로 놓고 다시 해보자.

    T(n)  <= 8(d(n/2)^3 - d'(n/2)^2) + cn^2
          = dn^3 - 2d'n^2 + cn^2
          = (dn^3 - d'n^2) - d'n^2 + cn^2
          # 이 때, c <= d'로 잡는다
          <= dn^3 - d'n^2
          

## Changing Variables
약간의 대수적 조작(algebraic manipulation)을 가해, 복잡해 보이는 재귀식을 조금이나마 친숙한 걸로 바꿔보자.

    T(n) = 2T(floor(sqrt(n))) + log_2(n)
    
보기만 해도 욕이 나온다. 하지만 m = log_2(n)으로 바꿔놓고 보면,

    T(2^m) = 2T(2^(m/2)) + m          # 이 때, S(m) = T(2^m)으로 바꾼다.
    S(m) = 2S(m/2) + m                # 친숙한 식이 되었다.
    S(m) = O(mlog_2(m))
    T(n) = T(2^m) 
         = S(m) 
         = O(mlog_2(m)) 
         = O(log_2(nlog_2(log_2(n))))
    
풀어 놓고 보니 흉악한 식이 그지없다. 그냥 풀었으면 가우스도 눈물 흘렸을 것이다.

## Recursion Tree
재귀 트리(recursion tree)는 재귀 호출의 각 층에 따른 코스트를 트리로 나타내어 재귀식을 푸는 방식이다. 정확히는 괜찮은 추측(guess)을 만드는 방법인데, 이는 substitution method로 검증할 수 있다. 예시로, 다음과 같이 정의된 재귀식을 풀어보자.

    T(n) = 3T(floor(n/4)) + O(n^2)
    
Big-O notation을 풀어 cn^2로 나타내어 보자. `T(n)`의 재귀 트리는 첫 호출에선 하나의 cn^2, 이후 3개의 자식 노드를 만들고, 각각은 c(n/4)^2가 된다. 그 다음은 9개가 c(n/16)^2, ... 하다가 T(1)에 수렴하게 된다. 전체 트리의 층과 마지막 리프 노드의 개수를 아는 것도 중요한데, `n/(4^i) = 1`인 i를 찾으면 되므로 트리의 층, i는 `log_4(n)`이고, 그에 따라 리프 개수는 `3^(log_4(n))`, 즉, `n^log_4(3)`이다. 이를 적용하면 아래와 같이 `T(n)`d을 나타낼 수 있다.

    T(n) = cn^2 + 3/16cn^2 + (3/16)^2cn^2 + ... + (3/16)^(log_4n-1)cn^2 + O(n^log_4(3))

등비수열의 합이다. 마지막 항은 트리의 리프 노드, `T(1)`의 개수가 `n^log_4(3)`개이므로, big-O나 big-theta로 위와 같이 나타낼 수 있다. 그 이후에 있을 항도 포함시켜서 등비급수로 전환해 부등호로 나타내면, `O(n^2)`이 됨을 알 수 있다. 앞에서도 언급했지만, 필요하다면 susbstitution method로 검증해보자.

## Master Method
마스터 정리(master method)는 `T(n) = aT(n/b) + f(n)`과 같이 주어진 재귀식을 보다 일반적으로, 그 bound를 알아낼 수 있는 방법이다. 세 가지의 가능한 경우가 있다. 편의상 `k = n^(log_b(a))`라 하자. `e`는 어떤 적당한 상수다.

1. `k`가 `f(n)`보다 크다면, 즉, `f(n) = O(n^(log_b(a-e)))`이면 `T(n) = Theta(k)`이다.
2. `k`가 `f(n)`과 comparable하다면, 즉, `f(n) = Theta(n^(log_b(a)))`이면 `T(n) = Theta(k lg(n))`이다. 
3. `f(n)`이 `k`보다 크다면, 즉, `f(n) = Omega(n^(log_b(a+e)))`이면 `T(n) = Theta(f(n))`이다.

여기서 주의해야 할 점은, 재귀이기 때문에, a는 1보다 같거나 커야 하고, b는 1보다 커야 한다. 코스트가 점점 작아져야 하기 때문이다. 또, 다항함수거나 어떤 다항함수보다 작아야 하는 조건이 있기도 하다. 이는 위의 `k`와 비교하기 위함이다.

또한, 3번의 경우, `f(n)`은 regularity condition을 만족해야 한다. 이 또한 재귀에서 코스트가 작아져야 하기 때문인데, 큰 수 `n`에 대해 `af(n/b) <= cf(n)` 인 `c<1`이 있으면 된다(저 식의 의미를 잘 파악하자). 다만, `f(n)`이 다항함수면 이를 굳이 체크할 필요가 없다. 

이제 예시로 하나 풀어보고 끝내자. Strassen algorithm의 시간 복잡도를 유도할 생각이다.

    T(n) = 7T(n/2) + Theta(n^2)
    
여기서 시작하자. `n^(log_b(a)) = n^(log_2(7))`이다. 이는 n^2보다 asymptotical, 그리고 polynomial하게 크다. 즉, 3번 케이스를 적용하여

    T(n) = Theta(n^(log_2(7)))
    
와우.


# 마치며
드디어 기나기니 분할 정복의 지옥이 끝난 것 같다. 하지만 과제로 분할 정복을 받아서 난 끝나지 않았다. 다음에 뭘 할지는 교수님 마음에 달렸다.
