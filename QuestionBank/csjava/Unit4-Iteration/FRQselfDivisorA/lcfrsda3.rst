.. activecode:: lcfrsda3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: FRQselfDivisorA
   :topics: Unit4-Iteration/FRQselfDivisorA
   :from_source: T
   :language: java
   :autograde: unittest

   public class Test
   {
      public static void main(String[] args)
      {
         System.out.println(26 % 6);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    //import java.util.regex.*;
    /* Do NOT change Main or CodeTestHelper.java. */
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "2\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }