.. activecode:: listGetSet
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-2-arraylist-methods
   :topics: Unit8-ArrayList/topic-8-2-arraylist-methods
   :from_source: T
   :language: java
   :autograde: unittest

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
            String output = getMethodOutput("main");
            String expect = "[Your name, John, Deja]";
            String searchString = "\\[[A-Za-z0-9 '-,]+, John, Deja\\]";

            String[] lines = output.split("\n");
            String longest = lines[0];
            for (int i = 0; i < lines.length; i++) {
                if (lines[i].length() > longest.length())
                    longest = lines[i];
            }

            boolean passed = output.matches("[\\s\\S]+" + searchString + "[\\s\\S]+");

            passed = getResults(expect, longest, "Add your name to the list", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String searchString = "Deja";

            boolean passed = output.contains("\n" + searchString + "\n") || output.matches("[\\s]+" + searchString + "[\\s]+");

            passed = getResults("true", "" + passed, "Prints last item in list (Deja)", passed);
            assertTrue(passed);
        }
    }