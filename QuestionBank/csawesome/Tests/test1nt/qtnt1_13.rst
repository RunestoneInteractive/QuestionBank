.. mchoice:: qtnt1_13
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: F
   :answer_a: In a program that uses A, more than one instance (object) of type A can be created.
   :answer_b: If a program has an object of type A that it calls methods on, then the class A must have a subclass that is not abstract.
   :answer_c: The class A needs to have a constructor that takes two parameters in order to initialize v1 and v2.
   :answer_d: Any program that uses class A will have an error since abstract classes cannot contain public instance variables.
   :answer_e: One or more methods in A must be declared abstract.
   :correct: b
   :feedback_a: Instances of abstract classes cannot be created.
   :feedback_b: Abstract classes can not be instantiated, so if a program has an object of type A the class A must have a subclass that is not abstract.
   :feedback_c: The fields v1 and v2 could be initiliazed in a default constructor that takes in no parameters.
   :feedback_d: An abstract class can contain any number of public, private, and protected instance variables.
   :feedback_e: The purpose behind abstract classes is having a class that cannot be instantiated. An abstract class is not required to have any abstract methods.
   :pct_on_first: 0.2916666667
   :total_students_attempting: 24
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 2.2083333333

   What of the following is true about class ``A`` below?
   
   .. code-block:: java
   
      public abstract class A
      {
        public int v1;
        public int v2;
   
        //methods of the class
      }