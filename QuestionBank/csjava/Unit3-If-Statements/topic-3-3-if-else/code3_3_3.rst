.. activecode:: code3_3_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :stdin: true

   Rewrite this code to use a single if-else rather than two separate if statements.

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
       public void testCodeContains() throws IOException
       {
           String target = "else";
           boolean passed = checkCodeContains("check else", target);
           assertTrue(passed);
       }
    }