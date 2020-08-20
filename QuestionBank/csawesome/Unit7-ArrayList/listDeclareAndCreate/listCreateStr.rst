.. activecode:: listCreateStr
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
          List<String> nameList = new ArrayList<String>();
          System.out.println("The size of nameList is: " + nameList.size());
          List<String> list2 = null;
          System.out.println("The size of list2 is: " + list2.size());
       }
   }