---
title: "[CSS] 속성: 테두리(Border)"
tags: HTML CSS
toc: true
---

대부분의 요소들은 테두리, 혹은 보더(border)를 가진다. 테두리는 각 요소들의 구분, 어떤 요소의 강조 등 여러 목적으로 사용될 수 있고, 그만큼 필수적이다. 

# Layout

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

위의 예시에서 알 수 있듯, 속성값 할당은 다음과 같이 이루어진다. 이는 테두리뿐 아니라 대부분의 요소에 해당된다(나중에 이와 관련한 내용을 따로 정리할 예정이다).

- 네 값이 주어짐: `top` `right` `bottom` `left`
- 세 값이 주어짐: `top` `right & left` `bottom`
- 두 값이 주어짐: `top & bottom` `right & left`
- 하나만 주어짐: `top & bottom & right & left`

## border-color
`border-color`는 테두리의 색상을 결정하는 속성이다. 색상은 다양한 방법으로 정의될 수 있다.

- CSS에서 미리 정의한 140개의 색상 키워드가 있다. 대소문자를 구분하지 않고, 동일한 색상을 가리키는 다른 키워드가 몇 있다. [키워드 보기](https://www.tutorialrepublic.com/css-reference/css-color-names.php)
  - Example: `black`, `red`
- 16진수 표기법(Hex)을 사용할 수 있다. R, G, B 각각이 0x0-0xFF까지의 값을 가질 수 있다.
  - Example: `0xFF0000`(red), `0xFFFFFF`(white)
- 10진수 RGB, RGBA 표현이 가능하다.
  - Example: `rgb(255, 0, 0)`, `rgba(255, 255, 0, 0.6)`


<script async src="https://static.codepen.io/assets/embed/ei.js"></script>



