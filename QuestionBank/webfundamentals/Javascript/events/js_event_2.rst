.. activecode:: js_event_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: events
   :topics: Javascript/events
   :from_source: T
   :language: html

    <html>
      <head>
        <title>Colors</title>
      </head>
      <body>
        <label for="redi">Red:</label>
        <input type="text" id="redi" onchange="changeColor()" value="255" /> <br>
        <label for="greeni">Green:</label>
        <input type="text" id="greeni" onchange="changeColor()" value="255" /><br>
        <label for="bluei">Blue:</label>
        <input type="text" id="bluei" onchange="changeColor()" value="255" />
        <br>
        <button onclick="changeColor();">Change Color</button>

        <script>
          changeColor = function() {
              red = document.querySelector('#redi').value;
              green = document.querySelector('#greeni').value;
              blue = document.querySelector('#bluei').value;
              colorStr = "rgb("+red+","+green+","+blue+")";
              document.body.style.backgroundColor = colorStr;
          }
        </script>
      </body>
    </html>