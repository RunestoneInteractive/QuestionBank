.. activecode:: 2DArrayCreate
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit9-2DArray
  :subchapter: topic-8-1-2D-arrays-Day1
  :topics: Unit9-2DArray/topic-8-1-2D-arrays-Day1
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  What will the following code print out? Can you change ticketInfo to be an array of 5 rows and 10 columns? Can you declare another array called studentNames that has 10 rows and 5 columns? The length property of arrays will be explained in the next lesson.
  ~~~~
  public class TicketInfo
  {
     public static void main(String[] args)
     {
        // declare arrays
        int[][] ticketInfo = new int[2][3];
        System.out.println(ticketInfo.length + " rows");
        System.out.println(ticketInfo[0].length + " columns");
     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("TicketInfo");
        }
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expected = "5 rows\n10 columns";

            boolean passed = output.contains(expected);passed = getResults(expected, output, "Changed ticketInfo to 5 rows and 10 columns", passed);

            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String expected = "studentNames = new String[10][5]";

            boolean passed = checkCodeContains(expected);
            assertTrue(passed);
        }
    }