.. activecode:: code_2-1-Turtle2
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

    You can create many objects of a class. In the code below, two turtle objects are created and
    referenced by different variable names: ``yertle`` and ``myrtle``.  Each turtle object
    is automatically given a different color pen for drawing its path.
    Notice each method call to forward, turnLeft and
    turnRight is prefaced with either variable ``yertle`` or variable ``myrtle``, which allows each
    turtle to move and turn independently.
    ~~~~

    public class TurtleTest2
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
            super("TurtleTest2");
        }

        @Test
        public void test1()
        {
            boolean passed = getResults("true", "true", "main()");
            assertTrue(passed);
        }

    }