---
layout: article
titles: "Sample"
key: page-sample
---

<style>
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
Here is a sample. Check in mobile, tablet and desktop!

## Sample hyperlink button
<div class="grid scale" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/3.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">Sample link 1</h5>
    <p id="p_for_list">Sample description 1</p>
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

## Sample Video clip (480 width, 16:9)

<iframe width="480" height="270" src="https://www.youtube.com/embed/6TWJaFD6R2s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Sample download link

[naive link](/contents/sample_material/sample_py.py)

<div class="grid" id="grid_for_list" onclick="location.href='https://eunseong-park.github.io/';">
  <div class="cell cell--2"><img src="/imgs/etc/2.png"></div>
  <div class="cell cell--auto">
    <h5 id="h_for_list">link via button</h5>
    <p id="p_for_list">Download now!!</p>
  </div>
</div>