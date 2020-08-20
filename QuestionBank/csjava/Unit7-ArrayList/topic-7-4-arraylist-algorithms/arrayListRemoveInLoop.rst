.. activecode:: arrayListRemoveInLoop
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-4-arraylist-algorithms
   :from_source: T
   :language: java

   The following code is supposed to initialize the ArrayList arr to [0,1,2,3,4] and then remove every other element to get [1,3]. However, when you remove an element the size of the array changes and elements move up an index! See if you can figure out why you get the unexpected result.
   ~~~~
   import java.util.*;

   public class ArrayListLoop
   {
    public static void main(String[] args)
    {
      ArrayList<Integer> arr = new ArrayList<Integer>();
      for(int i=0; i < 5; i++)
      {
         arr.add(i);

      }
      for(int i=0; i < arr.size(); i++)
      {
         if (i % 2 == 0)
         {
            System.out.println("Removing element " + i + " : " + arr.get(i));
            arr.remove(i);
         }
      }
      System.out.println(arr);
    }
   }