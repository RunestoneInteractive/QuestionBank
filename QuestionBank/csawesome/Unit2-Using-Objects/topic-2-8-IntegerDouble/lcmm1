.. activecode:: lcmm1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-8-IntegerDouble
   :topics: Unit2-Using-Objects/topic-2-8-IntegerDouble
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 276
   :num_students_correct: 276.0
   :mean_clicks_to_correct: 1.0

   What's the minimum and maximum numbers for an int? What happens if you go beyond these limits with - 1 or + 1?
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        System.out.println(Integer.MIN_VALUE);
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE - 1);
        System.out.println(Integer.MAX_VALUE + 1);
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
            String expect = "-2147483648\n2147483647\n2147483647\n-2147483648";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }