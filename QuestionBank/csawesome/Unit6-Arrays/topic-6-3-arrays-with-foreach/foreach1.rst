.. activecode:: foreach1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit6-Arrays/topic-6-3-arrays-with-foreach
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.156097561
   :total_students_attempting: 205
   :num_students_correct: 173.0
   :mean_clicks_to_correct: 1.8728323699

   Try the following code. Notice the for each loop with an int array and a String array. Add another high score and another name to the arrays and run again.
   ~~~~
   public class ForEachDemo
   {
      public static void main(String[] args)
      {
        int[] highScores = { 10, 9, 8, 8};
        String[] names = {"Jamal", "Emily", "Destiny", "Mateo"};
        // for each loop with an int array
        for (int value : highScores)
        {
            System.out.println( value );
        }
        // for each loop with a String array
        for (String value : names)
        {
            System.out.println(value); // this time it's a name!
        }
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ForEachDemo");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect1 = "10\n9\n8\n8";
            String expect2 = "Jamal\nEmily\nDestiny\nMateo";
   
            boolean passed = output.contains(expect1) && output.contains(expect2);
   
            passed = getResults(expect1 + " " + expect2, output, "Original main()", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "10 9 8 8 Jamal Emily Destiny Mateo".replaceAll(" ", "\n");
   
            boolean passed = !output.equals(expect) && output.length() > expect.length();
   
            passed = getResults(expect, output, "Added another high score and name", passed);
            assertTrue(passed);
        }
    }