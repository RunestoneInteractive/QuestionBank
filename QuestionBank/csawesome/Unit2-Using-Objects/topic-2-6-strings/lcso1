.. activecode:: lcso1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.2195121951
   :total_students_attempting: 287
   :num_students_correct: 259.0
   :mean_clicks_to_correct: 2.4324324324

   Try the following code. Add another variable for a lastname that is "Hernandez". Use += or + to add the lastname variable after name to the result. Use += or + to add 2 more exclamation points (!) to the end of the happy birthday greeting in result.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
          String start = "Happy Birthday";
          String name = "Jose";
          String result = start + " " + name;  // add together strings
          result += "!"; // add on to the same string
          System.out.println(result);
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
            String expect = "Happy Birthday Jose Hernandez!!!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }