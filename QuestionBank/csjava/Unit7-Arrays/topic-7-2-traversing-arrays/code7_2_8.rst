.. activecode:: code7_2_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-2-traversing-arrays
   :topics: Unit7-Arrays/topic-7-2-traversing-arrays
   :from_source: T
   :language: java

   What is wrong with the code below?  The first time through the loop it will start with the
   element at index 0 and check if the item at the array index equals the passed target string.
   If they have the same characters in the same order it will return 0, otherwise it will return -1.
   But, it has only processed one element of the array.  How would you fix the code to
   work correctly (process all array elements before returning)?
   ~~~~
   public class StringWorker
   {

      public static int findString(String target, String[] arr)
      {
        String word = null;
        for (int index = 0; index < arr.length; index++)
        {
          word = arr[index];

          if (word.equals(target))
          {
            return index;
          }
          else
          {
            return -1;
          }
        }
        return -1;
      }

      public static void main(String[] args)
      {
        String[] arr = {"Hello", "Hey", "Good morning!"};
        System.out.println(findString("Hey", arr));
      }
   }