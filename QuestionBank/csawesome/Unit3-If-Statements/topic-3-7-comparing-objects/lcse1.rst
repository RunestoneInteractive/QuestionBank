.. activecode:: lcse1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-7-comparing-objects
   :topics: Unit3-If-Statements/topic-3-7-comparing-objects
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 197
   :num_students_correct: 197.0
   :mean_clicks_to_correct: 1.0

   If you run the following, what will be printed?
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        String s1 = new String("Hello");
        String s2 = new String("Bye");
        String s3 = s2;
        System.out.println(s3);
        System.out.println(s2 == s3);
        System.out.println(s2.equals(s3));
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
            String expect = "Bye\ntrue\ntrue\n";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }