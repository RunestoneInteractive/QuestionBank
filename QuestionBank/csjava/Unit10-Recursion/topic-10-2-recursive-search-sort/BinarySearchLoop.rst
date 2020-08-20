.. activecode:: BinarySearchLoop
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit10-Recursion/topic-10-2-recursive-search-sort
  :from_source: T
  :language: java

  public class IterativeBinarySearch
  {
     public static int binarySearch(int[] elements, int target) {
        int left = 0;
        int right = elements.length - 1;
        while (left <= right)
        {
           int middle = (left + right) / 2;
           if (target < elements[middle])
           {
              right = middle - 1;
           }
           else if (target > elements[middle])
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
        int[] arr1 = {-20, 3, 15, 81, 432};

        int index = binarySearch(arr1,81);
        System.out.println(index);
     }
  }