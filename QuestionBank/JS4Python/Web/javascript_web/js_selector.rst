.. activecode:: js_selector
   :author: bmiller
   :difficulty: 3.0
   :basecourse: JS4Python
   :chapter: Web
   :subchapter: javascript_web
   :topics: Web/javascript_web
   :from_source: T
   :language: html

   <html>
      <body>
         <h1>Hello World!!</h1>
         <button onclick="changeThisPageFunc();">Click Me!</button>
         <main>
            <h1>Hello Main</h2>
            <p>The quick brown fox jumped over the lazy dog.</p>
         </main>
         <script type="text/javascript">
            changeThisPageFunc = function() {
               var myMain;
               document.body.style.backgroundColor = "lightblue";
               myMain = document.querySelector('main');
               myMain.innerHTML = "<h3>Where have all the flowers gone?<h3>";
               myMain.style.height = "50px";
               myMain.style.width = "50%";
               myMain.style.backgroundColor = "lightgreen";
            }
         </script>
      </body>
   </html>