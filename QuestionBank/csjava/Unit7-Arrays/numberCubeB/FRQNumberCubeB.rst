.. activecode:: FRQNumberCubeB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: numberCubeB
   :topics: Unit7-Arrays/numberCubeB
   :from_source: T
   :language: java

   public class NumberCube
   {

       public static int getLongestRun(int[] values)
       {
           // Complete this method
       }

       public static void main(String[] args){
           int[] values = {3, 5, 6, 6, 3, 6, 4, 4, 4, 2, 6, 4, 1, 1, 1, 1};
           int longestRunIdx = getLongestRun(values);

           if(longestRunIdx != 12){
              System.out.println("Your code does not return the correct index.");

              if(longestRunIdx == 2 || longestRunIdx == 6)
                  System.out.println("It is returning the start index of a run, but that run is not the longest.");

              System.out.println("Remember that your code must return the start index of the longest run of tosses.");
           } else {
              System.out.println("Looks like your code works well!");
           }
       }
   }