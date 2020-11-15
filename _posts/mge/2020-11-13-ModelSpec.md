---
title: "[Time Series Analysis 4] Model Specification"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
지금까지 우리는 여러 stationary / nonstationary 모델들을 알아보았는데, 이젠 **주어진(관측된) 시계열 데이터에 대해 어떤 모델을 적용할지** 결정할 방법에 대해 알아보자. 가령 다음과 같은 의문들을 떠올리고, 그에 대한 답을 찾아볼 수 있을 것이다.

- 주어진 데이터가 stationary할까, nonstationary할까?
- 가령 **ARIMA**($p,d,q$) 모델을 사용한다면, 파라미터 $p,d,q$는 어떻게 정해야 할까?
- 피팅한 모델이 적절할까? 혹은 이를 더욱 개선할 수 있을까?

이번엔 간단히, 그리고 얕게 여러 개념들을 살펴보자.


# ACF, PACF, EACF
## AutoCorrelation Function
어떤 적당한 정상적 시계열 데이터를 가지고, 그것의 sample ACF를 생각해보자. 가령 어떤 time lag, $q$ 이후로 ACF가 **cut-off** 당한다면, 우리는 아마 **MA**($q$)를 해당 시계열의 유력한 후보 모델로 생각할 수 있을 것이다. 반면, 만약 ACF가 tail-off 당한다면(즉, 절대값이 점점 줄어드는 형태로 작아진다면) **AR**$(p)$일 수도, **ARMA**$(p,q)$일 수도 있다. 둘 다 tail-off 형태이기 때문에 둘의 경계가 모호하고, 심지어 $p$ 또한 명확히 드러나지 않는다.

분명한 사실은, **ACF만으론 시계열 데이터의 모델을 확정하기 어렵다**는 점이다. 그러면 우린 어떻게 해야 할까?

## Partial AutoCorrelation Function
**Partial Correlation Function** 는 어떤 요소($Z$)를 제외한 두 대상($X, Y$)의 상관관계에 대한 지표다. 

$$\rho_{XY \vert Z} = Corr(X - \hat X, Y - \hat Y)$$

여기서, $\hat X, \hat Y$는 $Z$로의 $X, Y$의 linear regression이다. 즉, $\rho_{XY \vert Z}$는 $Z$의 linear effect를 제거한 결과들 간의 상관관계다.

이제 자신에 대한 partial correlation, 즉, **PACF(Partial AutoCorrelation Function)** 또한 생각할 수 있다. 정상적 시계열의 PACF는 다음과 같이 정의될 수 있다.

- $\phi_{11} = Corr(Y_{t+1}, Y_t) = \rho_1$
- $\phi_{kk} = Corr(Y_{t+k} - \hat Y_{t+k}, Y_t - \hat Y_t)$

여기서, $\hat Y_{t+k}$, $\hat Y_{t}$는 각각 $Y_{t+k}$, $Y_t$의 linear regression on {$Y_{t+k-1}, \cdots, Y_{t+1}$}이다.

**PACF으로 우리는 AR 프로세스의 order를 추정할 수 있다.** 왜냐? 그것은 PACF의 특성 때문인데, **AR**$(p)$ 프로세스의 **PACF는 time lag, $p$ 이후에 cut-off** 당한다. 반면, **MA**($q$)나 ARMA$(p,q)$의 PACF는 tail-off된다.

즉, ACF와 PACF를 함께 쓰면 모델이 어떻게 생겨먹었는지 확인할 수 있다.

- | **AR**($p$) | **MA**($q$) | **ARMA**($p, q$)
---|---|---|---
**ACF** | Tails off | Cuts off after $q$ | Tails off
**PACF** | Cuts off after $p$ | Tails off | Tails off

아직 한 가지 문제가 더 남아있다. 우리는 이제 AR, MA, ARMA를 구분할 수 있지만, **ARMA의 각각의 order는 아직 확인할 수 없다.**

## Extended AutoCorrelation Function
**EACF**를 사용하여 ARMA 모델의 order를 추정할 수 있다. 이건 대충 살펴보고 넘어갈 생각이다. 아이디어는 다음과 같다.

1. **ARMA**($p,q$)에서 time lag, $p$를 주어, **AR**($p$) 요소를 제거한다.
2. **MA**($q$)의 cut-off 지점을 확인한다.
3. EACF 테이블을 다음과 같이 만든다.
   1. **AR**$(i)$를 필터링 한 뒤, $j+1$의 ACF 유의할 수준으로 0과 다르다면 $i,j$ 엔트리에 **X**로 마킹한다.
   2. 그렇지 않다면 **O**로 마킹한다.
4. Upper left vertex를 확인하고, 그것을 candidate로 삼는다.

![](/imgs/mge/tsa8.png)

위와 같은 경우엔, **ARMA**$(1,1)$을 모델로 삼는 게 가장 적절해보인다.

# Examples of Model Specification Problem
몇 가지 시뮬레이션된 시계열들을 통해 앞서 배운 내용을 활용해보자.

## MA($1$), $\theta=0.9$
