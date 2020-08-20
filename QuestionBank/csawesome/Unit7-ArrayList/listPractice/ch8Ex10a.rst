.. activecode::  ch8Ex10a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   public class Test1 {
       public static String findLongest(ArrayList<String> list)
       {
           String longest = "";
           for (String element: list)
           {
               if (element.length() > longest.length())
               {
                   longest = element;
               }
           }
           return longest;
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<String> values = new ArrayList<String>();
           String[] words = {"singapore", "cattle", "metropolitan", "turnstile"};
           for (int i = 0; i < words.length; i ++)
           {
               values.add(words[i]);
           }
           System.out.println("Expected Result:\t metropolitan");
           System.out.print("Your Result:\t\t ");
           System.out.println(findLongest(values));
       }
   }