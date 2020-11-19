---
title: "[Time Series Analysis EX 1] Statistical Modeling Using statsmodels"
tags: Time-Series-Analysis Management-Engineering Data-Science Python
toc: true
---

# Intro
이론도 중요하지만 데이터를 가지고 실제로 활용해보는 연습 또한 필수적이다. 이번엔 주어진 시계열 데이터를 설명하기 위한 적절한 **ARIMA** 모델을 찾고, 분석하며 평가할 것이다.

# Time Series Modeling
## statsmodels
여기서 우리는 **statsmodels**를 사용한다. 이는 통계적 모델링을 위한 Python 모듈로, **pandas**, **matplotlib** 등 여러 인기있는 도구들과 호환성이 좋다. [여기](https://www.statsmodels.org/stable/index.html)서 사용 방법, 예시 등을 자세히 알아볼 수 있다. 역시 레퍼런스를 보는 것만큼 도움되는 게 없다.

또, 가능하면 **Jupyter Notebook**을 사용해서 중간 과정들을 쉽게 살펴보도록 하자. (이 포스트에서도 Jupyter를 사용하고 그 결과를 캡처해 가져올 것이다.)

## Import
우선, 필요한 라이브러리를 import하자.

```python
import numpy as np
import pandas as pd
import matplotlib as plt
from scipy import stats

import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.api import qqplot
```

## Dataset
우리는 **sunspots** dataset을 가져와 사용할 것이다. [여기](https://www.statsmodels.org/stable/examples/notebooks/generated/tsa_arma_0.html)를 참고하여 작성했다.

해당 dataset에 대한 정보는 `.NOTE`를 통해 볼 수 있다. 

```python
print(sm.datasets.sunspots.NOTE)
```

```
::

    Number of Observations - 309 (Annual 1700 - 2008)
    Number of Variables - 1
    Variable name definitions::

        SUNACTIVITY - Number of sunspots for each year

    The data file contains a 'YEAR' variable that is not returned by load.
```

이제 pandas DataFrame 포맷으로 가져오자.

```python
dat = sm.datasets.sunspots.load_pandas().data
```

```
YEAR	SUNACTIVITY
0	1700.0	5.0
1	1701.0	11.0
2	1702.0	16.0
3	1703.0	23.0
4	1704.0	36.0
...	...	...
304	2004.0	40.4
305	2005.0	29.8
306	2006.0	15.2
307	2007.0	7.5
308	2008.0	2.9
309 rows × 2 columns
```

보기 좋게 바꿔주자.
```python
dat.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
del dat["YEAR"]
```

이제, 주어진 데이터를 플로팅해보자. 적당히 큰 사이즈로 출력하기 위해 `figsize`를 지정한다.

```python
dat.plot(figsize=(12,8))
```

![](/imgs/mge/tsa19.png)

## Stationarity / Transformation
**이 데이터는 정상적(stationary)인가?** 만약 정상적이지 않다면 우리는 추가적인 transformation을 수행할 수 있다. 가령 로거리듬(logarithm)을 사용하거나, $1^{st}$, $2^{nd}$ differencing을 적용할 수도 있다. 만약 differencing을 사용한다면, 우리는 **ARIMA**($p,d,q$) for nonzero $d$로 여기게 될 것이다.

Transformation은 pandas DataFrame 레벨에서 수행할 수 있다. `DataFrame.transform(function)`은 DataFrame의 데이터 각각에 `function`을 적용함으로써 transformation을 가능케 한다. 만약 로거리듬을 적용한다면 다음과 같이 해볼 수 있을 것이다.

```python
dat = dat.transform(lambda x: math.log2(x))
```

여기선 추가적인 transformation을 적용하지 않는다. 즉, differencing도 하지 않으므로 일단은 **ARIMA($p,0,q$)**다.

## ACF / PACF
**MA**, **AR** 성분을 확인하기 위해 **ACF**와 **PACF**를 플로팅해보자.

```python
sm.graphics.tsa.plot_acf(dat, lags=50)
sm.graphics.tsa.plot_pacf(dat, lags=50)
```

![](/imgs/mge/tsa20.png)
![](/imgs/mge/tsa21.png)

파란 영역 내에 있는 점은 $0$과의 significant difference가 없다고 여길 수 있다. 여기서, ACF는 tail-off되는 양상을 보이고, PACF는 time lag, $2$ 이후로 cut-off되는 양상을 보인다. 즉, 이 두 그래프만을 봤을 때 우리는 우선 **ARIMA($2,0,0$)**을 candidate로 설정할 수 있다.

## Fitting Models / Residual Analysis
이제 **ARIMA($2,0,0$)**을 데이터에 피팅해보고, 잔차 분석(residual analysis)을 수행해보자.

```python
resid = ARIMA(dat, order=(2,0,0)).fit().resid
```

우선 잔차를 직접 플로팅해볼까?

![](/imgs/mge/tsa22.png)

정규성 검증은 아주 간단히 이루어진다. **scipy**의 `normaltest()`를 사용하자.

```python
stats.normaltest(resid)
```

아름다운 P-value다...
```
NormaltestResult(statistic=49.84412434485992, pvalue=1.501363733141781e-11)
```

마지막으로, 잔차의 **ACF** / **PACF**와 **Q-Q plot**을 그려보자.

![](/imgs/mge/tsa23.png)
![](/imgs/mge/tsa24.png)
![](/imgs/mge/tsa25.png)

꽤 괜찮게 모델링이 이루어진 것 같다!


# 마치며
생략한 부분이 조금 많은데, 문서를 잘 살펴보면 더 많은 유용한 도구를 찾아볼 수 있다. 아무튼 **statsmodels**는 통계적 분석을 위한 좋은 툴이므로 많이 활용해보자!