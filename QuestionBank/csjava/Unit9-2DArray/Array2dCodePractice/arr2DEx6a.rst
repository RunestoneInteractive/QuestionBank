.. activecode::  arr2DEx6a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit9-2DArray/Array2dCodePractice
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           String[][] arr = { {"Hey ", "there! "},{"I ", "hope "},
                             {"you ", "are "}, {"doing ", "well"} };

           for (int row = 0; row < arr.length; row++)
           {
               for (int col = 0; col < arr[0].length; col++)
               {
                   System.out.println(arr[row][col]);
               }
           }
       }
   }