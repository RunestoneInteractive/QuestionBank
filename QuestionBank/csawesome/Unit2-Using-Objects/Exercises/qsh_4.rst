.. mchoice:: qsh_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: unknown value
   :answer_b: 0
   :answer_c: compile error
   :answer_d: runtime error
   :correct: c
   :feedback_a: x needs to be initialized with a call to the SomeClass constructor.
   :feedback_b: x and someVar have not been initialized.
   :feedback_c: This will give an error that x has not been initialized. It needs to be initialized with a call to the SomeClass constructor.
   :feedback_d: This code will not run.
   :pct_on_first: 0.4035820896
   :total_students_attempting: 1675
   :num_students_correct: 1658.0
   :mean_clicks_to_correct: 1.8697225573

   Assume that SomeClass and MainClass are properly defined in separate files. What is the output of main()?
   
   .. code-block:: java
   
    class SomeClass
    {
        int someVar;
    }
   
    public class MainClass
    {
        public static void main(String[] args)
        {
            SomeClass x;
            System.out.println(x.someVar);
        }
    }