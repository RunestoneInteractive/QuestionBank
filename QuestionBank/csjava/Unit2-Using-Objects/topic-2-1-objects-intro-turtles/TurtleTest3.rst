.. activecode:: TurtleTest3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-1-objects-intro-turtles
    :topics: Unit2-Using-Objects/topic-2-1-objects-intro-turtles
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    Can you add another turtle object to the code below?
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleTest3
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
          Turtle myrtle = new Turtle(world);

          yertle.forward();
          yertle.turnLeft();
          yertle.forward();

          myrtle.turnRight();
          myrtle.forward();

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
            super("TurtleTest3");
        }

        @Test
        public void test1()
        {
            String code = getCode();
            String expect = "new Turtle(world)";

            int count = countOccurences(code, expect);

            boolean passed = count >= 3;
            passed = getResults("3+ Turtles", "" + count  + " Turtles", "Add a new Turtle(s)", passed);
            assertTrue(passed);
        }
    }