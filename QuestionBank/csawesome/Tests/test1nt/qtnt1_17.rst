.. mchoice:: qtnt1_17
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: C c1 = new C();
   :answer_b: B b1 = new B();
   :answer_c: B c2 = new C();
   :answer_d: B b3 = new B(10);
   :answer_e: C c3 = new C(24);
   :correct: e
   :feedback_a: Here we are simply creating a new instance of class C by calling the appropiate constructor. Nothing is wrong here.
   :feedback_b: Here we are simply creating a new instance of class B by calling the appropiate constructor. Nothing is wrong here.
   :feedback_c: Since class C is a subclass of class B, you can upcast an object of type C to be of type B.
   :feedback_d: This statement is creating a new object using the second constructor of the B class. This is also a valid way to create a B object.
   :feedback_e: Even though class C has a super class with a constructor that takes in a single int argument, class C does not have a constructor that takes an int value.
   :pct_on_first: 0.4158415842
   :total_students_attempting: 303
   :num_students_correct: 301.0
   :mean_clicks_to_correct: 2.196013289

   Consider the following class declarations. Which of the following statements will not compile?
   
   .. code-block:: java
   
      public class B
      {
   
         public int myValue;
   
         public B()
         {
            myValue = 0;
         }
   
         public B(int x)
         {
            myValue = x;
         }
      }
   
      public class C extends B
      {
   
         public C()
         {
            super(0);
         }
      }