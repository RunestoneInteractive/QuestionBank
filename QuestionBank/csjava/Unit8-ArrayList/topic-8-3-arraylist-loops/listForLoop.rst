.. activecode:: listForLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-3-arraylist-loops
   :topics: Unit8-ArrayList/topic-8-3-arraylist-loops
   :from_source: T
   :language: java

   The following code will throw an ArrayIndexOutOfBoundsException. Can you fix it?
   ~~~~
   import java.util.*;
   public class TestForLoop
   {
       public static void main(String[] args)
       {
           ArrayList<Integer> myList = new ArrayList<Integer>();
           myList.add(50);
           myList.add(30);
           myList.add(20);
           int total = 0;
           for (int i=0; i <= myList.size(); i++)
           {
               total = total + myList.get(i);
           }
           System.out.println(total);
       }
   }