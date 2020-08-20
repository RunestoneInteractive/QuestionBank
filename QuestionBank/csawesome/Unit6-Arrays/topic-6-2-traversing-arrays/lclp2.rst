.. activecode:: lclp2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.1043478261
   :total_students_attempting: 115
   :num_students_correct: 85.0
   :mean_clicks_to_correct: 1.9058823529

   Does this work for arrays that have an even number of elements?  Does it work for arrays that have an odd number of elements?  Modify the main code below to test with both arrays with an even number of items and an odd number.
   ~~~~
   public class ArrayWorker
   {
      private int[ ] values;
   
      public ArrayWorker(int[] theValues)
      {
         values = theValues;
      }
   
      public void doubleLastHalf()
      {
        for (int i = values.length / 2; i < values.length; i++)
        {
          values[i] = values[i] * 2;
        }
      }
   
      public void printArray()
      {
         for (int i = 0; i < values.length; i++)
         {
           System.out.println(  values[i] );
         }
      }
   
      public static void main(String[] args)
      {
          int[] numArray = {3,8,-3, 2};
          ArrayWorker worker = new ArrayWorker(numArray);
          worker.doubleLastHalf();
          worker.printArray();
      }
   }
   ====
   // Test for Lesson 6.2.4 - ArrayWorker
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayWorker");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "3\n8\n-6\n4".replaceAll(" ", "\n");
   
            boolean passed = getResults(expect, output, "Testing main()", true);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String orig = "public class ArrayWorker\n{\n   private int[ ] values;\n\n   public ArrayWorker(int[] theValues)\n   {\n      values = theValues;\n   }\n\n   public void doubleLastHalf()\n   {\n     for (int i = values.length / 2; i < values.length; i++)\n     {\n       values[i] = values[i] * 2;\n     }\n   }\n\n   public void printArray()\n   {\n      for (int i = 0; i < values.length; i++)\n      {\n        System.out.println(  values[i] );\n      }\n   }\n\n   public static void main(String[] args)\n   {\n     int[] numArray = {3,8,-3, 2};\n     ArrayWorker worker = new ArrayWorker(numArray);\n     worker.doubleLastHalf();\n     worker.printArray();\n   }\n}\n";
   
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    }