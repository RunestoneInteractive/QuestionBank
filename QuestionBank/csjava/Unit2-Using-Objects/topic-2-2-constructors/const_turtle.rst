.. mchoice:: const_turtle
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-2-constructors
   :topics: Unit2-Using-Objects/topic-2-2-constructors
   :from_source: F
   :practice: T
   :answer_a: Turtle t = Turtle(world);
   :answer_b: Turtle t = new Turtle();
   :answer_c: Turtle t = new Turtle(world, 100, 100);
   :answer_d: Turtle t = new Turtle(100, 100, world);
   :correct: d
   :feedback_a: You must use the new keyword to create a new Turtle.
   :feedback_b: All turtle constructors take a world as a parameter.
   :feedback_c: The order of the parameters matter.
   :feedback_d: This creates a new Turtle object in the passed world at location (100,100)

   Which of these is valid syntax for creating and initializing a Turtle object?