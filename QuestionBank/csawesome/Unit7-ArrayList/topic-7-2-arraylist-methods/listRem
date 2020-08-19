.. activecode:: listRem
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-2-arraylist-methods
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 24
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 1.0

   What will the following code print out? Try to guess before you run it. Were you surprised? Read the note below.
   ~~~~
   import java.util.*;  // import all classes in this package.
   public class listRem
   {
      public static void main(String[] arts)
      {
         ArrayList<Integer> list1 = new ArrayList<Integer>();
         list1.add(1);
         list1.add(2);
         list1.add(3);
         System.out.println(list1);
         list1.remove(1);
         System.out.println(list1);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("listRem");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[1, 2, 3]\n[1, 3]";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }