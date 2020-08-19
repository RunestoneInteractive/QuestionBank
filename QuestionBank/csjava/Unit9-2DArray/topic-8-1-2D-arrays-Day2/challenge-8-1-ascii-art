.. activecode:: challenge-8-1-ascii-art
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit9-2DArray
  :subchapter: topic-8-1-2D-arrays-Day2
  :topics: Unit9-2DArray/topic-8-1-2D-arrays-Day2
  :from_source: F
  :language: java
  :autograde: unittest

  Part 1: Add 2 assignment statements for the 2D array asciiArt to change the "o" characters to "@" characters. Part 2: Create a new asciiArt array and print it out.
  ~~~~
  public class AsciiArt
  {
     public static void main(String[] args)
     {

        String[][] asciiArt = {
              {" ", " ", "_", "_", "_", " ", " "},
              {" ", "(", "o", " ", "o", ")", " "},
              {"(", " ", " ", "V", " ", " ", ")"},
              {" ", "-", "m", "-", "m", "-", " "},
         };

        //Part 1: Add 2 assignment statements to change "o" to "@"


        // print the asciiArt for Part 1
        System.out.println("ASCII Art:");
        for(String[] row : asciiArt) {
          for(String column : row)
            System.out.print(column);
          System.out.println();
        }

        //Part 2: Create your own ASCII art array and print it out!


     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("AsciiArt");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "___  \n (@ @) \n(  V  )\n -m-m-";

            boolean passed = output.replaceAll(" ", "").contains(expect.replaceAll(" ", ""));
            passed = getResults(expect, output, "changed o to @", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "___  \n (@ @) \n(  V  )\n -m-m-";

            if (output.contains("-m-m-")) {
                int i = output.indexOf("-m-m-") + "-m-m-".length();
                output = output.substring(i);
            }

            String[] lines = output.split("\n");

            boolean passed = output.length() >= 10 && lines.length >= 3;

            passed = getResults("Your art", output, "added your own ascii art (should be at least 3 x 3)", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String expect = "asciiArt[#][#] = \"@\"";

            boolean passed = checkCodeContains(expect);
            assertTrue(passed);
        }
    }