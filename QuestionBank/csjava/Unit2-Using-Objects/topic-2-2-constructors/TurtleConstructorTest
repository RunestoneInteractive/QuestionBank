.. activecode:: TurtleConstructorTest
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-2-constructors
    :topics: Unit2-Using-Objects/topic-2-2-constructors
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    Try changing the code below to create a ``World`` object with 300x400 pixels.
    Where is the turtle placed by default? What parameters do you need to
    pass to the ``Turtle`` constructor to put the turtle near the top right corner? Recall that (0,0) is
    the top left corner and y increases as you go down the window. Experiment with different initial locations for the turtle. What happens if you mix up the order of the parameters?

    (If the code below does not work in your browser, you can also copy the code into
    this |repl link| (refresh page after forking if it gets stuck) or download the files |github| to use
    in your own IDE.)
    ~~~~

    public class TurtleConstructorTest
    {
      public static void main(String[] args)
      {
          // Change the World constructor to 300x400
          World world = new World(300,300);

          // Change the Turtle constructor to put the turtle in the top right corner
          Turtle t1 = new Turtle(world);

          t1.turnLeft();
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
            super("TurtleConstructorTest");
        }

        @Test
        public void test1()
        {
            String orig = "public class TurtleConstructorTest\n{\n  public static void main(String[] args)\n  {\n      // Change the World constructor to 300x400\n      World world = new World(300,300);\n\n      // Change the Turtle constructor to put the turtle in the top right corner\n      Turtle t1 = new Turtle(world);\n\n      t1.turnLeft();\n      world.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }

    }