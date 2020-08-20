.. activecode:: if-relational
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T

   Run the following active code a couple times until you see all the possible outputs. It prints out whether a random number is positive or equal to 0. Add another if statement that tests if it is a negative number.
   ~~~~
   public class TestNumbers
   {
      public static void main(String[] args)
      {
        // Get a random number from -10 up to 10.
        int number = (int) (Math.random()*21 - 10);
        System.out.println("The number is " + number);

        // is it positive?
        if (number > 0)
        {
           System.out.println(number + " is positive!");
        }
        // is it 0?
        if (number == 0)
        {
           System.out.println(number + " is zero!");
        }
      }
   }
   ====
   // Test Code for Lesson 3.2.1 - Activity 1 - if-relational
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;

    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testPositive()
        {
            String output = "";
            int num = -999;

            while(num <= 0) {
                output = getMethodOutput("main");
                num = getNumber(output);
            }

            String expect = "The number is " + num + "\n" + num + " is positive!";

            boolean passed = getResults(expect, output, "Testing positive numbers");
            assertTrue(passed);
        }

        @Test
        public void testZero()
        {
            String output = "";
            int num = -999;

            while(num != 0) {
                output = getMethodOutput("main");
                num = getNumber(output);
            }

            String expect = "The number is " + num + "\n" + num + " is zero!";

            boolean passed = getResults(expect, output, "Testing zero");
            assertTrue(passed);
        }

        @Test
        public void testNegative()
        {
            String output = "";
            int num = 999;

            while(num >= 0) {
                output = getMethodOutput("main");
                num = getNumber(output);
            }

            String expect = "The number is " + num + "\n" + num + " is negative!";

            boolean passed = getResults(expect, output,"Testing negative numbers");
            assertTrue(passed);
        }

        private int getNumber(String output) {
            output = output.replaceAll("The number is ", "");
            int space = output.indexOf("\n");

            String numStr = output;

            if (space >= 0)
                numStr = numStr.substring(0, space).trim();

            return Integer.parseInt(numStr);
        }
    }