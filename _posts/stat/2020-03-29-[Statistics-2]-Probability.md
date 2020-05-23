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
어떤 event, $E$의 확률(probability)을 다음과 같이 정의한다.

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