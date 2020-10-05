---
title: "[OM 5] Forecasting"
tags: Management-Engineering OM
toc: true
---

# Intro
Business analytics는 데이터를 사용하는 목적에 따라 크게 세 종류로 나눌 수 있다.

- Descriptive analytics: 현재 상황 또는 문제에 대한 정확하고 체계적인 파악을 위해 사용한다. 
- Predictive analytics: 미래에 발생할 동향이나 현상을 예측하기 위해 사용한다.
- Prescriptive analytics: 최선의 결정이나 선택을 고르기 위해 사용된다.

Forecasting은 predictive analytics의 일종이다. 이는 많은 분야와, 많은 종류의 과정에서 사용되어, 더 나은 결정을 하는 데 도움을 줄 수 있다. 


# Forecasting
## Features
대부분의 forecasting은 다음과 같은 특성을 가진다.

- Causal system을 가정한다. 즉, future input은 고려하지 않고, 현재와 과거의 input에 의존한다.
- 내재된 산포와 무작위성으로 인해, forecast는 대개 완벽할 수 없다.
- 그것의 정확성은 예측하려는 시점이 멀수록 떨어진다.

Forecasting은 어떻게 이루어질까? 정성적(qualitative)인 방법과 정량적(quantitative)인 방법이 있다.

- Qualitative: 추정은 과거의 경험과 사람(들)의 판단을 기반으로 한다. 정성적이어도 여기엔 논리적인 추론 및 가설 검증 단계를 필요로 하고, 어느 정도의 계산 및 수학적 테크닉을 수반할 수 있다.
- Quantitative: 수학적 모델을 활용한 data-based한 판단(judgement)을 내린다.

이러한 절차를 따라 forecasting을 하면 된다.

![](/imgs/mge/om19.png)

우리는 qunatitative forecasting을 중심으로 알아볼 것이다.

## Accuracy Measurement
정량적인 방법으로 forecasting을 했다면, 이것이 실제로 얼마나 정확한지 검증해야 한다. 실제 값과의 격차가 tolerable하지 않다면, 방법이나 모델을 수정 및 변경해야 할 것이다. 그렇다면, 어떻게 forecast accuracy를 측정할 수 있을까?

우선, error, $e_t$를 $e_t = D_t - F_t$라 정의한다.

- Mean Error: 각 항목의 error의 평균이다. 즉, $ME = \frac{\sum e_t}{n}$
- Mean Absolute Error: 각 항목의 error의 절댓값의 평균이다. 즉, $MAE = \frac{\sum \vert e_t \vert}{n}$
- Mean Squared Error: 각 항목의 제곱의 평균이다. 즉, $MSE = \frac{\sum e_t^2}{n}$

## Time Series Analysis
시계열 분석(time series analysis)은 과거의 데이터를 바탕으로 미래의 데이터를 예측하는 방법이다. 물론 이는 과거와 미래가 어느 정도 일관성있게 흘러감을 가정한다. 또, 이는 다른 변수에 의존하지 않고 오직 시간에 따른 데이터만을 고려한다.

시계열을 graphical하게 분석하면 그 데이터의 동향이 어떤지, 어떤 주기성과 특징을 가지는지 한 눈에 알아볼 수 있다.

- Trend: long-term movement in data
- Seasonality: short-term regular variations in data
- Cycles: wave-like variations of more than one year's duration
- Random variation: caused by chance
- Irregular variation: caused by unusual circumstances

예를 들어, 보일러, 에어컨같이 계절성을 띠는 제품은 시계열에서 seasonality를 확인할 수 있을 것이다. 그럼에도 전반적으로 판매량이 증가한다면 이것은 증가하는 trend를 보여주는 것이고. 이렇게 하나의 시계열은 위와 같은 요소들이 한 곳에 모인 형태다.

![](/imgs/mge/om20.png)

Stochastic한 process, ${X_t}$는 현실에서 white noise 등이 첨가된 형태의 ${x_t}$로 드러나고 관찰된다. 이러한 상황에서, 우리는 두 가지 선택지가 있다.

1. 별도의 모델 없이 관찰된 데이터, ${x_t}$에 주목한다.
2. Parameter의 추정을 수반한 모델링을 수행한다. 즉, ${X_t}$에 주목한다.

전자의 경우 moving average, smoothing 등의 기법이 있고, 후자의 경우 Box-Jenkins type method 등이 있다. 우리는 전자를 중심으로 알아볼 것이다.

