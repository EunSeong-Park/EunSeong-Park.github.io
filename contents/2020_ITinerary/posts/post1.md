---
title: ""
key: itinerary-post1
permalink: /itinerary/posts/pythonbasic1
header: false
comments: true
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

<a class="button button--primary button--rounded button--xl" href="/itinerary">HOME</a>


# Pre-class
<div class="grid scale" id="grid_for_list" onclick="location.href='/contents/2020_ITinerary/assets/session_1_2/preclass.pdf';">
  <div class="cell cell--2"><img src="/contents/2020_ITinerary/assets/imgs/ppt_icon.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Pre-class PPT</h5>
    <p id="p_for_list">Python Basics</p>
  </div>
</div>

[here](/contents/2020_ITinerary/assets/session_1_2/preclass.pdf).