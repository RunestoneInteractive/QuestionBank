.. activecode:: listDeclare
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listDeclareAndCreate
   :topics: ListBasics/listDeclareAndCreate
   :from_source: T
   :language: java

   import java.util.*; // import everything at this level
   public class Test
   {
       public static void main(String[] args)
       {
          List<String> nameList = null;
          System.out.println(nameList);
       }
    }