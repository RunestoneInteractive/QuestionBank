.. activecode:: stepTrackerCode2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: FRQstepTracker
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9117647059
   :total_students_attempting: 34
   :num_students_correct: 33.0
   :mean_clicks_to_correct: 1.0606060606

   Copy the code from your first draft of the class StepTracker above  with the instance variables and constructor. Write the accessor methods **activeDays** which returns the number of active days.
   ~~~~
   public class StepTracker
   {
      // copy the instance variable declarations here
   
   
      // copy the constructor with a parameter here
   
      // Write the accessor method activeDays() here
      // @return activeDays
   
      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
         System.out.println(tr.activeDays()); // returns 0. No data have been recorded yet.
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
        String expect = "0\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
      @Test
      public void checkCodeContains1(){
        //check accessor method activeDays()
        boolean passed = checkCodeContains("activeDays() method", "public int activeDays()");
        assertTrue(passed);
   
      }
   
      @Test
      public void checkCodeContains2(){
         //check that activeDays() returns a value
          boolean passed = checkCodeContains("return");
        assertTrue(passed);
   
      }
    }