.. activecode:: TemperatureBugs
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-7-static-vars-methods
  :topics: Unit5-Writing-Classes/topic-5-7-static-vars-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.6258503401
  :total_students_attempting: 147
  :num_students_correct: 124.0
  :mean_clicks_to_correct: 1.6209677419

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
  
            boolean passed = checkCodeContains("static printMax() header", "public static void printMax()");
            assertTrue(passed);
        }
  
         @Test
        public void testCodeContains2()
        {
  
            boolean passed = code.contains("System.out.println(maxTemp);") ||       code.contains("System.out.println(Temperature.maxTemp);");
            getResults("true",""+passed, "printMax method",passed);
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