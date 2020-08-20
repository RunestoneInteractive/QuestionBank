.. activecode::  arr2DEx7a
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
           String[][] colors = { {"red","yellow","blue"},
                                {"orange","green","purple"} };

           for (int row = 0; row < colors.length; row++)
           {
               for (int col = 0; col < colors[0].length; col++)
               {
                   System.out.println(colors[row][col]);
               }
           }
       }
   }