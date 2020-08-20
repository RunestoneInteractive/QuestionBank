.. activecode:: helper_array_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: helpObjects
   :topics: Javascript/helpObjects
   :from_source: T
   :language: html

   <html>
   <body>
     <ul>
        <li>Luther</li>
        <li>Coe</li>
        <li>Simpson</li>
        <li>Central</li>
        <li>Wartburg</li>
     </ul>
     <script>
         theList = document.querySelectorAll('li')
         alert(theList[0].innerText)
     </script>
   </body>
   </html>