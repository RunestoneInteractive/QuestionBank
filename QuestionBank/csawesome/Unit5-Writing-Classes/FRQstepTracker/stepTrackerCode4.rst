.. activecode:: stepTrackerCode4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: FRQstepTracker
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.2692307692
   :total_students_attempting: 26
   :num_students_correct: 25.0
   :mean_clicks_to_correct: 3.12

   Copy the code from your draft of the class StepTracker above  with the instance variables, constructor, accessor and mutator methods. Write the accessor method **averageSteps** which returns the average number of steps per day, calculated by dividing the total number of steps taken by the number of days tracked.
   ~~~~
   public class StepTracker
   {
      // copy the instance variable declarations here
   
   
      // copy the constructor with a parameter here
   
      // copy the accessor method activeDays() here
   
   
      // copy the mutator method addDailySteps here.
      // @param number of steps taken that day
   
   
      //Write the accessor method averageSteps() here
      // @return average steps calculated by dividing the total number of steps taken by the number of days tracked (which should be instance variables). Make sure you use type casting to double!
   
   
   
   
      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
         System.out.println(tr.activeDays()); // returns 0. No data have been recorded yet.
         System.out.println(tr.averageSteps()); // returns 0.0. When no step data have been recorded, the averageSteps method returns 0.0.
         tr.addDailySteps(9000); // This is too few steps for the day to be considered active.
         tr.addDailySteps(5000); // This is too few steps for the day to be considered active.
         System.out.println(tr.activeDays()); // returns 0.  No day had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 7000.0 The average number of steps per day is (14000 / 2).
         tr.addDailySteps(13000); // This represents an active day.
         System.out.println(tr.activeDays());  // returns 1. Of the three days for which step data were entered, one day had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 9000.0. The average number of steps per day is (27000 / 3).
         tr.addDailySteps(23000); // This represents an active day.
         tr.addDailySteps(1111); // This is too few steps for the day to be considered active.
         System.out.println(tr.activeDays()); // returns 2. Of the five days for which step data were entered, two days had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 10222.2. The average number of steps per day is (51111 / 5).
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
        String expect = "0\n0.0\n0\n7000.0\n1\n9000.0\n2\n10222.2\n";
        boolean passed = getResults(expect, output, "Expected output from main. Make sure you used casting to double for the last result!");
        assertTrue(passed);
      }
   
      @Test
      public void checkCodeContains1()
      {
        //check mutator method averageSteps()
        boolean passed = checkCodeContains("averageSteps() method","public double averageSteps()");
        assertTrue(passed);
   
      }
      }