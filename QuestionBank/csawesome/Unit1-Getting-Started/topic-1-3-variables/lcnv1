.. activecode:: lcnv1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9964768056
   :total_students_attempting: 1703
   :num_students_correct: 1703.0
   :mean_clicks_to_correct: 1.0041103934

   Java is case sensitive so ``playerScore`` and ``playerscore`` are not the same.  Run the code below to see the difference.
   ~~~~
   public class CaseSensitiveClass
   {
      public static void main(String[] args)
      {
        int playerScore = 0; // variable name using camel case
        int playerscore = 1; // this is a different variable
        System.out.println("playerScore is " + playerScore);
        System.out.println("playerscore is " + playerscore);
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
            String expect = "playerScore is 0\nplayerscore is 1";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }