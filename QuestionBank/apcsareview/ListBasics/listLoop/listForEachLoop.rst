.. activecode:: listForEachLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listLoop
   :topics: ListBasics/listLoop
   :from_source: T
   :language: java

   import java.util.*;  // import all classes in this package.
   public class Test
   {
       public static void main(String[] args)
       {
           List<Integer> myList = new ArrayList<Integer>();
           myList.add(50);
           myList.add(30);
           myList.add(20);
           int total = 0;
           for (Integer value: myList)
           {
               total = total + value;
           }
           System.out.println(total);
       }
   }