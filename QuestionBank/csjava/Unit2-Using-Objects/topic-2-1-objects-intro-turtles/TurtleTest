.. activecode:: TurtleTest
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

    Try clicking the |runbutton| button below to see what the following program does.
    (If the code below does not work for you, you can also see the ``Turtle`` code in action at this |repl link| (refresh page after forking and if it gets stuck) or download the files |github| to use in your own IDE.)
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleTest
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);

          yertle.forward();
          yertle.turnLeft();
          yertle.forward();

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
            super("TurtleTest");
        }

        @Test
        public void test1()
        {
            boolean passed = getResults("true", "true", "main()");
            assertTrue(passed);
        }
    }