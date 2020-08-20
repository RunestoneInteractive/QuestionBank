.. activecode::  ch8Ex6a
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
   import java.util.List;
   import java.util.ArrayList;

   public class Test1
   {
       public static int sumNegValues(ArrayList<Integer> list)
       {
           int sum = 0;
           for(Integer element: list)
           {
               if (element < 0) {
                   sum += element;
               }
           }
           return sum;
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {-2, 34, -11, 9, -6, 3};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           System.out.println("Expected Result:\t -19");
           System.out.print("Your Result:\t\t ");
           System.out.println(sumNegValues(values));
       }
   }