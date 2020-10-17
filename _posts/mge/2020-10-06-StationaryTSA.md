---
title: "[Time Series Analysis 2] Stationary Time Series"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
이번엔 정상성(stationarity)을 가정한, 혹은 실제로 그러한 시계열들을 모델링해보자. 앞서 언급하였듯, 정상성을 지닌 시계열 데이터는 여러 유용한 성질들을 지니고 있다. 

시작 전에, 다음과 같은 노테이션을 사용하자.

- {$Y_t$}: Observed time series
- {$e_t$}: Unobserved white noise series (seq. of i.i.d., zero-mean RV)


# General Linear Process
**General linear process**, {$Y_t$}는 현재와 과거의 화이트 노이즈의 선형 결합(linear combination)으로 나타내어진다:

$$Y_t = e_t + \psi_1e_{t-1}+\psi_2e_{t-2} + \cdots$$

보통 RHS가 infinite series라면 다음을 가정한다. Mathematical tractability를 위함이다.

$$\sum_{i=1}^{\infty}\psi_i^2 < \infty$$

예시를 통해 주어진 프로세스의 여러 성질을 구하는 방법을 알아보자.

## Example: Exponentially Decaying Sequence
$\psi_i = \phi^i, \text{ where } \phi \in (-1, 1)$인 경우의 linear process를 생각해보자. 그러면 다음과 같이 시계열을 표현할 수 있다.

$$ Y_t = e_t + \phi e_{t-1} + \phi^2 e_{t-2} + \cdots$$

먼저, mean을 구해보자. Mean의 linearity와 화이트 노이즈의 zero-mean 특성에 의하여, 

$$E(Y_t) = E(e_t + \phi e_{t-1} + \cdots) = 0 + 0 + \cdots = 0$$

Variance는 어떨까? $Var(aX+b) = a^2Var(X)$임을 기억하자. 그에 따라,

$$
 \begin{align} Var(Y_t) & = Var(e_t + \phi e_{t-1} + \phi^2 e_{t-2} + \cdots) \\
& =Var(e_t) + \phi^2 Var(e_{t-1}) + \cdots \\
& =\sigma_e^2(1+\phi^2 +\phi^4 + \cdots) \\
& = {\sigma_e^2 \over 1-\phi^2}
\end{align}
$$


이제 인접한 시점에서의 시계열 데이터 간의 covariance와 correlation을 구해보자. 먼저 covariance는 다음과 같다.

$$ \begin{align} Cov(Y_t) 
& = Cov(e_t + \phi e_{t-1} + \cdots ,e_{t-1} + \phi e_{t-2} + \cdots) \\ 
& = Cov(\phi e_{t-1}, e_{t-1}) + Cov(\phi^2e_{t-2}, e_{t-2}) + \cdots \\
& = \phi \sigma_e^2(1+\phi^2 + \phi^4 + \cdots) \\
&= {\phi \sigma_e^2 \over 1-\phi^2}
\end{align}
$$

자연스럽게, correlation은 다음과 같이 나온다.

$$ Corr(Y_t, Y_{t-1}) = \phi
$$

$Corr(Y_t, Y_s) =$ $\frac{Cov(Y_t, Y_s)}{\sqrt{Var(Y_t)Var(Y_s)}} = $ $\frac{\gamma_{t, s}}{\sqrt{\gamma_{t,t}\gamma_{s,s}}}$이란 사실을 기억하면 된다.

임의의 time lag에 대해서도 비슷한 방법으로 구할 수 있다.

- $Cov(Y_t, Y_{t-k}) = {\phi^k\sigma_e^2 \over 1 - \phi^2}$
- $Corr(Y_t, Y_{t-k}) = \phi^k$
  
이렇게 돌아보면, 왜 이 프로세스가 정상적(stationary)인지 알 수 있다. Mean이 일정하고(0), autocovariance가 time lag, $k$에만 의존하기 때문이다. 와, 소름!

## Stationarity of General Linear Process
**General linear process는 정상적이다.** 왜냐? weak stationarity의 두 조건을 만족하기 때문이다! 위에서와 같은 이유로 $E(Y_t) = 0$이고, autocovariance, $\gamma_k = Cov(Y_t, Y_{t-k}) = \sigma_e^2\sum_{i=0}^\infty \psi_i \psi_{i+k}$이기 때문이다. 계산은 생략...


# Moving Average Processes
**MA** 프로세스는 non-zero weight가 유한함을 가정하고, 다음과 같이 표현될 수 있다.

$$Y_t = e_t - \theta_1e_{t-1} - \theta_2e_{t-2} - \cdots - \theta_qe_{t-q}$$

$q$는 항의 수 + 1이자, 해당 MA 프로세스의 order를 나타낸다. 위의 경우엔 $q$-order MA process, 혹은 $MA(q)$로 나타낼 수 있다.

우선 간단한 케이스인 first-order와 second-order MA 프로세스를 살펴보고, 이를 일반적으로 확장해보자.

## First-order MA Process
가장 간단한 형태의 MA 프로세스다. 

$$Y_t = e_t - \theta e_{t-1}$$

평균, 분산, 공분산 모두 간단히 구할 수 있다.

$$E(Y_t) = E(e_t - \theta e_{t-1}) = 0$$

$$\begin{aligned}Var(Y_t)  & = E(e_t - \theta e_{t-1}) = 0\\
& = Var(e_t) + \theta^2 Var(e_{t-1}) \\
& = -\theta \sigma_e^2 \end{aligned}$$

$$\begin{aligned} Cov(Y_t, Y_{t-1})
& = Cov(e_t-\theta e_{t-1}, e_{t-1} -\theta e_{t-2}) \\
& = Cov(-\theta e_{t-1}, e_{t-1}) \\
& = -\theta \sigma_e^2
\end{aligned}$$

$$ Cov(Y_t, Y_{t-2}) = Cov(e_t-\theta e_{t-1}, e_{t-2} - \theta e_{t-3}) = 0$$ 

비슷하게, lag이 2 이상이면 $Cov(Y_t, Y_{t-k}) = 0$이다. 이제 $MA(1)$의 stationarity도 확인할 수 있게 되었다.


## Second-order MA Process

$$Y_t = e_t - \theta e_{t-1} - \theta_2 e_{t-2}$$

이제 조금 더 복잡해졌다. 하지만 못 풀 정도는 아니니 천천히 구해보자. 우선 간단하게 생각해서, 각자의 linearity에 의해 $E(Y_t) = 0$이고, $Var(Y_t)= \sigma_e^2 (1 + \theta_1^2 + \theta_2^2)$임을 직관적으로 알 수 있다. 

