.. activecode:: lcap1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aProcessAll
   :topics: ArrayBasics/aProcessAll
   :from_source: T
   :language: java

   public class StringWorker
   {
      private String[ ] arr = {"Hello", "Hey", "Good morning!"};

      public int findString(String target)
      {
        String word = null;
        for (int index = 0; index < arr.length; index++)
        {
          word = arr[index];

          if (word.equals(target))
          {
            return index;
          }
          else return -1;
        }
        return -1;
      }

      public static void main(String[] args)
      {
        StringWorker sWorker = new StringWorker();
        System.out.println(sWorker.findString("Hey"));
      }
   }