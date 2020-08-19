.. mchoice:: qsm_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: Hello Bob
   :answer_b: Hello Hello Bob
   :answer_c: Hello Bob Hello Bob
   :answer_d: Hello Bob Hello
   :correct: b
   :feedback_a: The constructor is called first and prints out one "Hello ".
   :feedback_b: The constructor is called first and prints out one "Hello " followed by the printSomething() method which prints out "Hello Bob ".
   :feedback_c: The constructor is called first and prints out one "Hello ".
   :feedback_d: The constructor is called first and prints out one "Hello " followed by printSomething().
   :pct_on_first: 0.4461269656
   :total_students_attempting: 1717
   :num_students_correct: 1696.0
   :mean_clicks_to_correct: 1.84375

   Assume that SomeClass and MainClass are properly defined in separate files. What is the output of the code in main()?
   
   .. code-block:: java
   
      class SomeClass
      {
          public SomeClass()
          {
              System.out.print("Hello ");
          }
   
          void printSomething(String name)
          {
              System.out.print("Hello " + name + " ");
          }
      }
   
      public class MainClass
      {
          public static void main(String[] args)
          {
              SomeClass someClass = new SomeClass();
              someClass.printSomething("Bob");
          }
      }