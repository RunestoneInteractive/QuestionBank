.. activecode::  ch7Ex8na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: ArrayPractice
   :topics: Unit6-Arrays/ArrayPractice
   :from_source: T
   :language: java
   :optional:

   Solution to question above.
   ~~~~
   public class Test1
   {
       public static int getSumChars(String[] strArr)
       {
           int sum = 0;
           for (String str : strArr)
           {
               sum = sum + str.length();
           }
           return sum;
       }

       public static void main(String[] args)
       {
           String[] strArr = {"hi", "bye", "hola"};
           System.out.println(getSumChars(strArr));
       }
   }