공분산도 위와 같은 맥락에서 time lag이 3 이상이면 covariance가 0일 것이다. 참고로 time lag이 1이면 $Cov(Y_t, Y_{t-1}= (-\theta_1 + \theta_1 \theta_2)\sigma_e^2$, 2면 $Cov(Y_t, Y_{t-2} = -\theta_2 \sigma_e^2$다. 이렇게 $MA(2)$의 stationarity도 확인하였다.


## General MA Process
직접 계산은 안할 거고, 위대한 옛날 사람들이 많이 계산해놨으니 결과만 보자. Mean이야 당연히 0이고,

- $\gamma_0 = Var(Y_t) = (1+ \theta_1^2 + \cdots + \theta_q^2)\sigma_e^2$
- $\rho_k = \frac{-\theta_k + \theta_1 \theta_{k+1} + \cdots + \theta_{q-k}\theta_q}{1+ \theta_1^2 + \cdots + \theta_q^2}$ (for $1 \le k \le q$, otherwise, $0$)


# AutoRegressive Process
**AR** 프로세스는 단어 그대로 스스로에 대한 regression이라 할 수 있다. 일반적으로($p$-order) 다음과 같이 표현된다.

$$Y_t = \phi_1Y_{t-1} + \phi_2Y_{t-2} + \cdots + \phi_pY_{t-p} + e_t$$

즉, $p$까지의 과거에 대한 값에 대한 linear combination이다. 거기에 $e_t$가 더해지고. ($e_t$는 모든 $Y_{t-k}$에 대해 독립적임을 가정하자.)

이번엔 $AR(1)$, $AR(2)$를 따로 살펴보진 않을 것이다. 너무 수식 쓰기 힘들어...

## Stationarity of AR Process
**모든 AR 프로세스가 정상적이진 않음**을 주의하자. Stationarity를 확인하는 과정이 추가적으로 필요하다.

주어진 AR 프로세스에 대한 정상성을 찾기 위한 좋은 방법이 있다. 바로 AR Characteristic Equation을 사용하는 것인데, 다음 방정식의 근들이 모두 복소 평면의 단위원 밖에 있으면 된다. 역도 성립한다.

$1-\phi_1x - \phi_2x^2 - \cdots - \phi_p x^p = 0$

## Yule-Walker Equations
**Yule-Walker equations**는 AR의 autocorrelation과 autocovariance를 구하기 위해 사용되는 방정식이다. 적당히 유도해보자.

우선, general $AR(p)$ process에 대해, $Y_{t-k}$를 곱해주자.

$$Y_tY_{t-k} = \phi_1Y_{t-1}Y_{t-k} + \cdots + \phi_pY_{t-p}Y_{t-k} + e_tY_{t-k} $$

여기다 expectation을 때리고 $\gamma_0$으로 나누면, 다음과 같이 정리된다.

$$\rho_k = \phi_1\rho_{k-1} + \cdots + \phi_p\rho_{k-p}$$

이제, 여기에 $k=1,2,\cdots,p$를 대입하고, $\rho_0 = 1$, $\rho_{-k} = \rho_k$를 대입하자. 다음과 같은 식을 얻을 수 있다.

$$\begin{matrix}
\rho_1 = \phi_1 + \phi_2\rho_1 + \cdots + \phi_p\rho_{p-1} \\
\rho_2 = \phi_1\rho_1 + \phi_2 + \cdots + \phi_p\rho_{p-2} \\
\rho_p = \phi_1\rho_{p-1} + \phi_2\rho_{p-2} + \cdots + \rho_p
\end{matrix}
$$

이렇게 $\mathbf \rho$가 unknown으로 존재하는 linear system이 만들어졌다.

# AutoRegressive Moving Average Process
뭐 이런 혼종이 다있냐... 아무튼 **ARMA** 프로세스는 AR과 MA의 특성을 나누어 가진 프로세스다. 즉, 부분적으로 AR이고, 부분적으로 MA다. 지금까지의 프로세스와 비교하여 조금 더 일반화된 형태다.

$$\begin{aligned}Y_t & = \phi_1Y_{t-1} + \phi_2Y_{t-2} + \cdots + \phi_pY_{t-p} \\ & + e_t - \theta_1e_{t-1} - \theta_2e_{t-2} - \cdots - \theta_qe_{t-q}
\end{aligned}
$$

이렇게 정의된 {$Y_t$}는 $ARMA(p,q)$와 같이 표현된다.

## ARMA(1,1) Model
$ARMA(1,1)$은 다음과 같이 나타낼 수 있다.

$$Y_t = \phi Y_{t-1} + e_t - \theta e_{t-1}$$

ARMA에도 Yule-Walker equation을 적용할 수 있다. 그 전에, $E(e_tY_t) = \sigma_e^2$, $E(e_{t-1}Y_t) = (\phi-\theta)\sigma_e^2$라는 사실을 알아두자. 그럼 $Y_{t-k}$를 곱한 다음 expectation을 때리면,

$$\begin{aligned}E(Y_{t-k}Y_t)& = E(\phi Y_{t-k} Y_{t-1} + Y_{t-k}e_t - \theta Y_{t-k}e_{t-1})\\
& = \phi E(Y_{t-k}Y_{t-1}) + \sigma_e^2 - (\phi - \theta)\sigma_e^2\end{aligned}
$$
$$
\begin{aligned}
for\;k = 0; \quad& \gamma_0 = \phi \gamma_1 + (1-\theta(\phi - \theta))\sigma_e^2 \\
for\;k = 1; \quad& \gamma_1 = \phi \gamma_0 - \theta \sigma_e^2 \\
for\;k \ge 2; \quad& \gamma_k = \phi \gamma_{k-1}
\end{aligned}
$$

이를 풀면, 다음과 같이 표현할 수 있다.

$$
\gamma_0 = \frac{1-2\phi\theta + \theta^2}{1-\phi^2} \sigma_e^2 $$

$$\rho_k = \frac{(1-\theta\phi)(\phi-\theta)}{1-2\theta\phi + \theta^2}\phi^{k-1}\quad(for\;k\ge 1)
$$

## ARMA(p, q) Model
일반적인 ARMA 모델에 대한 건 증명 없이 받아들이자...

우선, 다음 두 문장은 동치다.

- $ARMA(p,q)$는 정상적이다(stationary).
- AR characteristic equation, $\phi(x) = 0$의 모든 근의 복소평면 위에서의 크기가 1을 초과한다.

만약 주어진 ARMA가 정상성 조건을 만족할 경우, 이는 $\psi$를 계수로 하는 general linear process로 표현될 수 있다.

- $\psi_0 = 1$
- $\psi_1 = -\theta_1 + \phi_1$
- $\psi_2 = -\theta_2 + \phi_2 + \phi_1\psi_1$
- $\cdots$
- $\psi_j = -\theta_j + \phi_p\psi_{j-p}+\phi_{p-1}\psi_{j-p+1}+\cdots+\phi_1\psi_{j-1}$

또, 이러한 경우, ACF는 다음과 같이 표현된다.

$$\rho_k = \phi_1\rho_{k-1} + \phi_2\rho_{k-2} + \cdots + \phi_p\rho_{k-p}\quad for\;k>q$$

...슬슬 머리가 깨질 것 같다.


# Invertibility
## General Linear Process Representation
정상성이 보장된 경우의 $AR(p)$ 프로세스는 general linear process form으로 표현될 수 있다. 어떻게? 바로 $\psi$를 계수로 삼아서!

$$Y_t = e_t + \psi_1 e_{t-1} + \psi_2 e_{t-2} + \cdots$$

하지만 각각의 $\psi$는 $\phi_1, \cdots, \phi_p$의 함수로, 굉장히 복잡한 형태를 띠고 있다. 하지만 많은 사람들이 열심히 다 구해놔서 레퍼런스를 찾으면 된다!

위에서 언급하였듯, ARMA또한 정상성이 보장되었다면 general linear process with $\psi$-coefficient로의 표현이 가능하다. 또, 비슷한 맥락에서, 이들을 infinite-order MA로도 나타낼 수 있을 것이다.

그런데 여기서 궁금한 점은 이거다. **"그럼 MA 프로세스를 AR로 나타낼 수도 있나?"**

## Invertibility Example: MA(1)
**MA(1)** 모델을 생각해보자.

$$Y_t = e_t - \theta e_{t-1}$$

이는 $e_t = Y_t + \theta e_{t-1}$와 같고, $e_{t-1} = Y_{t-1} + \theta e_{t-2}$라는 점을 생각하면, 다음과 같이 나타낼 수 있다.

$$e_t = Y_t + \theta Y_{t-1} + \theta^2 e_{t-2}$$

더욱 확장하여, $\vert \theta \vert < 1$이어서 수렴성이 보장된다면, 

$$e_t = Y_t + \theta Y_{t-1} + \theta^2Y_{t-2} + \theta^3Y_{t-3} + \cdots$$

또는 다음과 같이 표현할 수도 있다.

$$Y_t = (-\theta Y_{t-1}-\theta^2Y_{t-2} - \cdots) + e_t$$

띠용? 어느새 AR이 되었다!?

다음 두 명제는 동치임이 알려져있다.

- $MA(1)$은 가역이다.
- $\vert \theta \vert < 1$이다.

## General MA / ARMA Process
일반적인 $MA(q)$, 또는 $ARMA(p,q)$ 모델에 대해서, **MA characteristic polynomial**을 다음과 같이 정의한다.

$$\theta(x) = 1 - \theta_1x - \cdots - \theta_q x^q$$

그리고 **MA characteristic equation**은 $\theta(x) = 0$이다.

다음 두 명제는 동치다.

- 해당 프로세스는 가역이어서, $Y_t = \pi_1 Y_{t-1} + \pi Y_{t-2} + \cdots + e_t$를 만족하는 $\pi_i$가 존재한다.
- MA characteristic equation의 모든 근이 복소평면 위에서 그 크기가 1을 초과한다.

## ACF and Invertibility
가역성에 대해 조심해야 할 사항이 조금 있다. 우선, 두 $MA(1)$ 모델을 보자.

- $Y_t = e_t - \theta e_{t-1}$
- $Y_t = e_t - \frac{1}{\theta} e_{t-1}$

두 프로세스는 동일한 ACF를 가지지만, 전자만이 가역적이다.


# Summary
이번에 다룬 내용이 너무 많아서 간단히 한 번 요약해본다.

### General Linear Process

$$ Y_t = e_t + \psi_1 e_{t-1} + \psi_2 e_{t-2} + \cdots $$

- **Stationary**
- $E(Y_t) = 0$
- $\gamma_k = \sigma_e^2 \sum_{i=0}^\infty \psi_i\psi_{i+k}\quad for\;k \ge 0$

### Moving Average Process

$$Y_t = e_t - \theta_1e_{t-1} - \theta_2e_{t-2} - \cdots - \theta_qe_{t-q}$$

- **Stationary**
- **$MA(q)$에서, $q$ 이후로 autocorrelation은 $0$**
- **MA characteristic equation 조건을 만족하면 AR 형태로 변환 가능.**

#### MA Characteristic Equation
$$\theta(x)=1-\theta_1 x - \theta_2 x^2 - \theta_3 x^3 - \cdots - \theta_q x^q = 0$$

### AutoRegressive Process
$$Y_t = \phi_1Y_{t-1} + \phi_2Y_{t-2} + \cdots + \phi_pY_{t-p} + e_t$$

- **AR characteristic equation을 통해 정상성 확인 가능.**
- **Yule-Walker equation을 통해 autocorrelation과 autocovariance 계산 가능.**
- **정상성이 보장된 경우 MA, general linear process 형태로 변환 가능.**

#### AR Characteristic Equation

$$\phi(x) = 1-\phi_1 x - \phi_2 x^2 - \cdots - \phi_p x^p = 0$$

### AutoRegressive Moving Average Process
$$\begin{aligned}Y_t & = \phi_1Y_{t-1} + \phi_2Y_{t-2} + \cdots + \phi_pY_{t-p} \\ &\; + e_t - \theta_1e_{t-1} - \theta_2e_{t-2} - \cdots - \theta_qe_{t-q}
\end{aligned}
$$

- **AR characteristic equation을 통해 정상성 확인 가능.**
- **정상성이 보장된 경우 MA, general linear process 형태로 변환 가능.**
- **MA characteristic equation 조건을 만족하면 AR 형태로 변환 가능.**


# 마치며
정말 길고 길었다... 아마 각 프로세스에서 특정 order의 형태와 성질, auto-covariance, auto-correlation 등을 모조리 기억하는 건 어려울 것이다. 하지만 대부분 이들을 유도하는 방식은 비슷하기 때문에, 필요에 따라 스스로 유도할 수 있는 정도만 되어도 괜찮을 것 같다. 

그러기 위해선 각 프로세스의 정의, $Cov$, $\gamma$, $\rho$ 등의 성질 정도는 잘 알고 능숙하게 사용할 수 있어야 한다. 역시 기본이 중요하지 음음