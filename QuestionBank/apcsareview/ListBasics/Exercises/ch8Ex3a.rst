.. activecode::  ch8Ex3a
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
       public static void printEvenIndex(ArrayList list)
       {
           for (int i = 0; i < list.size(); i++)
           {
               if (i % 2 == 0)
               {
                   System.out.print(list.get(i) + ", ");
               }
           }
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
           System.out.println("Expected Result:\t 1, 7, -2, 2,");
           System.out.print("Your Result:\t\t ");
           printEvenIndex(values);
       }
   }