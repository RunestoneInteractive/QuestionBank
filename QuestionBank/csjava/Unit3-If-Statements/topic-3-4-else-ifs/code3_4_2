.. activecode:: code3_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-4-else-ifs
   :topics: Unit3-If-Statements/topic-3-4-else-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   The else-if connection is necessary if you want to hook up conditionals together. In the following code, there are 4 separate if statements instead of the if-else-if pattern. Will this code print out the correct grade? First, trace through the code to see why it prints out the incorrect grade. Use the Code Lens button. Then, fix the code by adding in 3 else's to connect the if statements and see if it works.
   ~~~~
   public class IfDebug
   {
      public static void main(String[] args)
      {
        int score = 93;
        String grade = "";

        if (score >= 90)
        {
            grade = "A";
        }
        if (score >= 80)
        {
            grade = "B";
        }
        if (score >= 70)
        {
           grade = "C";
        }
        if (score >= 60)
        {
            grade = "D";
        }
        else
        {
          grade = "F";
        }

        System.out.println(grade);
      }
   }
   ====
   // Test Code for Lesson 3.4 - lccbIfDebug
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMainCorrectOutput() throws IOException
        {
            String output = getMethodOutput("main");
            String expected = "A\n";
            boolean passed = getResults(expected, output, "Expected output from main");
            assertTrue(passed);
        }

        @Test
        public void testCodeContainsFourElses()
        {
            String code = getCode();
            String[] tokens = code.split("\\s+");

            int expectedElseCount = 4;
            int actualElseCount  = 0;
            for (int i = 0; i < tokens.length; i++) {
                if (tokens[i].equals("else")) {
                    actualElseCount++;
                }
            }
            boolean passed = getResults(expectedElseCount, actualElseCount, "Expected number of else's");
            assertTrue(passed);
        }
    }