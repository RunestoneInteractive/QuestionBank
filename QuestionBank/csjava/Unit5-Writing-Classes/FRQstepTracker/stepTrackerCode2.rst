.. activecode:: stepTrackerCode2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :language: java

   Copy the code from your first draft of the class StepTracker above  with the instance variables and constructor. Write the accessor methods **activeDays** which returns the number of active days.
   ~~~~
   public class StepTracker
   {
      // copy the instance variable declarations here


      // copy the constructor with a parameter here

      // Write the accessor method activeDays() here
      // @return activeDays

      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
         System.out.println(tr.activeDays()); // returns 0. No data have been recorded yet.
      }
   }