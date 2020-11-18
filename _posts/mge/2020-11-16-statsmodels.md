---
title: "[Time Series Analysis EX 1] Statistical Modeling with statsmodels"
tags: Time-Series-Analysis Management-Engineering Data-Science Python
toc: true
---

# Intro
이론도 중요하지만 데이터를 가지고 실제로 활용해보는 연습 또한 필수적이다. 이번엔 주어진 시계열 데이터를 설명하기 위한 적절한 **ARIMA** 모델을 찾고, 분석하며 평가할 것이다.

# Time Series Modeling
## statsmodels
여기서 우리는 **statsmodels**를 사용한다. 이는 통계적 모델링을 위한 Python 모듈로, **pandas**, **matplotlib** 등 여러 인기있는 도구들과 호환성이 좋다. [여기](https://www.statsmodels.org/stable/index.html)서 사용 방법, 예시 등을 자세히 알아볼 수 있다. 역시 레퍼런스를 보는 것만큼 도움되는 게 없다.

또, 가능하면 **Jupyter Notebook**을 사용해서 중간 과정들을 쉽게 살펴보도록 하자. (이 포스트에서도 Jupyter를 사용하고 그 결과를 캡처해 가져올 것이다.)

## Getting Data
먼저 분석할 데이터를 가져오자. 