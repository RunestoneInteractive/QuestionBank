.. activecode::  ch8Ex9q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listPractice
   :topics: Unit8-ArrayList/listPractice
   :from_source: T
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test
   {
       public static void moveSmallest(ArrayList<Integer> list)
       {
           int smallestIndex = 0;
           for ()
           {
               if ()
               {
                   smallestIndex = i;
               }
           }
           //move smallest to front
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {3, 11, 54, 7, 1, 22};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           moveSmallest(values);
           System.out.println("Expected Result:\t [1, 3, 11, 54, 7, 22]");
           System.out.println("Your Result:\t\t " + values);
       }
   }