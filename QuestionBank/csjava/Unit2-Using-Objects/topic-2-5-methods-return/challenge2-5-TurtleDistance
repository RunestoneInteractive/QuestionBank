.. activecode:: challenge2-5-TurtleDistance
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-5-methods-return
    :topics: Unit2-Using-Objects/topic-2-5-methods-return
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    ~~~~
    public class TurtleTestDistance
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);

          // Can you find yertle's distance from the point (0,0)?

          // Can you find the distance between 2 turtles?



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
            super("TurtleTestDistance");
        }

        @Test
        public void test2()
        {
            String code = getCode();
            int num = countOccurences(code, ".getXPos()");

            boolean passed = num > 0;
            getResults(">=1", "" + num, "Calls to getXPos()");
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, ".getYPos()");

            boolean passed = num > 0;
            getResults(">=1", "" + num, "Calls to getYPos()");
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            String code = getCode();
            int num = countOccurences(code, ".getDistance(");

            boolean passed = num >= 2;
            getResults(">=2", "" + num, "Calls to getDistance(...)");
            assertTrue(passed);
        }

        @Test
        public void test1()
        {
            String code = getCode();
            int num = countOccurences(code, ".getDistance(0,0)");

            boolean passed = num >= 1;
            getResults(">=1", "" + num, "Calls getDistance(0,0)");
            assertTrue(passed);
        }
    }