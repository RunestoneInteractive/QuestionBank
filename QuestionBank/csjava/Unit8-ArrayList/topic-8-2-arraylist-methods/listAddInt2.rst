.. activecode:: listAddInt2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-2-arraylist-methods
   :topics: Unit8-ArrayList/topic-8-2-arraylist-methods
   :from_source: T
   :language: java

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