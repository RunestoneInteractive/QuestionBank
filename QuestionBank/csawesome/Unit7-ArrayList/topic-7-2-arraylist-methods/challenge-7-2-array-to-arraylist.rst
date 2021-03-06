.. activecode:: challenge-7-2-array-to-arraylist
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-2-arraylist-methods
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5263157895
   :total_students_attempting: 19
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 1.6428571429

   Rewrite the following code that uses an array to use an ArrayList instead. In the comments write why you think an ArrayList is a better data structure to use than an array for this problem.
   ~~~~
   import java.util.*;
   
   public class ToDoList
   {
      public static void main(String[] args)
      {
         // Rewrite this code to use an ArrayList instead of an array
         String[] toDoList = new String[3];
         toDoList[0] = "Do homework";
         toDoList[1] = "Help make dinner";
         toDoList[2] = "Call grandma";
   
         // changing element 1
         toDoList[1] = "Order pizza";
   
         System.out.println(toDoList.length + " things to do!");
         System.out.println("Here's the first thing to do: "
              + toDoList[0] );
   
         // remove item 0 and move everything down
         //  (this can be done in 1 command with ArrayList)
         toDoList[0] = toDoList[1];
         toDoList[1] = toDoList[2];
         toDoList[2] = "";
   
         System.out.println("Here's the next thing to do: "
              + toDoList[0] );
   
         // Why is an ArrayList better than an array for a toDoList?
         // Answer:
      }
   }
   ====
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ToDoList");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "3 things to do!\nHere's the first thing to do: Do homework\nHere's the next thing to do: Order pizza";
   
            boolean passed = getResults(expect, output, "Output is the same");
            assertTrue(passed);
        }
   
   
        @Test
        public void test2()
        {
            String output = removeSpaces(getCode());
            String expect = "ArrayList<String>";
   
            boolean passed = output.contains(expect);
   
            passed = getResults("true", "" + passed, "Declare ArrayList", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            String expect = "[*]";
   
            boolean passed = checkCodeNotContains(expect);
            assertTrue(passed);
        }
    }