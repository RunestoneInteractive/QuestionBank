.. activecode:: binSearchStrings
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit8-ArrayList
  :subchapter: topic-8-5-searching
  :topics: Unit8-ArrayList/topic-8-5-searching
  :from_source: T
  :language: java

  Demonstration of binary search with strings using compareTo.
  ~~~~
  public class BinSearchStrings
  {
     public static int binarySearch(String[] elements, String target) {
        int left = 0;
        int right = elements.length - 1;
        while (left <= right)
        {
           int middle = (left + right) / 2;
           if (target.compareTo(elements[middle]) < 0)
           {
              right = middle - 1;
           }
           else if (target.compareTo(elements[middle]) > 0)
           {
              left = middle + 1;
           }
           else {
              return middle;
           }
         }
         return -1;
     }

     public static void main(String[] args)
     {
        String[] arr1 = {"apple","banana","cherry","kiwi","melon"};

        // test when the target is in the middle
        int index = binarySearch(arr1,"cherry");
        System.out.println(index);

        // test when the target is the first item in the array
        index = binarySearch(arr1,"apple");
        System.out.println(index);

        // test when the target is in the array - last
        index = binarySearch(arr1,"melon");
        System.out.println(index);

        // test when the target is not in the array
        index = binarySearch(arr1,"pear");
        System.out.println(index);
     }
  }