.. activecode:: stepcounter
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-3-method-return
  :topics: Unit5-Writing-Methods/topic-5-3-method-return
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  A pedometer estimates that taking 2,000 steps is the same as walking 1 mile.
  Write a method ``convertToMiles`` that takes a parameter for the number of steps and returns the equivalent miles walked.
  Update the main method to call ``convertToMiles`` 4 times with values 500, 2000, 3000, 9000.
  Carefully consider what the return type should be.
  You can assume the number of steps is an integer.

  ~~~~
  public class StepCounter
  {
      //add convertToMiles method here

      public static void main(String[] args)
      {
         System.out.println("500 steps is equal to " + convertToMiles(500) + " miles");
         //add 3 more method calls here

      }
  }

  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("InchesToCentimeters");
    }

      @Test
      public void checkCodeContainsSig(){
        String code = getCode();
        int num = countOccurences(code, "public static double convertToMiles(int");
        boolean passed = num ==1;
        passed = getResults("1", num , "The convertToMiles signature is not correct. Check your return type and the parameter type", passed);
        assertTrue(passed);
      }

     @Test
      public void checkCodeContainsReturn(){
        String code = getCode();
        int num = countOccurences(code, "return");
        boolean passed = num ==1;
        passed = getResults("1", num , "The method convertToMiles is missing a return statement", passed);
        assertTrue(passed);
      }

      @Test
      public void testMain() throws IOException
      {
            String output = getMethodOutput("main");
            String expect = "500 steps is equal to 0.25 miles";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Expected output from main");
            assertTrue(passed);
      }

      @Test
      public void testMain2() throws IOException
      {
            String output = getMethodOutput("main");
            String expect = "2000 steps is equal to 1 mile";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Expected output from main");
            assertTrue(passed);
      }
    }
  }