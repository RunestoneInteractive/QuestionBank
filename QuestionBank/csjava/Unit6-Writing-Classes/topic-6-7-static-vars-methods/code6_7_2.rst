.. activecode:: code6_7_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-7-static-vars-methods
  :topics: Unit6-Writing-Classes/topic-6-7-static-vars-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T

  Fix the bugs in the following code.
  ~~~~
  public class Temperature
  {
    private double temperature;
    public static double maxTemp = 0;

    public Temperature(double t)
    {
        temperature = t;
        if (t > maxTemp)
           maxTemp = t;
    }

    public static printMax()
    {
       System.out.println(temperature);
    }

    public static void main(String[] args)
    {
       Temperature t1 = new Temperature(75);
       Temperature t2 = new Temperature(100);
       Temperature.printMax();
    }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testCodeContains1()
        {

            boolean passed = checkCodeContains("return type of printMax()", "public static void printMax()");
            assertTrue(passed);
        }

         @Test
        public void testCodeContains2()
        {

            boolean passed = checkCodeContains("static variable maxTemp in static function", "System.out.println(maxTemp);");
            assertTrue(passed);
        }

        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "100.0";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }