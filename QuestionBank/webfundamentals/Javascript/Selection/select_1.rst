.. activecode:: select_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: Selection
   :topics: Javascript/Selection
   :from_source: T
   :language: html

   <html>
      <label for="red">Red:</label>
      <input id="red" type="text" onchange="checkme(this)" />
      <label for="green">Green:</label>
      <input id="green" type="text" onchange="checkme(this)" />
      <label for="blue">Blue:</label>
      <input id="blue" type="text" onchange="checkme(this)" />

      <script type="text/javascript">
      checkme = function(textbox) {
         if (textbox.value > 255) {
            alert("Value is too large, must be less than 256");
            textbox.value = 255;
         }
      }
      </script>
   </html>