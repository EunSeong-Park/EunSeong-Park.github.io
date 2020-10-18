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

  a {
    color: blue;
    font-weight: normal;
  }

</style>

<div style = "text-align: center;">
<p style="font-size:2em;font-weight:bold;">Eunseong Park / 박은성</p></div>


<div style="text-align: center;">
<img src="/imgs/etc/3.png" style="border:none;">
</div>


- <i class="far fa-envelope"></i> <a href = "dmstjd517@unist.ac.kr">dmstjd517@unist.ac.kr</a>
- <i class="fab fa-github"></i> <a href = "https://github.com/eunseong-park">github.com/Eunseong-Park</a>


I am a third-grade undergraduate student majoring **Computer Sceince & Engineering(CSE)** at **UNIST**. I am interested in **computer archtecture & system** and **data science**. 



### Experiences
- **Majoring Computer Science and Engineering (2019.-)**
- **Minoring Industrial Engineering (2019.-)**
- **2019 World Friends ICT Volunteer in Ghana (2019.07-2019.08)**
  - App development education
  - OpenCV education
  - Automated agriculture project
- **Internship in ISSL(2020.06-)**
  - Trustworthiness of Serverless Computing
  
### Honors & Awards & Scholarships
- **2019 World Friends ICT (UNIST-GahU, 최우수, 2019.12)**
- **유하푸른재단 2기 장학생 (2018-)**
- **KT 그룹 희망나눔재단 장학생 (2020.07)**

### Skills
- **System Software Programming**
  - Intel SGX
  - Assembly (x86-64, MIPS)
- **Python Programming**
  - OpenCV
  - Data Science & Analysis
- **Cloud Computing**
  - OpenWhisk
- **Languages Available**
  - Python
  - C/C++
  - Java
  - Scala
  - OCaml
  - HTML / CSS / JavaScript
  


<!--
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
-->

<!--
<div class="grid scale" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/3.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">엄청난 해바라기</h5>
    <p id="p_for_list">어메이징한 부가설명</p>
  </div>
</div>
<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/2.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">놀라운 검정색</h5>
    <p id="p_for_list">어메이징한 부가설명</p>
  </div>
</div>
-->

<!--
<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/1.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">굉장한 그림</h5>
    <p id="p_for_list">어메이징한 부가설명</p>
  </div>
</div>
-->





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