.. activecode:: 2DArrayInitGet
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit8-2DArray/topic-8-1-2D-arrays-Day2
  :from_source: T
  :language: java
  :autograde: unittest

  Add another row to seatingInfo initialized to your name and a friend's name. Get these names out of the array using the correct indices and then print them out.
  ~~~~
  public class TwoDArrayInitGet
  {
     public static void main(String[] args)
     {
        String[][] seatingInfo = { {"Jamal", "Maria"},
                                   {"Jake", "Suzy"},
                                   {"Emma", "Luke"} };
        String name = seatingInfo[0][0];
        System.out.println(name + " is at [0,0]");

     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("TwoDArrayInitGet");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expected = "Jamal is at [0,0]";

            boolean passed = output.contains(expected);

            passed = getResults("true", "" + passed, "Output contains " + expected);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String[] lines = output.split("\n");

            String expected = "[3,0]";
            String actual = "";

            boolean passed = false;

            for (String l : lines) {
                if (l.replaceAll(" ", "").contains(expected)) {
                    actual = l;
                    passed = true;
                }
            }

            passed = getResults("Name is at "+ expected, actual, "Add one name to new row and print it out", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String output = getMethodOutput("main");
            String[] lines = output.split("\n");

            String expected = "[3,1]";
            String actual = "";

            boolean passed = false;

            for (String l : lines) {
                if (l.replaceAll(" ", "").contains(expected)) {
                    actual = l;
                    passed = true;
                }
            }

            passed = getResults("Name is at "+ expected, actual, "Add second name to new row and print it out", passed);
            assertTrue(passed);
        }
    }