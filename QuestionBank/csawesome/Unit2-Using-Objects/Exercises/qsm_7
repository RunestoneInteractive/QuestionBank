.. mchoice:: qsm_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: Woo Hoo Hoo Woo
   :answer_b: Hoo Woo Hoo
   :answer_c: Woo Hoo Woo Hoo
   :answer_d: Woo Woo Hoo Hoo
   :correct: c
   :feedback_a: 'Woo Hoo' is what gets passed to someOtherFunc()
   :feedback_b: 'Woo ' gets printed first.
   :feedback_c: We first print 'Woo ' then 'Hoo ' then the appended "Woo Hoo"
   :feedback_d: 'Woo ' gets printed first, then the 'Hoo ' from someOtherFunc().
   :pct_on_first: 0.4458672875
   :total_students_attempting: 1718
   :num_students_correct: 1696.0
   :mean_clicks_to_correct: 1.8472877358

   What is the output of the following code?
   
   .. code-block:: java
   
     public class Test
     {
        String someFunc(String str)
        {
            return someOtherFunc(str + " Hoo");
        }
   
        String someOtherFunc(String str)
        {
            return "Hoo " + str;
        }
   
        public static void main(String[] args)
        {
            Test x = new Test();
            System.out.print("Woo " + x.someFunc("Woo"));
        }
     }