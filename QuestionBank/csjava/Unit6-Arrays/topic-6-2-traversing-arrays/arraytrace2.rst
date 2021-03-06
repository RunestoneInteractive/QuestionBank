.. activecode:: arraytrace2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest

   What do you think the following code will print out? First trace through it on paper keeping track of the array and the index variable. Then, run it to see if you were right. Try the Code Lens button. Then, try adding your name and a friend's name to the array names and run the code again. Did the code work without changing the loop?
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        String[ ] names = {"Jamal", "Emily", "Destiny", "Mateo", "Sofia"};

        for (int i = 0; i < names.length; i++)
        {
            System.out.println( names[i] );
        }
      }
   }
   ====
   // Test for Lesson 6.2

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Test2");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Jamal\nEmily\nDestiny\nMateo\nSofia";

            boolean passed = output.contains(expect);
            passed = getResults(expect, output, "Did you run the code?", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "Jamal\nEmily\nDestiny\nMateo\nSofia\nYour name\nFriend's name";

            int len = output.split("\n").length;

            boolean passed = len >= 6;

            passed = getResults(expect, output, "Did you add two more names?", passed);
            assertTrue(passed);
        }
    }