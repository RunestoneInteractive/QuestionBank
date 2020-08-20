.. activecode:: code5_2_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T

  Update the code below to add the ``calculatePay`` method shown in Figure 2.  Update the ``main`` method to
  call the ``calculatePay`` method twice to compute the pay for each employee.
  Use the CodeLens button to confirm that your main method makes the two calls to calculatePay, with the correct values passed into the method.

  ~~~~
  public class PayrollCalculator
  {

    //add a new static method calculatePay here



    public static void main(String[] args) {

        //call calculatePay for employee Fred, hourly rate 12.50 and hours worked 20.0

        //call calculatePay for employee Amir, hourly rate 15.0 and hours worked 35.0

    }
  }
  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("PayrollCalculator");
    }

    @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Fred:250.0\nAmir:525.0\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }

    @Test
        public void test2()
        {
           String code = getCode();
           int sig = countOccurences(code, "public static void calculatePay(");
           boolean passed = sig == 1;
           passed = getResults("1 method signature", sig + " method signature", "Add a new method calculatePay", passed);
           assertTrue(passed);
        }

    @Test
        public void test3()
        {
           String code = getCode();
           int calls = countOccurences(code, "calculatePay(\"");
           boolean passed = (calls==2);
           passed = getResults("2 calls", calls + " calls", "Update the main with two calls to calculatePay", passed);
           assertTrue(passed);
        }

  }