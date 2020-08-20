.. activecode:: button_context_2
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
          <script type="text/javascript">
             var b1 = document.createElement("button");
             b1.innerHTML = "Button1";
             var b2 = document.createElement("button");
             b2.innerHTML = "Button2";

             hello = function() {
                 alert("Hello, who am I?");
             }

             document.body.appendChild(b1);
             document.body.appendChild(b2);
             b1.onclick = hello;
             b2.onclick = hello;
          </script>
      </body>
   </html>