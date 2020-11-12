---
title: "[Time Series Analysis 3] Nonstationary Time Series"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
지난 시간엔 정상성을 지닌 시계열 데이터들을 알아보았다. 당연한 이야기지만, 모든 시계열 데이터가 정상적일 순 없고, 그것의 트렌드 또한 반드시 결정론적(deterministic)일 수도 없다. 정상적이지 않은 시계열 데이터를 표현하는 모델과 그러한 모델들을 분석하는 방법을 알아보자.


# Nonstationary Time Series
**Constant mean over time이 아닌 모든 시계열을 nonstationary하다고 한다.** 즉, $\mu$는 $t$에 의존하므로, non-constant mean function, $\mu_t$와 zero-mean stationary series, $X_t$를 이용해 다음과 같이 표현할 수 있다.

$$Y_t = \mu_t + X_t $$ 

정상적이지 않은 여러 중요한 모델들을 알아보도록 하자.

## Explosive AR
$AR(1)$ 모델을 다시 떠올려보자. 아마 다음과 같이 표현할 수 있을 것이다.

$$Y_t = \phi Y_{t-1} + e_t$$

이 때, 우리는 이 모델이 정상적이기 위해 $\vert\phi\vert < 1$이어야 함을 알고 있다. 그러면 $\vert \phi \vert > 1$인 경우엔 어떨까? 아마 데이터는 시간이 흐를 수록 지수적으로(exponentially) 증가할 것이다. $Y_0$에 대하여 $Y_t$를 다음과 같이 나타낼 수 있다.

$$ Y_t = e_t + \phi e_{t-1} + \phi^2 e_{t-2} + \cdots + \phi^{t-1}e_1 + \phi^t Y_0 $$

이러한 AR 프로세스는 그것의 지수적이고 폭발적인 경향성으로 인해, **explosive AR process**라고 불린다. 직관적으로, 분명 mean이 constant over time이 아닐 것이고, 시간에 따라 폭발적으로 증가/진동하는 양상을 보일 것이다.

## Difference
### First Difference
조금 더 reasonable한 케이스인, $\phi=1$인 $AR(1)$ 프로세스를 생각해보자. 이는 랜덤 워크(random walk)와 같다.

$$ Y_t = Y_{t-1} + e_t$$

여기서, 우리는 인접한 이전 시점과의 차이를 다음과 같이 나타낼 수 있다.

$$\nabla Y_t = e_t $$

이 때, $\nabla Y_t$를 $Y_t$의 **first difference**라고 한다. 이 경우, first difference가 화이트 노이즈인데, 우리는 랜덤 워크를 조금 더 확장하여, first difference가 화이트 노이즈가 아닌, 다른 어떤 정상 프로세스인 일반적인 모델을 생각해볼 수도 있다. 실제로, first difference가 정상 프로세스라면 여러 유용한 성질이 많다. 

이제, 다음과 같은 프로세스를 생각해보자.

$$Y_t = M_t + X_t$$

여기서 몇 가지 가정을 하자.

1. $M_t$는 시간에 따라 **"천천히"** 변화한다. 여기서 $M_t$는 결정론적일 수도, 확률론적일 수도 있다.
2. $M_t$는 두 인접한 시점에 대해 근사적으로(approximately) 상수다.
3. $X_t$는 **정상 프로세스**다.

이러한 가정에 따라, 우리는 $\beta_0$을 적절히 골라 $M_t$를 추정(estimate)할 수 있다. 어떻게? $\sum_{j=0}^{1} (Y_{t-j} - \beta_{0,t})^2$를 최소화하는 방향으로!!


