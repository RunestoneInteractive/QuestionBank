.. activecode::  ch4Ex1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           String firstName = "Sofia";
           String middleName = "Maria";
           String lastName = "Hernandez";
           String initials = firstName.substring(0,1) +
                             middleName.substring(0,1) +
                             lastName.substring(0,1);
           System.out.println(initials.toLowerCase());
       }
   }