.. activecode:: lcfrssa5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: FRQstringScrambleA
   :topics: Unit4-Iteration/FRQstringScrambleA
   :from_source: T
   :language: java
   :autograde: unittest

   Write the method scrambleWord.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;

   public class ScrambledStrings
   {
      /********************** Part (a) *********************/

      /** Scrambles a given word.
       *  @param word the word to be scrambled
       *  @return the scrambled word (possibly equal to word)
       *  Precondition: word is either an empty string or contains
       *    only uppercase letters.
       *  Postcondition: the string returned was created from word
       *      as follows:
       *   - the word was scrambled, beginning at the first letter
       *      and continuing from left to right
       *   - two consecutive letters consisting of "A" followed by
       *        a letter that was not "A" were swapped
       *   - letters were swapped at most once
       */
      public static String scrambleWord(String word)
      {
         /* to be implemented in part a */
      }

      /********************** Test *********************/
      public static void main(String[] args)
      {
         System.out.println("\nTesting Part (a):\n");

         String[] words = {"TAN", "ABRACADABRA", "WHOA",
                           "AARDVARK", "EGGS", "A", ""};
         for (String word : words)
            System.out.println(word + " becomes " + scrambleWord(word));
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Testing Part (a):\nTAN becomes TNA\nABRACADABRA becomes BARCADABARA\nWHOA becomes WHOA\nAARDVARK becomes ARADVRAK\nEGGS becomes EGGS\nA becomes A\n becomes \n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }

        @Test
        public void testIfLoop()
        {
           String code = getCode();
           boolean passed = code.contains("if") && (code.contains("for") || code.contains("while"));
           getResults("Expected loop and if",""+passed, "Checking for loop and if statement",passed);
            assertTrue(passed);
        }

            @Test
        public void testCodeContains()
        {
            String target = ".substring(";
            boolean passed = checkCodeContains("substring method", target);
            assertTrue(passed);
        }
    }