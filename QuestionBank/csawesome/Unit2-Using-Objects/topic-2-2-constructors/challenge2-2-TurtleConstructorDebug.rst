.. activecode:: challenge2-2-TurtleConstructorDebug
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-2-constructors
    :topics: Unit2-Using-Objects/topic-2-2-constructors
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar
    :pct_on_first: 1.0
    :total_students_attempting: 141
    :num_students_correct: 141.0
    :mean_clicks_to_correct: 1.0

    Debug the following code.
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleConstructorDebug
    {
      public static void main(String[] args)
      {
          World w = new World(300,0);
          turtle t0;
          Turtle t1 = new Turtle();
          Turtle t2 = new Turtle(world, 100, 50)
          t0.forward();
          t1.turnRight();
          t2.turnLeft();
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
            super("TurtleConstructorDebug");
        }
    
        @Test
        public void test1()
        {
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtleConstructorDebug\n{\n  public static void main(String[] args)\n  {\n      World w = new World(300,0);\n      turtle t0;\n      Turtle t1 = new Turtle();\n      Turtle t2 = new Turtle(world, 100, 50)\n      t0.forward();\n      t1.turnRight();\n      t2.turnLeft();\n      world.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    }