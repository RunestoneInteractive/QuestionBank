.. activecode:: challenge2-3-Turtle_Letter
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
    :pct_on_first: 0.5625
    :total_students_attempting: 112
    :num_students_correct: 90.0
    :mean_clicks_to_correct: 1.5222222222

    Create a drawing of a simple letter or number that uses just straight lines (no curves or diagonals). It could be an initial in your name or a number from today's date.
    ~~~~
    import java.util.*;
    import java.awt.*;
    
    public class TurtleLetter
    {
      public static void main(String[] args)
      {
          World habitat = new World(300,300);
    
    
    
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
            super("TurtleLetter");
        }
    
        @Test
        public void test1()
        {
            String orig = "import java.util.*;\nimport java.awt.*;\n\npublic class TurtleLetter\n{\n  public static void main(String[] args)\n  {\n      World habitat = new World(300,300);\n\n\n\n      habitat.show(true);\n  }\n}\n";
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
    
        @Test
        public void test2()
        {
            String code = getCode();
            String[] lines = code.split("\n");
    
            boolean passed = lines.length >= 20;
            passed = getResults("20 or more lines", lines.length + " lines", "Adding a reasonable amount of lines to code", passed);
            assertTrue(passed);
        }
    }