.. activecode:: ArrayListCreateStr
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java

   The following code demonstrates a NullPointerException. Change list2 so that it creates a new Arraylist to remove the NullPointerException.
   ~~~~
   import java.util.*; // import everything at this level
   public class ArrayListCreateStr
   {
       public static void main(String[] args)
       {
          ArrayList<String> nameList = new ArrayList<String>();
          System.out.println("The size of nameList is: " + nameList.size());
          ArrayList<String> list2 = null;
          System.out.println("The size of list2 is: " + list2.size());
       }
   }