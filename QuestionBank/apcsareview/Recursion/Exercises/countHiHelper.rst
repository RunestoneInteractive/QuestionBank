.. activecode:: countHiHelper
   :author: Doug Vermes
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: Exercises
   :topics: Recursion/Exercises
   :from_source: F
   :timelimit: 2
   :language: java

   Given a string, compute recursively (no loops) the number of times 
   lowercase "hi" appears in the string. In this example, you will be writing 
   a helper method. Do NOT use the substring method anywhere in your 
   solution. Do not use indexOf, loops, or any method that secretly contains
   a loop. Implement the countHiHelper method. 

   countHi("xxhixx") → 1

   countHi("xhixhix") → 2

   countHi("hi") → 1
   ~~~~
   public class RecursionHW
   {
     public static int countHi(String str) 
     {
       // DO NOT MODIFY THIS METHOD
       return countHiHelper(str,0);
      }

      private static int countHiHelper(String str, int startIndex) 
      {
            return -1; // REPLACE WITH YOUR CODE
      }
      public static void main(String[] args)
      {
          // DO NOT CHANGE ANYTHING IN THIS METHOD
           String[] testCases = {"xxhixx","xhixhix","hi","hihih","h","","ihihihihih","ihihihihihi","hiAAhi12hi","xhixhxihihhhih","ship","hiihihi","hhhhihhii"};

           int[] correctAnswers = {1,2,1,2,0,0,4,5,3,3,1,3,2};
           for (int i=0; i < testCases.length; i++)
           {
                  int userResponse = countHi(testCases[i]);
                  System.out.print("countHi(\"" + testCases[i] + "\") == " + userResponse + " (should be " + correctAnswers[i] + ") ");
                  if (correctAnswers[i] != userResponse)
                  {
                         System.out.println("X");
                  }
                  else
                  {
                         System.out.println("Yay!");
                  }
           }
      }
   }
   ====