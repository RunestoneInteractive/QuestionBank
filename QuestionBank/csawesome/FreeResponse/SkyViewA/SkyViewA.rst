.. activecode:: SkyViewA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: FreeResponse
   :subchapter: SkyViewA
   :topics: FreeResponse/SkyViewA
   :from_source: T
   :language: java

   public class SkyView

   {
       private double[][] view;

       /** Constructs a SkyView object from a 1-dimensional array of scan data.
         * @param numRows the number of rows represented in the view
         * Precondition: numRows > 0
         * @param numCols the number of columns represented in the view
         * Precondition: numCols > 0
         * @param scanned the scan data received from the telescope, stored in telescope order
         * Precondition: scanned.length == numRows * numCols
         * Postcondition: view has been created as a rectangular 2-dimensional array
         * with numRows rows and numCols columns and the values in
         * scanned have been copied to view and are ordered as
         * in the original rectangular area of sky.
         */
       public SkyView(int numRows, int numCols, double[] scanned)
       {
          //*** Write the constructor! ***
       }

       /** This is a main method for testing the class */
       public static void main(String[] args)
       {
           double[] values = {0.3, 0.7, 0.8, 0.4, 1.4, 1.1, 0.2, 0.5, 0.1, 1.6, 0.6, 0.9};
           SkyView sView = new SkyView(4, 3, values);
           System.out.println("It should print the following:");
           System.out.println("0.3, 0.7, 0.8,");
           System.out.println("1.1, 1.4, 0.4,");
           System.out.println("0.2, 0.5, 0.1,");
           System.out.println("0.9, 0.6, 1.6,");
           System.out.println();
           System.out.println("Your results");
           for (int row = 0; row < sView.view.length; row++)
           {
               for (int col = 0; col < sView.view[0].length; col++)
               {
                   System.out.print(sView.view[row][col] + ", ");
               }
               System.out.println();
            }

           System.out.println();

           double[] val2 = {0.3, 0.7, 0.8, 0.4, 1.4, 1.1};
           sView = new SkyView(3, 2, val2);
           System.out.println("It should print the following:");
           System.out.println("0.3, 0.7,");
           System.out.println("0.4, 0.8,");
           System.out.println("1.4, 1.1,");
           System.out.println();
           System.out.println("Your results");
           for (int row = 0; row < sView.view.length; row++)
           {
               for (int col = 0; col < sView.view[0].length; col++)
               {
                   System.out.print(sView.view[row][col] + ", ");
               }
               System.out.println();
            }

        } // end of main

   } // end of class