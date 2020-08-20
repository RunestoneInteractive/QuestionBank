.. activecode:: listAdd1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-2-arraylist-methods
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.2
   :total_students_attempting: 60
   :num_students_correct: 42.0
   :mean_clicks_to_correct: 1.9523809524

   Run the code below to see how the list changes as each object is added to the end.  Notice that we added the same string to the list more than once.  Lists can hold duplicate objects. Can you add your name to the list and then print out the list?
   ~~~~
   import java.util.*;  // import all classes in this package.
   public class listAdd1
   {
      public static void main(String[] args)
      {
         ArrayList<String> nameList = new ArrayList<String>();
         nameList.add("Diego");
         System.out.println(nameList);
         nameList.add("Grace");
         System.out.println(nameList);
         nameList.add("Diego");
         System.out.println(nameList);
         System.out.println(nameList.size());
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("listAdd1");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[Diego, Grace, Diego, Your name]";
            String searchString = "\\[Diego, Grace, Diego, [A-Za-z0-9 '-,]+\\]";
   
            String[] lines = output.split("\n");
            String longest = lines[0];
            for (int i = 0; i < lines.length; i++) {
                if (lines[i].length() > longest.length())
                    longest = lines[i];
            }
   
            boolean passed = output.matches("[\\s\\S]+" + searchString + "[\\s\\S]*");
   
            passed = getResults(expect, longest, "Add your name to the list", passed);
            assertTrue(passed);
        }
    }