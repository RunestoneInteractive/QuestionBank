.. activecode:: button_context_1
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
          <button onclick="hello()">Button1</button>
          <button onclick="hello()">Button2</button>
          <script type="text/javascript">
             hello = function() {
                 alert("Hello, who am I?");
             }
          </script>
      </body>
   </html>