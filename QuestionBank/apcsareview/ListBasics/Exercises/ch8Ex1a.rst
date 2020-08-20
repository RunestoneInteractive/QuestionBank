.. activecode::  ch8Ex1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: Exercises
   :topics: ListBasics/Exercises
   :from_source: T
   :language: java

   import java.util.List;
   import java.util.ArrayList;

   public class Test
   {
       public static void main(String[] args)
       {
           List<String> names = new ArrayList<String>();
           String[] friends = {"Sam", "Jessica", "Mark", "Alexis"};
           for (int i = 0; i < friends.length; i++)
           {
               names.add(friends[i]);
           }
           System.out.println(names);
       }
   }