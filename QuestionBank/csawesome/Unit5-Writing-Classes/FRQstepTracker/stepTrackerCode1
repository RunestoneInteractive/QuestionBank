.. activecode:: stepTrackerCode1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: FRQstepTracker
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5555555556
   :total_students_attempting: 36
   :num_students_correct: 33.0
   :mean_clicks_to_correct: 1.4545454545

   Write the first draft of the class StepTracker below with the class name, the instance variables, and the constructor with a parameter for the minimum number of steps threshold for active days. Make sure it compiles.
   ~~~~
   // Write class name here
   
   {
      // write instance variable declarations here
   
   
      // write the constructor with a parameter here
   
   
      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void test1(){
        //check class name
        boolean passed = checkCodeContains("correct class heading", "public class StepTracker");
        assertTrue(passed);
   
      }
   
      @Test
      public void test2(){
         //constructor with 1 parameter for threshold minSteps
         String args = "int";
         String results = checkConstructor(args);
   
         boolean passed = getResults("pass", results, "Checking constructor with one int argument");
         assertTrue(passed);
   
      }
   
      @Test
      public void test3(){
            //check int - declaration of instance variables and parameter in constructor
            String actual = testPrivateInstanceVariables();
            String expected = "4 Private";
   
            boolean passed = getResults(expected, actual, "Checking declaration of instance variables");
            assertTrue(passed);
   
      }
    }