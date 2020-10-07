---
title: "[Time Series Analysis 2] Stationary Time Series"
tags: Time-Series-Analysis Management-Engineering
toc: true
---

# Intro
이번엔 정상성(stationarity)을 가정한, 혹은 실제로 그러한 시계열들을 모델링해보자. 앞서 언급하였듯, 정상성을 지닌 시계열 데이터는 여러 유용한 성질들을 지니고 있다. 

시작 전에, 다음과 같은 노테이션을 사용하자.

{$Y_t$}: Observed time series
{$e_t$}: Unobserved white noise series (seq. of i.i.d., zero-mean RV)


# General Linear Process
General linear process, {$Y_t$}는 현재와 과거의 화이트 노이즈의 선형 결합(linear combination)으로 나타내어진다:

$$Y_t = e_t + \psi_1e_{t-1}+\psi_2e_{t-2} + \cdots$$

보통 RHS가 infinite series라면 다음을 가정한다. Mathematical tractability를 위함이다.

$$\sum_{i=1}^{\infty}\psi_i^2 < \infty$$

예시를 통해 주어진 프로세스의 여러 성질을 구하는 방법을 알아보자.

## Example: Exponentially Decaying Sequence
$\psi_i = \phi^i, \text{ where } \phi \in (-1, 1)$인 경우의 linear process를 생각해보자. 그러면 다음과 같이 시계열을 표현할 수 있다.

$$ Y_t = e_t + \phi e_{t-1} + \phi^2 e_{t-2} + \cdots$$

먼저, mean을 구해보자. Mean의 linearity와 화이트 노이즈의 zero-mean 특성에 의하여, $E(Y_t) = E(e_t + \phi e_{t-1} + \cdots) = 0 + 0 + \cdots = 0$이다.

Variance는 어떨까? $Var(aX+b) = a^2Var(X)$임을 기억하자. 그에 따라, $Var(Y_t) = Var(e_t + \phi e_{t-1} + \phi^2 e_{t-2} + \cdots)$ $=Var(e_t) + \phi^2 Var(e_{t-1}) + \cdots$ $=\sigma_e^2(1+\phi^2 +\phi^4 + \cdots)=$ $\sigma_e^2 \over 1-\phi^2$와 같이 표현할 수 있다. 여기서 $sigma_e^2$는 화이트 노이즈의 variance다.

이제 인접한 시점에서의 시계열 데이터 간의 covariance와 correlation을 구해보자. 먼저 covariance는 다음과 같다.

$$ Cov(Y_t) \begin{align}
& 
&
\end{align}
$$