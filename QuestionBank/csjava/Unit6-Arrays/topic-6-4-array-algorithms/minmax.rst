.. activecode:: minmax
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-4-array-algorithms
   :from_source: T
   :language: java

   The code below finds the minimum (smallest element) in an array. Try it in the |Java visualizer| with the CodeLens button. Can you change it to find the maximum element instead? Can you also compute the average of the elements?
   ~~~~
   public class MinMax
   {
      public static void main(String[] args)
      {
        int[ ] values = {6, 2, 1, 7, 12, 5};
        int min = values[0]; // initialize min to the first element
        for (int val : values)
        {
          if (val < min) // found a new min!
              min = val;
        }
        System.out.println("Min is " + min );
      }
   }