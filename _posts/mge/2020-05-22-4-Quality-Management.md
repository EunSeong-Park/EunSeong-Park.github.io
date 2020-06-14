---
title: "[OM 4] Quality Management"
tags: Management-Engineering OM
toc: true
---

# Intro
제품 및 서비스의 품질(quality)을 분석 및 관리하는 게 중요하다는 것은 굳이 설명하지 않아도 될 것이다. 하지만 그에 대한 방법을 명확히 할 필요가 있는데, 이를 위해 이번엔 품질 관리를 위한 process capability analysis, statistical process control 등의 유용한 기법들을 알아볼 것이다.


# Quality Management

- Proces control: Identification and control of major variance source
- Process improvement: Further reduction of variation and mean improvement


품질 관리에서의 가장 중요한 원칙은, _"Control comes first before improvement"_ 라 할 수 있다. 달리 말하면, 목표 평균치에 가까운데 막 퍼져있는 것보단, 좀 멀리 떨어져 있어도 편차가 적은 편이 낫다는 것이다. 왜냐? 이미 잘 control되어 있다면, 여기에 mean improvement를 수행하면 되기 때문이다. 사격 훈련이랑 비슷한 맥락이다.

![](/imgs/mge/om12.png)

우리는 다음과 같은 절차를 따라 품질 관리(quality management)의 방법을 알아볼 것이다.

![](/imgs/mge/om13.png)


# Statistical Process Control
우리는 보다 균일하고 안정적인 품질의 제품을 생산하기 위해 SPC를 사용한다. SPC는 통계적이고 수학적인 기법을 사용해 프로세스에 대한 객관적인 지표를 제공하며 그에 대한 개선책을 세울 수 있도록 한다.

![](/imgs/mge/om14.png)

우리는 여러 control chart를 이용해 프로세스를 분석 및 관리할 수 있다. Control chart는 관심 있는 대상이 무엇인지에 따라 크게 두 종류로 나눌 수 있다.

- Variable(계량형): 두께, 길이 등과 같이 numerical scale로 측정 가능한 값. $\bar{X}, R, S$ chart 등이 여기에 포함된다.
- Attribute(계수형): 불량/정상, 불량품 개수 등 이산적인 값. $p, np, c, u$ chart 등이 여기에 포함된다.

우리는 mean value와 variability에 관심이 있으므로, 여기선 $\bar{X}$와 $R$ chart를 이용할 것이다. 

기본적인 통계적 베이스는 간단히만 설명하고, 이후에 statistics 관련 포스팅에 따로 정리할 예정이다. 

## Construction of X-bar & R Chart
우리는 프로세스가 가지는 평균과 표준 편차를 모르고 있음을 가정한다. 즉, 표본으로부터 추정(estimation)을 해야 한다.

### R Chart
$R$은 주어진 샘플이 가지는 범위(range)다. 즉, 샘플 $j$에 대한 $R_j$는, $R_j = X_{max} - X_{min}$이다. R chart의 중심선(CL, Center Line)과 LCL/UCL(Lower/Upper Control Limit)은 다음과 같다.

- CL: $CL = \bar{R}$
- LCL/UCL: $\bar{R} \pm 3\sigma_{R}$

$\sigma_{R}$은 $\frac{d_3}{d_2} \hat{\sigma_{\bar{R}}}$를 통해 추정될 수 있다.

### X-bar Chart
$\bar{X}$는 샘플의 일부를 따와 평균을 낸 sample mean이다. 

- CL: $\bar{\bar{X}}$
- LCL/UCL: $\bar{\bar{X}} \pm 3\sigma_{\bar{X}} $

$\sigma_{\bar{X}}$는 $\frac{\hat{\sigma}_ {X}}{\sqrt{n}}$을 통해 추정될 수 있다.

좀 더 깔끔하게 정리하면 다음과 같다.

![](/imgs/mge/om16.png)

