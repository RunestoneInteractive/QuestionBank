.. activecode::  arr2DEx6q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.1666666667

   public class Test1
   {
       public static void main(String[] args)
       {
           String[][] arr = { {"Hey ", "there! "},{"I ", "hope "},
                             {"you ", "are "}, {"doing ", "well"} };
   
           // ADD CODE HERE //
   
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
            String expect = "Hey there! \nI hope \nyou are \ndoing well ";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
       public void test1()
       {
        String code = getCode();
        String target = "for";
   
        int num = countOccurences(code, target);
        boolean passed = (num >= 2);
   
        getResults("2", ""+num, "2 for loops", passed);
        assertTrue(passed);
      }
    }