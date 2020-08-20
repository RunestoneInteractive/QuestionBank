.. activecode:: IT105_AY182_TEE_TURTLES_2
  :author: Kyle King
  :difficulty: 0.0
  :basecourse: thinkcspy
  :chapter: IT105Resources
  :subchapter: Exercises
  :topics: IT105Resources/Exercises
  :from_source: F
  :language: python
  :autograde: unittest
  :nocodelens:

  ::

   Function: star.ray(t)
   Parameters: t - a turtle object
   What it does: This function draws a ray of a nautical star 
      using the given turtle then returns None. This function 
      will return the turtle to its original position and heading
   Returns: None

  The star module, described above, provides a ray funtion that takes a ``Turtle`` object and uses it to draw one ray of a nautical star, like this:

  .. Image:: https://runestone.academy/runestone/static/AY182_IT105/_static/IT105_ray.png
    :width: 200
    
  Your turtle will return to its original position at the end of the function. Use the ``ray`` function to draw a blue, five-pointed star, **exactly like this**:

  .. Image:: https://runestone.academy/runestone/static/AY182_IT105/_static/IT150_star.png
    :width: 200

  ~~~~
  import star
  import turtle

  # YOUR CODE GOES HERE
  ====
  
  from unittest.gui import TestCaseGui

  </textarea><script>
    var star = (function() {/*

      # begin star.py

      def ray(t):
        import math
        start = t.heading()
        t.speed(0)
        t.left(36)
        t.forward(75)
        t.right(52.527)
        t.forward(146.309)
        t.right(162)
        t.forward(200)
        t.begin_fill()
        t.left(144)
        t.forward(75)
        t.left(52.527)
        t.forward(145.309)
        t.left(162)
        t.forward(200)
        t.end_fill()
        t.right(180)

      # end star.py

    */}).toString().match(/[^]*\/\*([^]*)\*\/\}$/)[1].replace(/^ {4}/gm,'');
    Sk.externalLibraryCache['star'] = Sk.compile(star,'star.py','exec',true);
  </script><textarea style="display:none">