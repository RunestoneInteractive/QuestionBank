.. activecode:: lclp2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit7-Arrays/topic-6-2-traversing-arrays
   :from_source: F
   :language: java

   Does this work for arrays that have an even number of elements?  Does it work for arrays that have an odd number of elements?  Modify the main code below to test with both arrays with an even number of items and an odd number.
   ~~~~
   public class ArrayWorker
   {
      private int[ ] values;

      public ArrayWorker(int[] theValues)
      {
         values = theValues;
      }

      public void doubleLastHalf()
      {
        for (int i = values.length / 2; i < values.length; i++)
        {
          values[i] = values[i] * 2;
        }
      }

      public void printArray()
      {
         for (int i = 0; i < values.length; i++)
         {
           System.out.println(  values[i] );
         }
      }

      public static void main(String[] args)
      {
        int[] numArray = {3,8,-3, 2};
        ArrayWorker worker = new ArrayWorker(numArray);
        worker.doubleLastHalf();
        worker.printArray();
      }
   }