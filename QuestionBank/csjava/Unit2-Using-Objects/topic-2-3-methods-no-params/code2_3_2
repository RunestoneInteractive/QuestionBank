.. activecode:: code2_3_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-3-methods-no-params
    :topics: Unit2-Using-Objects/topic-2-3-methods-no-params
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar


    ~~~~

    public class Turtle2Letters
    {
      public static void main(String[] args)
      {
          World world = new World(400,400);



          world.show(true);
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Turtle2Letters");
        }

        @Test
        public void test1()
        {
            String code = getCode();
            String expect = "new Turtle(";

            int count = countOccurences(code, expect);

            boolean passed = count >= 2;
            passed = getResults("2+ Turtles", "" + count  + " Turtles", "Add two Turtles", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            String[] lines = code.split("\n");

            boolean passed = lines.length >= 20;
            passed = getResults("20 or more lines", lines.length + " lines", "Adding a reasonable amount of lines to code", passed);
            assertTrue(passed);
        }
    }