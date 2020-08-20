.. activecode:: listGetSet
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-2-arraylist-methods
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 55
   :num_students_correct: 19.0
   :mean_clicks_to_correct: 3.2105263158

   Try to guess what the code below will print before running it. Can you get the last element in the nameList to print it out? Can you set the first element in the list to your name and print out the list?
   ~~~~
   import java.util.*;  // import all classes in this package.
   public class listGetSet
   {
      public static void main(String[] args)
      {
         ArrayList<String> nameList = new ArrayList<String>();
         nameList.add("Diego");
         nameList.add("Grace");
         nameList.add("Deja");
         System.out.println(nameList);
         System.out.println(nameList.get(0));
         System.out.println(nameList.get(1));
         nameList.set(1, "John");
         System.out.println(nameList);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("listGetSet");
        }
   
        @Test
        public void test1()
        {
            boolean passed = checkCodeContainsRegex("nameList.set(0, \"Your name\")", "nameList.set(0, ");
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String searchString = "Deja";
   
            boolean passed = output.contains("\n" + searchString + "\n") || output.matches("\\s+" + searchString + "\\s+");
   
            passed = getResults("true", "" + passed, "Prints last item in list (Deja)", passed);
            assertTrue(passed);
        }
    }