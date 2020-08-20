.. activecode:: ArrayListFromArray
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-1-arraylist-basics
   :topics: Unit8-ArrayList/topic-8-1-arraylist-basics
   :from_source: T
   :language: java

   import java.util.*;
   public class ArrayListFromArray
   {
       public static void main(String[] args)
       {
          String[] names = {"Dakota", "Madison", "Brooklyn"};
          ArrayList<String> namesList = new ArrayList<String>(Arrays.asList(names));
          System.out.println(namesList);
       }
   }