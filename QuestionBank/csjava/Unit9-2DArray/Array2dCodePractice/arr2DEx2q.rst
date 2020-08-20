.. activecode::  arr2DEx2q
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


           // Should print the values in students in order
           for (int row = 0; row < students.length; row++)
           {
               for (int col = 0; col < students[0].length; col++)
               {
                   System.out.print(students[row][col] + " ");
               }
           }
       }
   }