.. activecode:: StringTest1
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/topic-9-7-Object
   :from_source: T
   :language: java

   Try to guess what this code will print out before running it.
   ~~~~
   public class StringTest
   {
      public static void main(String[] args)
      {
         String s1 = "hi";
         String s2 = "Hi";
         String s3 = new String("hi");
         System.out.println(s1.equals(s2));
         System.out.println(s2.equals(s3));
         System.out.println(s1.equals(s3));
      }
   }