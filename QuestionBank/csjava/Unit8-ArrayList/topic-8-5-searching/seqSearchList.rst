.. activecode:: seqSearchList
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit8-ArrayList
    :subchapter: topic-8-5-searching
    :topics: Unit8-ArrayList/topic-8-5-searching
    :from_source: T
    :language: java

    Here is a linear search using ArrayLists. Notice that size() and get(i) is used with ArrayLists instead of length and [i] which are used in arrays.
    ~~~~
    import java.util.*;

    public class ArrayListSearcher
    {

      /** Finds the index of a value in an ArrayList of integers.
        * @param elements an array containing the items to be searched.
        * @param target the item to be found in elements.
        * @return an index of target in elements if found; -1 otherwise.
        */
      public static int sequentialSearch(ArrayList<Integer> elements, int target)
      {
        for (int j = 0; j < elements.size(); j++)
        {
          if (elements.get(j) == target)
          {
            return j;
          }
        }
        return -1;
      }

      public static void main(String[] args)
      {
        ArrayList<Integer> numList = new ArrayList<Integer>();
        numList.add(3);
        numList.add(-2);
        numList.add(9);
        numList.add(38);
        numList.add(-23);
        System.out.println("Tests of sequentialSearch");
        System.out.println(sequentialSearch(numList,3));
        System.out.println(sequentialSearch(numList,9));
        System.out.println(sequentialSearch(numList,-23));
        System.out.println(sequentialSearch(numList,99));
      }

    }