.. activecode:: code2_5_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-5-methods-return
    :topics: Unit2-Using-Objects/topic-2-5-methods-return
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: turtleClasses.jar

    Try the code below that changes the turtle's width and height. How big or small can you make yertle?

    (If the code below does not work in your browser, you can also copy in the code below into the Turtle code at this |repl link| (refresh page after forking and if it gets stuck) or download the files |github| to use in your own IDE.)
    ~~~~
    public class TurtleTestGetSet
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
          System.out.println("Yertle's original width is: " + yertle.getWidth());
          System.out.println("Yertle's original height is: " + yertle.getHeight());
          yertle.setWidth(200);
          yertle.setHeight(200);
          System.out.println("Yertle's new width is: " + yertle.getWidth());
          System.out.println("Yertle's new height is: " + yertle.getHeight());
          yertle.turnRight();
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
            super("TurtleTestGetSet");
        }

        @Test
        public void test1()
        {
            String orig = "public class TurtleTestGetSet\n{\n  public static void main(String[] args)\n  {\n      World world = new World(300,300);\n      Turtle yertle = new Turtle(world);\n      System.out.println(\"Yertle's width is: \" + yertle.getWidth());\n      yertle.setWidth(200);\n      yertle.setHeight(200);\n      System.out.println(\"Yertle's width is: \" + yertle.getWidth());\n      yertle.turnRight();\n      world.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    }