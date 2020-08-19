.. activecode:: TurtleTest2
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
    :pct_on_first: 0.5245202559
    :total_students_attempting: 469
    :num_students_correct: 442.0
    :mean_clicks_to_correct: 1.6063348416

    In the code below, ``yertle`` goes forward and then turns left. Can you change the code to make ``yertle`` go ``forward`` twice and then ``turnRight``?
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleTest2
    {
      public static void main(String[] args)
      {
          World habitat = new World(300,300);
          Turtle yertle = new Turtle(habitat);
    
          yertle.forward();
          yertle.turnLeft();
    
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
            super("TurtleTest2");
        }
    
        @Test
        public void test1()
        {
            String code = getCode();
            String expect = "yertle.forward";
    
            int count = countOccurences(code, expect);
    
            boolean passed = getResults("2 time(s)", "" + count  + " time(s)", "yertle.forward() twice");
            assertTrue(passed);
        }
    
        @Test
        public void test2()
        {
            String code = getCode();
            String expect = "yertle.turnRight()";
    
            int count = countOccurences(code, expect);
    
            boolean passed = count >= 1;
            passed = getResults("1+ time(s)", "" + count + " time(s)", "yertle.turnRight()", passed);
            assertTrue(passed);
        }
    }