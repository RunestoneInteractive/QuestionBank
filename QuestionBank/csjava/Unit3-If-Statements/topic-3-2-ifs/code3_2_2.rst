.. activecode:: code3_2_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :stdin: true

   This program reads in a boolean value from standard input and tests whether the value is true ``if (passedExam)`` or false ``if (!passedExam)``.
   Use the CodeLens to step through the program.   Change the value in the standard input window to test the program with each possible boolean value.

   ~~~~
   import java.util.Scanner;
   public class TestMidterm
   {
      public static void main(String[] args)
      {
        Scanner scan = new Scanner(System.in);

        System.out.println("Did you pass the midterm exam?");

        boolean passedExam = scan.nextBoolean();
        if (passedExam)
        {
           System.out.println("Good job studying!");
        }
        if (!passedExam)
        {
           System.out.println("Study harder next time.");
        }
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            boolean passed = getResults("true", "true", "main()");
            assertTrue(passed);
        }
    }