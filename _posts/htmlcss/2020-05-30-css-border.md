---
title: "[CSS] 속성: 테두리(border)"
tags: HTML CSS
toc: true
---

대부분의 요소들은 테두리, 혹은 보더(border)를 가진다. 테두리는 각 요소들의 구분, 어떤 요소의 강조 등 여러 목적으로 사용될 수 있고, 그만큼 필수적이다. 

# Layout
<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="css,result" data-user="eunseong-park" data-slug-hash="gOaVvNY" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="008">
  <span>See the Pen <a href="https://codepen.io/eunseong-park/pen/gOaVvNY">
  008</a> by EunSeong-Park (<a href="https://codepen.io/eunseong-park">@eunseong-park</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

위 코드에서, id가 `b`인 `<div>` 태그에 주목해보자. 회색 영역을 마진(margin), 파랑색 영역을 외곽선(outline), 검정색 영역을 테두리(border), 빨강색 영역을 패딩(padding), 그리고 초록색 영역을 내용(content)으로 볼 수 있다. 

테두리가 어느 위치에 있는지 간단히 확인만 해보았다. 이후 별도의 포스팅에서 더 자세히 다룰 예정이다.

# Property
## border
`border`는 테두리에 대한 단축 속성(shorthand property)으로, 테두리의 두께(`border-width`), 스타일(`border-style`), 그리고 색상(`border-color`)을 한 번에 지정할 수 있다. 이들 중 일부는 생략 가능하며, 생략된 값은 그 속성의 기본값으로 설정된다. 스타일은 기본값이 `none`이므로 생략하면 테두리가 보이지 않는다.

`border: (width) (style) (color)`

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="css,result" data-user="eunseong-park" data-slug-hash="GRpVrxq" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="004">
  <span>See the Pen <a href="https://codepen.io/eunseong-park/pen/GRpVrxq">
  004</a> by EunSeong-Park (<a href="https://codepen.io/eunseong-park">@eunseong-park</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>

또, 특정 방향(`top`, `bottom`, `left`, `right`)의 속성을 지정하고 싶다면 `border-(side)` 속성을 사용할 수 있다. 이는 아래의 세부 속성들에도 사용 가능하다.

이제 테두리에 대한 세부적인 속성들을 알아보도록 하자.

## border-width
`border-width`는 테두리의 두께를 결정하는 속성이다. CSS에서 지원하는 다양한 길이 단위(px, em 등)를 사용할 수 있고, `thin`과 같은 몇 가지 추가적인 키워드를 사용할 수 있다. 또, 테두리 네 방향 각각에 다른 값을 부여할 수도 있다. 

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="css,result" data-user="eunseong-park" data-slug-hash="dyYxJdv" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="005">
  <span>See the Pen <a href="https://codepen.io/eunseong-park/pen/dyYxJdv">
  005</a> by EunSeong-Park (<a href="https://codepen.io/eunseong-park">@eunseong-park</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>

위의 예시에서 알 수 있듯, 속성값 할당은 다음과 같이 이루어진다. 이는 테두리뿐 아니라 대부분의 요소에 해당된다. (나중에 이와 관련한 내용을 따로 정리할 예정이다.)

- 네 값이 주어짐: `top` `right` `bottom` `left`
- 세 값이 주어짐: `top` `right & left` `bottom`
- 두 값이 주어짐: `top & bottom` `right & left`
- 하나만 주어짐: all

## border-color
`border-color`는 테두리의 색상을 결정하는 속성이다. 색상은 다양한 방법으로 정의될 수 있다.

- CSS에서 미리 정의한 140개의 색상 키워드가 있다. 대소문자를 구분하지 않고, 동일한 색상을 가리키는 다른 키워드가 몇 있다. [(키워드 리스트)](https://www.tutorialrepublic.com/css-reference/css-color-names.php)
  - Example: `black`, `red`
- 16진수 표기법(Hex)을 사용할 수 있다. R, G, B 각각이 0x0-0xFF까지의 값을 가질 수 있다.
  - Example: `0xFF0000`, `0xFFFFFF`(
- 10진수 RGB, RGBA 표현이 가능하다. 투명도($\alpha$)는 0과 1 사이의 값을 가진다.
  - Example: `rgb(255, 0, 0)`, `rgba(255, 255, 0, 0.6)`
- HSL 표현이 가능하다. 색조는 0-360, 채도와 명도는 백분율을 값으로 가진다.
  - Example: `hsl(160, 50%, 100%)`
- `transparent` 키워드를 사용하여 투명하게 만들 수 있다.

또, `border-color`가 지정되지 않은 경우, 그 값은 부모로부터 상속받는다.

## border-style
`border-color`는 테두리의 스타일, 혹은 모양을 결정하는 속성이다. 

Keyword | Description
---|---
`none` | 테두리를 표시하지 않는다. 일반적인 경우 `border-width`는 지정된 값을 무시하고 0이 되며, 테두리 간 가장 낮은 우선순위를 가진다.
`hidden` | 테두리를 표시하지 않는다. 일반적인 경우 `border-width`는 지정된 값을 무시하고 0이 되며, 테두리 간 가장 높은 우선순위를 가진다.
`solid` | 테두리가 실선(solid line)으로 이루어진다.
`dotted` | 테두리가 점선(dotted line)으로 이루어진다.
`dashed` | 테두리가 파선(dashed line)으로 이루어진다.
`double` | 테두리가 두 개의 실선으로 이루어진다.
`groove` | 테두리에 파인 느낌을 준다.
`ridge` | 테두리에 튀어나온 느낌을 준다.
`inset` | 요소에 파인 느낌을 준다.
`outset` | 요소에 튀어나온 느낌을 준다.

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="html,result" data-user="eunseong-park" data-slug-hash="ExVqQYN" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="006">
  <span>See the Pen <a href="https://codepen.io/eunseong-park/pen/ExVqQYN">
  006</a> by EunSeong-Park (<a href="https://codepen.io/eunseong-park">@eunseong-park</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>

## border-radius
지금까지는 전부 사각형 테두리만을 그려보았다. 이젠 `border-radius` 속성을 사용하여 모서리를 둥글게 만들어 보자.

한 테두리는 모서리를 네 개 가지고 있고, 각 모서리에 접하는 타원은 그것의 너비와 높이에 의해 결정된다. (이 때, 너비와 높이가 같으면 일반적인 원이 된다.) 즉, 우리는 `border-radius`를 온전히 결정하기 위해 총 8개의 값이 필요한 셈이다.

가장 일반적인 형태는 다음과 같다.

```
border-radius: w_top-left w_top-right w_bottom-right w_bottom-left / h_top-left h_top-right h_bottom-right h_bottom-left
```

`/`에 의해 너비와 높이가 구분되며, 그 안에서 각 속성값은 공백에 의해 구분되고, 2, 1, 4, 3 사분면 순서로 지정된다. 여기엔 다음과 같은 생략 규칙이 있다.

- `/`가 생략된 경우, 너비와 높이는 같은 것으로 본다.
  - 즉, 원형 모서리다.
- 너비 지정이나 높이 지정 내에서, 주어진 속성값의 개수에 따라 다음과 같이 설정된다.
  - 네 값이 주어짐: `top-left` `top-right` `bottom-right` `bottom-left`
  - 세 값이 주어짐: `top-left` `top-right & bottom-left` `bottom-right`
  - 두 값이 주어짐: `top-left & bottom-right` `top-right & bottom-left`
  - 하나만 주어짐: all

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="css,result" data-user="eunseong-park" data-slug-hash="eYpqVEg" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="007">
  <span>See the Pen <a href="https://codepen.io/eunseong-park/pen/eYpqVEg">
  007</a> by EunSeong-Park (<a href="https://codepen.io/eunseong-park">@eunseong-park</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>

익숙하지 않다면 할당 방식이 조금 복잡하게 느껴질 수도 있다. 헷갈릴 때마다 레퍼런스를 확인하거나 직접 시뮬레이션을 해보자.

<script async src="https://static.codepen.io/assets/embed/ei.js"></script>



