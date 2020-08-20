.. activecode:: lcab1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-1-array-basics
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6902985075
   :total_students_attempting: 268
   :num_students_correct: 246.0
   :mean_clicks_to_correct: 1.3048780488

   In the following code, add another array declaration that creates an array of 5 doubles called prices and another array of 5 Strings called names and corresponding System.out.println commands.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
          // Array example
          int[] highScores = new int[10];
          // Add an array of 5 doubles called prices.
   
          // Add an array of 5 Strings called names.
   
          System.out.println("Array highScores declared with size " + highScores.length);
          // Print out the length of the new arrays
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Test1");
        }
   
        @Test
        public void testDouble() throws IOException
        {
            String target = "new double[5];";
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
        }
   
        @Test
        public void testString() throws IOException
        {
            String target = "new String[5];";
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
        }
    }