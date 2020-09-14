---
title: "[OM 6] Inventory Management"
tags: Management-Engineering OM
toc: true
---

# Inventory
재고(inventory)란 경제적 가치를 지닌, 유휴 상태의(idle) 자원을 의미한다. 일상적인 의미보다 실제로 더 넓은 범위에 해당하는 용어인데, 제조업의 경우 생산품뿐 아니라 원자재나 비품 등을 모두 포함한다. 

유휴 상태인 만큼, 재고는 "지금 당장은" 사용하지 않는다. 그러면 우리는 왜 재고를 비축할까?

- 판매 및 생산, 자재 조달의 불확실성에 대비해 재고를 보유할 수 있다. 이로써 돌발적인 조달 기간 동안 고객의 수요를 충족시킬 수 있다.
- 수요의 상승을 기대하여 미리 재고를 비축할 수 있다. 특히, 계절적(seasonal)인 수요를 형성하는 제품의 경우, 본격적으로 계절이 시작하기 전 생산하는 등의 시도를 해볼 수 있다.
- 정기적이거나 대량의 자재 발주를 통해 생산 비용을 줄이기 위한 시도로 재고가 비축될 수 있다.

우리는 재고와 수요(demand)를 파악하고 관리함으로써 재고의 효과를 누림과 동시에 재고로 인한 피해를 최소화할 수 있다. 그게 재고 관리(inventory management)의 목적이다.


# Inventory Management
## Economic Order Quantity Model
EOQ 모델은 가장 기초적인 재고 관리 모델이다. EOQ에선 수요가 일정하게 유지되며 재고가 0이 될 때 다시 채워짐을 가정한다. 즉, 다음과 같은 시간-재고 그래프가 나온다.

![](/imgs/mge/om25.png)

물론, 재고가 0이 될 때 바로 채워넣는 건 현실적으로 불가능하다. 그래서 재고가 일정량 이하로 떨어질 때 재고를 채워넣기 시작한다.

![](/imgs/mge/om26.png)

EOQ 모델에서, 재고 관리에 드는 비용은 carrying cost와 order set-up cost의 합으로 나타낼 수 있다.

- Carrying cost: 재고를 유지하는 데 발생하는 비용
- Order set-up cost: 재고를 구매 및 생산하는 데 발생하는 비용

$$(Total) = \frac{Q}{2}H + \frac{D}{Q}S$$

- $Q$ : Order quantity (in units)
- $H$ : Holding cost per unit, per unit of time
- $D$ : Demand (in units) per unit of time
- $S$ : Order set-up cost

주문량 $Q$를 기준으로 보자. 주문량이 클 수록 유지 비용은 많이 들고, 생산 비용은 확실히 줄어들 것이다. 여기서, 우리는 주문량을 적절히 고름으로써 최소한의 비용만을 발생시킬 수 있다. 바로 두 종류의 cost가 만나는 교점이다.

![](/imgs/mge/om27.png)

또는, 프로세스의 개선을 통해 $H$ 또는 $S$를 줄이는 방법도 생각해볼 수 있다.

물론, 주문량에 따른 할인의 적용, 주문 자체에 따른 비용, 주문량이 한 번에 들어오지 않는 경우 등 더 많은 요소를 고려할 수 있다. 그건 여기서 커버할 필요는 없어보이니 생략한다.


## Economic Production Quantity Model
앞서 EOQ에선 "얼마나 주문을 해야 하는가?"를 알아보았다. 이젠 재고나 수요에 따라 "얼마나 생산해야 하는가?"에 대한 답을 찾아보자. 기본적인 EPQ 모델에서의 최적 생산량은 다음과 같다.

$Q^* = \sqrt{\frac{2DS}{H}}\sqrt{\frac{p}{p-u}}$

- $Q$ : Production quantity (in units)
- $H$ : Holding cost per unit, per unit of time
- $D$ : Demand (in units) per unit of time
- $S$ : Production set-up cost
- $p$ : Production or delivery rate
- $u$ : Usage rate

## Just-In-Time System
만약 주문이 들어오자마자 (추가적 비용 없이) 바로 생산을 할 수 있는 시스템이 있다면, 재고 관리에 드는 비용은 없거나 아주 적어질 것이다. 왜냐? 재고율이 제로가 되기 때문이다. 실제로 그것은 불가능에 가까운 일이지만, 그에 준하는 생산 전략으로 재고율을 제로로, 혹은 그에 가깝게 만들 수 있다. 이러한 전략 및 시스템을 JIT라고 한다.

JIT는 어떻게 달성할 수 있을까? Total-cost curve에서 optimal quantity($Q$)를 줄이면 된다. $Q$의 감소는 재고량의 감소를 의미하기 때문이다. 즉, $\sqrt{\frac{2DS}{H}}$에 주목하여, set-up cost를 줄이는 것이다. 수요나 holding cost를 늘릴 순 없잖아?

## Stochastic Inventory Model
위에서의 가정과 달리, 현실에선 수요가 항상 일정할 수 없고, 예기치 못한 사건으로 인해 수요 및 재고 조달 상황이 변할 수 있다. 재고를 다시 채워넣는 시점(ROP, ReOrder Point)이나 lead time은 어느 정도의 무작위성을 내포하고 있고, 그것은 재고 관리를 망가뜨릴 수도 있다. 

Stochastic inventory model은 여러 통계적, 수학적 기법으로 적절한 ROP 및 lead time을 추정하는 방법을 제공한다. 재고 관리는 수요에만 의존하는 게 아니므로, 다른 많은 요소들에 대해 이러한 방식을 잘 활용할 수 있다.

구체적인 파트는 생략한다. 


# 마치며
음..생각보다 코스에서 다룬 내용이 별로 없다. 

