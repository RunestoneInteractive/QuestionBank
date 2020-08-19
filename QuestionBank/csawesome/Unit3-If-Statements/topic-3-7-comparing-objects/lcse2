.. activecode:: lcse2
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
   :total_students_attempting: 187
   :num_students_correct: 187.0
   :mean_clicks_to_correct: 1.0

   What will the following print?
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        String s1 = new String("Hello");
        String s2 = new String("Hello");
        System.out.println(s1 == s2);
        System.out.println(s1.equals(s2));
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
            String expect = "false\ntrue\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }