.. activecode:: lcso2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.1118881119
   :total_students_attempting: 286
   :num_students_correct: 260.0
   :mean_clicks_to_correct: 2.2653846154

   What do you think the following will print? Guess before you hit run. If you want the addition to take place before the numbers are turned into a string what should you do? Try to modify the code  so that it adds 4 + 3 before appending the value to the string. Hint: you used this to do addition before multiplication in arithmetic expressions.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        String message = "12" + 4 + 3;
        System.out.println(message);
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
            String expect = "127";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }