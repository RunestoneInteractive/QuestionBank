.. activecode:: danglingelse
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.3271375465
   :total_students_attempting: 269
   :num_students_correct: 224.0
   :mean_clicks_to_correct: 2.1026785714

   Try the following code with a dangling else. Notice that the indentation does not matter. How could you get the else to belong to the first if statement?
   ~~~~
   public class DanglingElseTest
   {
      public static void main(String[] args)
      {
          boolean sunny = true;
          boolean hot = false;
          if (sunny)
            if (hot)
                System.out.println("Head for the beach!");
           else // Which if is else attached to??
          System.out.println("Bring your umbrella!");
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "";
            boolean passed = getResults(expect, output, "Expected no output from main");
            assertTrue(passed);
        }
    }