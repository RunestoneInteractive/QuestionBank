.. activecode:: TurtleConstructorTest
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
    :pct_on_first: 0.6256410256
    :total_students_attempting: 195
    :num_students_correct: 179.0
    :mean_clicks_to_correct: 1.3631284916

    Try changing the code below to create a ``World`` object with 300x400 pixels. Where is the turtle placed by default? What parameters do you need to pass to the ``Turtle`` constructor to put the turtle at the top right corner? Experiment and find out. What happens if you mix up the order of the parameters?
    
    (If the code below does not work in your browser, you can also use the ``Turtle`` code at this |repl link| (refresh page after forking and if it gets stuck) or download the files |github| to use in your own IDE.)
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleConstructorTest
    {
      public static void main(String[] args)
      {
          // Change the World constructor to 300x400
          World world1 = new World(300,300);
    
          // Change the Turtle constructor to put the turtle in the top right corner
          Turtle t1 = new Turtle(world1);
    
          t1.turnLeft();
          world1.show(true);
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
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtleConstructorTest\n{\n  public static void main(String[] args)\n  {\n      // Change the World constructor to 300x400\n      World world1 = new World(300,300);\n\n      // Change the Turtle constructor to put the turtle in the top right corner\n      Turtle t1 = new Turtle(world1);\n\n      t1.turnLeft();\n      world1.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    
    }