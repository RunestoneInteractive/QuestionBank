.. mchoice:: traceReturnMethods
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-5-methods-return
   :topics: Unit2-Using-Objects/topic-2-5-methods-return
   :from_source: F
   :practice: T
   :answer_a: 5
   :answer_b: 7
   :answer_c: 4 3
   :answer_d: 2 3
   :answer_e: Does not compile.
   :correct: b
   :feedback_a: Make sure you call both methods and compute the square of 2 and then add the results.
   :feedback_b: Yes, square(2) returns 4 which is added to divide(6,2) which returns 3. The total of 4 + 3 is 7.
   :feedback_c: Make sure you add the results before printing it out.
   :feedback_d: Make sure you square(2) and add the results before printint it out.
   :feedback_e: Try the code in an active code window.

   What does the following code print out?

   .. code-block:: java

      public class MethodTrace
      {
        public int square(int x)
        {
            return x*x;
        }
        public int divide(int x, int y)
        {
              return x/y;
        }
        public static void main(String[] args) {
            MethodTrace traceObj = new MethodTrace();
            System.out.println( traceObj.square(2) + traceObj.divide(6,2) );
        }
       }