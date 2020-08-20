.. mchoice:: JP_AP2-3-3
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: practice-test-objects
   :topics: Unit2-Using-Objects/practice-test-objects
   :from_source: F
   :random: 
   :answer_a: core.shutdown(250);
   :answer_b: core.shutdown();
   :answer_c: core.increaseTemp();
   :answer_d: coreshutdown();
   :answer_e: core.shutdown;
   :correct: b
   :feedback_a: Method shutdown() does not take any parameters.
   :feedback_b: Correct
   :feedback_c: There is no method increaseTemp() in the ReactorCore class definition.
   :feedback_d: The dot operator is required between the object name and the method name.
   :feedback_e: Parentheses are required after a method name.
   :pct_on_first: 0.4285714286
   :total_students_attempting: 35
   :num_students_correct: 34.0
   :mean_clicks_to_correct: 2.3529411765

    Consider the following class. Assume that the ReactorCore object core has been properly declared and initialized in a method in a class other than ReactorCore.  Which of the following statements are valid?
   
    .. code-block:: java
   
        public class ReactorCore
        {
          private double criticalTemp;
          private double shutdownTemp;
          private double currentTemp;
   
          public ReactorCore(double b)
          {
            criticalTemp = b;
          }
   
          void lowerTemp()
          {
            currentTemp -= 10;
          }
   
          void raiseTemp()
          {
            currentTemp += 10;
          }
   
          void shutdown()
          {
            currentTemp = shutdownTemp;
          }
        }