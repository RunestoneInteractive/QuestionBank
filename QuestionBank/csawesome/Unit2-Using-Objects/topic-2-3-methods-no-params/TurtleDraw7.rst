.. activecode:: TurtleDraw7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-3-methods-no-params
    :topics: Unit2-Using-Objects/topic-2-3-methods-no-params
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar
    :pct_on_first: 0.6474820144
    :total_students_attempting: 139
    :num_students_correct: 120.0
    :mean_clicks_to_correct: 1.525

    import java.util.*;
    import java.awt.*;
    
    public class TurtleDraw7
    {
      public static void main(String[] args)
      {
          World habitat = new World(300,300);
          Turtle yertle = new Turtle(habitat);
          // Make yertle draw a 7 using the code above
    
    
    
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
            super("TurtleDraw7");
        }
    
        @Test
        public void test1()
        {
            String orig = "yertle.forward();\nyertle.turnLeft();\nyertle.forward();";
            boolean passed = checkCodeContains(orig);
            assertTrue(passed);
        }
    }