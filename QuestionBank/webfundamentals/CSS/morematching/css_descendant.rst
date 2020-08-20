.. activecode:: css_descendant
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: CSS
   :subchapter: morematching
   :topics: CSS/morematching
   :from_source: T
   :language: html

   <html>
      <head>
         <style>
         article h1 {
             color: purple;
         }
         </style>
      </head>
      <body>
      <h1>This is outside the article</h1>
      <article>
          <h1>This is inside the article</h1>
          <section>
              <h1>This is in a section of an article</h1>
          </section>
      </article>
      </body>
   </html>