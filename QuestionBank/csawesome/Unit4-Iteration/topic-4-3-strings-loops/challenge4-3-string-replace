.. activecode:: challenge4-3-string-replace
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-3-strings-loops
   :topics: Unit4-Iteration/topic-4-3-strings-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.2072072072
   :total_students_attempting: 222
   :num_students_correct: 153.0
   :mean_clicks_to_correct: 3.7320261438

   Write a while loop that replaces every occurrence of "cat" in the message with "dog" using the indexOf and substring methods.
   ~~~~
   public class ChallengeReplace
   {
     public static void main(String[] args)
     {
          String message = "I love cats! I have a cat named Coco. My cat's very smart!";
   
          // Write a loop here that replaces every occurrence of "cat"
          // in the message with "dog", using indexOf and substring.
   
   
   
          System.out.println(message);
      }
   }
   ====
   // Test Code for Lesson 4.3.3 - String Replacement - ChallengeReplace
   
    import static org.junit.Assert.*;
   
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
   
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ChallengeReplace");
        }
   
        @Test
        public void test1() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "I love cats! I have a cat named Coco. My cat's very smart!".replaceAll("cat","dog");
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
   
        @Test
        public void testWhile() throws IOException
        {
            String target = "while(";
            boolean passed = checkCodeContains("while loop", target);
            assertTrue(passed);
        }
   
        @Test
        public void testSubString()
        {
            String target = "substring(";
            boolean passed = checkCodeContains("substring", target);
            assertTrue(passed);
        }
   
        @Test
        public void testReplace() throws IOException
        {
            String target = ".replace";
            boolean passed = checkCodeNotContains("shortcut replace", target);
            assertTrue(passed);
        }
   
    }