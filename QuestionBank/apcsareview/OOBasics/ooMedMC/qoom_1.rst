.. mchoice:: qoom_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooMedMC
   :topics: OOBasics/ooMedMC
   :from_source: T
   :answer_a: Won't compile since <code>GradStudent</code> doesn't have a <code>getInfo</code> method
   :answer_b: Taco
   :answer_c: Pizza
   :answer_d: Won't compile since you are creating a <code>GradStudent</code>, not a <code>Student</code>
   :answer_e: Won't compile since you use <code>this.getFood()</code>
   :correct: b
   :feedback_a: <code>GradStudent</code> will inherit the <code>getInfo</code> method from <code>Student</code>. This would be true if <code>getInfo</code> was a private method.
   :feedback_b: Objects know what class they are created as and all methods are resolved starting with that class at run time. If the method isn't found in that class the parent class is checked (and so on until it is found). So it will first look for <code>getInfo</code> in <code>GradStudent</code> and when it doesn't find it it will look in <code>Student</code>. In <code>getInfo</code> it calls <code>this.getFood</code>. Again, it will first look for this method in <code>GradStudent</code>. It will find the <code>getFood</code> method there and return "Taco".
   :feedback_c: This would be true if it was <code>Student s1 = new Student();</code>
   :feedback_d: An object of a subclass can be substituted for a parent class object. A <code>GradStudent</code> is a <code>Student</code>.
   :feedback_e: In object methods if you leave off the <code>this.</code> when invoking an object method it will be added for you by the compiler. The keyword <code>this</code> refers to the current object which is implicitly passed to all object methods.

   Given the following class declarations, what is the output from ``Student s1 = new GradStudent();`` followed by ``s1.getInfo();``?

   .. code-block:: java

      public class Student {
         public String getFood() {
            return "Pizza";
         }
         public String getInfo()  {
            return this.getFood();
         }
      }

      public class GradStudent extends Student {
         public String getFood() {
            return "Taco";
         }
      }