.. activecode::  ch8Ex2q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listPractice
   :topics: Unit8-ArrayList/listPractice
   :from_source: T
   :language: java

   import java.util.list;
   import java.util.ArrayList;

   public class Test
   {
       public static ArrayList<Integer> reverse(ArrayList<Integer> list)
       {
           ArrayList<int> reversed = new ArrayList<int>();
           for (Integer element: list)
           {

           }
           return reversed;
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 5, 7, 9, -2, 3, 2};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           ArrayList<Integer> result = reverse(values);
           System.out.println("Expected Result:\t [2, 3, -2, 9, 7, 5, 1]");
           System.out.println("Your Result:\t\t " + result);
       }
   }