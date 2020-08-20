.. activecode:: frqScrambleOrRemove
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: stringScrambleB
   :topics: Unit7-ArrayList/stringScrambleB
   :from_source: T
   :language: java
   :autograde: unittest

   Write the method ``scrambleOrRemove`` below. The main has code to test the result.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;

   public class ScrambledStrings
   {

      /** Scrambles a given word.
        *  @param word the word to be scrambled
        *  @return the scrambled word (possibly equal to word)
        *  Precondition: word is either an empty string or contains only uppercase letters.
        *  Postcondition: the string returned was created from word as follows:
        *   - the word was scrambled, beginning at the first letter and continuing from left to right
        *   - two consecutive letters consisting of "A" followed by a letter that was not "A" were swapped
        *   - letters were swapped at most once
        */
      public static String scrambleWord(String word)
      {
         String scrambled = "";
         int i = 0;

         while (i < word.length())
         {
            String letter1 = word.substring(i, i+1);
            String letter2 = "";
            if (i < word.length() - 1)
            letter2 = word.substring(i+1, i+2);

            if (letter1.equals("A") && !letter2.equals("A") && !letter2.equals(""))
            {
               scrambled += letter2 + letter1;
               i += 2;
            }
            else
            {
               scrambled += letter1;
               i += 1;
            }
        }
        return scrambled;
      }

      /********************** Part (b) *********************/

      /** Modifies wordList by replacing each word with its scrambled
        *  version, removing any words that are unchanged as a result of scrambling.
        *  @param wordList the list of words
        *  Precondition: wordList contains only non-null objects
        *  Postcondition:
        *   - all words unchanged by scrambling have been removed from wordList
        *   - each of the remaining words has been replaced by its scrambled version
        *   - the relative ordering of the entries in wordList is the same as it was
        *        before the method was called
        */

      public static void scrambleOrRemove(List<String> wordList)
      {

      }

      /********************** Test *********************/

      public static void main(String[] args)
      {

         System.out.println("\nTesting Part (b):\n");

         String[] words2 = {"TAN", "ABRACADABRA", "WHOA", "APPLE", "EGGS"};
         ArrayList<String> wordList = new ArrayList<String>();
         for (String word : words2)
            wordList.add(word);
         System.out.print(wordList);
         scrambleOrRemove(wordList);
         System.out.println(" ==> " + wordList);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.List;
    import java.util.ArrayList;
    import java.util.Arrays;

    public class RunestoneTests extends CodeTestHelper
    {
      public RunestoneTests()
      {
        super("ScrambledStrings");
      }

      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "[TNA, BARCADABARA, PAPLE]";
        boolean passed = output.contains(expect);
        assertTrue(passed);
        System.out.println("expected output from main");
      }

      @Test
      public void test1()
      {
        ArrayList<String> wordList = new ArrayList(Arrays.asList("TAN", "ABRACADABRA", "WHOA", "APPLE", "EGGS"));

        ArrayList<String> wordListExpect = new ArrayList(Arrays.asList("TNA", "BARCADABARA", "PAPLE"));

        ScrambledStrings.scrambleOrRemove(wordList);

        boolean result = wordList.equals(wordListExpect);

        boolean passed = getResults("true", ""+result, "scrambleOrRemove works for ArrayList #1: TAN, ABRACADABRA, WHOA, APPLE, EGGS");

        assertTrue(passed);
      }

       @Test
        public void test2()
        {
          ArrayList<String> wordList = new ArrayList(Arrays.asList("TESTING", "ONE", "TWO", "THREE"));

          ArrayList<String> wordListExpect = new ArrayList(Arrays.asList());

          ScrambledStrings.scrambleOrRemove(wordList);

          boolean result = wordList.equals(wordListExpect);

          boolean passed = getResults("true", ""+result, "scrambleOrRemove works for ArrayList #2: TESTING, ONE, TWO, THREE");

          assertTrue(passed);
        }
    }