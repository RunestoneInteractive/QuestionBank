.. activecode::  ch8Ex3a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
   import java.util.*;

   public class Test1
   {
       public static void printEvenIndex(ArrayList<Integer> list)
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