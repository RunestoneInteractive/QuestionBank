.. mchoice:: qoo_11
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-6-polymorphism
   :topics: Unit9-Inheritance/topic-9-6-polymorphism
   :from_source: T
   :practice: T
   :answer_a: Pizza
   :answer_b: Taco
   :answer_c: You will get a compile time error
   :answer_d: You will get a run-time error
   :correct: b
   :feedback_a: This would be true if s1 was actually a Student, but it is a GradStudent.  Remember that the run-time will look for the method first in the class that created the object.
   :feedback_b: Even though the getInfo method is in Student when getFood is called the run-time will look for that method first in the class that created this object which in this case is the GradStudent class.
   :feedback_c: This code will compile.  The student class does have a getInfo method.
   :feedback_d: There is no problem at run-time.
   :pct_on_first: 0.5651162791
   :total_students_attempting: 1290
   :num_students_correct: 1279.0
   :mean_clicks_to_correct: 1.7193119625

   What is the output from running the main method in the Student class?
   
   .. code-block:: java
   
      public class Student {
   
         public String getFood() {
            return "Pizza";
         }
   
         public String getInfo()  {
           return this.getFood();
         }
   
         public static void main(String[] args)
         {
           Student s1 = new GradStudent();
           s1.getInfo();
         }
      }
   
      class GradStudent extends Student {
   
        public String getFood() {
           return "Taco";
        }
   
      }