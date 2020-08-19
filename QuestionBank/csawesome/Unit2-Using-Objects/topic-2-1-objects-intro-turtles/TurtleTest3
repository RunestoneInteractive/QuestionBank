.. activecode:: TurtleTest3
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
    :pct_on_first: 0.6061269147
    :total_students_attempting: 457
    :num_students_correct: 417.0
    :mean_clicks_to_correct: 1.4100719424

    Can you add another turtle object to the code below?
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleTest3
    {
      public static void main(String[] args)
      {
          World habitat = new World(300,300);
          Turtle yertle = new Turtle(habitat);
          Turtle myrtle = new Turtle(habitat);
    
          yertle.forward();
          yertle.turnLeft();
          yertle.forward();
    
          myrtle.turnRight();
          myrtle.forward();
    
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
            super("TurtleTest3");
        }
    
        @Test
        public void test1()
        {
            String code = getCode();
            String expect = "new Turtle(habitat)";
    
            int count = countOccurences(code, expect);
    
            boolean passed = count >= 3;
            passed = getResults("3+ Turtles", "" + count  + " Turtles", "Add a new Turtle(s)", passed);
            assertTrue(passed);
        }
    }