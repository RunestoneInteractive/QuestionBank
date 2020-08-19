.. activecode:: challenge-5-6-costCalculator
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: F
  :language: java
  :autograde: unittest

  - Update the program below to add a new method  ``calculateShipping`` that has one formal parameter for ``weight``.  The method will need a local variable for ``cost``.  The method should test the weight and print the corresponding cost.
  - Update the main method to replace the existing code with 3 calls to ``calculateShipping``, each passing an actual value for weight.  The main method will no longer need local variables.
  - Confirm that the new version of the program produces the same output as the original version.

  ~~~~
  public class ShippingCostCalculator {

  public static void main(String[] args) {

     double weight1, weight2, weight3;
     double cost1, cost2, cost3;

     weight1 = 22.0;
     weight2 = 10.0;
     weight3 = 12.0;

     //calculate cost for item#1
     if (weight1 < 15.0)
     {
        cost1 = 9.95;
     }
     else
     {
        cost1 = 12.95;
     }
     System.out.println(cost1);

     //calculate cost for item#2
     if (weight2 < 15.0)
     {
        cost2 = 9.95;
     }
     else
     {
        cost2 = 12.95;
     }
     System.out.println(cost2);

     //calculate cost for item#3
     if (weight3 < 15.0)
     {
        cost3 = 9.95;
     }
     else
     {
        cost3 = 12.95;
     }
     System.out.println(cost3);

    }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {

    public RunestoneTests() {
      super("ShippingCostCalculator");
    }
      @Test
      public void checkCodeContains3(){
        String code = getCode();
        int num = countOccurences(code, "public static void calculateShipping(");
        boolean passed = num = 1;
        passed = getResults("1 method declaration", num + " method declaration", "Declare the static calculateShipping method", passed);
        assertTrue(passed);
      }

      @Test
      public void checkCodeContains3(){
        String code = getCode();
        int num = countOccurences(code, "calculateShipping(");
        boolean passed = num >=3;
        passed = getResults("3 method calls", num + " method calls", "Call the calculateShipping method 3 times", passed);
        assertTrue(passed);
      }

      @Test
      public void testMain() throws IOException
      {
            String output = getMethodOutput("main");
            String expect = "12.95\n9.95\n9.95";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Expected output from main");
            assertTrue(passed);
      }
    }