.. activecode:: listAdd1
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
      public static void main(String[] args)
      {
         List<String> nameList = new ArrayList<String>();
         nameList.add("Diego");
         System.out.println(nameList);
         nameList.add("Grace");
         System.out.println(nameList);
         nameList.add("Diego");
         System.out.println(nameList);
         System.out.println(nameList.size());
      }
   }