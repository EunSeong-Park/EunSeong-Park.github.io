---
title: "[Time Series Analysis 8] Seasonal Models"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
앞서 몇 번 seasonal trend를 지닌 시계열 데이터와 모델을 보았다. 이번엔 조금 더 일반적인 경우를 포용하기 위해, **stochastic seasonal model**들을 알아보도록 하자.


# Seasonal ARIMA Models
다음과 같은 monthly series model을 생각해볼 수 있다.

$$Y_t = e_t - \Theta e_{t-12}$$

이 경우,

- $Cov(Y_t, Y_{t-1}) = Cov(e_t - \Theta e_{t-12}, e_{t-1} - \Theta e_{t-13}) = 0$
- $Cov(Y_t, Y_{t-12}) = Cov(e_t - \Theta e_{t-12}, e_{t-12} - \Theta e_{t-24}) = -\Theta \sigma_e^2$

오, 꽤 흥미롭다! 

## Seasonal MA
아무튼 이런 아이디어를 가져와, 우선 주기가 $s$인 **seasonal MA(Q)**를 생각할 수 있다.

$$Y_t = e_t - \Theta_1 e_{t-s} - \Theta_2 e_{t-2s} - \cdots - \Theta_Q e_{t-Qs}$$

그리고 이 모델의 MA characteristic polynomial은 다음과 같이 나타낼 수 있을 것이다.

$$\Theta(x) = 1- \Theta_1 x^s - \Theta_2 x^{2s} - \cdots - \Theta_Q x^{Qs}$$

우리는 이로부터 다음과 같은 사실을 알아낼 수 있다.

- 이 모델은 항상 정상적이다.
- ACF는 seasonal lags($s, 2s, \cdots, Qs$)에 대해서만 non-zero일 수 있다.
- 이 모델이 가역(invertible)이려면, $\Theta(x)=0$의 모든 근의 절댓값이 $1$을 초과해야 한다.

## Seasonal AR
비슷한 방식으로, 주기가 $s$인 **seasonal AR(P)** 모델도 생각해 볼 수 있다. 이렇게!

$$Y_t = \Phi_1 Y_{t-s} + \Phi_2 Y_{t-2s} + \cdots + \Phi_P Y_{t-Ps} + e_t$$

그리고 AR characteristic polynomial은...

$$\Phi(x) = 1 - \Phi_1x^{s} - \Phi_2x^{2s} - \cdots - \Phi_Px^{Ps}$$

Seasonal AR은 다음과 같은 성질을 가지고 있다.

- $e_t$는 $Y_{t-1}, Y_{t-2}, \cdots$에 대해 독립적이어야 한다.
- 이 모델이 정상적(stationary)이려면, $\Phi(x)=0$의 모든 근의 절댓값이 $1$을 초과해야 한다.
- ACF는 seasonal lags($s, 2s, \cdots, Qs$)에 대해서만 non-zero일 수 있다.

## Multiplicative Seasonal ARMA Models
하지만 이상과 달리 위에서 본 모델처럼 seasonal lag에서만 ACF가 들어가는 케이스는 현실에 별로 없다. 그래서 우리는 seasonal model과 non-seasonal model을 결합함으로써, **기본적으로 seasonal ARMA를 따르되, 주변의 데이터와 어느 정도의 자기상관을 가지는 모델**을 고안해낼 수 있다.

예시로 다음과 같은 경우를 생각해볼 수 있다. 어떤 MA characteristic polynomial이 이렇게 생겼다고 하자.

$$(1-\theta x)(1- \Theta x^{12}) = 1 - \theta x - \Theta x ^{12} + \theta\Theta x^{13}$$

확실히 RHS가 MA characteristic polynomial의 형태를 띠니 문제될 것은 없어보인다. 아무튼 이는 다음과 같은 시계열 모델과 대응된다.

$$Y_t = e_t - \theta e_{t-1} - \Theta e_{t-12} + \theta \Theta e_{t-13}$$

이 경우, ACF는 $12$에서 확연히 크지만, 그 근처의 값인 $1, 11, 12, 13$도 ACF가 non-zero일 수 있다.

이제 이를 조금 일반화 하면, 우리는 **multiplicative seasonal model**, **ARMA(p, q)$\times$(P, Q)$_s$** 를 seasonal period가 $s$이면서, AR characteristic polynomial이 $\phi(x)\Phi(x)$고 MA characteristic polynomial이 $\theta(x)\Theta(x)$인 모델로 정의할 수 있다. (추가로, constant term, $\theta_0$도 생각해볼 수 있다)

## Nonstationary Seasonal ARIMA Models
점점 맛이 간다.. 아무튼 여기서 우리는 새로운 연산, **seasonal difference**를 정의해보자.

$$\nabla_sY_t = Y_t - Y_{t-s}$$

직관적으로, 바로 전 주기에 해당하는 데이터와 differencing을 한다고 보면 될 것 같다. 이걸로 뭘 하냐? **multiplicative seasonal ARIMA model**을 정의할 것이다. 허미... 아무튼 differencing으로 **ARIMA**를 정의하는 과정과 꽤 비슷하다.

$$ W_t = \nabla^d\nabla_s^DY_t $$

에서, $W_t$가 **ARMA(p,q)$\times$(P,Q)$_s$** 모델인 경우, 우리는 원래 모델, {$Y_t$}를 **ARIMA(p,d,q)$\times$(P,D,Q)$_s$** 로 정의한다. 와! 직접 하면 죽어나가겠지만, 우리는 컴퓨터가 다 해줄테니 뭐 괜찮다.

