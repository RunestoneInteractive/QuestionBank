.. activecode::  arr2DEx1q
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
           // ADD CODE HERE //

           // Should print the values in table
           int count = 0;
           for (int row = 0; row < table.length; row++)
           {
               for (int col = 0; col < table.length; col++)
               {
                   table[row][col] = count;
                   count++;
                   System.out.print(table[row][col] + " ");
               }
           }
       }
   }