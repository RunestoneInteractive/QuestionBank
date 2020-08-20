.. activecode:: code4_2_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit4-Iteration
    :subchapter: topic-4-2-for-loops
    :topics: Unit4-Iteration/topic-4-2-for-loops
    :from_source: T
    :language: java
    :autograde: unittest
    :nocodelens:
    :datafile: turtleClasses.jar

    Can you change the code below to remove the repeated lines of code and use a loop to draw 4 sides of the square?
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleDrawSquare
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);

          // Change the following code to use a for loop to draw the square
          yertle.forward();
          yertle.turn(90);
          yertle.forward();
          yertle.turn(90);
          yertle.forward();
          yertle.turn(90);
          yertle.forward();
          yertle.turn(90);

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
            super("TurtleDrawSquare");
        }

        @Test
        public void test1()
        {
           String target = "for (int * = #; * ? #; *~)";
           boolean passed = checkCodeContains("for loop", target);
           assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            String forwards = ".forward()";

            int count = countOccurences(code, forwards);

            boolean passed = count == 1;

            passed = getResults("1 forward()", "" + count  + " forward()", "Should only need forward() once", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            String forwards = ".turn(90)";

            int count = countOccurences(code, forwards);

            boolean passed = count == 1;

            passed = getResults("1 turn(90)", "" + count  + " turn(90)", "Should only need turn(90) once", passed);
            assertTrue(passed);
        }
    }