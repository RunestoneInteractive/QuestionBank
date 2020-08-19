.. activecode:: listForEachLoopObj
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java

   What does the following code do? Guess what it does before running it. Can you change the code so that it only removes the first name it finds in the list that matches? (Hint: use the found variable).
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
          boolean found = false;
          int index = 0;
          while (index < nameList.size())
          {
              if (name.equals(nameList.get(index)))
              {
                  nameList.remove(index);
                  found = true;
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