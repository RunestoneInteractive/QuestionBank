.. activecode:: js_iter2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: iteration
   :topics: Javascript/iteration
   :from_source: T
   :language: html

   <html>
   <table id="mytable"></table>
   <script>
   tbl = document.querySelector("#mytable")
   for(i = 0; i < 10; i++) {
       row = document.createElement("tr")
       cell = document.createElement("td")
       cell.innerText = i
       row.appendChild(cell)
       tbl.appendChild(row)
   }

   </script>
   </html>