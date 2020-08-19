.. activecode:: code5_3_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-3-method-return
  :topics: Unit5-Writing-Methods/topic-5-3-method-return
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T

  The code below contains a method ``inchesToCentimeters`` that computes and prints the centimeter equivalent of the value passed into the inches parameter.
  Instead of printing the centimeter value inside the inchesToCentimeters method, you should update the
  method to return the value and then move the printing to the main method.  You will have to change
  the return type of the inchesToCentimeters method to match the type of the value being returned.
  Update the ``main`` method to print the value returned by the ``inchesToCentiments`` method.

  ~~~~
  public class InchesToCentimeters
  {
    public static void inchesToCentimeters(double inches)
        {
            double centimeters = inches * 2.54;
            System.out.println(centimeters);
        }

        public static void main(String[] args)
        {
            inchesToCentimeters(10);
            inchesToCentimeters(12.5);
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
      int num = countOccurences(code, "public static double inchesToCentimeters(double inches)");
      boolean passed = num ==1;
      passed = getResults("1 signature", num + " signature", "Change the return type of inchesToCentimeters", passed);
      assertTrue(passed);
    }

    @Test
    public void checkCodeContainsReturn(){
      String code = getCode();
      int num = countOccurences(code, "return");
      boolean passed = num ==1;
      passed = getResults("1 return", num + " return" , "The method inchesToCentiments is missing a return statement", passed);
      assertTrue(passed);
    }

    @Test
    public void testMain() throws IOException
    {
          String output = getMethodOutput("main");
          String expect = "25.4\n31.75";
          boolean passed = output.contains(expect);
          getResults(expect, output, "Expected output from main");
          assertTrue(passed);
    }
  }