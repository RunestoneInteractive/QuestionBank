.. activecode::  arr2DEx2a
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
           // Can declare and initialize in one line
           String[][] students = { {"Brice", "Marvin", "Anna"},
                                  {"Kamal", "Maria", "Elissa"} };

           for (int row = 0; row < students.length; row++)
           {
               for (int col = 0; col < students[0].length; col++)
               {
                   System.out.print(students[row][col] + " ");
               }
           }
       }
   }