.. mchoice:: traceMethods
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-4-methods-with-params
   :topics: Unit2-Using-Objects/topic-2-4-methods-with-params
   :from_source: F
   :practice: T
   :answer_a: 25 and 2
   :answer_b: 25 and .5
   :answer_c: 2 25
   :answer_d: 25 2
   :answer_e: Nothing, it does not compile.
   :correct: a
   :feedback_a: Correct.
   :feedback_b: The order of the arguments to the divide(x,y) method will divide x by y and return an int result.
   :feedback_c: The square(x) method is called before the divide(x,y) method.
   :feedback_d: The main method prints out " and " in between the method calls.
   :feedback_e: Try the code in the visualizer link below.

   What does the following code print out?

   .. code-block:: java

      public class MethodTrace
      {
        public void square(int x)
        {
            System.out.print(x*x);
        }
        public void divide(int x, int y)
        {
            System.out.println(x/y);
        }
        public static void main(String[] args) {
            MethodTrace traceObj = new MethodTrace();
            traceObj.square(5);
            System.out.print(" and ");
            traceObj.divide(4,2);
        }
       }