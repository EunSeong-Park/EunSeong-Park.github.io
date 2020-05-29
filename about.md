---
layout: article
titles: "About"
key: page-about
---

<style>
  .swiper-demo {
    height: 150px;
  }
  .swiper-demo .swiper__slide {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    color: #fff;
  }
  .swiper-demo .swiper__slide:nth-child(even) {
    background-color: #ff69b4;
  }
  .swiper-demo .swiper__slide:nth-child(odd) {
    background-color: #2593fc;
  }
  .swiper-demo--dark .swiper__slide:nth-child(even) {
    background-color: #312;
  }
  .swiper-demo--dark .swiper__slide:nth-child(odd) {
    background-color: #123;
  }
  .swiper-demo--image .swiper__slide:nth-child(n) {
    background-color: #000;
  }
</style>



<div class="swiper swiper--light my-3 swiper-demo swiper-demo--1">
  <div class="swiper__wrapper">
    <div class="swiper__slide">
      about을 가장한 테스트용 페이지    
    </div>
    <div class="swiper__slide">
      <a href="https://tianqi.name/jekyll-TeXt-theme/test/">참고 자료</a>
    </div>
    <div class="swiper__slide">3</div>
    <div class="swiper__slide">4</div>
    <div class="swiper__slide">5</div>
    <div class="swiper__slide">6</div>
    <div class="swiper__slide">7</div>
  </div>
  <div class="swiper__button swiper__button--prev fas fa-chevron-left"></div>
  <div class="swiper__button swiper__button--next fas fa-chevron-right"></div>
</div>


```python
def hello():
    print("it is test" + 3)
    return a
```

<div class="item" style="box-shadow: 1px 1px 1px 1px gray;  margin-bottom: 2px; border-radius: 3px; cursor: pointer;" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="item__image">
    <img class="image" src="/imgs/etc/3.png">
  </div>
  <div class="item__content" style="padding-bottom: 0;">
    <div class="item__header">
      <h4>Sample</h4>
    </div>
    <div class="item__description">
      <p>이것은 굉장한 프로젝트로, 정말 굉장한 프로젝트여서 남들로 하여금 굉장한 프로젝트가 굉장한 프로젝트임을 부인할 수 없도록 만들 정도의 굉장한 프로젝트임을 보여준다. 그래서 이 굉장한 프로젝트는 그것의 굉장함을 굉장하게 표현하는 굉장한 프로젝트라고 할 수 있겠다. 그리하여 이 굉장한 프로젝트는 실로 굉장한 프로젝트라 부를 수 있을 만한 굉장한 프로젝트가 되었다.</p>
    </div>
  </div>
</div>



<div class="card" style="display: inline-block;">
  <div class="card__image">
    <img src="/imgs/etc/2.png">
  </div>
  <div class="card__content" style="height: 2rem; padding:0;">
    <div class="card__header">
      <p style ="margin:0; padding: 0 0.5rem 0 0.5rem;">sample pic2</p>
    </div>
  </div>
</div>

<table class="item">
    <tr>
        <th><img class = "img_table_item" src="https://eunseong-park.github.io/imgs/etc/2.png"></th>
        <td>
          <p class="p_table_item">Hello i am eunseong park nice to meet you Hello i am eunseong park nice to meet youHello i am eunseong park nice to meet you</p>
        </td>
    </tr>
</table>




<!-- SCRIPT -->
<script>
  {%- include scripts/lib/swiper.js -%}
  var SOURCES = window.TEXT_VARIABLES.sources;
  window.Lazyload.js(SOURCES.jquery, function() {
    $('.swiper-demo--0').swiper();
    $('.swiper-demo--1').swiper();
    $('.swiper-demo--2').swiper();
    $('.swiper-demo--3').swiper();
    $('.swiper-demo--4').swiper({ animation: false });
  });
</script>