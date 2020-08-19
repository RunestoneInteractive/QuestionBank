.. activecode:: code1_4_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest

   Click on the ``Show CodeLens`` button to step through the code and see how the score value changes.
   ~~~~
   public class UpdateScore
   {
      public static void main(String[] args)
      {
        int score = 0;
        System.out.println(score);
        score = score + 1;
        System.out.println(score);
        score = score + 1;
        System.out.println(score);
      }
   }
   ====
   // Test Code for Lesson 1.4 Expressions - iccv1
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;

    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "0\n1\n2\n";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }