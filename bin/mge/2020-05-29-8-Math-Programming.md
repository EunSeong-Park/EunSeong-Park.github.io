---
title: "[OM 8] Mathematical Programming"
tags: Management-Engineering OM
toc: true
---

# Intro
이전 포스트에서, 미래의 동향을 예측하는 forecasting을 알아보았다. 이는 predictive analysis의 일종이었는데, 이번엔 prescriptive analytics, 즉, 이후 운영 및 관리의 방향을 설정하기 위한 분석을 알아볼 것이다. 그 중에서도, mathematical programming을 중심으로 살펴보자. 딱 봐도 수학 냄새가 풀풀 난다.


# Mathematical Programming
Mathematical programming은 어떤 (시간, 자본 등과 같은) 제한 요인 하에서의 최적의 솔루션을 찾기 위해 사용된다. 최적화 하려는 목적 함수의 종류나, 해결 방식에 따라 여러 종류로 나뉘어진다. 예를 들어, LP(linear programming)은 선형 목적 함수 및 contraint를 다루고, NLP는 비선형적 함수를 다룬다.

우리는 어떤 프로세스에 대하여, 주어진 상황을 인풋으로 보고, 이에 대한 적절한 수학적 모델을 적용하여 그 상황에 알맞는 최적화된 계획 또는 결과를 이끌어낼 수 있다.

![](/imgs/mge/om34.png)

Mathematical programming에 의한 최적화는 그 적용 범위가 굉장히 넓다. 재고 관리(inventory management)에도, 재무 관리에도, 투자 비율 결정에도, 혹은 일상 속에서의 의사 결정에도 다방면으로 활용할 수 있다. 

여기선 어떤 종류의 mathematical programming이 있는지만 대충 알아볼 것이다.

## Linear Programming
LP(Linear Programming)에 관한 기초적인 내용은 [이전 포스트](https://eunseong-park.github.io/2020/05/18/Optimization.html) 에 작성해두었다. 그래서 LP에 관한 과정 및 디테일은 생략할 예정이다.

## Integer Programming
IP(Integer Programming)은 이산적인(discrete) 대상의 최적화를 위한 기법이다. Integer라고 해서 반드시 정수만을 가질 필욘 없고, 이산적인 변수 및 함수를 가진다는 게 중요하다. 

Traveling salesman problem(TSP)은 IP의 대표적인 예시다. 주어진 지점들을 모두 방문하면서, 최단 경로를 짜는 문제다. 

![](/imgs/mge/om35.png)

이러한 점에서, 각종 그래프 탐색 문제도 IP로 해결이 가능할 것처럼 보인다. 저 문제도 결국 그래프화해서 다익스트라 등으로 풀 수 있단 점을 생각해보면...

## Nonlinear Programming
목적 함수가 non-linear하다면 어떨까? 상황은 조금 더 복잡해진다. LP 때 처럼 몇 개의 코너를 확인하는 것만으론 부족하다.

![](/imgs/mge/om36.png)

![](/imgs/mge/om37.png)

이처럼, optimal solution이 어디에나 있을 수 있다. 좀 더 똑똑한 방법이 필요한 셈이다. 물론 그 방법을 여기서 논의하지는 않는다.


# 마치며
LP 부분 빼니까 쓸 게 없다 어엌ㅋㅋ