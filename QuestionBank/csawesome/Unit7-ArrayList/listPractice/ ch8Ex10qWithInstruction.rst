.. activecode::  ch8Ex10qWithInstruction
   :author: Steve Emerson
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: F
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test {
       public static String findLongest(ArrayList<String> list)
       {
           //Insert code that will return the longest string in "list"
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