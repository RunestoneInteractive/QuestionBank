.. activecode:: insertionSort
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit8-ArrayList
  :subchapter: topic-8-6-sorting
  :topics: Unit8-ArrayList/topic-8-6-sorting
  :from_source: T
  :language: java

  Demonstration of insertion sort.
  ~~~~
  import java.util.Arrays;

  public class SortTest
  {
     public static void insertionSort(int[] elements)
     {
        for (int j = 1; j < elements.length; j++)
        {
           int temp = elements[j];
           int possibleIndex = j;
           while (possibleIndex > 0 && temp < elements[possibleIndex - 1])
           {
              elements[possibleIndex] = elements[possibleIndex - 1];
              possibleIndex--;
           }
           elements[possibleIndex] = temp;
        }
    }

     public static void main(String[] args)
     {
        int[] arr1 = {3, 86, -20, 14, 40};
        System.out.println(Arrays.toString(arr1));
        insertionSort(arr1);
        System.out.println(Arrays.toString(arr1));
     }
  }