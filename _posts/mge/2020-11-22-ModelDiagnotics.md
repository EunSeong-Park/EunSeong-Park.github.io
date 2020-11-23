---
title: "[Time Series Analysis 6] Model Diagnotics"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
지난 시간까지 우리는 주어진 시계열 데이터를 바탕으로 모델을 결정하고 그에 대한 파라미터를 특정하는 방법을 배웠다. 이번엔 그렇게 특정한 모델이 적합한 모델인지 판단할 방법을 알아볼 것이다. 이전에 잔차 분석(residual analysis)을 잠깐 살펴보았는데, 이번에 조금 더 자세히 알아보고, 오버피팅(overfitting)에 관한 이슈도 배워보자!


# Residual Analysis
**잔차(residual)는 predicted value와 actual value 사이의 차이**로 볼 수 있다. 즉, 얼마나 우리의 모델이 참값(true value)에 근접한지에 대한 지표로 볼 수 있는데, 이상적인 상황에서 **잔차는 화이트 노이즈의 특성을 따라야 한다.** 즉, IID normal variable with zero mean / common stddev을 가지면 된다.

## Examples
**AR(2)**는 다음과 같이 표현되며, $\phi_1, \phi_2, \theta_0$를 추정해야 한다.

$$Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \theta_0 + e_t$$

이 때, 잔차는 다음과 같을 것이다.

$$\hat e_t = Y_t - \hat\phi_1Y_{t-1}- \hat\phi_2Y_{t-2} - \hat\theta_0$$

MA 텀을 포함하는 general **ARMA** 프로세스도 생각해보자. 이전의 화이트 노이즈 텀을 포함하므로 위와 같이 간단히 나타낼 수 없는데, 하지만 이를 **inverted infinite AR** 형태로 표현함으로써 해결할 수 있다.

$Y_t = \pi_1Y_{t-1} + \pi_2Y_{t-2}+\cdots + e_t$

즉,

$\hat e_t = \hat\pi_1Y_{t-1} -\hat\pi_2Y_{t-2} \cdots$

## Plotting
가장 먼저 시도해 볼 수 있는 diagnosis로, 잔차와 관련된 그래프를 직접 그려보는 방법이 있다. 그래프의 형태를 보면 모델의 적합성을 일차적으로 판단할 수 있다.

- **Residuals over time**: 시간에 따라 zero-mean의 직사각형 형태로 분포하는지 확인함으로써 등분산성과 no-trend를 확인한다.
- **Q-Q plot**: Q-Q 플롯을 이용하여 직선형으로 잘 피팅되는지 확인하여 normality를 판단한다.
- **ACF of residuals**: 모델의 white noise term의 independence를 확인한다.

또, **Ljung-Box test**라는 검정 방법이 있다. 지금까지 각각의 lag에 대한 residual correlation에 주목했지만, 특정 기간에 대한 잔차를 그룹화해서 검정할 수 있는 방법이다.

$$Q^* = n(n+2)(\frac{\hat r_1^2}{n-1}+\frac{\hat r_2^2}{n-2}+\cdots+\frac{\hat r_K^2}{n-K}) \sim \chi(K-p-q)$$

$Q^*$가 크다면 주어진 ACF가 white noise로부터 나온 게 아니라고 생각할 수 있다.

# Overfitting & Parameter Redundancy
모델을 특정할 때, 우리가 종종 빠지기 좋은 pitfall들이 있다. 

## Overfitting
**오버피팅(overfitting)**은 말 그대로 과하게 피팅하는 행위다.

![](/imgs/mge/tsa26.png)

첫 번째 케이스는 너무 underfit되었고, 두 번째는 꽤 적절한 모델링이 이루어졌으며, 세 번째는 overfit되었다.

오버피팅된 모델은 오히려 모델로서의 가치가 떨어지게 된다. 너무 지엽적인 특성과 변화에 편향되어 실제값을 잘 예측하지 못하기 때문이다. 가령 화이트 노이즈에도 민감하게 반응하는 모델을 생각하면 참 슬픈 일이다.

시계열에서는 필요 이상으로 higher-order를 사용하는 경우 오버피팅이 일어날 수 있다. 예를 들어, **AR(2)**로 모델을 잡았을 때 적당히 잘 들어맞는다고 치자. 이 상황에서 **AR(3)**이나 그 이상을 써버리면 오버피팅이 일어나는 셈이다. Higher-order를 사용하는 게 적합한지 아닌지는 다음을 통해 판단할 수 있다.

- Higher-order를 사용했을 때 추가되는 parameter와 $0$과 significant difference가 있는가?
- 원래 모델과 higher-order 모델이 공유하는 parameter 사이의 significant difference가 있는가?

## Parameter Redundancy
어떤 **ARMA(p,q)**를 생각해보자. 이를 임의의 $p' >0, q'>0$에 대해 **ARMA(p', q')**로 놓고, 그 사이의 parameter가 $0$이라고 가정할 수도 있다. 비슷한 방식으로 같은 형태를 보이는 더 간단한 모델이 있고, 더 복잡한 모델이 있다.

하지만 복잡한 모델을 선택함으로써 발생하는 **redundancy**는 바람직하지 않다. 모델은 데이터를 충분히 설명할 수 있는 한, 가능하면 단순한 모델이 여러 측면에서 좋다. 

예측한 모델에서 parameter redundancy를 확인하려면, 모델에 대한 characteristic polynomial에  factorization을 수행하고 common factor가 있는지 확인하면 된다.

## Implications
그래서, 우리는 모델을 결정할 때 다음과 같은 사항을 명심해야 한다.

1. 모델을 신중하게 선택한다. 만약 간단한 형태의 모델이 조금이라도 괜찮아 보이면, 더 복잡한 형태를 사용하기 전에 한 번 확인해 본다.
2. Order를 급하게 올리지 않는다.
3. 잔차 분석의 결과를 바탕으로 모델을 수정해나간다.


# 마치며
이번엔 좀 짧았다. 야호!