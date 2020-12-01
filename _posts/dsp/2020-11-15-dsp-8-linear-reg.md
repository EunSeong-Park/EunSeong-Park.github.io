---
title: "[Data Science Programming 8] Linear Regression"
tags: Data-Science Statistics Python
toc: true
---

# Regression Analysis
**회귀 분석(regression analysis)**은 어떤 데이터로부터 둘 혹은 그 이상의 변수 사이의 관계를 추정하는 통계적 방법이다. 이는 어떤 절차에 의해 이루어질까?

- Dependant(response) variable과 independent variable(predictor) 사이의 관계를 나타내기 위한 **mathematical model**을 가정한다.
- 관측된 데이터를 바탕으로 그 관계(relationship)을 추정(**estimate**)한다.
- 추정된 모델이 데이터와 잘 들어맞는지 검정(**test**)한다.
- 모델을 바탕으로 주어진 independent variable에 대한 response를 예측(**predict**)한다.


# Linear Regression
선형적인 관계, 즉 $Y=\beta_0 + \beta_1X$를 가정하여 수행하는 회귀 분석을 **선형 회귀(linear regression)**라고 한다. 그 중에서도,

- **Single linear regession**: $Y = \beta_0 + \beta_1 X$
- **Multiple linear regression**: $Y =\beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p$

그리고 각각의 계수, $\beta$들을 **regression parameter**라고 한다. 이 값들은 미지수이며, 우리가 이들을 추정해야 한다.

그리고 데이터 각각에 대해,

- **Single linear regession**: $y_i = \beta_0 + \beta_1 x_i + e_i$
- **Multiple linear regression**: $y_i =\beta_0 + \beta_1 x_{1i} + \cdots + \beta_p x_{pi} + e_i$

여기서 $e_1, e_2, \cdots, e_N$은 zero-mean에 common variance를 가진 IID다.

## Simple Linear Regression
### Estimation: Least-square Method
Simple linear regression을 위한 가장 간단한 방법 중 하나로, **least-square method**가 있다. 말 그대로 squared error가 최소가 되도록 하는 파라미터를 찾는 방식이다. 즉,

$$\text{Minimize } \sum_{i=1}^N (y_i - (\beta_0+\beta_1 x_i))^2$$

위 식을 적당히 정리하여, 적당한 $\hat \beta_0, \hat \beta_1$을 다음과 같이 나타낼 수 있다.

