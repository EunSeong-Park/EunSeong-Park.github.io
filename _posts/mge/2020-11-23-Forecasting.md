---
title: "[Time Series Analysis 7] forcasting"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
지금까지 모델을 결정하고, 파라미터를 추정하고, 그렇게 만든 모델을 진단하는 작업까지 해왔다! 여기서 **"우리는 왜 모델링을 할까?"** 라고 생각하면 그에 대한 답이 여럿 있겠지만, 가장 중요한 이유 중 하나는 미래의 값을 **예측**하기 위함일 것이다. 

우리는 얻은 모델을 바탕으로 미래의 값을 예측하며, 그에 대한 정확도를 평가할 것이다. 어떻게? 이번 포스팅에서 간단하게나마 알아보도록 하자. 간단하게!


# Forecasting
어떤 시계열, {$Y_t$}가 $1, 2, \cdots, t\;(t: \text{forecast origin})$까지 관측되었다고 가정하자. 우리가 forecasting으로 얻고 싶은 값은 아마 $Y_{t+l}\;(l: \text{lead time})$ 일 것이다. 

## Minimum MSE Forecasting
**Minimum MSE(Mean Square Error) forcast**는 다음과 같이 표현된다.

$$\hat Y_t(l) = E(Y_{t+l} \vert Y_1, Y_2, \cdots, Y_t)$$

### Deterministic Trend
여기서 deterministic trend model(즉, $Y_t = \mu_t + X_t$)을 생각해보자. 그럼 다음과 같이 표현할 수 있을 것이다.

$$\begin{aligned}
\hat Y_t(l) &= E(Y_{t+l} \vert Y_1, Y_2, \cdots, Y_t) \\ 
&= E(\mu_{t+l} + X_{t+l} \vert Y_1, Y_2, \cdots, Y_t) \\
&= E(\mu_{t+l} \vert Y_1, Y_2, \cdots, Y_t) \\ &\quad + E(X_{t+l} \vert Y_1, Y_2, \cdots, Y_t) \\
&= \mu_{t+l}
\end{aligned}$$

즉, forecast는 $\hat Y_t(l) = \mu_{t+l}$, forecast error는 $e_t(l) = Y_{t+l} - \hat Y_t(l) = X_{t+l}$이다. 또한, 이에 따라 오차의 평균($E(e_t(l))$는 $0$, 분산은 $\gamma_0$이다.

### AR Forecasting
Non-zero mean **AR(1)** 프로세스를 생각해보자.

$$Y_{t+1} - \mu = \phi(Y_{t} - \mu) + e_t$$

식을 적당히 정리하여 conditional expectation을 적용하면...

$$\hat Y_t(1) - \mu = \phi(E(Y_t \vert Y_1, \cdots, Y_t) -\mu) + E(e_{t+1} \vert Y_1, \cdots, Y_t) = \phi(Y_t -\mu)$$

이러한 규칙에 따라, 우리는 $\hat Y_t(l) - \mu$를 재귀식으로 표현할 수 있다. 이를 적당히 풀면 다음과 같은 결과를 얻는다.


$$\hat Y_t(l) = \mu + \phi^l (Y_t - \mu)$$

이 때, 적당히 큰 $l$에 대해, forecast는 $\mu$와 비슷해짐을 알 수 있다. 

### MA Forecasting
Non-zero mean **MA(1)** 프로세스를 생각해보자.

$$Y_{t+1} - \mu = e_{t+1} - \theta e_{t}$$

Conditional expectation을 적용해보자.

$$\hat Y_t(1) = \mu + E(e_{t+1} \vert Y_1, \cdots, Y_t) - \theta E(e_t \vert Y_1, \cdots, Y_t) = \mu - \theta e_t$$

아까와 비슷한 방법으로, $l>1$인 $l$에 대해 $\hat Y_t(l) = \mu$를 이끌어낼 수 있다.

### ARIMA Forecasting
간단한 **ARIMA** 모델 중 하나인 random walk with drift를 생각해보자. 

$$Y_{t+1} = Y_t + \theta_0 + e_{t+1}$$

Conditional expectation을 적용해보자.

$$\hat Y_t(1) = E(Y_t \vert Y_1, \cdots, Y_t) + \theta_0 + E(e_{t+1} \vert Y_1, \cdots, Y_t) = Y_t + \theta_0$$

따라서, $l > 1$에 대하여,

$$\hat Y_t(l) = Y_t + \theta_0 l$$

forecast error는 $\sum_{i=1}^l e_{t+i}$이고, 그것의 분산은 $l\sigma_e^2$다.