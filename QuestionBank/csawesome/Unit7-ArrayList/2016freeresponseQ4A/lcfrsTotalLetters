.. activecode:: lcfrsTotalLetters
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: 2016freeresponseQ4A
   :topics: Unit7-ArrayList/2016freeresponseQ4A
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Finish writing the ``totalLetters`` method below so that it returns the number of letters for all the strings in ``wordList``.  The ``main`` method below will test your code to check that you solved it correctly.
   ~~~~
   import java.util.*;
   public class StringFormatter
   {
       /** Returns the total number of letters in wordList.
        *  Precondition: wordList contains at least two words, consisting of letters only.
        */
       public static int totalLetters(List<String> wordList)
       {
       }
   
       public static void main(String[] args)
       {
            List<String> myWords = new ArrayList<String>();
            myWords.add("A");
            myWords.add("frog");
            myWords.add("is");
            System.out.println("Should print 7 and prints: " + totalLetters(myWords));
   
            List<String>words2 = new ArrayList<String>();
            words2.add("Hi");
            words2.add("Bye");
            System.out.println("Should print 5 and prints: " + totalLetters(words2));
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
      public RunestoneTests()
      {
        super("StringFormatter");
      }
   
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Should print 7 and prints: 7\n" +
                        "Should print 5 and prints: 5\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
    @Test
      public void test1()
      {
        List<String> myWords = new ArrayList<String>();
        myWords.add("A");
        myWords.add("dog");
        myWords.add("is");
   
        String output = String.valueOf(StringFormatter.totalLetters(myWords));
        String expect = "6";
   
        boolean passed = getResults(expect, output, "totalLetters method test on A, dog, is");
        assertTrue(passed);
      }
    }