.. activecode:: APLineFRQ
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: APLine
   :topics: Unit5-Writing-Classes/APLine
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4117647059
   :total_students_attempting: 17
   :num_students_correct: 16.0
   :mean_clicks_to_correct: 2.8125

   Write a class APLine with instance variables, a constructor with 3 paramaters for a, b, c, and the methods getSlope() and isOnLine(x,y).
   ~~~
   // Declare the APLine class
   {
    /** Declare instance variables */
   
    /** Constructor with 3 int parameters. */
   
    /** method getSlope(): Determine the slope of this APLine. */
   
    /** method isOnLine(x,y): Determine if coordinates (x,y) represent a point on this APLine. */
   
    /** Test with this main method */
    public static void main(String[] args)
    {
        APLine line1 = new APLine(5, 4, -17);
        double slope1 = line1.getSlope(); // slope1 is assigned -1.25
        boolean onLine1 = line1.isOnLine(5, -2); // true because 5(5) + 4(-2) + (-17) = 0
   
        APLine line2 = new APLine(-25, 40, 30);
        double slope2 = line2.getSlope(); // slope2 is assigned 0.625
        boolean onLine2 = line2.isOnLine(5, -2); // false because -25(5) + 40(-2) + 30 != 0
        // Should print out true and false
        System.out.println(onLine1 + " " + onLine2);
     }
   }
   ====
   // Test Code for Lesson 5.15 - FRQ - APLine
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests()
        {
            super("APLine");
            // This sets default values for when objects are instantiated
            Object[] values = new Object[]{3, 2, -6};
            setDefaultValues(values);
        }
   
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = " true false";
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
   
        @Test
        public void testConstructor()
        {
            String output = checkConstructor(3);
            String expect = "pass";
   
            boolean passed = getResults(expect, output, "Checking constructor with 3 parameters");
            assertTrue(passed);
        }
   
        @Test
        public void testGetSlope() throws IOException
        {
            double output = Double.parseDouble(getMethodOutput("getSlope"));
            double expect = -1.5;
   
            boolean passed = getResults(expect, output, "Checking method getSlope()");
            assertTrue(passed);
        }
   
        @Test
        public void testIsOnLine1() throws IOException
        {
            Object[] args =  {2, 0};
            String output = getMethodOutput("isOnLine", args);
            String expect = "true";
   
            boolean passed = getResults(expect, output, "Checking method isOnLine(5, -2)");
            assertTrue(passed);
        }
   
        @Test
        public void testIsOnLine2() throws IOException
        {
            Object[] args =  {5, -2};
            String output = getMethodOutput("isOnLine", args);
            String expect = "false";
   
            boolean passed = getResults(expect, output, "Checking method isOnLine(5, -2)");
            assertTrue(passed);
        }
   
        @Test
        public void testPrivateVariables()
        {
            String expect = "3 Private";
            // Will produce a printout with number of private and public variables
            String output = testPrivateInstanceVariables();
   
            boolean passed = getResults("3 Private", output, "Checking Instance Variable(s)");
   
            assertTrue(passed);
        }
    }