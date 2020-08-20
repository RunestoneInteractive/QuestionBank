.. activecode:: stepTrackerCode3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: FRQstepTracker
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6153846154
   :total_students_attempting: 26
   :num_students_correct: 25.0
   :mean_clicks_to_correct: 1.68

   Copy the code from your draft of the class StepTracker above  with the class name, the instance variables, constructor, and accessory method. Write the mutator method **addDailySteps** which takes a parameter and adds it to the appropriate instance variable and changes other instance variables appropriately.
   ~~~~
   public class StepTracker
   {
      // copy the instance variable declarations here
   
   
      // copy the constructor with a parameter here
   
      // copy the accessor method activeDays() here.
   
      // Write the mutator method addDailySteps here.
      // @param number of steps taken that day
   
   
   
      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
         System.out.println(tr.activeDays()); // returns 0. No data have been recorded yet.
         tr.addDailySteps(9000); // This is too few steps for the day to be considered active.
         tr.addDailySteps(5000); // This is too few steps for the day to be considered active.
         System.out.println(tr.activeDays()); // returns 0.  No day had at least 10,000 steps.
         tr.addDailySteps(13000); // This represents an active day.
         System.out.println(tr.activeDays());  // returns 1. Of the three days for which step data were entered, one day had at least 10,000 steps.
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
        String expect = "0\n0\n1\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
      @Test
      public void checkCodeContains1()
      {
        //check mutator method addDailySteps()
        boolean passed = checkCodeContains("addDailySteps method with parameter", "public void addDailySteps(int");
        assertTrue(passed);
   
      }
   
     @Test
      public void checkCodeContains2()
      {
        //check mutator method addDailySteps() contains "if"
        boolean passed = checkCodeContains("if statement","if (");
        assertTrue(passed);
      }
    }