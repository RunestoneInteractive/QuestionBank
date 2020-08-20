.. activecode:: slot_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: bandit
   :topics: Javascript/bandit
   :from_source: T
   :language: javascript

   count = 0;

   getImage = function() {
      imgarray = Array("../_images/seven.png", "../_images/watermellon.png",
      "../_images/cherry.png", "../_images/bell.png",
      "../_images/diamond.png", "../_images/bar.png");

      rNum = Math.floor(Math.random()*imgarray.length);
      return imgarray[rNum];
   }

   swapImage = function() {
       d = document.getElementById("slot_2_js");
       iTag = document.createElement("img");
       iTag.src = getImage();
       d.innerHTML = "";
       d.appendChild(iTag);
       count++;
       if(count > 50) {
           window.clearInterval(intId,100);
       }
    }

    intId = window.setInterval(swapImage)