.. activecode:: mod
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit4-Iteration
    :subchapter: FRQcalendar
    :topics: Unit4-Iteration/FRQcalendar
    :from_source: T
    :language: java
    :autograde: unittest
    :pct_on_first: 0.675
    :total_students_attempting: 40
    :num_students_correct: 37.0
    :mean_clicks_to_correct: 1.6486486486

    Complete the program below to figure out a day of the week from 0-6 where 0 is Sunday and 6 is Saturday for 7 days of the week. What value would you use for the divisor?
    ~~~~
    public class Mod
    {
       public static void main(String[] args)
       {
         int day1 = 7;
         int day2 = 8;
         int day3 = 9;
         // fill in the divisor value below
         int divisor =   ;
         System.out.println("Remainder of " + day1 + "/" + divisor + " is " + (day1 % divisor) );
         System.out.println("Remainder of " + day2 + "/" + divisor + " is " + (day2 % divisor) );
         System.out.println("Remainder of " + day3 + "/" + divisor + " is " + (day3 % divisor) );
       }
    }
    ====
    import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;
    
     public class RunestoneTests extends CodeTestHelper
     {
         public RunestoneTests() {
             super("Mod");
         }
    
         @Test
         public void test1()
         {
             String output = getMethodOutput("main");
             String expect = "Remainder of 7/7 is 0\nRemainder of 8/7 is 1\nRemainder of 9/7 is 2";
    
             boolean passed = getResults(expect, output, "Running main");
             assertTrue(passed);
         }
     }