.. activecode:: array-set
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-1-array-basics
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3846153846
   :total_students_attempting: 234
   :num_students_correct: 215.0
   :mean_clicks_to_correct: 1.8558139535

   Try out the following code which has two parallel arrays, highScores and names. Can you print out Mateo's score? Can you change Sofia's score to 97 using an assignment statement in the code? Can you change the arrays so that they have 6 elements and add your name and score and print them out?
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        // declare, create, initialize arrays
        int[ ] highScores = {99,98,98,88,68};
        String[ ] names = {"Jamal", "Emily", "Destiny", "Mateo", "Sofia"};
   
        // Print corresponding names and scores
        System.out.println(names[0] + " has a score of " + highScores[0]);
        System.out.println(names[1] + " has a score of " + highScores[1]);
      }
   }
   ====
   // Test for Lesson 6.1.2 - While Loop FindAndReplace lclw1
   
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Test1");
        }
   
        @Test
        public void test1() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Jamal has a score of 99\nEmily has a score of 98";
   
            boolean passed = !output.equals(expect);
   
            passed = getResults(expect, output, "Did you change the main?", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Mateo has a score of 88";
   
            boolean passed = output.contains("Mateo");
   
            passed = getResults(expect, output, "Did you print out Mateo?", passed);
            assertTrue(passed);
        }
    }