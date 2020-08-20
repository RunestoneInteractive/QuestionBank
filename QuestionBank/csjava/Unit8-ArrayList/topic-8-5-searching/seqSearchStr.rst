.. activecode:: seqSearchStr
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit8-ArrayList
  :subchapter: topic-8-5-searching
  :topics: Unit8-ArrayList/topic-8-5-searching
  :from_source: T
  :language: java

  Demonstration of a linear search for a String.
  ~~~~
  public class SearchTest
  {

     public static int sequentialSearch(String[] elements, String target)
     {
        for (int j = 0; j < elements.length; j++)
        {
           if (elements[j].equals(target))
           {
              return j;
           }
       }
       return -1;
     }

     public static void main(String[] args)
     {
        String[] arr1 = {"blue", "red", "purple", "green"};

        // test when the target is in the array
        int index = sequentialSearch(arr1,"red");
        System.out.println(index);

        // test when the target is not in the array
        index = sequentialSearch(arr1,"pink");
        System.out.println(index);
     }
  }