.. activecode::  ch8Ex7a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test
   {
       public static void removeLongStrings(ArrayList<String> list)
       {
           int count = 0;
           while(count < list.size())
           {
               if (list.get(count).length() > 4)
               {
                   list.remove(count);

               }
               count++;
           }
       }

       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<String> values = new ArrayList<String>();
           String[] words = {"bathtub", "fish", "computer", "cat", "foo"};
           for (int i = 0; i < words.length; i ++)
           {
               values.add(words[i]);
           }
           removeLongStrings(values);
           System.out.println("Expected Result:\t [fish, cat, foo]");
           System.out.println("Your Result:\t\t " + values);
       }
   }