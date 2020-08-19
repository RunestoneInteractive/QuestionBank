.. activecode:: evenLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit6-Arrays/topic-6-3-arrays-with-foreach
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.245
   :total_students_attempting: 200
   :num_students_correct: 126.0
   :mean_clicks_to_correct: 2.3015873016

   Rewrite the following for loop which prints out the even numbers in the array as an enhanced for-each loop. Make sure it works!
   ~~~~
   public class EvenLoop
   {
      public static void main(String[] args)
      {
          int[ ] values = {6, 2, 1, 7, 12, 5};
          // Rewrite this loop as a for each loop and run
          for (int i=0; i < values.length; i++)
          {
              if (values[i] % 2 == 0)
              {
                 System.out.println(values[i] + " is even!");
              }
          }
      }
   }
   ====
   // Test for Lesson 6.3.2 - EvenLoop
   
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("EvenLoop");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "6 is even!\n2 is even!\n12 is even!";
   
            boolean passed = getResults(expect, output, "main()");
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            boolean passed = checkCodeContains("for each loop", "for(int * : values)");
            assertTrue(passed);
        }
    }