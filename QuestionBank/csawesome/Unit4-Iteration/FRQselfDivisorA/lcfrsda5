.. activecode:: lcfrsda5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: FRQselfDivisorA
   :topics: Unit4-Iteration/FRQselfDivisorA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3684210526
   :total_students_attempting: 19
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 4.4117647059

   FRQ SelfDivisor: Write the method isSelfDivisor.
   ~~~~
   public class SelfDivisor
   {
   
      /** @param number the number to be tested
       *         Precondition: number > 0
       *  @return true if every decimal digit of
       *          number is a divisor of number;
       *          false otherwise
       */
      public static boolean isSelfDivisor(int number)
      {
        // part A
      }
   
      /****************/
   
      public static void main (String[] args)
      {
        System.out.println("128: " + isSelfDivisor(128));
        System.out.println("26: " + isSelfDivisor(26));
        System.out.println("120: " + isSelfDivisor(120));
        System.out.println("102: " + isSelfDivisor(102));
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "128: true\n26: false\n120: false\n102: false\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   
        @Test
        public void testIfLoop()
        {
           String code = getCode();
           boolean passed = code.contains("if") && (code.contains("for") || code.contains("while"));
           getResults("Expected loop, if, %",""+passed, "Checking for loop and if statement",passed);
            assertTrue(passed);
        }
   
        @Test
        public void testModDiv()
        {
           String code = getCode();
           boolean passed = code.contains("%") && code.contains("/");
           getResults("Expected % and /",""+passed, "Checking for use of % and /",passed);
            assertTrue(passed);
        }
    }