.. activecode:: listCreateInt
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listDeclareAndCreate
   :topics: Unit7-ArrayList/listDeclareAndCreate
   :from_source: F
   :language: java

   import java.util.*; // import everything at this level
   public class Test
   {
       public static void main(String[] args)
       {
          List<Integer> numList = new ArrayList<Integer>();
          System.out.println(numList.size());
       }
   }