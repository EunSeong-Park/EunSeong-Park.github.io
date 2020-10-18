---
layout: article
titles: "Sample"
key: page-sample
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

  /* DON'T USE JS TO THIS!! */
  #grid_for_list{
    box-shadow: 1px 1px 1px 1px #ccc;  
    border: 1px solid gray;
    border-radius: 3px;
    cursor: pointer;

    transform: scale(1);
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transition: all 0.1s ease-in-out;
  }

  #grid_for_list:hover {
    transform: scale(1.0125);
    -webkit-transform: scale(1.0125);
    -moz-transform: scale(1.0125);
    -ms-transform: scale(1.0125);
    -o-transform: scale(1.0125);
  }

  #cell_for_list{
    padding: 2px 2px 2px 2px;
  }
  #h_for_list{
    margin: 0 0 0 0.5rem;
  }
  #p_for_list{
    margin: 0 0 0 0.5rem;
  }
  div.cell img{
    border-right: 1px solid gray;
  }
</style>

# Sample
Here is a sample. Check in mobile, tablet and desktop! (only checked in desktop yet...)

## Sample hyperlink button
<div class="grid scale" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/contents/sample_material/sample_post1.html';">
  <div class="cell cell--2"><img src="/imgs/etc/3.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Sample link 1</h5>
    <p id="p_for_list">Move to dummy page!</p>
  </div>
</div>

<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/2.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Sample link 2</h5>
    <p id="p_for_list">Sample description 2</p>
  </div>
</div>

<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/1.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Sample link 3</h5>
    <p id="p_for_list">Sample description 3</p>
  </div>
</div>


<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/2.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Sample link 4</h5>
    <p id="p_for_list">Sample description 4</p>
  </div>
</div>

## Sample Video clip (Responsive)
<div style="position: relative; height:0; padding-bottom: 30%;">
<iframe width="480" height="270" src="https://www.youtube.com/embed/6TWJaFD6R2s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Sample download link

[naive link](/contents/sample_material/sample_py.py)

<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/contents/sample_material/sample_py.py';">
  <div class="cell cell--2"><img src="/imgs/etc/2.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">link via button</h5>
    <p id="p_for_list">Download now!!</p>
  </div>
</div>

## Sample PDF Viewer (only for tablet / desktop)

If the browser couldn't show the below PDF file properly, then [download](/contents/sample_material/sample_py.py) PDF directly.

<div stype="position: relative; height:0; padding-bottom: 56.25%;">
<iframe src="https://eunseong-park.github.io/contents/sample_material/sample_pdf.pdf" width="100%" height="700"></iframe>
</div>

Adjust size according to the PDF file!!

## Sample paragraph
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Sample Swiper
<div class="swiper swiper--light my-3 swiper-demo swiper-demo--1">
  <div class="swiper__wrapper">
    <div class="swiper__slide">
      Sample Swiper  
    </div>
    <div class="swiper__slide">
      <a href="https://tianqi.name/jekyll-TeXt-theme/test/">Reference</a>
    </div>
    <div class="swiper__slide">Slide 3</div>
    <div class="swiper__slide">Slide 4</div>
    <div class="swiper__slide">Slide 5</div>
    <div class="swiper__slide">Slide 6</div>
    <div class="swiper__slide">Slide 7</div>
  </div>
  <div class="swiper__button swiper__button--prev fas fa-chevron-left"></div>
  <div class="swiper__button swiper__button--next fas fa-chevron-right"></div>
</div>


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