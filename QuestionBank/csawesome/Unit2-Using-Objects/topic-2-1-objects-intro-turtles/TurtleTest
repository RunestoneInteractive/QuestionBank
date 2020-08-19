.. activecode:: TurtleTest
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-1-objects-intro-turtles
    :topics: Unit2-Using-Objects/topic-2-1-objects-intro-turtles
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar
    :pct_on_first: 0.9964912281
    :total_students_attempting: 570
    :num_students_correct: 570.0
    :mean_clicks_to_correct: 1.0035087719

    Try clicking the run button below to see what the following program does.
    (If the code below does not work or is too slow in your browser, you can also see the ``Turtle`` code in action at this |repl link| (refresh page after forking and if it gets stuck) or download the files |github| to use in your own IDE.)
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleTest
    {
      public static void main(String[] args)
      {
          World habitat = new World(300,300);
          Turtle yertle = new Turtle(habitat);
    
          yertle.forward();
          yertle.turnLeft();
          yertle.forward();
    
          habitat.show(true);
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