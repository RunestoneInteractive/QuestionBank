.. activecode::  ch8Ex8a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test
   {
       public static void shiftLeftOne(ArrayList<Integer> list)
       {
           Integer firstVal = list.remove(0);
           list.add(firstVal);
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 2, 3, 4, 5};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           shiftLeftOne(values);
           System.out.println("Expected Result:\t [2, 3, 4, 5, 1]");
           System.out.println("Your Result:\t\t " + values);
       }
   }