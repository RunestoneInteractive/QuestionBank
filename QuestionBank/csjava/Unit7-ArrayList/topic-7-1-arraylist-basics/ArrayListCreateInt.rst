.. activecode:: ArrayListCreateInt
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java

   import java.util.*; // import everything at this level
   public class ArrayListCreateInt
   {
       public static void main(String[] args)
       {
          ArrayList<Integer> numList = new ArrayList<Integer>();
          System.out.println(numList.size());
       }
   }