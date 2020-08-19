.. activecode:: lcaf2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit6-Arrays/topic-6-3-arrays-with-foreach
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 182
   :num_students_correct: 182.0
   :mean_clicks_to_correct: 1.0

   Try the code below.
   ~~~~
   public class ArrayWorker
   {
       private int[ ] values;
   
       public ArrayWorker(int[] theValues)
       {
          values = theValues;
       }
   
       public double getAverage()
       {
          double total = 0;
          for (int val : values)
          {
             total  = total + val;
          }
          return total / values.length;
       }
   
       public static void main(String[] args)
       {
           int[] numArray =  {2, 6, 7, 12, 5};
           ArrayWorker aWorker = new ArrayWorker(numArray);
           System.out.println(aWorker.getAverage());
       }
   }
   ====
   // Test for Lesson 6.3.3 - IncrementLoop
   
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayWorker");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "6.4";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }