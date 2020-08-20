.. activecode:: turtle-preconditions
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit6-Writing-Classes
    :subchapter: topic-6-3-comments-conditions
    :topics: Unit6-Writing-Classes/topic-6-3-comments-conditions
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    import java.util.*;
    import java.awt.*;

    public class TurtlePreconditions
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          // Change 0,0 to other values outside of 0-300 to break the preconditions and see what happens
          Turtle t = new Turtle(0,0,world);
          t.turnRight();
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
            super("TurtlePreconditions");
        }

        @Test
        public void test1()
        {
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtlePreconditions\n{\n  public static void main(String[] args)\n  {\n      World world = new World(300,300);\n      // Change 0,0 to other values outside of 0-300 to break the preconditions and see what happens\n      Turtle t = new Turtle(0,0,world);\n      t.turnRight();\n      world.show(true);\n  }\n}";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    }