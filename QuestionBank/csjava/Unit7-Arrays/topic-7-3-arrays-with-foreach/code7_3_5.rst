.. activecode:: code7_3_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-3-arrays-with-foreach
   :topics: Unit7-Arrays/topic-7-3-arrays-with-foreach
   :from_source: T
   :language: java
   :autograde: unittest

   Write a spellcheck() method using an enhanced for-each loop that takes a word as a parameter and returns true if it is in the dictionary array. Return false if it is not found.
   ~~~~
   public class SpellChecker
   {
      // Re-write the spellcheck(word, dictionary) (and optionally the printStartsWith(firstLetters, dictionary)) methods to use enhanced for-each loops.



      public static void main(String[] args)
      {
        String[] dictionary = {"the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","cat","dog","cats","dogs"};

        /* Uncomment to test your method
        String word = "catz";
        if (checker.spellcheck(word, dictionary) == true)
            System.out.println(word + " is spelled correctly!");
        else
            System.out.println(word + " is misspelled!");
        */

       // Optional (not autograded)
       // checker.printStartsWith("a", dictionary);
      }
   }
   ====
   // Test for Lesson 6.2.5 - challenge-6-2-spell-checker

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("SpellChecker");
        }

        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "catz is misspelled!";

            boolean passed = output.contains(expect);

            passed = getResults(expect, output, "Did you uncomment the main method?", passed);
            assertTrue(passed);
        }



        @Test
        public void test3()
        {
            Object[] args = {"dogz"};
            String output = getMethodOutput("spellcheck", args);
            String expect = "false";

            boolean passed = getResults(expect, output, "spellcheck(\"dogz\")");
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            Object[] args = {"dog"};
            String output = getMethodOutput("spellcheck", args);
            String expect = "true";

            boolean passed = getResults(expect, output, "spellcheck(\"dog\")");
            assertTrue(passed);
        }

        @Test
        public void testFor() throws IOException
        {
            String target = "for (int * = #; * ? #; *~)";
            boolean passed = checkCodeNotContains("for loop", target);
            assertTrue(passed);
        }

        @Test
        public void testForEach()
        {
            boolean passed = checkCodeContains("for each loop", "for(String * : dictionary)");
            assertTrue(passed);
        }
    }