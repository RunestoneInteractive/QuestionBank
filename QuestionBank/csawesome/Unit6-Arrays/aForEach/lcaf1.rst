.. activecode:: lcaf1
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: aForEach
   :topics: Unit6-Arrays/aForEach
   :from_source: F
   :language: java

   public class Test1
   {
      public static double getAvg(int[] values)
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
        int[ ] values = {2, 6, 7, 12, 5};
        System.out.println(getAvg(values));
      }
   }