.. activecode::  JP_ch4Ex1a
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: F
   :language: java


   The following code should get the first letter of the first name, middle name, and last name and append (concatenate) them together and then return them all in lowercase.  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String firstName = "Bogdan';
           String middleName = "Andrei";
           String lastName  "Disca";
           String initials = firstname.substring(0,1) +
                             middleName.subString(0,1) +
                             lastName.substring(0,1);
           System.out.println(initials.toLowerCase();
       }
   }