### Smoothing Method
스무딩(smoothing)은 말 그대로 시계열을 부드럽게 만들어주는 기법이다. 그럼으로써 각종 불규칙한 변동을 완화시킬 수 있다는 점에서 유용하다.

![](/imgs/mge/om21.png)

가장 간단한 방법은 simple moving average 기법이다. 특정 시점으로부터 최근 데이터 몇 개의 평균을 내면서 스무딩을 수행한다. 이 방법은 간단하지만, trend, seasonality를 반영하지 못하고, 모든 데이터를 고려할 수 없다는 단점이 있다. (초반 혹은 후반에 몇 개의 데이터가 누락된다)

![](/imgs/mge/om22.png)

Exponential smoothing은 이전 데이터의 영향을 받되, 시점으로부터 멀어질 수록 그 영향력이 exponential하게 감소하는 형태의 smoothing이다. 즉, 가장 직전의 값이 가장 영향을 크게 준다.

이는 각 시점에서 모든 데이터를, 그리고 더 정교하게 고려할 수 있게 만들어준다. 하지만 여전히 trend나 seasonality를 systemical하게 분석할 방법을 주진 않는데, 이는 다음과 같은 방법으로 개선될 수 있다.

![](/imgs/mge/om23.png)

일명 weighted exponential smoothing이다. Trend factor를 도입함으로써 시계열을 보정한다.

$\alpha$, 혹은 $\beta$는 임의로 설정하는 계수다. 그 값에 따라 smoothing의 정도가 달라지는데, 너무 크면 스무딩이 안되고, 너무 작으면 데이터가 씹히는 등의 문제가 발생한다.

관련 예제를 풀어보진 않을 것이다. 별 이유는 없고 귀찮아서(...)

### Model-Based Method
Smoothing method는 몇 가지 단점을 내포하고 있는데,

- $\alpha, \beta$ 설정의 어려움
- 직전 값이 irregular하다면 forecasting을 망칠 수 있음
- 현상 자체를 설명해주지는 않음

적절한 모델의 설계는 forecasting 자체뿐 아니라 다른 많은 측면에서의 도움을 줄 수 있다. Model-based한 방법은 관측값 ${x_t}$보단 ${X_t}$에 주목하여, 프로세스 그 자체를 설명하기 위한 방법을 찾는다.

이는 계산 알고리즘을 이용한 파라미터의 추정을 수반하는데, 그 수가 적다면 Box-Jenkins method를 사용하는 게 가장 일반적이다.

여기서 커버할 범위는 아니라 생략한다. 또 나도 못알아먹겠다... 똑똑해지면 다시 공부해보자

## Explanatory Model
시계열 분석에서 드는 근본적인 의문이 조금 있다. 실제로 과거랑 비슷한 경향을 따라 일관성있게 일이 발생할지 알 수 없다는 점, 그리고 오직 시간만을 의존하는 게 충분할지에 대한 의문 등이 있다. 종합적인 요소를 고려하면서도, 현상을 보다 잘 설명해주는 forecasting method가 없을까?

Explanatory model은 관심 있는 데이터에 대해, 그것에 영향을 줄 수 있는 여러 요소들을 고려할 수 있게 해준다. 특정 시점과 그 때의 데이터만을 고려하는 시계열 분석과는 대비된다. 예를 들어, 일기 예보를 위해선 온도, 습도, 기압 등 수 많은 요소들을 고려해야 한다. 시계열 분석으론 충분하지 않을 것이다.

Explanatory Model은 광범위하게 사용되는데, regression도 explanatory model의 용례라고 볼 수 있다. 왜? 주어진 $X$들을 통해 미래의, 그리고 일반적인 $Y$를 forecast하기 때문이다. 그런데 regression이 뭐지?

### Regression
회귀분석(regression)은 독립 변수와 종속 변수 간의 관계를 함수로 표현 및 설명하는 방법이다. 엑셀에서 점 몇 개만을 가지고도 추세선을 그릴 수 있다는 사실을 알 것이다. 그것 또한 regression의 용례로 볼 수 있다.

가장 간단한 regression은 linear한 trend를 예측하는, linear regression일 것이다. $y = ax + b$의 형태로 나타내어, $a$와 $b$의 값을 추정하는 것이다.

![](/imgs/mge/om24.png)

물론 non-linear한 경우에도 적절한 모델을 사용함으로써 분석할 수 있다. 이건 다른 과목에서 하자.


# 마치며
솔직히 이해가 안되는 부분이 꽤 있다. 아직 지식이 너무 얕아서 그런 것 같은데, 공부를 좀 하고 나중에 글을 다듬어야지.