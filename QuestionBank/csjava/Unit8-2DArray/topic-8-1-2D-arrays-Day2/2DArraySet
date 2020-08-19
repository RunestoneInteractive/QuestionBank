.. activecode:: 2DArraySet
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit8-2DArray/topic-8-1-2D-arrays-Day2
  :from_source: T
  :language: java
  :autograde: unittest

  Add another row of data to the arrays by changing the size of the arrays and adding in the assignment statements for the cells in those rows. Use the CodeLens button to see the contents of the array.
  ~~~~
  public class TwoDArraySet
  {
     public static void main(String[] args)
     {
        // declare arrays
        int[][] ticketInfo;
        String[][] seatingChart;

        // create arrays
        ticketInfo = new int [2][3];
        seatingChart =  new String [3][2];

        // initialize the array elements
        ticketInfo[0][0] = 15;
        ticketInfo[0][1] = 10;
        ticketInfo[0][2] = 15;
        ticketInfo[1][0] = 25;
        ticketInfo[1][1] = 20;
        ticketInfo[1][2] = 25;
        seatingChart[0][0] = "Jamal";
        seatingChart[0][1] = "Maria";
        seatingChart[1][0] = "Jacob";
        seatingChart[1][1] = "Suzy";
        seatingChart[2][0] = "Emma";
        seatingChart[2][1] = "Luke";

        // print the contents
        System.out.println(ticketInfo);
        System.out.println(seatingChart);
     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("TwoDArraySet");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expected = "[[I@", expected2 = "[[Ljava.lang.String;@";

            boolean passed = output.contains(expected) && output.contains(expected2);

            passed = getResults("true", ""+passed, "Prints two 2D arrays");
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            String expected = "new String [4][2]";

            boolean passed = code.contains(expected);

            passed = getResults("true", ""+passed, "Add another row to seatingChart");
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            String expected1 = "seatingChart[3][0]";
            String expected2 = "seatingChart[3][1]";

            boolean passed = code.contains(expected1) && code.contains(expected2);

            passed = getResults("true", ""+passed, "Give values to new elements");
            assertTrue(passed);
        }
    }