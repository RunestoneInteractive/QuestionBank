.. activecode:: code2_9_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-9-Math
   :topics: Unit2-Using-Objects/topic-2-9-Math
   :from_source: T
   :language: java
   :autograde: unittest

   Try out the following code.  Run it several times to see what it prints each time.
   ~~~~
   public class Test3
   {
      public static void main(String[] args)
      {
        System.out.println(Math.random());
        System.out.println(Math.random());
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