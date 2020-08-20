.. activecode::  arr2DEx1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :optional:

   public class Test1
   {

       public static void main(String[] args)
       {
           int[][] table = new int[3][3];

           int count = 0;
           for (int row = 0; row < table.length; row++)
           {
               for (int col = 0; col < table[0].length; col++)
               {
                   table[row][col] = count;
                   count++;
                   System.out.print(table[row][col] + " ");
               }
           }
       }
   }