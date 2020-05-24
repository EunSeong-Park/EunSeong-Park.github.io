---
title:  "[Statistics 5] Statistical Hypothesis"
tags: Statistics
toc: true
---

# Intro
흠

# Statistical Hypothesis
__Statistical hypothesis__ 란, population parameter에 대한 추측(conjecture)이다. 일단은 가설이기 때문에, 추측은 맞을 수도 있고 틀릴 수도 있다.

Statistical hypothesis는 크게 두 종류로 나누어 볼 수 있다. 한국어로 귀무가설(__null hypothesis__)과 대립가설(__alternative hypothesis__)이라고 하는 것 같다. 

- Null hypothesis($H_0$): 기각을 위해 세우는 가설. Parameter와 어떤 값에 유의미한 차이가 없다고 추측한다.
- Alternative hypothesis($H_1$): null hypothesis에 대립되는 가설. Parameter와 어떤 값, 혹은 두 parameter간 유의미한 차이가 있다고 추측한다.

우리는 귀무가설을 먼저 세우고 검증하지만, 보통 실제로 입증하고자 하는 가설은 대립가설이다. 우리가 해야 하는 일은 간단하다. 어떤 parameter에 대하여, $H_0$을 기각(reject)하고, $H_1$을 채택(accept)할 수 있는지 확인하는 것이다.

## Example
각 상황에서 $H_0$과 $H_1$이 무엇인지 각각 확인해보자.

> A researcher thinks that if expectant mothers use vitamin pills, the birth weight of the babies will increase. The average birth weight of the population is 8.6 pounds.

- $H_0$: $\mu = 8.6$
- $H_1$: $\mu > 8.6$

> An engineer hypothesizes that the mean number of defects can be decreased in a manufacturing process of USB drives by using robots instead of humans for certain tasks. The mean number of defective drives per 1000 is 18.

- $H_0$: $\mu = 18$
- $H_1$: $\mu < 18$

> A psychologist feels that playing soft music during a test will change the results of the test. The psychologist is not sure whether the grades will be higher or lower. In the past, the mean of the scores was 73.

- $H_0$: $\mu = 73$
- $H_1$: $\mu \ne 73$

## Level of Significance
### Statistical Error
가설을 세우고 검증하는 과정에서, 통계적 오류(statistical error)가 발생할 수 있다.

- Type I error: false-positive. 실제로 $H_0$이 참이지만, 이를 기각한 경우.
- Type II error: false-negative. 실제로 $H_0$이 거짓이지만, 이를 채택한 경우.

### Level of Significance
유의 수준(level of significance)은 귀무가설, 참인 $H_0$을 기각할 오류를 범할 최대 확률을 의미한다. 즉, type I error가 발생할 확률이다. 이 값을 $\alpha$로 나타내도록 하자.

이제 critical region과 noncritical region에 대해 알아보자. 전자의 경우, 검사하려는 값이 안에 있을 경우 $H_0$이 기각되도록 하는 영역이고, 후자의 경우, 안에 있을 경우 $H_0$이 기각되지 않도록 하는 영역이다. 또, 그 두 영역의 경계를 CV(Critical Value)라고 한다.

우리가 해야 할 일은, test value가 있는 영역이 critical인지 noncritical인지 확인하고, 그에 따라 $H_0$의 채택/기각 여부를 결정하는 것이다.

## Test of Population Mean
이제, 우리는 population mean에 대한 추측이 옳은지 아닌지를 검증해볼 것이다. Population은 normal하다고 가정할 것이다.

### z-test
z-test는 population mean에 대한 statistical test다. 이는 샘플 사이즈, $n$이 30 이상이거나, 
