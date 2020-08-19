.. mchoice:: qtnt1_11
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: II and III only
   :answer_d: III only
   :answer_e: I, II and III
   :correct: c
   :feedback_a: This method call compiles because class C inherits all the public methods in class B. This will not produce an error.
   :feedback_b: Method II will produce a compile time error because class B (the superclass) does not inherit the methods of class C due to the fact that class C is its subclass. But, it is not the only call that will result in a compile time error.
   :feedback_c: Method II will produce a compile time error because class B (the superclass) does not inherit the methods of class C due to the fact that class C is its subclass. Method III will produce an error because of the parameter it takes in. objectB is not a class C type object which is what the method definition for method III required.
   :feedback_d: This method produces a compile time error, but method II will also produce a compile time error.
   :feedback_e: Methods II and III will both produce compile time errors, but method I works because class C inherits all the public methods of class B.
   :pct_on_first: 0.3949044586
   :total_students_attempting: 314
   :num_students_correct: 313.0
   :mean_clicks_to_correct: 1.9520766773

   Consider the following class definitions. Which of I, II and III below would cause an error when used in place of the missing code in the main method?
   
   .. code-block:: java
   
      public class A
      {
        public void method1() { };
      }
   
      public class B extends A
      {
          // Instance variables and other methods not shown
   
          public void method1()
          {
            /* implementation not shown */
          }
      }
   
      public class C extends B
      {
        //Instance variables and other methods not shown
   
        public void method2(C o)
        {
           /* implementation not shown */
        }
   
        public static void main(String[] args)
        {
          C objectC = new C();
          B objectB = new B();
          // Missing code
        }
      }
   
      I objectC.method1();
      II objectB.method2(objectC);
      III objectC.method2(objectB);