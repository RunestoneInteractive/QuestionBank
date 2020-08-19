.. activecode:: lcfrsbasicGapWidth
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: 2016freeresponseQ4B
   :topics: Unit7-ArrayList/2016freeresponseQ4B
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.5

   Finish writing the ``basicGapWidth`` method below so that it returns the size that the gap should be.  The ``main`` method below will test your code to check that you solved it correctly.
   ~~~~
   import java.util.*;
   public class StringFormatter
   {
       /** Returns the basic gap width when wordList is used to produce
       *  a formatted string of formattedLen characters.
       *  Precondition: wordList contains at least two words, consisting of letters only.
       *            formattedLen is large enough for all the words and gaps.
       */
       public static int basicGapWidth(List<String> wordList,
                                       int formattedLen)
       {
       }
   
       public static int totalLetters(List<String> wordList)
       {
           int numLetters = 0;
           for (String s : wordList)
           {
               numLetters = numLetters + s.length();
           }
           return numLetters;
       }
   
       public static void main(String[] args)
       {
           List<String> wordList = new ArrayList<String>();
           wordList.add("AP");
           wordList.add("COMP");
           wordList.add("SCI");
           wordList.add("ROCKS");
           System.out.println("Should print 2 and prints: " + basicGapWidth(wordList,20));
   
           List<String>words2 = new ArrayList<String>();
           words2.add("GREEN");
           words2.add("EGGS");
           words2.add("AND");
           words2.add("HAM");
           System.out.println("Should print 1 and prints: " + basicGapWidth(words2,20));
   
           List<String>words3 = new ArrayList<String>();
           words3.add("BEACH");
           words3.add("BALL");
           System.out.println("Should print 11 and prints: " + basicGapWidth(words3,20));
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
        String expect = "Should print 2 and prints: 2\n" +
                        "Should print 1 and prints: 1\n" +
                        "Should print 11 and prints: 11\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        List<String> wordList = new ArrayList<String>();
        wordList.add("AP");
        wordList.add("COMP");
        wordList.add("SCI");
        wordList.add("ROCKS");
   
        String output = String.valueOf(StringFormatter.basicGapWidth(wordList,20));
        String expect = "2";
   
        boolean passed = getResults(expect, output, "basicGapWidth method test 01");
        assertTrue(passed);
      }
   
       @Test
      public void test2()
      {
        List<String>words2 = new ArrayList<String>();
            words2.add("GREEN");
            words2.add("EGGS");
            words2.add("AND");
            words2.add("HAM");
   
        String output = String.valueOf(StringFormatter.basicGapWidth(words2,20));
        String expect = "1";
   
        boolean passed = getResults(expect, output, "basicGapWidth method test 02");
        assertTrue(passed);
      }
   
       @Test
      public void test3()
      {
        List<String>words3 = new ArrayList<String>();
        words3.add("SOCCER");
        words3.add("BALL");
   
        String output = String.valueOf(StringFormatter.basicGapWidth(words3,20));
        String expect = "10";
   
        boolean passed = getResults(expect, output, "basicGapWidth method test on SOCCER, BALL");
        assertTrue(passed);
      }
    }