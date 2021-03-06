.. activecode:: IT105_AY182_GradedLab01_03
   :author: Tom Babbitt
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: IT105Resources
   :subchapter: Exercises
   :topics: IT105Resources/Exercises
   :from_source: F
   :language: python
   :nocodelens:
   :include: IT105_AY182_GradedLab01_01, IT105_AY182_GradedLab01_02

   Write a function ``drawTriangles(a,b,c,color)`` that will create a Turtle and Screen object
   and draw three equilateral triangles with the area written in the triangle. 
   The function has no ``return``.

   The three equilateral triangles will have the bottom left corners at **(0,100)** with side length a, 
   **(0, -100)** with side length b, and **(-100,0)** with side length c. The turtle will return to origin **(0,0)** 
   and face east. The screen background will be changed to color. The first image shows the coordinates 
   where triangles are drawn.

   .. image:: https://runestone.academy/runestone/static/AY182_IT105/_static/AY182_GradedLab01_03a.png
       :alt: Picture of requirements   

   Example function call:

   ::

      drawTriangles(50,45,40,"lightblue")
   
   results in

   .. image:: https://runestone.academy/runestone/static/AY182_IT105/_static/AY182_GradedLab01_03b.png
       :alt: Picture of results

   **Use The Function from Question 1 and 2 Here.** Note you can call
   ``areaOfEqTriangle(side)`` and ``drawEqTriangle(turtle, side)`` in 
   this code block. 

   For full credit **do not copy them here.**   
   ~~~~
   ### Name:

   ### define the drawTriangles(a,b,c,color) function here

   ### test drawTriangles(a,b,c,color)
   
   ====
   print("Check your results against the picture.")