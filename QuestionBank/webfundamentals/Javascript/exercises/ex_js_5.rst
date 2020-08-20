.. actex:: ex_js_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Javascript
   :subchapter: exercises
   :topics: Javascript/exercises
   :from_source: T
   :language: html

   Create an html page with two text input boxes and four buttons.  The buttons should be labeled ``+``, ``-``, ``*``, and ``/``.  When one of these buttons is pressed you should get the `value` from both text input boxes and add, subtract, multiply, or divide the numbers entered in the text input boxes.  The result should be displayed below the buttons.  **Note** In order to do math  on the values you read from the text input boxes you will need to use ``Number.parseInt`` on the value.  for example   suppose you get a reference to input box 1 using ``myIn1 = document.querySelector("#in1id");`` then the statement ``value1 = Number.parseInt(myIn1.value)`` converts the string from the text input box to an integer.  In fact   most of the time Javascript will do the conversion for you automatically except for addition.
   ~~~~
   <html>



   </html>