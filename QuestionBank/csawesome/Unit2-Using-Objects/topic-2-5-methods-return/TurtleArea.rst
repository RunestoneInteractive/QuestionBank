.. activecode:: TurtleArea
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-5-methods-return
    :topics: Unit2-Using-Objects/topic-2-5-methods-return
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar
    :pct_on_first: 0.7227722772
    :total_students_attempting: 101
    :num_students_correct: 95.0
    :mean_clicks_to_correct: 1.3052631579

    Fix the errors in the code below so that it prints out the area of the space that the turtle occupies by multiplying its width and height. Remember that you have to do something with the values that the get methods return.
    ~~~~
    import java.util.*;
    import java.awt.*;
    import java.lang.Math;
    
    public class TurtleArea
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
    
          int area;
          yertle.getWidth() * getHeight;
          System.out.println("Yertle's area is: ");
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("TurtleArea");
        }
    
        @Test
        public void test1()
        {
            String actual = getMethodOutput("main");
            String expected = "Yertle's area is: 270";
            boolean passed = getResults(expected, actual, "Prints correct answer");
            assertTrue(passed);
        }
         @Test
        public void test2() {
            String code = getCode();
            String target = ".getHeight()";
    
            int num = countOccurences(code, target);
    
            boolean passed = num >= 1;
    
            getResults("1+", "" + num, "Calls to " + target, passed);
            assertTrue(passed);
        }
    
        @Test
        public void test3() {
            String code = getCode();
            String target = ".getWidth()";
    
            int num = countOccurences(code, target);
    
            boolean passed = num >= 1;
    
            getResults("1+", "" + num, "Calls to " + target, passed);
            assertTrue(passed);
        }
    }