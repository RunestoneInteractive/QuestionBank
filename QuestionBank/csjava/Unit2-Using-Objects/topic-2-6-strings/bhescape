.. activecode:: bhescape
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: F
   :language: java
   :autograde: unittest


   ~~~~
   public class TestEscape
   {
      public static void main(String[] args)
      {
        String message = "Here is a backslash quote \" " +
          " and a backslashed backslash (\\) " +
          "Backslash n \n prints out a new line.";
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
            String expect = output;
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }