.. activecode::  ch7Ex8na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: Exercises
   :topics: ArrayBasics/Exercises
   :from_source: T
   :language: java

   public class Test
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