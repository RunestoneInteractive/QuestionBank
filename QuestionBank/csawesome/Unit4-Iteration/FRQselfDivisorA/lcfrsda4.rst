.. activecode:: lcfrsda4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit4-Iteration
    :subchapter: FRQselfDivisorA
    :topics: Unit4-Iteration/FRQselfDivisorA
    :from_source: T
    :language: java
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 22
    :num_students_correct: 22.0
    :mean_clicks_to_correct: 1.0

    public class TestDigits
    {
       public static void main(String[] args)
       {
          System.out.println(128 % 10);
          System.out.println(128 / 10);
          System.out.println(12 % 10);
          System.out.println(12 / 10);
       }
    }
    ====
    import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     //import java.util.regex.*;
     /* Do NOT change Main or CodeTestHelper.java. */
     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testMain() throws IOException
         {
             String output = getMethodOutput("main");
             String expect = "8\n12\n2\n1\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }