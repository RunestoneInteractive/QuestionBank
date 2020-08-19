.. activecode:: code1_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-5-shortcutoperators
   :topics: Unit1-Getting-Started/topic-1-5-shortcutoperators
   :from_source: T
   :language: java
   :autograde: unittest

   Run the code below to see what the ++ and shorcut operators do.
   Use the Codelens to trace through the code and observe how the
   variable values change. Try creating more compound assignment
   statements with shortcut operators and guess what they would
   print out before running the code.
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