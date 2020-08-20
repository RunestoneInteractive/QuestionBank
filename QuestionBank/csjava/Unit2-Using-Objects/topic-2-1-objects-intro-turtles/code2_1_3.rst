.. activecode:: code2_1_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-1-objects-intro-turtles
    :topics: Unit2-Using-Objects/topic-2-1-objects-intro-turtles
    :from_source: T
    :language: java
    :autograde: unittest
    :nocodelens:
    :datafile: turtleClasses.jar

    public class TurtleChallenge
    {
      public static void main(String[] args)
      {
          World world = new World(500,500);
          // 1. Create a Turtle object in the world

          // 2. Have the turtle draw a small square

          // 3. Have the turtle draw a large square

          // 4. Play around!



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
            super("TurtleChallenge");
        }

        @Test
        public void test1()
        {
            String code = getCode();
            String expect = "new Turtle(world)";

            int count = countOccurences(code, expect);

            boolean passed = count >= 1;

            passed = getResults("1+ Turtle(s)", "" + count  + " Turtle(s)", "At least 1 Turtle", passed);
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

    }