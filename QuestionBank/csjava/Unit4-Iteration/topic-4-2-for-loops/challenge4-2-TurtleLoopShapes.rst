.. activecode:: challenge4-2-TurtleLoopShapes
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit4-Iteration
    :subchapter: topic-4-2-for-loops
    :topics: Unit4-Iteration/topic-4-2-for-loops
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    Use a for-loop to draw a triangle. Then, change it to a pentagon. Then change it to draw any polygon using a variable n that holds the number of sides. Note that the angles in the turns have to add up to 360.
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleDrawShapes
    {
      public static void main(String[] args)
      {
          World world = new World(400,400);
          Turtle yertle = new Turtle(world);
          yertle.penUp();  // move a little to the left
          yertle.moveTo(100,200);
          yertle.penDown();
          yertle.setColor(Color.blue);

          // Add your loop here!
          yertle.forward(100);
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
            super("TurtleDrawShapes");
        }

        @Test
        public void test1()
        {
           String target = "for (int * = *; * ? *; *~)";
           boolean passed = checkCodeContains("for loop", target);
           assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            String forwards = ".forward(";

            int count = countOccurences(code, forwards);

            boolean passed = count == 1;

            passed = getResults("1 forward(...)", "" + count  + " forward(...)", "Should only need forward() once", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            String forwards = ".turn(";

            int count = countOccurences(code, forwards);

            boolean passed = count == 1;

            passed = getResults("1 turn(...)", "" + count  + " turn(...)", "Should only need turn(...) once", passed);
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            String code = getCode();
            String forwards = "int n";

            int count = countOccurences(code, forwards);

            boolean passed = count == 1;

            passed = getResults("true", "" + passed, "Declare int n", passed);
            assertTrue(passed);
        }

        @Test
        public void test5()
        {
            String code = getCode();
            String test = "360/n";

            int count = countOccurences(code.replaceAll(" ",""), test);
            boolean passed = count == 1;

            passed = getResults("true", "" + passed, "Calculates angle correctly using n", passed);
            assertTrue(passed);
        }
    }