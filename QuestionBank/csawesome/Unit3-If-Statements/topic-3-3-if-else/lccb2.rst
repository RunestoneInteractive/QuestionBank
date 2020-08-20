.. activecode:: lccb2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 282
   :num_students_correct: 282.0
   :mean_clicks_to_correct: 1.0

   Try the following code. If ``isHeads`` is true it will print ``Let's go to the game`` and then ``after conditional``.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        boolean isHeads = true;
        if (isHeads)
        {
            System.out.println("Let's go to the game");
        }
        else
        {
            System.out.println("Let's watch a movie");
        }
        System.out.println("after conditional");
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
           String expect = "Let's go to the game\nafter conditional";
   
           boolean passed = getResults(expect, output, "Expected output from main", true);
           assertTrue(passed);
       }
   
    }