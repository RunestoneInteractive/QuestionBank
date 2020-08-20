.. activecode:: listAddInt2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listAdd
   :topics: ListBasics/listAdd
   :from_source: T
   :language: java

   import java.util.*;  // import all classes in this package.
   public class Test
   {
      public static void main(String[] arts)
      {
         List<Integer> list1 = new ArrayList<Integer>();
         list1.add(1);
         System.out.println(list1);
         list1.add(2);
         System.out.println(list1);
         list1.add(1, 3);
         System.out.println(list1);
         list1.add(1, 4);
         System.out.println(list1);
         System.out.println(list1.size());
      }
   }