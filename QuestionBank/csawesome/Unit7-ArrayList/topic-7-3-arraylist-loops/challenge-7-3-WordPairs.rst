.. activecode:: challenge-7-3-WordPairs
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0952380952
   :total_students_attempting: 21
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 5.0

   FRQ WordPairs Challenge: Complete the constructor for WordPairsList below which will add pairs of words from a given array to the ArrayList. Then, complete the method numMatches().
   ~~~~
   import java.util.*;
   
    public class WordPairsList
    {
        private ArrayList<WordPair> allPairs;
   
        public WordPairsList(String[] words)
        {
           // WRITE YOUR CODE HERE
           // initialize allPairs to an empty ArrayList of WordPair objects
   
           // nested loops through the words array to add each pair to allPairs
   
   
        }
   
        public int numMatches()
        {
          //Write the code for the second part described below
          return 0;
        }
   
        public String toString() {
            return allPairs.toString();
        }
   
   
        public static void main(String[] args)
        {
            String[] words = {"Hi", "there", "Tyler", "Sam"};
            WordPairsList list = new WordPairsList(words);
            System.out.println(list);
            // For second part below, uncomment this test:
            //System.out.println("The number of matched pairs is: " + list.numMatches());
        }
    }
   
    class WordPair {
        private String word1;
        private String word2;
   
        public WordPair(String w1, String w2) {
            word1 = w1;
            word2 = w2;
        }
        public String getFirst() {
            return word1;
        }
        public String getSecond() {
            return word2;
        }
        public String toString() {
            return "(" + word1 + ", " + word2 + ")";
        }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("WordPairsList");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[(Hi, there), (Hi, Tyler), (Hi, Sam), (there, Tyler), (there, Sam), (Tyler, Sam)]";
   
            boolean passed = output.contains(expect);
   
            String[] lines = output.split("\n");
            if (lines.length > 1)
                output = lines[0];
   
            getResults(expect, output, "Part 1 - Add all word pairs from main()", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "The number of matched pairs is: 0";
   
            boolean passed = output.contains(expect);
            String[] lines = output.split("\n");
            if (lines.length > 1)
                output = lines[1];
   
            getResults(expect, output, "Part 2 - numMatches from main()", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test3() {
            String[] words = {"Hi", "Hi", "Test", "Test"};
            WordPairsList list = new WordPairsList(words);
            String output = list.toString();
            String expect = "[(Hi, Hi), (Hi, Test), (Hi, Test), (Hi, Test), (Hi, Test), (Test, Test)]";
   
            boolean passed = getResults(expect, output, "Part 1 - Add all word pairs with {\"Hi\", \"Hi\", \"Test\", \"Test\"}");
            assertTrue(passed);
   
        }
   
        @Test
        public void test4() {
            String[] words = {"Hi", "Hi", "Test", "Test"};
            WordPairsList list = new WordPairsList(words);
            String output = "The number of matched pairs is: " + list.numMatches();
            String expect = "The number of matched pairs is: 2";
   
            boolean passed = getResults(expect, output, "Part 2 - numMatches() with {\"Hi\", \"Hi\", \"Test\", \"Test\"}");
            assertTrue(passed);
        }
    }