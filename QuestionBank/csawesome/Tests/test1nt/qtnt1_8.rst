.. mchoice:: qtnt1_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II
   :answer_e: II and III
   :correct: c
   :feedback_a: A subclass needs to specify its own constructors.
   :feedback_b: A subclass has the ability to add new methods and variables that are unique to it (meaning its parent class dosen't contain them)
   :feedback_c: Subclasses can overide public methods from their parent classes to specialize behavior.
   :feedback_d: Neither of these statements are true.
   :feedback_e: Statement III is correct, but not statement II.
   :pct_on_first: 0.3722222222
   :total_students_attempting: 360
   :num_students_correct: 358.0
   :mean_clicks_to_correct: 2.1033519553

   Consider the following class declarations. Which statements are true?
   
   .. code-block:: java
   
      public class Animal
      {
       /* Some code */
      }
   
      public class Cat extends Animal
      {
         /* Some code */
      }
   
     I. Cat inherits the constructors of Animal
     II. Cat cannot add new methods and private instance variables that Animal does not have.
     III. Cat can override existing public methods of Animal