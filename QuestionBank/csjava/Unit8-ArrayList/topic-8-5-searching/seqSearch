.. activecode:: seqSearch
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit8-ArrayList
  :subchapter: topic-8-5-searching
  :topics: Unit8-ArrayList/topic-8-5-searching
  :from_source: T
  :language: java


  ~~~~
  public class ArraySearcher
  {

     /** Finds the index of a value in an array of integers.
       * @param elements an array containing the items to be searched.
       * @param target the item to be found in elements.
       * @return an index of target in elements if found; -1 otherwise.
       */
     public static int sequentialSearch(int[] elements, int target)
     {
       for (int j = 0; j < elements.length; j++)
       {
         if (elements[j] == target)
         {
           return j;
         }
       }
       return -1;
     }

     public static void main(String[] args)
     {
       int[] numArray = {3, -2, 9, 38, -23};
       System.out.println("Tests of sequentialSearch");
       System.out.println(sequentialSearch(numArray,3));
       System.out.println(sequentialSearch(numArray,9));
       System.out.println(sequentialSearch(numArray,-23));
       System.out.println(sequentialSearch(numArray,99));
     }

  }