.. activecode:: boolRef
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-1-booleans
   :topics: Unit3-If-Statements/topic-3-1-booleans
   :from_source: F
   :language: java
   :datafile: turtleClasses.jar
   :autograde: unittest

   What will the code below print out? Try to guess before you run it!
   ~~~~
   import java.util.*;
   import java.awt.*;

   public class BoolTestRef
   {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle juan = new Turtle(world);
          Turtle mia = new Turtle(world);

          // Will these print true or false?
          System.out.println(juan == mia);
          Turtle friend = mia; // set friend to be an alias for mia
          System.out.println(friend == mia);
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("BoolTestRef");
        }

        @Test
        public void test1()
        {
           boolean passed = getResults("true", "true", "main()");
            assertTrue(passed);
        }
    }