.. activecode:: lcab2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest

   Try running the code below to see the length. Try adding another value to the highScores initializer list and run again to see the length value change.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        int[ ] highScores = {99,98,98,88,68};
        System.out.println(highScores.length);
      }
   }
   ====
   // Test for Lesson 6.1.2 - While Loop FindAndReplace lclw1
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Test2");
        }

        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main").trim();
            String expect = "6";

            //boolean pass = !output.equals(expect.trim());

            boolean passed = getResults(expect, output, "Did you add another value?");
            assertTrue(passed);
        }

        @Test
        public void testChangedCode() {
            String origCode = "public class Test2 { public static void main (String [] args) { int [] highScores = {99,98,98,88,68}; System.out.println(highScores.length); } }";

            boolean changed = codeChanged(origCode);

            assertTrue(changed);

        }
    }