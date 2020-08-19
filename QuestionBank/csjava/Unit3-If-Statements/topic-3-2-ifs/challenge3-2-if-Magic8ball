.. activecode:: challenge3-2-if-Magic8ball
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: F
   :language: java
   :autograde: unittest

   public class Magic8Ball
   {
      public static void main(String[] args)
      {
        // Get a random number from 1 to 8

        // Use if statements to test the random number
        // and print out 1 of 8 random responses


      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.ArrayList;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Magic8Ball");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");

            boolean passed = output.length() > 0;

            passed = getResults("Output length > 0", "Output length of " + output.length(), "Prints a statement", passed);
            assertTrue(passed);
        }


        @Test
        public void test2()
        {
            String[] output = new String[200];

            for (int i = 0; i < output.length; i++) {
                output[i] = getMethodOutput("main");
            }

            ArrayList <String> lines = new ArrayList <String> ();

            for (int i = 0; i < output.length; i++) {
                if (!lines.contains(output[i]))
                    lines.add(output[i]);
            }

            int responses = lines.size();
            boolean passed = lines.size() >= 8;

            passed = getResults("8", ""+responses, "Unique responses", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCodeWithoutComments();

            int numIfs = countOccurences(code, "if");

            boolean passed = numIfs >= 7;

            passed = getResults("7 or more", ""+numIfs, "Code has at least 7 if statements", passed);
            assertTrue(passed);
        }
    }