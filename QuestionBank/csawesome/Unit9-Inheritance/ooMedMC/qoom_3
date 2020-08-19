.. mchoice:: qoom_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooMedMC
   :topics: Unit9-Inheritance/ooMedMC
   :from_source: T
   :practice: T
   :answer_a: t1.method1(t1,t1);
   :answer_b: t2.method1(t2,t2);
   :answer_c: t3.method1(t1,t1);
   :answer_d: t2.method1(t3,t2);
   :answer_e: t3.method1(t3,t3);
   :correct: e
   :feedback_a: You can't pass an object of class <code>Test1</code> since it is not either an object of type <code>Test2</code> or an object of type <code>Test3</code>. You can pass the specified type or an object that is a subclass of the specified type but <code>Test1</code> is not a subclass of <code>Test2</code> or <code>Test3</code>.
   :feedback_b: You can't pass an object of class <code>Test2</code> as a parameter of type <code>Test3</code>. <code>Test2</code> is the parent class of <code>Test3</code> not a subclass. You can pass an object of the specified type or an object of any subclass.
   :feedback_c: You can't pass an object of class <code>Test1</code> since it is not either an object of type <code>Test2</code> or an object of type <code>Test3</code>. You can pass the specified type or an object that is a subclass of the specified type but <code>Test1</code> is not a subclass of <code>Test2</code> or <code>Test3</code>.
   :feedback_d: You can't pass <code>t2</code> as an object of type <code>Test3</code> since it is an object of class <code>Test2</code> and class <code>Test2</code> is not either class <code>Test3</code> or a subclass of class <code>Test3</code>. Class <code>Test2</code> is the parent of class <code>Test3</code>.
   :feedback_e: Since <code>method1</code> is a public method of class <code>Test1</code> objects of any subclasses of <code>Test1</code> can invoke the method. So, it can be invoked on <code>t3</code> since it is an object of <code>Test3</code> and this is a subclass of <code>Test1</code>.  And, since <code>method1</code> takes an object of class <code>Test2</code> and <code>Test3</code> as parameters. This actually means it can take an object of <code>Test2</code> or any subclass of <code>Test2</code> and an object of <code>Test3</code> or any subclass of <code>Test3</code>. So it can take <code>t3</code> which is an object of class <code>Test3</code> as an object of <code>Test2</code> since <code>Test3</code> is a subclass of <code>Test2</code>.
   :pct_on_first: 0.3212795549
   :total_students_attempting: 719
   :num_students_correct: 709.0
   :mean_clicks_to_correct: 2.6445698166

   Given the following class declarations and initializations in a client program, which of the following is a correct call to ``method1``?
   
   .. code-block:: java
   
      public class Test1
      {
         public void method1(Test2 v1, Test3 v2)
         {
            // rest of method not shown
         }
      }
   
      public class Test2 extends Test1
      {
      }
   
      public class Test3 extends Test2
      {
      }
   
      The following initializations appear in a different class.
      Test1 t1 = new Test1();
      Test2 t2 = new Test2();
      Test3 t3 = new Test3();