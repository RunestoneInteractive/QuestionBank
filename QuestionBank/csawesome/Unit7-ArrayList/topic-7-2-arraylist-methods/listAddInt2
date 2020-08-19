.. activecode:: listAddInt2
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
   :total_students_attempting: 23
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 1.0

   What will the code below print out? Try figuring it out before running it. Remember that ArrayLists start at index 0 and that the add(index,obj) always has the index as the first argument.
   ~~~~
   import java.util.*;  // import all classes in this package.
   public class listAddInt2
   {
      public static void main(String[] arts)
      {
         ArrayList<Integer> list1 = new ArrayList<Integer>();
         list1.add(1);
         System.out.println(list1);
         // adds the number 2 to the end of the list
         list1.add(2);
         System.out.println(list1);
         // This will add the number 3 at index 1
         list1.add(1, 3);
         System.out.println(list1);
         // This will add the number 4 at index 1
         list1.add(1, 4);
         System.out.println(list1);
         System.out.println(list1.size());
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("listAddInt2");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[1]\n[1, 2]\n[1, 3, 2]\n[1, 4, 3, 2]\n4\n";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }