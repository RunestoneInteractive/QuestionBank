.. activecode:: lcab2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-1-array-basics
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.1015037594
   :total_students_attempting: 266
   :num_students_correct: 244.0
   :mean_clicks_to_correct: 2.0327868852

   Try running the code below to see the length. Try adding another value to the highScores initializer list and run again to see the length value change.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        int[ ] highScores = {99,98,98,88,68};
        System.out.println(highScores.length);
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
            super("Test2");
        }
   
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main").trim();
            String expect = "6";
   
            //boolean pass = !output.equals(expect.trim());
   
            boolean passed = getResults(expect, output, "Did you add another value?");
            assertTrue(passed);
        }
   
        @Test
        public void testChangedCode() {
            String origCode = "public class Test2 { public static void main (String [] args) { int [] highScores = {99,98,98,88,68}; System.out.println(highScores.length); } }";
   
            boolean changed = codeChanged(origCode);
   
            assertTrue(changed);
   
        }
    }