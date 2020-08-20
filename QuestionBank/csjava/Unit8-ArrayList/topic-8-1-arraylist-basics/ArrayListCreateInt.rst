.. activecode:: ArrayListCreateInt
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-1-arraylist-basics
   :topics: Unit8-ArrayList/topic-8-1-arraylist-basics
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