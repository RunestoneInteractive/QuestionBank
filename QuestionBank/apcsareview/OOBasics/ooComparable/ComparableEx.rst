.. activecode:: ComparableEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooComparable
   :topics: OOBasics/ooComparable
   :from_source: T
   :language: java

   public class ComparableExample
   {

       public static void main(String[] args)
       {
          System.out.println("hi".compareTo("apple"));
          System.out.println("baby".compareTo("zebra"));
          System.out.println("dog".compareTo("dogged"));
          System.out.println("Dog".compareTo("dog"));
          System.out.println("cat".compareTo("baby"));
       }
   }