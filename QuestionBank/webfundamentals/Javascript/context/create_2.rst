.. activecode:: create_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: context
   :topics: Javascript/context
   :from_source: T
   :language: html

   <html>
      <body>
          <button onclick="savetime()">Time</button>
          <table id="timetable">
          </table>
          <script type="text/javascript">
             clickon = function() {
                 alert("Hello!");
             }
             savetime = function() {
                t = document.querySelector("#timetable");
                trow = document.createElement("tr");
                td = document.createElement("td");
                contents = document.createTextNode(Date());
                td.appendChild(contents);
                td.onclick = clickon;
                trow.appendChild(td);
                t.appendChild(trow);
             }
          </script>
      </body>
   </html>