.. activecode:: challenge2-6-MadLibs
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T

   If you used repl.it for this challenge, copy the url of your repl here to turn in.
   ~~~~
   public class MadLibs1
   {
      public static void main(String[] args)
      {
        // fill these in with silly words/strings (don't read the poem yet)
        String pluralnoun1 =
        String color1 =
        String color2 =
        String food =
        String pluralnoun2 =


        // Run to see the silly poem!
        System.out.println("Roses are " + color1);
        System.out.println(pluralnoun1 + " are " + color2);
        System.out.println("I like " + food);
        System.out.println("Do " + pluralnoun2 + " like them too?");

        // Now come up with your own silly poem!

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
            String expect = "Roses are *\n* are *\nI like *\nDo * like them too?";

            boolean passed = getResultsRegEx(expect, output, "Expected output from main");
            assertTrue(passed);
        }

        @Test
        public void testNull() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "null";

            String actual = countOccurences(output, expect) + " null values";

            boolean passed = getResults("0 null values", actual, "No null values");
            assertTrue(passed);
        }
    }