.. activecode:: code1_4_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest

   Fix the code below to perform a correct swap of x and y.
   You need to add a new variable named ``temp`` to use for the swap.
   ~~~~

    public class CorrectSwap
    {
      public static void main(String[] args)
      {
        int x = 3;
        int y = 5;
        System.out.println(x);
        System.out.println(y);
        x = y;
        y = x;
        System.out.println(x);
        System.out.println(y);
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;

    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "3\n5\n5\n3\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }


        @Test
        public void test2()
        {
            String code = getCode();
            String expect = "int temp";

            int count = countOccurences(code, expect);

            boolean passed = count >= 1;

            passed = getResults("1 temp declaration", "" + count  + " temp declaration", "Declare variable temp", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            String expect = "temp = x";

            int count = countOccurences(code, expect);

            boolean passed = count >= 1;

            passed = getResults("1 temp assignment to x", "" + count  + " temp assignment to x", "Assign variable temp to x", passed);
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            String code = getCode();
            String expect = "y = temp";

            int count = countOccurences(code, expect);

            boolean passed = count >= 1;

            passed = getResults("1 y assignment to temp", "" + count  + " y assignment to temp", "Assign variable y to temp", passed);
            assertTrue(passed);
        }


    }