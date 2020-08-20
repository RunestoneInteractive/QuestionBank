.. activecode:: 2012greyScaleForEach_A
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: grayImageA
   :topics: Unit8-2DArray/grayImageA
   :from_source: T
   :language: java

    public class Test
    {
       public static void main(String[] args)
       {
       int[][] arr = new int[5][5];
        for (int[] row : arr) {
           for (int ent : row) {
              System.out.print(ent);
            }
            System.out.println();
          }
        }
    }