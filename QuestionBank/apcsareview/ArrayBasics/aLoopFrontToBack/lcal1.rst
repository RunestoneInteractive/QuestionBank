.. activecode:: lcal1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aLoopFrontToBack
   :topics: ArrayBasics/aLoopFrontToBack
   :from_source: T
   :language: java

   public class ArrayWorker
   {
      private int[ ] values;

      public ArrayWorker(int[] theValues)
      {
         values = theValues;
      }

      public void multAll(int amt)
      {
        for (int i = 0; i < values.length; i++)
        {
          values[i] = values[i] * amt;
        } // end for loop
      } // end method

      public void printValues()
      {
        for (int val : values )
        {
          System.out.println(val);
        }
      }

      public static void main(String[] args)
      {
        int[] numArray =  {2, 6, 7, 12, 5};
        ArrayWorker aWorker = new ArrayWorker(numArray);
        aWorker.multAll(2);
        aWorker.printValues();

      }
   }