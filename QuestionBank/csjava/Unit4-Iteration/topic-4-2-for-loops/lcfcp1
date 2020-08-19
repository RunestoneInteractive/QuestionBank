.. activecode:: lcfcp1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-2-for-loops
   :topics: Unit4-Iteration/topic-4-2-for-loops
   :from_source: F
   :language: java
   :autograde: unittest

   What do you think will happen when you run the code below?  How would it change if you changed line 11 to initialize i's value to 3? Try the Code Lens button to visualize and trace through this code.
   ~~~~
   public class SongTest
   {

      public static void printPopSong()
      {
         String line1 = " bottles of pop on the wall";
         String line2 = " bottles of pop";
         String line3 = "Take one down and pass it around";

         // loop 5 times (5, 4, 3, 2, 1)
         for (int i = 5; i > 0; i--)
         {
            System.out.println(i + line1);
            System.out.println(i + line2);
            System.out.println(line3);
            System.out.println((i - 1) + line1);
            System.out.println();
         }
      }

      public static void main(String[] args)
      {
         SongTest.printPopSong();
      }
   }
   ====
   // Test Code for Lesson 4.1 - popSong
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("SongTest");
        }

        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "3 bottles of pop on the wall";

            String expect1 = expect.split("\n")[0];
            String output1 = output.split("\n")[0];

            boolean passed = output.contains(expect);
            passed = getResults(expect1, output1, "Print the song from 3", passed);
            assertTrue(passed);
        }

        @Test
        public void testMain2() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "5 bottles of pop on the wall";

            boolean passed = !output.contains(expect);

            String expect1 = expect.split("\n")[0];
            String output1 = output.split("\n")[0];

            passed = getResults(expect1, output1, "Do not start loop from 5", passed);
            assertTrue(passed);
        }
    }