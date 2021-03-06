.. activecode:: APCalendarFRQPartA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: FRQcalendar
   :topics: Unit4-Iteration/FRQcalendar
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.7272727273
   :total_students_attempting: 44
   :num_students_correct: 42.0
   :mean_clicks_to_correct: 1.6666666667

   Write the code for the method numberOfLeapYears below and run to test it.
   ~~~~
   import java.util.Calendar;
   import java.util.GregorianCalendar;
   
   public class APCalendar
   {
   
    /** Returns the number of leap years between year1 and year2, inclusive.
     * Precondition: 0 <= year1 <= year2
    */
    public static int numberOfLeapYears(int year1, int year2)
    {
      // WRITE YOUR CODE HERE
   
    }
   
    /** Returns true if year is a leap year and false otherwise. */
    private static boolean isLeapYear(int year)
    {
        return new GregorianCalendar().isLeapYear(year);
    }
   
    public static void main(String[] args)
    {
        int answer = APCalendar.numberOfLeapYears(2000, 2050);
        System.out.println("Your answer should be 13: " + answer);
    }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("APCalendar");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Your answer should be 13: 13";
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            int answer = APCalendar.numberOfLeapYears(1990, 2100);
            int expect = 27;
   
            boolean passed = getResults("" + expect, "" + answer, "numberOfLeapYears(1990, 2100)");
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            int answer = APCalendar.numberOfLeapYears(2001, 2002);
            int expect = 0;
   
            boolean passed = getResults("" + expect, "" + answer, "numberOfLeapYears(2001, 2002)");
            assertTrue(passed);
        }
    }