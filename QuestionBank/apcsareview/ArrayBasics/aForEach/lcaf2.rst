.. activecode:: lcaf2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aForEach
   :topics: ArrayBasics/aForEach
   :from_source: T
   :language: java

   public class ArrayWorker
   {
      private int[ ] values;

      public ArrayWorker(int[] theValues)
      {
         values = theValues;
      }

      public double getAverage()
      {
        double total = 0;
        for (int val : values)
        {
          total  = total + val;
        }
        return total / values.length;
      }

      public static void main(String[] args)
      {
        int[] numArray =  {2, 6, 7, 12, 5};
        ArrayWorker aWorker = new ArrayWorker(numArray);
        System.out.println(aWorker.getAverage());
      }
   }