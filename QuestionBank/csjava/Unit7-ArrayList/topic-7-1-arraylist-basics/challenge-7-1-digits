.. activecode:: challenge-7-1-digits
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest

   Complete the challenge below to put the digits of a number in an ArrayList.
   ~~~~
   import java.util.*;

   public class Digits
   {
      /** A list of digits */
      private ArrayList<Integer> digitList;

      /** Constructs a list of digits from the given number */
      public Digits(int number)
      {
         // initialize digitList to an empty ArrayList of Integers

         // Use a while loop to add each digit in number to digitList

         //Use Collections.reverse(digitList); to reverse the digits

      }

      /** returns the string representation of the digits list */
      public String toString()
      {
         return digitList.toString();
      }

      public static void main(String[] args)
      {
         Digits d1 = new Digits(154);
         System.out.println(d1);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Digits");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[1, 5, 4]";

            boolean passed = getResults(expect, output, "Digits(154)");
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            Digits test = new Digits(123456);
            String output = test.toString();
            String expect = "[1, 2, 3, 4, 5, 6]";

            boolean passed = getResults(expect, output, "Digits(123456)");
            assertTrue(passed);
        }
    }