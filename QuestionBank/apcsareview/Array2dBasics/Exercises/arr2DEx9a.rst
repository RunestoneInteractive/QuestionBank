.. activecode::  arr2DEx9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: Exercises
   :topics: Array2dBasics/Exercises
   :from_source: T
   :language: java

   public class Test1
   {

       public static void main(String[] args)
       {
            int[][] table = { {1,4,9},{11,4,3},{2,2,3} };
            int sum = 0;

            for (int col = 0; col < table[0].length; col++)
            {
                sum += table[1][col];
            }

            System.out.println("The sum is: "+sum);
       }
   }