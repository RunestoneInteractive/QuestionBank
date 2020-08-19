.. activecode:: listForEachLoopObj
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 1.0
   :total_students_attempting: 18
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.0

   The following code removes a name from a list. Set the found variable to the appropriate true or false values at line 13 and line 20 to make the code work.
   ~~~~
   import java.util.*;
   public class ListWorker
   {
      private ArrayList<String> nameList;
   
      public ListWorker(ArrayList<String> theNames)
      {
          nameList = theNames;
      }
   
      public boolean removeName(String name)
      {
          boolean found =   // true or false?
          int index = 0;
          while (index < nameList.size())
          {
              if (name.equals(nameList.get(index)))
              {
                  nameList.remove(index);
                  found =    // true or false?
              }
              else index++;
          }
          return found;
       }
   
       public static void main(String[] args)
       {
           ArrayList<String> myList = new ArrayList<String>();
           myList.add("Amun");
           myList.add("Ethan");
           myList.add("Donnie");
           myList.add("Ethan");
           ListWorker listWorker = new ListWorker(myList);
           System.out.println(listWorker.nameList);
           listWorker.removeName("Ethan");
           System.out.println("After removing Ethan: "
                     + listWorker.nameList);
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "[Amun, Ethan, Donnie, Ethan]\nAfter removing Ethan: [Amun, Donnie]";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }