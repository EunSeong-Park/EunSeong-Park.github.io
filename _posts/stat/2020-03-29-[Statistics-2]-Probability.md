---
title:  "[Statistics 2] Probability"
tags: Statistics
toc: true
---

# Intro
이제 확률(probability)에 대한 간단한 내용을 살펴보려 한다. 몇 번은 배운 내용이고, 내용 자체도 쉬우니 빠르게 넘어가자.


# Definitions
다 아는 내용이므로 예시를 써가며 설명할 필요는 없을 것 같다. 굳이 한국어로 적을 필욘 없어보여서 영어로 쓴다.

## Basic Terminology
- __Experiment__ : any process that produces an observation
- __Outcome__ : the observation by experiment
- __Sample space(S)__ : the set of all possible outcomes
- __Event(E)__ : subset of sample space, S

Event에 대한 intersection, union, complement 등은 모두 생략한다.

## Probability of Event
어떤 event, $E$의 __확률(probability)__ 을 다음과 같이 정의한다.

$P(E) = \frac{n(E)}{n(S)}$

$n(E), n(S)$는 각 집합에 포함된 원소의 수를 의미한다. 그런데 이런 의문이 들 수 있다. "그럼 로또는 1등부터 5등, 그리고 꽝이 있으니 1등 확률은 $\frac{1}{6}$이겠네?" 물론 이건 터무니없는 소리지만, 저 정의대로 생각하면 반박할 수 없기도 하다.

그래서 우리는 다음과 같은 가정을 추가한다.

> Each outcome in the sample space S is equally likely to occur.

이러면 위의 질문은 가정을 만족하기 위해 수정되어야 한다. 이제 "일단은" 정의에 문제가 없는 것으로 보인다.


# Properties of Probability
## Axioms of Probability
아래의 세 성질은 확률의 공리(axiom)이다. 즉, 증명을 필요로 하지 않지만, 이들은 충분히 납득할 수 있을 정도로 직관적이기 때문에 가벼운 마음으로 보자.

1. $0 \le P(A) \le 1$ 
2. $P(S) = 1$
3. If $A$ and $B$ are disjoint, $P(A \cup B) = P(A) + P(B)$

이제 위의 세 공리를 이용해 몇 가지 유용한 정리를 이끌어낼 것이다.

## Properties
모두 증명이 쉬운 성질들이지만, 그래도 적어놨다.

$P(A^c) = 1 - P(A)$
<details>
	<summary>Proof</summary>
	<ul>
		<li>$P(S) = P(A \cup A^c)$</li>
		<li>$P(S) = P(A) + P(A^c)$ ($A$ and $A^c$ are disjoint, and by axiom 3)</li>
		<li>$1 = P(A) + P(A^c)$ (by axiom 2)</li>
		<li>$P(A^c) = 1 - P(A)$</li>
	</ul> 
</details>

$P(A \cup B) = P(A) + P(B) - P(A \cap B)$
<details>
	<summary>Proof</summary>
	<ul>
		<li>$A = (A-B) \cup (A \cap B) $ (and they are disjoint)</li>
		<li>$B = (B-A) \cup (A \cap B) $ (and they are disjoint)</li>
		<li>$P(A) = P(A-B) + P(A \cap B)$ (by axiom 3)</li>
		<li>$P(B) = P(B-A) + P(A \cap B)$ (by axiom 3)</li>
		<li>$P(A) + P(B)$ $= P(A-B) + P(B-A) + 2P(A \cap B)$ </li>
		<li>$P(A) + P(B)$ $= 2P(A \cap B) + P((A-B) \cup (B-A))$ (disjoint)</li>
		<li>$P((A-B) \cup (B-A)) + P(A \cap B)$ $= P(((A-B) \cup (B-A)) \cup (A \cap B)) = P(A \cup B)$ </li>
		<li>So, $P(A) + P(B) = P(A \cap B) + P(A \cup B) $</li>
		<li>$P(A \cup B) = P(A) + P(B) - P(A \cap B)$</li>
	</ul> 
</details>

생각보다 정리할 게 별로 없다. 기초적인 확률 계산은 공리와 이 성질들만 써도 문제 없다. "계산은"...


# Conditional Probability
__조건부 확률(conditional probability)__ 은 어떤 event가 발생했을 때 다른 event가 발생할 확률을 의미한다. "다른 event"라고는 했지만, 구분을 위해 그렇게 불렀을 뿐, 같은 event여도 문제가 되진 않는다.

Conditional probability of B given that A, 즉, A가 발생했을 때 B가 발생할 확률은 $P(B \vert A)$와 같이 표기한다. 

## Properties
아래는 가장 간단한 multiplication rule이다. Non-empty event인 $A$에 대해 다음과 같은 식이 성립한다.

$P(B \vert A) = \frac{P(A \cap B)}{P(A)}$

이는 아래와 같이 표현할 수도 있다.

$P(A)P(B \vert A) = P(A \cap B)$

또, 더욱 일반화하여 다음과 같은 식도 성립한다.

$P(A_1 \cap A_2 \cap ... \cap A_n)$ $= P(A_1)P(A_2 \vert A_1)P(A_3 \vert A_1 \cap A_2)...P(A_n \vert A_1 \cap ... \cap A_{n-1})$

## Independence
두 event에 대해, 한 event의 발생 여부가 다른 event의 확률에 영향을 주지 않는다면, 두 event는 독립적(independent)이라고 한다. 더 정확히 정의하면, $P(A \cap B) = P(A)P(B)$일 때 $A$와 $B는 독립이다. 또, 독립이면 위의 식을 만족한다.

이는 empty하지 않은 $A$와 $B$에서 그 의미가 직관적으로 다가온다. 왜냐?

$P(A \vert B)$ $= \frac{P(A \cap B)}{P(B)}$ $= \frac{P(A)P(B)}{P(B)}$ $=P(A)$

보통 empty한 event와 임의의 event는 서로 독립인 걸로 본다(어떤 책은 non-zero probability를 독립 조건에 추가하기도 한다). 다만 empty한 event의 경우 바로 위의 공식이 유도될 수 없다. 분모가 0이 되기 때문이다.

독립의 정의는 임의의 $n$개의 event에도 적용될 수 있다.


# 마치며
예제를 안푸니 굉장히 빨리 끝난다.

