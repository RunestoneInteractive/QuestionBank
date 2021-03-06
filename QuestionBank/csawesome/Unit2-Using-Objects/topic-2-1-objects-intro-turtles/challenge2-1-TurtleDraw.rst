.. activecode:: challenge2-1-TurtleDraw
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
    :pct_on_first: 0.1126436782
    :total_students_attempting: 435
    :num_students_correct: 297.0
    :mean_clicks_to_correct: 3.7609427609

    Create a Turtle object and have it draw a shape, for example a small square and then a larger square (by calling the forward method multiple times).
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleTest
    {
      public static void main(String[] args)
      {
          World habitat = new World(500,500);
          // 1. Create a Turtle object in the habitat
    
          // 2. Have the turtle draw a small square
    
          // 3. Have the turtle draw a large square
    
          // 4. Play around!
    
    
    
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
            String code = getCode();
            String expect = "new Turtle(habitat)";
    
            int count = countOccurences(code, expect);
    
            boolean passed = count >= 1;
    
            passed = getResults("1+ Turtle(s)", "" + count  + " Turtle(s)", "At least 1 Turtle in habitat", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test2()
        {
            String code = getCode();
            String right = ".turnRight()";
            String left  = ".turnLeft()";
    
            int countR = countOccurences(code, right);
            int countL = countOccurences(code, left);
            int count = countR + countL;
    
            boolean passed = countR >= 8 || countL >= 8 || (countL >= 4 && countR >= 4);
    
            passed = getResults("8+ turns", "" + count  + " turns(s)", "two squares (8 right or left turns total)", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test3()
        {
            String code = getCode();
            String forwards = ".forward";
            String backwards = ".backward";
    
            int forward = countOccurences(code, forwards);
            int backward = countOccurences(code, backwards);
            int moves = forward + backward;
    
            boolean passed = forward >= 8 || backward >= 8 || (backward >= 4 && forward >= 4);
    
            passed = getResults("8+ moves", "" + moves  + " move(s)", "two squares (8 moves total)", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test4() {
            String[] code = getCode().split("\n");
            int expect = 38;
    
            boolean passed = code.length >= expect;
    
            passed = getResults(expect + "+ line(s)", "" + code.length  + " lines(s)", "More than " + expect + " lines of code", passed);
            assertTrue(passed);
        }
    }