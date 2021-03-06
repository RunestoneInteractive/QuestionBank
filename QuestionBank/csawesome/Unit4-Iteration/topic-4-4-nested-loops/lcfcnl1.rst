.. activecode:: lcfcnl1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-4-nested-loops
   :topics: Unit4-Iteration/topic-4-4-nested-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.2266666667
   :total_students_attempting: 150
   :num_students_correct: 127.0
   :mean_clicks_to_correct: 2.3858267717

   Can you change the code to print a rectangle with 10 rows and 8 columns of stars? You can also try replacing line 10 with this print statement to see the rows and columns: ``System.out.print(row + "-" + col + " ");``
   ~~~~
   public class NestedLoops
   {
   
      public static void main(String[] args)
      {
          for (int row = 1; row <= 3; row++)
          {
              for (int col = 1; col <= 5; col++)
              {
                  System.out.print("*");
              }
              System.out.println();
          }
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("NestedLoops");
        }
   
        @Test
        public void test1()
        {
            String orig = "public class NestedLoops\n{\n\n   public static void main(String[] args)\n   {\n       for (int row = 1; row <= 3; row++)\n       {\n           for (int col = 1; col <= 5; col++)\n           {\n               System.out.print(\"*\");\n           }\n           System.out.println();\n       }\n   }\n}\n";
   
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
          boolean passed = checkCodeContains("10 rows","row <= 10")
               && checkCodeContains("8 columns","col <= 8");
          assertTrue(passed);
        }
    }