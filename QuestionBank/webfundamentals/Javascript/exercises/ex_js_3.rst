.. actex:: ex_js_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: exercises
   :topics: Javascript/exercises
   :from_source: T
   :language: html

   Given the following html.  Every time the button is pressed you should add a row to the table, where the new row of the table contains the sum of the previous two rows.  You should make use  of the lastChild, previousSibling, and innerText attributes in this exercise.
   ~~~~
   <html>
      <body>
         <button onclick="addrow()">Next</button>
         <ul id="mytable"><li id=0>1</li><li id=1>1</li></ul>
      </body>
   </html>