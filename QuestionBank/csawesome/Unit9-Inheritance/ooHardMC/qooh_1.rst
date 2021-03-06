.. mchoice:: qooh_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooHardMC
   :topics: Unit9-Inheritance/ooHardMC
   :from_source: T
   :practice: T
   :answer_a: ABDC
   :answer_b: AB
   :answer_c: ABCD
   :answer_d: ABC
   :correct: a
   :feedback_a: Even though b is declared as type <code>Base</code> it is created as an object of the <code>Derived</code> class, so all methods to it will be resolved starting with the <code>Derived</code> class. So the <code>methodOne()</code> in <code>Derived</code> will be called. This method first calls <code>super.methodOne</code> so this will invoke the method in the superclass (which is <code>Base</code>). So next the <code>methodOne</code> in <code>Base</code> will execute. This prints the letter "A" and invokes <code>this.methodTwo()</code>. Since <code>b</code> is really a <code>Derived</code> object, we check there first to see if it has a <code>methodTwo</code>. It does, so execution continues in the <code>Derived</code> class <code>methodTwo</code>. This method invokes <code>super.methodTwo</code>. So this will invoke the method in the super class (<code>Base</code>) named <code>methodTwo</code>. This method prints the letter "B" and then returns. Next the execution returns from the call to the <code>super.methodTwo</code> and prints the letter "D". We return to the <code>Base</code> class <code>methodOne</code> and return from that to the <code>Derived</code> class <code>methodOne</code> and print the letter "C".
   :feedback_b: This would be true if the object was created of type <code>Base</code>. But the object is really a <code>Derived</code>  object. So all methods are looked for starting with the <code>Derived</code>  class.
   :feedback_c: After the call to <code>methodOne</code> in the super class printing "A", the code continues with the implicit <code>this.methodTwo</code> which resolves from the current object's class which is <code>Derived</code>. Next, <code>methodTwo</code> in the <code>Derived</code> class is executed which then calls <code>super.methodTwo</code> which invokes <code>println</code> "B" from <code>methodTwo</code> in the <code>Base</code> class. Then the "D" in the <code>Derived</code> <code>methodTwo</code> is printed. Finally the program returns to <code>methodOne</code> in the <code>Derived</code> class are prints "C".
   :feedback_d: The call to <code>methodTwo</code> in <code>super.methodOne</code> is to <code>this.methodTwo</code> which is the method from the <code>Derived</code> class. Consequently the "D" is also printed.
   :pct_on_first: 0.5048701299
   :total_students_attempting: 616
   :num_students_correct: 606.0
   :mean_clicks_to_correct: 2.001650165

   Assume that ``Base b = new Derived();`` appears in a client program.  What is the result of the call ``b.methodOne();``?
   
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
      }
   
      public class Derived extends Base
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