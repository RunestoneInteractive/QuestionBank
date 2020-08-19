.. activecode:: lccb1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9548192771
   :total_students_attempting: 332
   :num_students_correct: 324.0
   :mean_clicks_to_correct: 1.0216049383

   The variable ``isRaining`` is a boolean variable that is either true or false. If it is true then the message ``Take an umbrella!`` will be printed and then execution will continue with the next statement which will print ``Drive carefully``. Run the code below to see this.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        boolean isRaining = true;
        if (isRaining)
        {
           System.out.println("Take an umbrella!");
        }
        System.out.println("Drive carefully");
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
            String expect = "Take an umbrella! \nDrive carefully";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }