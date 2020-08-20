.. activecode:: lcalaint
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
         list1.add(new Integer(1));
         System.out.println(list1);
         list1.add(new Integer(2));
         System.out.println(list1);
         list1.add(1, new Integer(3));
         System.out.println(list1);
         list1.add(1, new Integer(4));
         System.out.println(list1);
         System.out.println(list1.size());
      }
   }