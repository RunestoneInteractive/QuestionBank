.. activecode:: lcal1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 236
   :num_students_correct: 236.0
   :mean_clicks_to_correct: 1.0

   What does the following code print out? Trace through it keeping track of the array values and the output. Then run it to see if you're right. Notice that in this code, the array is passed as an argument to the methods. You can also try the code in the |Java visualizer| with the Code Lens button.
   ~~~~
   public class ArrayLoop
   {
   
     // What does this method do?
      public static void multAll(int[] values, int amt)
      {
        for (int i = 0; i < values.length; i++)
        {
          values[i] = values[i] * amt;
        }
      }
   
      // What does this method do?
      public static void printValues(int[] values)
      {
        for (int i = 0; i < values.length; i++)
        {
           System.out.println(  values[i] );
        }
      }
   
      public static void main(String[] args)
      {
        int[] numArray =  {2, 6, 7, 12, 5};
        multAll(numArray, 2);
        printValues(numArray);
      }
   }
   ====
   // Test for Lesson 6.2
   
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayLoop");
        }
   
        @Test
        public void test1() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "4 12 14 24 10";
   
            boolean passed = getResults(expect, output, "Did you run the code?",true);
            assertTrue(passed);
        }
    }