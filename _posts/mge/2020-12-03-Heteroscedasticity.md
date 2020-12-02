---
title: "[Time Series Analysis 9] Heteroscedasticity"
tags: Time-Series-Analysis Management-Engineering Data-Science
toc: true
---

# Intro
아니 이름이 왜이러냐? 아무튼, 단어가 조금 괴악하게 생겨서 그렇지, 번역하면 **이분산성**이다. 그 반대 개념은 **등분산성(homoscedasticity)**이고. 이제 무슨 주제를 다루려는지 딱 감이 올 것이다.

등분산성 / 이분산성은 모델링 과정에 어떤 영향을 주며, 우리는 그러한 성질의 시계열 데이터를 어떻게 다루어야 할까? 이제부터 알아보도록 하자.


# Heteroscedasticity
지금까지 살펴본 **ARMA** 모델들은 conditional variance가 일정하다고 가정해왔다. 가령 **AR(1)** 모델이라면,

- $E(Y_t \vert Y_{t-1}, Y_{t-2}, \cdots) = \phi Y_{t-1}$
- $Var(Y_t \vert Y_{t-1}, Y_{t-2}, \cdots) = Var(e_t) = \sigma_e^2$

하지만, 현실에선 이러한 가정이 위반되는 경우가 많다. 이게 이분산성(heteroscedasticity)과 이를 반영하는 모델을 고려해야 하는 이유다. 아무튼 다시 정리하면,

- **등분산성(Homoscedasticity):** 모든 RV가 같은 (finite) variance를 지닌 경우.
- **이분산성(Heteroscedasticity):** RV 중에 다른 RV들과 다른 분산성을 지닌 subpopulation이 존재하는 경우.




