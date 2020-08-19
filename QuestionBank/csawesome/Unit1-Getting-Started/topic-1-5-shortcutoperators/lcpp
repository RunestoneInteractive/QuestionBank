.. activecode:: lcpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-5-shortcutoperators
   :topics: Unit1-Getting-Started/topic-1-5-shortcutoperators
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.997698504
   :total_students_attempting: 869
   :num_students_correct: 869.0
   :mean_clicks_to_correct: 1.002301496

   Run the code below to see what the ++ and shorcut operators do. Click on the Show Code Lens button to trace through the code and the variable values change in the visualizer. Try creating more compound assignment statements with shortcut operators and work with a partner to guess what they would print out before running the code.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        int score = 0;
        System.out.println(score);
        score++;
        System.out.println(score);
        score *= 2;
        System.out.println(score);
        int penalty = 5;
        score -= penalty/2;
        System.out.println(score);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "0\n1\n2\n0";
   
            boolean passed = getResults(expect, output, "Expected output from main",true);
            assertTrue(passed);
        }
    }