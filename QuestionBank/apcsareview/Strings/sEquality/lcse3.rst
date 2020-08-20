.. activecode:: lcse3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Strings
   :subchapter: sEquality
   :topics: Strings/sEquality
   :from_source: T
   :language: java

   public class Test2
   {
      public static void main(String[] args)
      {
        String s1 = "Hello";
        String s2 = "Hello";
        System.out.println(s1 == s2);
        System.out.println(s1.equals(s2));
      }
   }