.. activecode:: ArrayListWordPair1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 11
   :num_students_correct: 11.0
   :mean_clicks_to_correct: 1.0

   Create an Arraylist of WordPair objects.
   ~~~~
   import java.util.*;
   
   public class WordPairTest {
        public static void main(String[] args)
        {
            // Create an ArrayList of WordPair objects called pairs
   
   
            pairs.add(new WordPair("hi","there"));
            pairs.add(new WordPair("hi","bye"));
            System.out.println(pairs);
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
            super("WordPairTest");
        }
   
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "[(hi, there), (hi, bye)]";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void hasArrayList()
        {
          boolean passed = checkCodeContains("ArrayList declaration", "ArrayList<WordPair>");
          assertTrue(passed);
        }
    }