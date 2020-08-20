.. mchoice:: qoo_14
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-6-polymorphism
   :topics: Unit9-Inheritance/topic-9-6-polymorphism
   :from_source: F
   :practice: T
   :answer_a: ABDC
   :answer_b: AB
   :answer_c: ABCD
   :answer_d: ABC
   :correct: a
   :feedback_a: Even though b is declared as type Base it is created as an object of the Derived class, so all methods to it will be resolved starting with the Derived class.
   :feedback_b: This would be true if the object was created of type Base using new Base. But the object is really a Derived object. So all methods are looked for starting with the Derived class.
   :feedback_c: After the call to methodOne in the super class printing "A", the code continues with the implicit this.methodTwo which resolves from the current object's class which is Derived. methodTwo in the Derived class is executed which then calls super.methodTwo which invokes printin "B" from methodTwo in the Base class. Then the "D" in the Derive methodTwo is printed. Finally the program returns to methodOne in the Derived class are prints "C".
   :feedback_d: The call to methodTwo in super.methodOne is to this.methodTwo which is the method from the Derived class. Consequently the "D" is also printed.
   :pct_on_first: 0.4504249292
   :total_students_attempting: 353
   :num_students_correct: 348.0
   :mean_clicks_to_correct: 2.1120689655

   Assume that the following declaration appears in a client program **Base b = new Derived();**.  What is the result of the call **b.methodOne()**?
   
   .. code-block:: java
   
      public class Base
      {
         public void methodOne()
         {
            System.out.print("A");
            methodTwo();
         }
   
         public void methodTwo()
         {
            System.out.print("B");
         }
   
         public static void main(String[] args)
         {
            Base b = new Derived();
            b.methodOne();
         }
      }
   
      class Derived extends Base
      {
         public void methodOne()
         {
            super.methodOne();
            System.out.print("C");
         }
   
         public void methodTwo()
         {
            super.methodTwo();
            System.out.print("D");
         }
      }