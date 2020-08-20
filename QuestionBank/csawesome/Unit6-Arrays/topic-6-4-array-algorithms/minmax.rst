.. activecode:: minmax
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-4-array-algorithms
   :topics: Unit6-Arrays/topic-6-4-array-algorithms
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.048
   :total_students_attempting: 125
   :num_students_correct: 85.0
   :mean_clicks_to_correct: 5.0235294118

   The code below finds the minimum (smallest element) in an array. Try it in the |Java visualizer| with the CodeLens button. Can you change it to find the maximum element instead? Can you also compute the average of the elements?
   ~~~~
   public class MinMax
   {
      public static void main(String[] args)
      {
        int[ ] values = {6, 2, 1, 7, 12, 5};
        int min = values[0]; // initialize min to the first element
        for (int val : values)
        {
          if (val < min) // found a new min!
              min = val;
        }
        System.out.println("Min is " + min );
      }
   }
   ====
   // Test for Lesson MinMax
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("MinMax");
   
            int[] numArray =  {2, 6, 7, 12, 5};
            setDefaultValues(new Object[]{numArray});
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Max is 12";
   
            boolean passed = output.contains(expect);
   
            passed = getResults(expect, output, "Max element", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "Average is 5.5";
   
            boolean passed = output.contains(expect);
   
            passed = getResults(expect, output, "Average", passed);
            assertTrue(passed);
        }
        @Test
        public void test3()
        {
          boolean passed = checkCodeContains("if statement using val >","if (val >");
          assertTrue(passed);
        }
    }