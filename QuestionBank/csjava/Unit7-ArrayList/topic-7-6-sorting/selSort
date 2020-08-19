.. activecode:: selSort
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit7-ArrayList/topic-7-6-sorting
  :from_source: T
  :language: java

  Demonstration of selection sort.
  ~~~~
  import java.util.Arrays;

  public class SortTest
  {
     public static void selectionSort(int[] elements)
     {
        for (int j = 0; j < elements.length - 1; j++)
        {
           int minIndex = j;
           for (int k = j + 1; k < elements.length; k++)
           {
              if (elements[k] < elements[minIndex])
              {
                 minIndex = k;
              }
           }
           int temp = elements[j];
           elements[j] = elements[minIndex];
           elements[minIndex] = temp;
         }
     }

     public static void main(String[] args)
     {
        int[] arr1 = {3, 86, -20, 14, 40};
        System.out.println(Arrays.toString(arr1));
        selectionSort(arr1);
        System.out.println(Arrays.toString(arr1));
     }
  }