.. activecode::  arr2DEx13q
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
           String[][] arr = { {"red","orange", "purple"}, {"green","blue", "indigo"} };

           // ADD CODE HERE //

           for (int row = 0; row < arr.length; row++)
           {
               for (int col = 0; col < arr[1].length; col++)
               {
                   System.out.println(arr[row][col]);
               }
           }
       }
   }