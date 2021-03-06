.. activecode:: TurtleTestMethods1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-4-methods-with-params
    :topics: Unit2-Using-Objects/topic-2-4-methods-with-params
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar
    :pct_on_first: 0.0583333333
    :total_students_attempting: 120
    :num_students_correct: 67.0
    :mean_clicks_to_correct: 3.6865671642

    1. Can you make yertle draw a square and change the pen color for each side of the square? Try something like: yertle.setColor(Color.red); This uses the |Color| class in Java which has some colors predefined like red, yellow, blue, magenta, cyan. You can also use more specific methods like setPenColor, setBodyColor, and setShellColor.
    2. Can you draw a triangle? The turnRight() method always does 90 degree turns, but you'll need 60 degree angles for a equilateral triangle. Use the turn method which has a parameter for the angle of the turn in degrees. For example, turn(90) is the same as turnRight(). Try drawing a triangle with different colors.
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleTestMethods1
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
    
          yertle.forward(100);
          yertle.turnLeft();
          yertle.forward(75);
    
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
            super("TurtleTestMethods1");
        }
    
        @Test
        public void test1()
        {
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtleTestMethods1\n{\n  public static void main(String[] args)\n  {\n      World world = new World(300,300);\n      Turtle yertle = new Turtle(world);\n\n      yertle.forward(100);\n      yertle.turnLeft();\n      yertle.forward(75);\n\n      world.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    
        @Test
        public void test2()
        {
            String code = getCode();
            int numColors = countOccurences(code, "Color(");
    
            boolean passed = numColors >= 4;
            passed = getResults("4 or more", ""+numColors, "Changing color at least 4 times", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test3()
        {
            String code = getCode();
            int numTurns = countOccurences(code, ".turn");
    
            boolean passed = numTurns >= 4;
            passed = getResults("4 or more", ""+numTurns, "Number of turns", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test4()
        {
            String code = getCode();
            int numTurns = countOccurences(code, ".turn(");
    
            boolean passed = numTurns >= 1;
            passed = getResults("1 or more", ""+numTurns, "Calls to turn(...)", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test5()
        {
            String code = getCode();
            int numForward = countOccurences(code, ".forward(");
    
            boolean passed = numForward >= 4;
            passed = getResults("4 or more", ""+numForward, "Calls to forward()", passed);
            assertTrue(passed);
        }
    }