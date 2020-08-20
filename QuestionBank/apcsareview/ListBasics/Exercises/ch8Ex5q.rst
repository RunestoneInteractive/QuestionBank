.. activecode::  ch8Ex5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: Exercises
   :topics: ListBasics/Exercises
   :from_source: T
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test
   {
       public static void main(String[] args)
       {
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 44, 7, 9, -16, 3};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           System.out.println("Expected Result:\t [1, 44, 7, 9, -16, 3]");
           System.out.println("Your Result:\t\t " + values);
       }
   }