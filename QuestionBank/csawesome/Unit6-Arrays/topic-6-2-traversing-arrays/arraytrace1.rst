.. activecode:: arraytrace1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 238
   :num_students_correct: 238.0
   :mean_clicks_to_correct: 1.0

   What do you think the following code will print out? First trace through it on paper keeping track of the array and the index variable. Then, run it to see if you were right. You can also follow it in the |visualizer2| by clicking on the Show Code Lens button.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        String[ ] names = {"Jamal", "Emily", "Destiny", "Mateo", "Sofia"};
   
        int index = 1;
        System.out.println(names[index - 1]);
        index++;
        System.out.println(names[index]);
        System.out.println(names[index/2]);
        names[index] = "Rafi";
        index--;
        System.out.println(names[index+1]);
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
            super("Test1");
        }
   
        @Test
        public void test1() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Jamal\nDestiny\nEmily\nRafi";
   
            boolean passed = getResults(expect, output, "Did you run the code?", true);
            assertTrue(passed);
        }
    }