$$\begin{aligned}
\hat\beta_1 &= \frac{\sum_{i=1}^N (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^N (x_i - \bar x)^2} = \frac{S_{XY}}{S_X^2} = \frac{S_{XY}}{S_{XX}} \\
\hat\beta_0 &= \bar y - \hat\beta_1\bar x
\end{aligned}$$

즉, regression line은 다음과 같다.

$$\hat y: \hat E (Y \vert X = x) = \hat\beta_0 + \hat\beta_1 x$$

### Properties
우선, 다음을 기억하자.

$$\begin{aligned}
\hat\beta_1 &= \frac{\sum_{i=1}^N (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^N (x_i - \bar x)^2} = \frac{S_{XY}}{S_X^2} = \frac{S_{XY}}{S_{XX}} \\
\hat\beta_0 &= \bar y - \hat\beta_1\bar x
\end{aligned}$$

이에 따르면, 추정치에 대한 expectation은 다음과 같을 것이다.

- $E(\hat \beta_1) = \beta_1$
- $E(\hat \beta_0) = \beta_0$

그럼 variance는 어떨까? 독립적인 두 RV에 대해 $\text{Var}(Y_1 + Y_2) = \text{Var}(Y_1) + \text{Var}(Y_2)$임을 이용하여,

- $\text{Var}(\hat \beta_1) = \frac{\sigma^2}{S_{XX}}$
-  $\text{Var}(\hat\beta_0) = \bar x^2\frac{\sigma^2}{S_{XX}} + \frac{\sigma^2}{N}$

엇, 그럼 variance 자체는 어떻게 구하지? 잔차(residual)를 사용하자!

$$\hat e_i = y_i - (\hat\beta_0 + \hat\beta_1 x_1) = y_1 - \hat y_i$$

이를 이용하여,

$\hat\sigma^2 = MSE = \frac{SSE}{N-2} = \frac{\sum_{i=1}^N (y_i - \hat y_1)^2}{N-2}$

### R-Squared
여기서, **SST, SSE, SSR** 등에 대한 의미를 명확히 짚고 넘어가자.

어떤 observed value, $y_i$와 그에 대한 regression, $\hat y_i$, 그리고 전체 데이터 평균 $\bar y$를 생각해볼 수 있다.

- **SST(Sum of Squares Total)**: 개별 데이터와 데이터 평균 간 편차에 대한 SS.
- **SSE(Sum of Squares Explained)**: 개별 데이터와 regrssion line 간 편차에 대한 SS.
- **SSR(Sum of Squares Residual)**: Regression line과 데이터 평균 간 평차에 대한 SS.

즉, 이들을 이용해 주어진 변동, 혹은 편차에서 얼마나 설명되었는지(explained)를 판단할 수 있다.

$\mathbf R^2$은 주어진 회귀식이 variation을 설명해주는 비율을 나타낸다. 즉,

$$R^2 := \frac{SSE}{SST} = 1- \frac{SSR}{SST}$$

그리고 이는 정의에 따라 다음과 같이 표현될 수 있기도 하다.

$$R^2 = \frac{S^2_{XY}}{S_{XX}S_{YY}}=r^2_{XY}$$

유도는 알아서...

### Testing
Regression에 대해서도 **statistical testing**을 시도해볼 수 있다. 우선 이를 위해, 그 통계량에 대한 분포를 알 필요가 있다.

우선, $e_i$는 IID고, $\mathcal{N}(0, \sigma^2)$인 분포를 따른다고 가정하자. 그러면 $x_1, \cdots, x_N$이 fixed되었을 때, $y_1, y_2, \cdots, y_N$또 normal하게 분포한다.

$$\hat\beta_1 \sim \mathcal N(\beta_1, \frac{\sigma^2}{S_{XX}})$$

그럼 다음과 같이 가설을 세우고 검정할 수 있다.

- $H_0: \beta_1 = \beta_{1,0}$
- $H_1: \beta_1 \ne \beta_{1,0}$

$$Z = \frac{\hat\beta_1 - \beta_{1,0}}{\sigma / \sqrt{S_{XX}}} \sim \mathcal N(0,1)$$

즉, **Z-test**를 사용할 수 있다. $\beta_0$도 똑같은 방법으로 진행한다.

$$\hat\beta_0 = \bar y - \hat\beta_1 \bar x \sim \mathcal N(\beta_0, \frac{\sigma^2}{N} + \bar x^2 \frac{\sigma^2}{S_{XX}})$$

- $H_0: \beta_0 = \beta_{0,0}$
- $H_1: \beta_0 \ne \beta_{0,0}$

$$Z = \frac{\hat\beta_0 - \beta_{0,0}}
{\sigma\sqrt{\frac{1}{N} + \frac{\bar x^2}{S_{XX}}}}$$

만약 우리가 $\sigma$를 모른다면, **T-test**를 사용할 수도 있다.

$${(N-2)\hat\sigma_2 \over \sigma^2} = \mathcal X^2(N-2)$$

따라서, $H_0: \beta_1 = \beta_{1,0}$에서,

$$T = \frac{\hat\beta_1 - \beta_{1,0}}{\hat\sigma / \sqrt{S_{XX}}} \sim \mathcal t(N-2)$$

그리고 $H_0(\beta_0 = \beta_{0,0})$에서,

$$Z = \frac{\hat\beta_0 - \beta_{0,0}}
{\hat\sigma\sqrt{\frac{1}{N} + \frac{\bar x^2}{S_{XX}}}} \sim t(N - 2)$$

## Multiple Linear Regression

$$ Y = \begin{bmatrix}
y_1 \\ y_2 \\ \cdots \\ y_N
\end{bmatrix} \in \mathbb R^{N\times 1},
X = \begin{bmatrix}
1 & x_{11} & \cdots & x_{p1} \\
1 & x_{12} & \cdots & x_{p2} \\
\cdots & \cdots & \cdots & \cdots \\
1 & x_{1N} & x_{2N} \cdots & x_{pN}
\end{bmatrix} \in \mathcal R^{N \times (p+1)}
$$

$$E = \begin{bmatrix}
e_1 \\ e_2 \\ \cdots \\ e_N
\end{bmatrix} \in \mathbb R^{N\times 1},
\beta = \begin{bmatrix}
\beta_1 \\ \beta_2 \\ \cdots \\ \beta_p
\end{bmatrix} \in \mathbb R^{(p+1) \times 1}
$$

$$ Y = X\beta + E $$

### Estimation
추정을 위해, 우리는 다음과 같은 식을 쓸 수 있다.

$$\begin{aligned}
\sum_{i=1}^N (y_i - (\beta_0 + \beta_1 x_{1i} + \beta_2 x_{2i} + \cdots + \beta_p x_{pi}))^2 &=(Y-X\beta)^T(Y-X\beta) \\
&= Y^TY-2Y^TX\beta + \beta^TX^TX\beta\end{aligned}
$$

이를 최소로 만드는 minimizer는 $X^TX\beta = X^TY$의 해다. 즉, 만약 $(X^TX)^{-1}$이 존재한다면, $\hat\beta$는 다음과 같이 표현된다.

$$\hat\beta = (X^TX)^{-1}X^TY$$

이제 이거 적당히 풀면 된다.

### Properties
$p=1$, single linear regression의 경우부터  볼까?

$$\text{Var}(\hat\beta) = \text{Var}(\begin{bmatrix}\hat\beta_0 \\ \hat\beta_1 \end{bmatrix}) = \begin{bmatrix} \text{Var}(\hat\beta_0) & \text{Cov}(\hat\beta_0, \hat\beta_1) \\ \text{Cov}(\hat\beta_1, \hat\beta_0) & \text{Var}(\hat\beta_1)\end{bmatrix}$$

위 식으로부터 일반적인 경우의 규칙성을 알 수 있을 것이다. 

우리는 다음 식을 구하는 게 우선적인 목표였는데, 

$$\hat\beta = (X^TX)^{-1}X^TY$$

아마 여기서 $(X^TX)^{-1}$를 적절히 계산할 방법이 필요하다. 직접 계산하기가 조금 어려우므로 우리는 여기에 적당한 **decomposition method**를 적용할 수 있는데, 이건 다음 포스팅에서...

### Variance Estimation
$\sigma^2$를 구하기 위해, **잔차**를 사용한다.

$$\hat e_i = y_i-(\hat\beta_0 + \hat\beta_1 x_{1i} + \hat\beta_2 x_{2i} + \cdots + \hat\beta_p x_{pi}) = y_i - \hat y_i$$

Variance estimation은...

$$\hat\sigma^2 = MSE = \frac{SSE}{N- (p+1)} = \frac{\sum_{i=1}^N (y_i - \hat y_i)^2}{N-p-1}$$

그리고 행렬 $\hat Y$에 대해, $\hat Y = X \hat\beta$고,

$$SSE = (Y- \hat Y) \cdot (Y- \hat Y) = (Y- \hat Y)^T (Y- \hat Y)$$

또, $\hat Y = X(X^TX)^{-1}X^T Y$로부터, $H =X(X^TX)^{-1}X^T$를 Hat matrix라 하자. 여기서 $H$는 여러 흥미로운 성질을 가지는데,

- $H$는 $N \times N$이고 **symmetric**이다.
- $H$는 **idempotent**하여, $HH=H$이다.

아무튼 이를 이용하여,

$$SSE = Y^TY - Y^THY = Y^T(I-H)Y$$

그렇다면, $E(\hat\sigma^2)$을 계산해볼까? 우리는 **trace**를 이용해 이를 유도할 것이다. 잠깐, 여기서 trace라 함은..

$$Tr(A) = \sum_{i=1}^n a_{ii}$$

정의에 따라, 이는 linearity를 가지며, $Tr(BC) = Tr(CB)$ (만약 곱셈이 정의된다면)라는 특성도 있다.

아무튼, $E((n-p-1)\hat\sigma^2) = E(SSE)$인 점을 이용해서, 이를 여차저차 정리하면,

$$E((n-p-1)\hat\sigma^2) = \sigma^2 Tr(I) - \sigma^2 Tr(H) + E(Y)^T(I-H)E(Y)$$

이를 또 정리하면, $E((n-p-1)\hat\sigma^2) = (N-p-1)\sigma^2$ 다. 따라서 $E(\hat\sigma^2) = \sigma^2)$ 이다. 굿