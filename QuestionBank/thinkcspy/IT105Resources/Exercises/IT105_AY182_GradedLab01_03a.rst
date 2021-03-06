.. activecode:: IT105_AY182_GradedLab01_03a
   :author: Tom Babbitt
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: IT105Resources
   :subchapter: Exercises
   :topics: IT105Resources/Exercises
   :from_source: F
   :language: python
   :nocodelens:

   **This is your chance to increase your grade on graded lab 1. No late submissions will be accepted.**

   ::

      1. If you earned more than 14 points on question 3, you can earn up to 11 points or  a maximum of 110 total points for the lab, which ever is lower.
      2. Else you can replace your question 3 grade with up to  25.
      

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

   **Use the prewritten functions. Make sure you put your code below them.** You must use
   ``areaOfEqTriangle(side)`` and ``drawEqTriangle(turtle, side)`` to solve the problem and get full credit. 

 
   ~~~~
   ###Put your code below both function.
   import math
   import turtle
   def areaOfEqTriangle(side):
   #This function has one parameter side (length of one sides of a equilateral triangle).
   #It calculates the area and returns the area. If side is less than or equal to zero it returns -1.
      if side <= 0:
         area = -1
      else:
         area = math.sqrt(3)/4*side**2
      return area

   def drawEqTriangle(t, length):
   #This function has two parameters t (turtle object) and length (length of the side of an equilateral triangle). 
   # There is no return. The function prints the triangle to the screen with the length under it.
      t.fd(length)
      t.lt(120)
      t.fd(length)
      t.lt(120)
      t.fd(length)
      t.lt(120)
      t.rt(90)
      t.pu()
      t.fd(10)
      t.lt(90)
      t.write(areaOfEqTriangle(length))
      t.lt(90)
      t.fd(10)
      t.rt(90)
      t.pd()
   
   
   ###Put your code below this point.

   ### Name:

   ### define the drawTriangles(a,b,c,color) function here

   ### drawTriangles(50,45,40,"lightblue") #uncomment to test

   
   ====
   print("Note: This message does not mean your code is incorrect.") 
   print ("Please check your results against the picture for confirmation.")

   
    
.. activecode:: uniqueid
   :nocanvas:  -- do not create a canvas
   :autograde: unittest
   :nopre: -- do not create an output component
   :above: -- put the canvas above the code
   :autorun: -- run this activecode as soon as the page is loaded
   :caption: this is the caption
   :include: div1,div2 -- invisibly include code from another activecode
   :hidecode: -- Don't show the editor initially
   :nocodelens: -- Do not show the codelens button
   :timelimit: -- set the time limit for this program in seconds
   :language: python, html, javascript, java, python2, python3
   :tour_1: audio tour track
   :tour_2: audio tour track
   :tour_3: audio tour track
   :tour_4: audio tour track
   :tour_5: audio tour track
   :stdin: : A file to simulate stdin (java, python2, python3)
   :datafile: : A datafile for the program to read (java, python2, python3)
   :sourcefile: : source files (java, python2, python3)
   :available_files: : other additional files (java, python2, python3)

    If this is a homework problem instead of an example in the text
    then the assignment text should go here.  The assignment text ends with
    the line containing four tilde ~
    ~~~~
    print("hello world")
    ====
    print("Hidden code, such as unit tests come after the four = signs")