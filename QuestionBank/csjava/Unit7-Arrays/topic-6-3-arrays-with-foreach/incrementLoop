.. activecode:: incrementLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit7-Arrays/topic-6-3-arrays-with-foreach
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T

   The for-each loop below cannot change the values in the array because only the loop variable value will change. Run it with the CodeLens button to see why this is. Then, change the loop to an indexed for loop to make it change the array values.
   ~~~~
   public class IncrementLoop
   {
      public static void main(String[] args)
      {
        int[ ] values = {6, 2, 1, 7, 12, 5};
        // Can this loop increment the values?
        for (int val : values)
        {
          val++;
          System.out.println("New val: " + val);
        }
        // Print out array to see if they really changed
        System.out.println("Array after the loop: ");
        for (int v : values)
        {
          System.out.print(v + " ");
        }
      }
   }
   ====
   // Test for Lesson 6.3.3 - IncrementLoop

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("IncrementLoop");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "New val: 7\nNew val: 3\nNew val: 2\nNew val: 8\nNew val: 13\nNew val: 6\nArray after the loop:\n7 3 2 8 13 6";

            boolean passed = getResults(expect, output, "main()");
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String target = "for (int * = #; * ? *.length; *~)";
            boolean passed = checkCodeContains("for loop", target);
            assertTrue(passed);

        }
    }