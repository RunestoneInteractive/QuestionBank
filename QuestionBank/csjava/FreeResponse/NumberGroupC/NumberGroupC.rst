.. activecode:: NumberGroupC
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: FreeResponse
   :subchapter: NumberGroupC
   :topics: FreeResponse/NumberGroupC
   :from_source: T
   :language: java

   import java.util.ArrayList;

   class NumberGroup
   {
      public boolean contains(int num)
      {
       /* Implementation not shown */
        return true;
      }
   }

   class Range extends NumberGroup
   {
     // copy in your Range class from the previous lesson here
   }

   public class MultiGroups extends NumberGroup
   {

     private ArrayList<NumberGroup> groupList;

     public MultiGroups(Range r1, Range r2, Range r3)
     {
         groupList = new ArrayList<NumberGroup>();
         groupList.add(r1);
         groupList.add(r2);
         groupList.add(r3);
     }

     /** Returns true if at least one of the number groups
      *  in this multiple group contains num;
      *  false otherwise
     */
     public boolean contains(int num)
     {
           // Write the MultiGroup contains method here


     }

     //Main method to test the class
     public static void main(String[] args)
     {
       MultiGroups multiple1 = new MultiGroups(new Range(5, 8),new Range(10, 12),new Range(1, 6));
       System.out.println("Multiple1 contains 2 (should be true)? " + multiple1.contains(2));
       System.out.println("Multiple1 contains 9 (should be false)? " + multiple1.contains(9));
       System.out.println("Multiple1 contains 6 (should be true)? " + multiple1.contains(6));
     } // end of main
    }