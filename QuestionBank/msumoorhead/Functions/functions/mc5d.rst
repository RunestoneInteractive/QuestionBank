.. mchoice:: mc5d
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Functions
   :subchapter: functions
   :topics: Functions/functions
   :from_source: None
   :answer_a: def drawSquare(t, sz)
   :answer_b: drawSquare
   :answer_c: drawSquare(t, sz)
   :answer_d: Make turtle t draw a square with side sz.
   :correct: b
   :feedback_a: This line is the complete function header (except for the semi-colon) which includes the name as well as several other components.
   :feedback_b: Yes, the name of the function is given after the reserved word def and before the list of parameters.
   :feedback_c: This includes the function name and its parameters
   :feedback_d: This is a comment stating what the function does.

   What is the name of the following function?

   .. code-block:: python

     def drawSquare(t, sz):
         """Make turtle t draw a square of with side sz."""
         for i in range(4):
             t.forward(sz)
             t.left(90)