관리도 계수, $A, d$ 등은 [링크](http://www.moonrepeat.org/wiki/doku.php?id=%EA%B4%80%EB%A6%AC%EB%8F%84_%EA%B3%84%EC%88%98%ED%91%9C&redirect=1)에서 볼 수 있다.

### Example
![](/imgs/mge/om15.png)

[출처](http://www.moonrepeat.org/wiki/doku.php?id=x_bar_%EA%B4%80%EB%A6%AC%EB%8F%84)

위와 같은 프로세스가 있다고 생각해보자. CL은 각 샘플 그룹이 가지는 평균($\bar{x}$)의 평균, 57.6051이다. 또, 샘플 전체의 $\bar{R}$은 0.354로, 이를 이용해 UCL과 LCL을 구할 수 있다. $CL \pm A_2\bar{R} = 57.3933, 57.8169$

이렇게 데이터가 주어졌을 때, control chart는 어떻게 그릴까? 엑셀을 사용하는 방법도 있지만, [Minitab](http://datalabs.co.kr/html/support/DemoDownload.php)이라는 유용한 도구가 있다. 심심하면 써보자.

## Management
주로 $R$ chart를 먼저 분석하여 이를 관리하고, 만족스런 결과가 나오면 $\bar{X}$ chart를 분석하여 이를 관리하는 식으로 이루어진다. (맨 위쪽 그림에서 볼 수 있다)

만약 제대로 컨트롤이 되지 않고 있다면, 그러한 원인을 찾아야 한다. 원인은 프로세스 자체에 내재되었을 수도, 여러 작은 요인들이 뭉치고 뭉쳐 만들어졌을 수도, 일부 설비, 재료, 인원의 문제일 수도 있다. 또는, 잘못된 방식으로 설비나 도구를 이용했을 수도, 공정 내에 비합리적이고 불필요한 절차가 있었을 수도 있다.

일부는 우연히, 그리고 필연적으로 발생할 수 있지만, 어떠한 문제는 충분히 개선이 가능할 것이다. 그렇다면 이를 찾아내 고치면 된다. 말은 쉽다.

또, 5M1E라는 품질 변동의 원인들을 나타내는 범주가 있다.

- Men: 사람 각각의 역량 및 업무 방식
- Meterials: 제품 생산을 위한 재료의 특성
- Methods: 업무 수행 방식, 설비 및 공정 배치 등
- Measurements: 측정 방식 및 도구 등
- Machine: 기계 및 설비의 성능, 노후화 여부 등
- Environments: 다양한 측면에서의 업무 환경

이를 이용해 문제들을 잘 카테고라이징해서 분석하면 보다 용이할 것이다.

## Summary
정리하면, SPC를 통해 품질의 균일화를 추구할 수 있고, 계량적인 요소(variable)의 경우 $\bar{X}, R$ chart 등을 사용할 수 있다. 만약 어떤 품질에 대하여 프로세스 자체의 평균 혹은 표준 편차를 알지 못한다면, 샘플을 통해 추정을 할 수 있다.

또, 이렇게 세운 control chart를 통해, 개선 가능한(assignable) 품질 변동의 원인들을 분석 및 해결할 수 있다.


# Process Capability Analysis
Process capability란, 프로세스를 평가하기 위한 간단한 형태의 지표다. 공정능력 정도로 번역되는 듯하다. 이는 프로세스가 안정적(in control)인 상태에 있을 때, 프로세스가 산출해내는 품질에 대한 달성능력을 의미한다. 달리 말하면, "얼마나 규격에 맞는 제품을 생산해낼 수 있는가?"에 대한 척도다.

그 전에 몇 가지 간단한 개념들을 짚고 가자.

## Tolerance
대부분의 제품과 서비스, 그리고 이들을 구성하는 각 요소는 그에 맞는 tolerance, 즉 허용 범위가 있다. 예를 들어, 아메리카노에 물을 30mL만 넣는다거나, 0.5mm 샤프심을 만드는데 0.9mm로 만든다거나, 이런 경우는 명백히 허용 범위를 넘는, defect일 것이다. 반면, 5kg 덤벨을 생산하는데, 정확한 무게를 만들기 위해 CGPM에서 정의한 1kg의 정의를 따라 한치의 오차도 없이 만들기 위해 노력하는 건 분명한 낭비다.

그래서 어떤 이상적인 수치를 기준으로 그 허용 범위 내에 있으면 해당 제품은 통과하는 방식을 사용한다. 물론 이상적인 값에 가까울 수록 좋을 것이다.

Tolerancing은 ideal value(basic)로부터 그 범위의 방향에 따라 세 타입으로 나누어 볼 수 있다.

### N-Type
Nominal-the-best. Basic으로부터 LSL(Lower Specification Limit)과 USL(Upper Specification Limit)이 모두 존재하는 형태다. 샤프심 두께는 아마 N-type일 것이다. 너무 얇아도, 너무 두꺼워도 문제가 생기기 때문이다.

$X \in [LSL, USL]$이면 그 샘플은 통과하고, 그렇지 않으면 불량으로 간주한다. 이를 통해 우리는 proportion of reject를 계산할 수 있다.

우선, central limit theorem을 적용해, 각 sample은 normal distribution에 근사될 수 있다고 가정한다. 즉, $X \sim N(\mu, \sigma^2)$이면,

$p = P[X < LSL] + P[X > USL] =$ $P[Z < \frac{LSL - \mu}{\sigma}] + P[Z > \frac{USL - \mu}{\sigma}]$

![](/imgs/mge/om17.png)

### S-Type
Smaller-the-best. Basic으로부터 USL만 존재한다. 보통은 non-negative로 범위를 한정한다. 예를 들어 화학 제품의 불순물 양, 모니터의 불량 화소 개수 등은 적을 수록 좋을 것이다.

Proportion of reject는 USL보다 큰 경우일 것이다.

$p = P[X > USL] = P[Z > \frac{USL - \mu}{\sigma}]$

### L-Type
Larger-the-best. Basic으로부터 LSL만 존재한다. 예를 들어 물체의 내구성(강도 등)이나 배터리 수명 등은 클 수록 좋을 것으로 보인다. 

Proportion of reject는 LSL보다 작은 경우다.

$p = P[X < LSL] = P[Z < \frac{LSL - \mu}{\sigma}]$

## Process Capability Index
$C_p$는 다음과 같이 정의된다. 즉, natural tolerance($6\sigma$)에 대한 specification width의 비율이다. 

$ C_p = \frac{USL-LSL}{6\sigma}$

예를 들어, $USL-LSL$이 6이고, 표준 편자가 1이라면 $C_p$는 1.0이 된다. 그럼 어느 정도가 좋은 공정능력이라고 볼 수 있을까? 보통은 1.33 이상을 적합한 수준으로, 1 미만을 부족한 수준으로 본다. 높을 수록 좋은 수치지만, 과도하게 높다면(1.68 이상) 프로세스를 어느 정도 간소화하는 등의 방향으로 품질 관리의 비용을 절약하는 전략을 세워볼 수 있다.

$C_p$는 얼마나 분산되어 있는지(variability)만을 보기 때문에, 분포의 치우침, 즉 mean-shift를 고려하지 못한다. 아래의 B, C는 A와 같은 $C_p$를 갖는데, 이는 분명히 문제가 있어 보인다.

![](/imgs/mge/om18.png)

$C_{pk}$는 $C_p$에서 치우침의 정도, $k$를 함께 고려한 지수다. $C_{pk}$는 다음과 같이 정의된다.

$C_{pk} = min(C_{pL}, C_{pR})$ where $C_{pL} = \frac{\mu - LSL}{3\sigma}, C_{pR} = \frac{USL - \mu}{3\sigma}$

둘 중 minimum을 선택한다는 것은, 더 안좋은 쪽을 고려하겠다는 의미다. (conservative decision) $C_{pk}$ 또한 1.33 이상을 적합한 수준으로 본다. 

$C_{pk}$는 평균이 치우친 상황에서도 적용 가능한 점에서 $C_p$보다 나은 지표처럼 보이나, 여기에도 한계가 있다. 목표치(target)를 고려하지 않는다는 점, (가정을 하고 시작하므로) 분포 자체의 형태를 고려하지 않는다는 점 등이 있다. 본격적인 Process capability analysis 전에 normality test가 필요한 이유일 듯 하다.


# 마치며
꽤 분량을 길게 썼다. 기초적인 통계적 베이스가 어느 정도 필요한 내용이었는데, 아무래도 통계 복습을 해야할 것 같다.

아무튼 다음엔 forecasting에 대해 알아보도록 하자.