.. activecode:: css_disp1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: CSS
   :subchapter: layoutattributes
   :topics: CSS/layoutattributes
   :from_source: T
   :language: html

   <html>
      <head>
         <style>
            h1.gone {
                background-color: #bbbbbb;
                display: none;
            }
         </style>
       </head>
   <body>

      <h1>Hello World One</h1>
      <h1 class="gone">Hello World Two</h1>
      <h1>Hello World Three</h1>
      <h1 class="gone">Hello World Four</h1>
      <h1>Hello World Five</h1>
   </body>
   </html>