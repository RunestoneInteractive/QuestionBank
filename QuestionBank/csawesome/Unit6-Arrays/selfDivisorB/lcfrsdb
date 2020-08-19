.. activecode:: lcfrsdb
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: selfDivisorB
   :topics: Unit6-Arrays/selfDivisorB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.0

   FRQ SelfDivisor B: write the method firstNumSelfDivisors below.
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
        int currNumber = number;
        int digit = 0;
        while (currNumber > 0)
        {
           digit = currNumber % 10;
           if (digit == 0) return false;
           if (number % digit != 0) return false;
           currNumber = currNumber / 10;
        }
        return true;
      }
   
      /**
       * @param start starting point for values to be checked
       * Precondition: start > 0
       * @param num the size of the array to be returned
       * Precondition: num > 0
       * @return an array containing the first num
       * integers >= start that are self-divisors
       */
      public static int[] firstNumSelfDivisors(int start,
                                               int num)
      { /* to be implemented in part (b) */ }
   
      public static void main (String[] args)
      {
        System.out.println("Self divisors for firstNumSelfDivisors(10, 3):");
        for (int n : firstNumSelfDivisors(10, 3))
           System.out.print(n + " ");
        System.out.println();
   
        System.out.println("Self divisors for firstNumSelfDivisors(22, 5):");
        for (int n : firstNumSelfDivisors(22, 5))
           System.out.print(n + " ");
        System.out.println();
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.Arrays;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "Self divisors for firstNumSelfDivisors(10, 3):\n11 12 15\nSelf divisors for firstNumSelfDivisors(22, 5):\n22 24 33 36 44";
            boolean passed = getResults(expect, output, "Checking output from main");
            assertTrue(passed);
        }
   
        @Test
        public void test2() {
            String msg = "Checking firstNumSelfDivisors(5, 10)";
            String output = Arrays.toString(SelfDivisor.firstNumSelfDivisors(5, 10));
            String expect = "[5, 6, 7, 8, 9, 11, 12, 15, 22, 24]";
   
            boolean passed = getResults(expect, output, msg);
            assertTrue(passed);
        }
    }