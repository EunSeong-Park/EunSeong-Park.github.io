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

그렇다면 자연스럽게, 

$$\hat{M_t} = \frac{1}{2}(Y_t + Y_{t-1})$$

로 이어지고, Y_t에서 트렌드를 제거한(detrended) 시계열은 다음과 같이 표현된다.

$$Y_t - \hat{M_t} = Y_t - \frac{1}{2}(Y_t + Y_{t-1}) = \frac{1}{2}\nabla Y_t$$

그럼으로써, $M_t$가 *임의의 두 인접한 시점에서 근사적으로 상수*라는 가정은 $Y_t$의 first difference를 정상 프로세스로 만들어준다.

또한, $M_t$가 시간에 따라 천천히 변화한다는 가정, 즉, $M_t = M_{t-1} + \epsilon_t (\text{where }\epsilon_t \text{ is white noise series}{})$으로 다음을 이끌어 낼 수 있다.

$$\nabla Y_t = \nabla M_t + \nabla e_t = \epsilon_t + e_t - e_{t-1}$$

그리고 이는 $MA(1)$ 프로세스의 autocorrelation function을 가진다.

$\rho_1 = -\frac{1}{2 + \frac{\sigma_\epsilon^2}{\sigma_e^2}}$

### Second difference
이제 first difference의 개념을 쉽게 second, 또는 further order로 확장시킬 수 있을 것이다. *$M_t$가 임의의 세 시점에 대해 linear하다*고 가정하자. 그러면 우리는 $M_t$를 다음과 같은 objective function을 가지고 추정할 수 있다.

$$\text{Minimize } \sum_{j=-1}^1 (Y_{t-j} - (\beta_{0,t}+j\beta_{1,t}))^2$$

결국, $\hat{M_t} = \frac{1}{3}(Y_{t+1} + Y_t + Y_{t-1})$이다. Detrended series는 어떨까?

$$\begin{aligned}
Y_t - \hat{M_t} &= Y_t - \frac{1}{3}(Y_{t+1} + Y_t + Y_{t-1}) \\ &= - \frac{1}{3}(Y_{t+1} - 2Y_t + Y_{t-1}) \\ &= -\frac{1}{3}\nabla(\nabla Y_{t+1}))
= - \frac{1}{3}\nabla^2 Y_{t+1}
\end{aligned}$$

여기서 $\nabla^2 Y_{t+1}$은 $(Y_{t+1} - Y_t) - (Y_t - Y_{t-1})$이다. 그리고 아까와 비슷하게,

$Y_t = M_t + e_t\; /\; M_t = M_{t-1} + W_t \;/\; W_t = W_{t-1} + \epsilon_t$

라면,

$$\begin{aligned}
\nabla^2 Y_t &= \nabla W_t + \nabla^2e_t \\ &= \epsilon_t + (e_t - e_{t-1}) - (e_{t-1} - e_{t-2}) \\ &= \epsilon_t + e_t - 2e_{t-1} + e_{t-2}
\end{aligned}$$

이고, 이는 $MA(2)$ 프로세스의 autocorrelation function을 가진다. 또, nonstationary process인 {$Y_t$}의 second difference가 stationary라는 점도 주목할 만하다.


# ARIMA Model
**어떤 시계열 {$Y_t$}의 $d^{th}$ difference, $W_t = \nabla^d Y_t$가 stationary ARMA 프로세스일 때, 그 시계열을 ARIMA 프로세스라고 한다.** 조금 더 자세하게, {$W_t$}가 **ARMA**$(p, q)$ 모델을 따를 때, {$Y_t$}는 **ARIMA**$(p,d,q)$와 같이 표현한다. 또, {$W_t$}가 **MA**($q$)모델을 따른다면, 간단하게 **IMA**($d,q$)와 같이 표현한다.

일반적으로 우리는 $d=1, d=2$인 케이스만을 다룬다. 참 다행인 일이다!

## Examples
### ARIMA($p, 1, q$)
먼저, **ARIMA**($p, 1, q$) 모델을 생각해보자. $d=1$이므로, $W_t = Y_t - Y_{t-1}$로 놓고 다음과 같은 식을 얻을 수 있다.

$$W_t = \phi_1W_{t-1} + \phi_2W_{t-2} + \cdots + \phi_pW_{t-p} \newline +e_t - \theta_1e_{t-1} - \theta_2e_{t-2}-\cdots - \theta_qe_{t-q}$$

또는 $W_t$의 정의에 따라 다음과 같이 쓸 수도 있다.

$$Y_t - Y_{t-1} = \phi_1(Y_{t-1} - Y_{t-2}) + \phi_2(Y_{t-2}-Y_{t-3}) + \cdots + \phi_p(Y_{t-p}- Y_{t-p-1}) \newline +e_t - \theta_1e_{t-1} - \theta_2e_{t-2}-\cdots - \theta_qe_{t-q}$$

마지막으로, 다음과 같이 정리한 형태를 **difference equation form**이라고 한다.

$$Y_t = (1+\phi_1)Y_{t-1} + (\phi_2 - \phi_1)Y_{t-2} + \cdots + \phi_p Y_{t-p-1} \newline +e_t -\theta_1 e_{t-1} - \theta_2e_{t-2} - \cdots \theta_q e_{t-q}
$$

이렇게 보면, **ARIMA**($p, 1, q$)의 difference equation form은 **ARMA**($p+1, q$)의 형태로 나타나는 것 같다. 그런데, 이것의 characteristic polynomial은...

$$1-(1+\phi_1)x + (\phi_2 - \phi_1)x^2 + \cdots + (\phi_p-\phi_{p-1})x^p -\phi_px^{p+1} \newline = (1-\phi_1x-\phi_2x^2-\cdots-\phi_px^p)(1-x)$$

$x=1$이란 근이 명확히 있고, 이것으로부터 우리는 이 프로세스가 nonstationary임을 알 수 있다. 한편, $(1-x)$를 제외한 나머지는 stationary process, $\nabla Y_t$의 characteristic polynomial이기도 하다.

### IMA($1,1$)
앞서 언급하였듯, **ARIMA**$(p,d,q)$에서 $p=0$이면 우리는 그것을 **IMA**($d,q$)와 같이 부른다. 즉, $Y_t - Y_{t-1} = e_t - \theta e_{t-1}$이니,

$$Y_t = Y_{t-1} + e_t -\theta e_{t-1}$$

그리고 이걸 적당히 변형(?)하면, 다음과 같이 표현할 수 있다.

$$Y_t = e_t + (1-\theta)e_{t-1} + (1-\theta)e_{t-2} + \cdots + (1-\theta)e_{-m} -\theta e_{-m-1}$$

**ARMA** 모델과 다르게, 화이트 노이즈에 들어간 weight는 과거 시점으로 가도 죽어가지 않는다는 점을 볼 수 있다.

마지막으로 분산과 자기상관을 확인해볼까?

- $Var(Y_t) = (1+\theta^2 + (1-\theta)^2(t+m))\sigma_e^2$
- $Corr(Y_t, Y_{t-k}) = \frac{(1-\theta +\theta^2 + (1-\theta)^2(t+m-k))\sigma_e^2}{\sqrt{Var(Y_t)Var(Y_{t-k})}} \approx \sqrt{\frac{t+m-k}{t+m}} \approx 1 $

적당하게 큰 $m$과 적당한 $k$에 대해, autocorrelation이 꽤 강한 경향을 보인다.

### IMA($2,2$)
**IMA**($2,2$) 모델은 다음과 같이 표현할 수 있다.

$$\nabla^2 Y_t = e_t - \theta_1 e_{t-1} - \theta_2 e_{t-2}$$

또는,

$$Y_t = 2Y_{t-1} -Y_{t-2} + e_t - \theta_1e_{t-1} - \theta_2 e_{t-2}$$

이건 계산이 화딱지나니 생략한다. 하지만 식을 통해 직관적으로 알 수 있는 몇 가지 사실이 있다.

- 분산은 $t$를 따라 빠르게 증가한다.
- Time lag, $k$에 대한 자기상관은 적당한 $k$에 대해선 1에 가깝다.

## Constant Terms in ARIMA
**ARIMA**($p,d,q$) 모델에서, $\nabla^dY_t=W_t$는 stationary **ARMA**($p,q$) 프로세스다. 그런데 우리는 기본적으로 정상적인 모델은 zero mean을 가진다고 가정했는데, $W_t$가 nonzero mean, $\mu$를 가진다면?

$$W_t -\mu = \phi_1W_{t-1} + \phi_2W_{t-2} + \cdots + \phi_pW_{t-p} \newline +e_t - \theta_1e_{t-1} - \theta_2e_{t-2}-\cdots - \theta_qe_{t-q}$$

와 같이 나타내거나,

$$W_t = \theta_0 + \phi_1W_{t-1} + \phi_2W_{t-2} + \cdots + \phi_pW_{t-p} \newline +e_t - \theta_1e_{t-1} - \theta_2e_{t-2}-\cdots - \theta_qe_{t-q}$$

와 같이 constant term, $\theta_0$을 도입하는 방법도 있다.

# Other Transformations
## Logarithm
$Y_t$가 인접한 시점에 대해 어느 정도 stable한 percentage change를 가지고 있다고 가정하여, 이를 다음과 같이 표현해보자.

$$Y_t = (1+X_t)Y_{t-1}$$

여기서 $100X_t$는 $Y_{t-1}$에서 $Y_t$로의 percentage change다. 이를 logarithm으로 표현하면

$$log(Y_t) - log(Y_{t-1}) = log(Y_t / Y_{t-1}) = log(1+X_t) $$

와 같다. 그에 따라, 이 logarithm의 first difference는 $\nabla(log(Y_t)) = log(1+X_t)$고, $\vert X_t \vert$가 적당히 작다면($<0.2$), 이는 $X_t$로 근사될 수 있다. 즉,

$$\nabla(log(Y_t)) \approx X_t$$
