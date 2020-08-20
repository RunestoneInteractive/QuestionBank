.. activecode:: code7_2_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-2-traversing-arrays
   :topics: Unit7-Arrays/topic-7-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest

   public class SpellChecker
   {

      /* 1. Write a print10() method that takes an array as a parameter and prints out the first
       * 10 words of the array.
       */

      /* 2. Write a spellcheck() method that takes a word and an array as
       * parameters  and returns true if the word is in the array.
       * Return false if it is not found.
       */

      public static void main(String[] args)
      {
        String[] dictionary = {"the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","cat","dog","cats","dogs"};

        /* Uncomment to test Part 1
        print10(dictionary);
            */

            /* Uncomment to test Part 2
        String word = "catz";
        if (spellcheck(word, dictionary) == true)
            {
            System.out.println(word + " is spelled correctly!");
        }
        else
            {
            System.out.println(word + " is misspelled!");
            }
        */

        // 3. optional and not autograded
        // printStartsWith("a", dictionary);
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
            String expect = "the of and a to in is you that it".replaceAll(" ", "\n") + "\ncatz is misspelled!";

            boolean passed = output.contains(expect);

            passed = getResults(expect, output, "Did you uncomment the main method?", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("print10");
            String expect = "the of and a to in is you that it".replaceAll(" ", "\n");

            boolean passed = getResults(expect, output, "print10()");
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
    }