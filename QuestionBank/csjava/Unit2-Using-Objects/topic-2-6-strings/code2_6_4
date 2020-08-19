.. activecode:: code2_6_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   Try the following code. Add another variable lastName that is "Hernandez". Use += or + to add the lastname variable after name
   to the result, with a space between first and last name. Add 2 more exclamation points (!) to the end of the happy birthday greeting in result.
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