.. activecode:: challenge4-4-Turtle-Nested-Loop-Snowflakes
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit4-Iteration
    :subchapter: topic-4-4-nested-loops
    :topics: Unit4-Iteration/topic-4-4-nested-loops
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    Use nested for-loops to have the turtle draw a snowflake of polygons. Use the variable turnAmount to turn after each shape and the variable n for the sides of the polygon.
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleSnowflakes
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
          yertle.setColor(Color.blue);

          // Use this variable in the loops
          int turnAmount = 30;

          // 1. Write a for loop that runs many times
          // 2. Change it to use turnAmount to figure out how many times to run

             // 1 & 2. Write an inner loop that draws a triangle
             // 3. Then change it to be any polygon with a variable n



             // turn turnAmount degrees before drawing the polygon again

             // 4. Add an if statement that changes the colors depending on the loop variables

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
            super("TurtleSnowflakes");
        }

        @Test
        public void test1()
        {
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtleSnowflakes\n{\n  public static void main(String[] args)\n  {\n      World world = new World(300,300);\n      Turtle yertle = new Turtle(world);\n      yertle.setColor(Color.blue);\n\n      // Write a for loop that runs many times\n\n         // Write an inner loop that draws a triangle\n\n\n\n         // turn 30 degrees before drawing triangle again\n\n\n      world.show(true);\n  }\n}\n";

            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }

        @Test
        public void test2() {
            String code = getCode();
            String target = "for (int * = #; * ? *; *~)";

            int num = countOccurencesRegex(code, target);

            boolean passed = num == 2;

            getResults("2", ""+num, "2 For loops (nested)", passed);
            assertTrue(passed);
        }

        @Test
        public void test3() {
             boolean passed = checkCodeContains("if statement to change colors", "if");
              assertTrue(passed);
        }

        @Test
            public void test4()
            {
                String code = getCode();
                String forwards = ".forward(";

                int count = countOccurences(code, forwards);

                boolean passed = count == 1;

                passed = getResults("1 forward(...)", "" + count  + " forward(...)", "Should only need forward() once", passed);
                assertTrue(passed);
            }

            @Test
            public void test5()
            {
                String code = getCode();
                String forwards = ".turn(";

                int count = countOccurences(code, forwards);

                boolean passed = count == 2;

                passed = getResults("2 turn(...)", "" + count  + " turn(...)", "Should only need turn(...) twice", passed);
                assertTrue(passed);
            }


            @Test
            public void test6()
            {
                 boolean passed = checkCodeContains("Calculates number of iterations using turnAmount", "360/turnAmount");
                 assertTrue(passed);
            }
    }