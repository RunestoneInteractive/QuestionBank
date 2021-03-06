.. activecode:: challenge2-4-TurtleHouse
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-4-methods-with-params
    :topics: Unit2-Using-Objects/topic-2-4-methods-with-params
    :from_source: F
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    public class TurtleHouse
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);



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
            super("TurtleHouse");
        }

        @Test
        public void test1()
        {
            String orig = "public class TurtleHouse\n{\n  public static void main(String[] args)\n  {\n      World world = new World(300,300);\n\n\n\n      world.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            int num = countOccurences(code, "moveTo(");

            boolean passed = num >= 1;
            passed = getResults("1 or more", ""+num, "Calls moveTo(...)", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, ".penUp()");

            boolean passed = num >= 1;
            passed = getResults("4 or more", ""+num, "Calls penUp()", passed);
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            String code = getCode();
            int num = countOccurences(code, ".penDown(");

            boolean passed = num >= 1;
            passed = getResults("1 or more", ""+num, "Calls penDown()", passed);
            assertTrue(passed);
        }
        @Test
        public void test5()
        {
            String code = getCode();
            int numTurns = countOccurences(code, ".turn");

            boolean passed = numTurns >= 6;
            passed = getResults("6 or more", ""+numTurns, "turns", passed);
            assertTrue(passed);
        }

        @Test
        public void test6()
        {
            String code = getCode();
            int numForward = countOccurences(code, ".forward(");

            boolean passed = numForward >= 6;
            passed = getResults("6 or more", ""+numForward, "Calls to forward()", passed);
            assertTrue(passed);
        }
    }