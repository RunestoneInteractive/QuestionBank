.. activecode:: bool1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-1-booleans
   :topics: Unit3-If-Statements/topic-3-1-booleans
   :from_source: F
   :language: java
   :autograde: unittest

   What will the code below print out? Try to guess before you run it! Note that 1 equal sign (=) is used for assigning a value and 2 equal signs (==) for testing values.
   ~~~~
   public class BoolTest1
   {
      public static void main(String[] args)
      {
        int age = 15;
        int year = 14;
        // Will this print true or false?
        System.out.println( age == year );
        year = 15;
        // Will this print true or false?
        System.out.println( age == year );
        // Will this print true or false?
        System.out.println( age != year );
      }
   }
   ====
   // should pass if/when they run code
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "false\ntrue\nfalse\n";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }