.. activecode:: rotate
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: array-algorithms
   :topics: Unit7-Arrays/array-algorithms
   :from_source: T
   :language: java

   The code below rotates array elements to the left. Note that you need to use an indexed loop for this because you need to change the array and access two elements at different indices. Try it in the |visualizer| with the CodeLens button. Can you change it to rotate the elements to the right instead?
   ~~~~
   public class Rotate
   {
      public static void main(String[] args)
      {
        int[ ] values = {6, 2, 1, 7, 12, 5};
        int first = values[0];
        for (int i=0; i < values.length; i++)
        {
           // if it's not the last element, copy the next one over
          if (i < values.length - 1)
              values[i] = values[i+1];
          else {
             // last element gets first
             values[i] = first;
            }
        }
        // print them out to see the results
        for (int val : values)
        {
           System.out.print(val + " ");
        }

    }
   }