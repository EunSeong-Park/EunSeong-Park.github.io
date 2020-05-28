---
layout: article
titles: "About"
key: page-about
---

<style>
  .swiper-demo {
    height: 20px;
  }
  .swiper-demo .swiper__slide {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
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
[참고문서](https://tianqi.name/jekyll-TeXt-theme/test/)
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

<div class="card">
  <div class="card__image">
    <img src="/imgs/etc/1.gif">
  </div>
  <div class="card__content">
    <div class="card__header">
      <h4>미안하다</h4>
    </div>
    <p>이거 보여주려고 어그로끌었다..나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..</p>
  </div>
</div>


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