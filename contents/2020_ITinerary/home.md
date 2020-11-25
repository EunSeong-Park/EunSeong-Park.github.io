---
layout: article
key: page-itinerary-home
header: false
title: "Basic Python Programming"
permalink: /itinerary
article_header:
  type: overlay
  theme: dark
  background_color: '#203028'
  background_image:
    gradient: 'linear-gradient(135deg, rgba(34, 139, 87 , .4), rgba(139, 34, 139, .4))'
    src: /contents/sample_material/sample_bg.jpg
comment: false
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

# Welcome to the Course!

(Introduction video will be uploaded soon)

Hello, This is team **ITinerary**. In this course, we will learn about the basic and application of **Python**. The course will cover:

- **Python Basics**
- **Network Programming**
- **OpenCV**
- **PyGame**

# Guides
## Syllabus
The syllabus is available [here](assets/docs/syllabus.pdf).

## About the Class
Our class consists of three parts:

- **Pre-class**: We will provide some exercises or materials to prepare the class. **Don't worry, it is not mandatory.** We expect that you guys can follow real-time class very well even if you skipped the pre-class. But this pre-class may be helpful for you!
- **Real-time class**: We will meet on **Zoom** at every [class time]. Some lecture and lab session will be given. **Lab session** is a mini-project for exercising the concepts we covered. 
- **Post-class**: After the class, we will post the recording, additional materials. Like pre-class, **it is also not mandatory.** But reviewing with post-class will help you to fully acquire what you learned!

## If you have any issues...

- **Comments**: I opened the comment for each class material. If there are some typos, incorrect / unclear explanation or some question, feel free to ask me via comment. Disqus comment requires to sign up, but the task is easy and simple. (supports social login) **I recommend to use comment because it will be helpful to those who are having same / similar issues!**
- **WhatsApp**; (It will be announced soon)
- **E-mail**: 
  - **Eunseong Park**: dmstjd517@unist.ac.kr
  - **Jongmin Choi**: jm990621@unist.ac.kr
  - **Dohun Kim**: dohun1607@unist.ac.kr

# Contents
<div class="grid scale" id="grid_for_list" onclick="location.href='/itinerary/posts/pythonbasic';">
  <div class="cell cell--2"><img src="/contents/sample_material/pylogo.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">1. Python Basics </h5>
    <p id="p_for_list">Basic concepts and skills for Python</p>
  </div>
</div>

<div class="grid" id="grid_for_list" onclick="location.href='/itinerary/posts/network';">
  <div class="cell cell--2"><img src="/contents/2020_ITinerary/assets/imgs/Ego_network.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">2. Network Programming</h5>
    <p id="p_for_list">Networking, client-server</p>
  </div>
</div>


<div class="grid" id="grid_for_list" onclick="location.href='/itinerary/posts/opencv';">
  <div class="cell cell--2"><img src="/contents/2020_ITinerary/assets/imgs/opencv.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">3. OpenCV</h5>
    <p id="p_for_list">A computer-vision library for Python</p>
  </div>
</div>

<div class="grid" id="grid_for_list" onclick="location.href='/itinerary/posts/pygame';">
  <div class="cell cell--2"><img src="/contents/2020_ITinerary/assets/imgs/pygame.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">4. Pygame</h5>
    <p id="p_for_list">Python library for game and multimedia</p>
  </div>
</div>

# Timeline
- **2020-11-14**: Syllabus uploaded (v1)
- **2020-11-14**: S1 pre-class PPT uploaded
- **2020-11-15**: "Python Basics" sessions are merged (S1)
- **2020-11-15**: S1 pre-class PPT updated
- **2020-11-15**: S2 pre-class PPT uploaded
- **2020-11-16**: Session page updated
  - Fixed some bug in comment, video clip
- **2020-11-18**: S3 pre-class PPT uploaded (not completed)
- **2020-11-21**: S3 pre-class PPT completed
- **2020-11-22**: Session page updated
- **2020-11-23**: Session page updated
- **2020-11-24**: Some minor changes in main page
- **2020-11-24**: Syllabus updated (v2)
- **2020-11-24**: S4 pre-class PPT uploaded
- **2020-11-25**: S1 pre-class lecture video uploaded