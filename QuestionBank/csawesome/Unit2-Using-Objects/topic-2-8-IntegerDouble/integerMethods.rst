.. activecode:: integerMethods
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-8-IntegerDouble
   :topics: Unit2-Using-Objects/topic-2-8-IntegerDouble
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9961089494
   :total_students_attempting: 257
   :num_students_correct: 257.0
   :mean_clicks_to_correct: 1.0038910506

   Run the code below to see useful methods in the Integer and Double wrapper classes.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        Integer i = 2;
        Double d = 3.5;
        System.out.println( i.intValue() ); // intValue() returns the primitive value
        System.out.println( d.doubleValue() );
   
        String ageStr = "16";
        // Integer.parseInt and Double.parseDouble are often used to
        // convert an input string to a number so you can do math on it.
        // They are not on the AP exam
        System.out.println("Age " + ageStr + " in 10 years is " + (Integer.parseInt(ageStr) + 10) );
        System.out.println("Note that + with strings does concatenation, not addition: " + (ageStr + 10));
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
            String expect = "2\n3.5\nAge 16 in 10 years is 26\nNote that + with strings does concatenation, not addition: 1610";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }