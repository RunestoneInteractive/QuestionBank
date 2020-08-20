.. activecode:: TurtleTestMethodsReturn2
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

    Try some of the get methods and the toString() method in the program below. Note that you have to print out what the get methods return in order to see what they do!
    ~~~~
    public class TurtleTestMethods2
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);

          // Try some get methods here!



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
            super("TurtleTestMethods2");
        }

        @Test
        public void test1()
        {
            String code = getCode();
            int num = countOccurences(code, "getWidth()");

            boolean passed = num > 0;
            getResults(">=1", "" + num, "Calls to getWidth()");
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            int num = countOccurences(code, "getHeight()");

            boolean passed = num > 0;
            getResults(">=1", "" + num, "Calls to getHeight()");
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, "toString()") + countOccurences(code, "System.out.println(yertle)");

            boolean passed = num > 0;
            getResults(">=1", "" + num, "Calls to toString()");
            assertTrue(passed);
        }
    }