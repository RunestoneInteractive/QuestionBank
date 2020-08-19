.. mchoice:: KD.2.2.B
   :author: Kuri DiFede
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: F
   :practice: T
   :answer_a: Rectangle m1 = new Rectangle();
   :answer_b: int x = 2; Rectangle r = new Rectangle( x, x );
   :answer_c: Rectangle rect = new Rectangle( 4.0, 3.0 );
   :answer_d: Rectangle rect = new Rectangle( 4, 3 );
   :correct: c
   :feedback_a: This is fine, there is a constructor listed with no parameters.
   :feedback_b: This is fine, x is initialized as an integer and then used in the parameter.
   :feedback_c: The arguments inside the constructor signature are ints, this code uses doubles.
   :feedback_d: This is fine, 4 and 3 are both integers
   :pct_on_first: 0.487804878
   :total_students_attempting: 164
   :num_students_correct: 151.0
   :mean_clicks_to_correct: 1.8079470199

   Based off of the Monster constructor signature below, which is a invalid statement?
   
   .. code-block:: java
   
     public Rectangle( int length, int width );
     public Rectangle();