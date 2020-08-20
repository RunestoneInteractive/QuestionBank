.. activecode:: code7_2_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-2-traversing-arrays
   :topics: Unit7-Arrays/topic-7-2-traversing-arrays
   :from_source: T
   :language: java

   Does this work for arrays that have an even number of elements?  Does it work for arrays that have an odd number of elements?  Modify the main code below to test with both arrays with an even number of items and an odd number.
   ~~~~
   public class ArrayWorker
   {

      public static void doubleLastHalf(int[] values)
      {
        for (int i = values.length / 2; i < values.length; i++)
        {
          values[i] = values[i] * 2;
        }
      }

      public static void printArray(int[] values)
      {
         for (int i = 0; i < values.length; i++)
         {
           System.out.println(  values[i] );
         }
      }

      public static void main(String[] args)
      {
        int[] numArray = {3,8,-3, 2};
        doubleLastHalf(numArray);
        printArray(numArray);
      }
   }