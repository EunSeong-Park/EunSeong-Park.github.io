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
  .video-container {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56.25%;
  }

  .video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;  
  
  }
</style>


**The entire class is over. We want to express our appreciation for taking our course. Although we could not meet you face-to-face, this was a great time for us. We sincerely hope that our course was helpful for you, too. Take care, and enjoy your life with programming. Thank you, all!**
{:.success}


## Welcome to the Course!

<div style="width:100%; ">
  <div class="video-container">
    <iframe src="https://www.youtube.com/embed/J4MlP3mxXJk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

Hello, This is team **ITinerary**. In this course, we will learn about the basic and application of **Python**. The course will cover:

- **Python Basics**
- **Network Programming**
- **OpenCV**
- **PyGame**


## Syllabus
The syllabus is available [here](assets/docs/syllabus.pdf).

<img style="border: none;" src="/contents/2020_ITinerary/assets/imgs/announce/a.png">

## Announcements
<details>
<summary><b>View</b></summary>
<h4>201210</h4>
Session 4 recording is uploaded. Thank you!

<h4>201210</h4>
Session 3 recording is uploaded. Thank you!

<h4>201209</h4>
Session 2 recording is uploaded. Thank you!

<h4>201209</h4>
Session 1 recording is uploaded. Thank you!

<h4>201208</h4>
The lab session will be held at every 10:00AM - 1:00PM (GMT). You can access to the classroom via the <a href='https://us02web.zoom.us/j/9965189658?pwd=dGxPY1o4clZENnlvWC9MTW5aY09XUT09'>link</a>

<h4>201204</h4>
Simple and naive sample solution for 1.EX and 3.EX is uploaded. We think it is sufficient to help you come up with idea.

<h4>201203</h4>
Now, session 4, Pygame is available, good luck!

<h4>201202</h4>
Now, session 3, OpenCV is available.

<h4>201130</h4>
We inform that the syllabus is updated. Session 4 starts one-day earlier. It is to give you sufficient time for exercising by yourself, and preparing the real-time class. Thank you.

<h4>201130</h4>
Now, session 2, network programming is available, good luck!

<h4>201128</h4>
Now, session 1, Python basics is available.

<h4>201127</h4>
Hi all. Each sessions will be available on Nov 28, Nov 30, Dec 2, and Dec 4, respectively.  Also, we will inform the schedule about real-time class as soon as it is determined. Thank you.
</details>

## About the Class
Our class consists of three parts:

- **Pre-class**: We adopted **flipped learning** for this program. In the pre-class of each session, we will provide several exercises or supplement materials to prepare the class. Because of the short period of this program, we are trying to help you study in the pre-class as much as possible. So, please refer the materials, solve the exercises we provided, and **feel free to ask us** via comments. 
- **Real-time class**: We will meet on **Zoom** at **10:00AM to 1:00PM (GMT)**. In the class, we will review the lecture we covered, and hold an lab session. In the **Lab session**, you can apply the concepts and skills you learned, by implementing several mini-projects. 
- **Post-class**: After the class, we will post the recording, additional materials, and sample solutions for the lab session. Reviewing the contents may be helpful to you, so we strongly recommend to do that! 

## If you have any issues...

- **Comments**: I opened the comment for each class material. If there are some typos, incorrect / unclear explanation or some question, feel free to ask me via comment. Disqus comment requires to sign up, but the task is easy and simple. (supports social login) **I recommend to use comment because it will be helpful to those who are having same / similar issues!**
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
    <p id="p_for_list">Networking, client-server model, socket</p>
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



<!--

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
-->

<!--
- **2020-11-14**: Syllabus uploaded (v1)
- **2020-11-14**: S1 pre-class PPT uploaded
- **2020-11-15**: "Python Basics" sessions are merged (S1)
- **2020-11-15**: S1 pre-class PPT updated
- **2020-11-15**: S2 pre-class PPT uploaded
- **2020-11-16**: Session page updated
- **2020-11-18**: S3 pre-class PPT uploaded (not completed)
- **2020-11-21**: S3 pre-class PPT completed
- **2020-11-22**: Session page updated
- **2020-11-23**: Session page updated
- **2020-11-24**: Some minor changes in main page
- **2020-11-24**: Syllabus updated (v2)
- **2020-11-24**: S4 pre-class PPT uploaded
- **2020-11-25**: S1 pre-class lecture video uploaded
- **2020-11-26**: Session page updated
- **2020-11-26**: S1 supplement uploaded
- **2020-11-26**: Submission box added  
- **2020-11-27**: Session 1 completed
-->