.. activecode::  ch4Ex1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: T
   :language: java
   :optional:

   Answer: This is the answer to the previous question.
   ~~~~
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