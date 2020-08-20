.. activecode:: stepTrackerCode_SSell_2
   :author: Stephen Sell
   :difficulty: 1.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: Exercises
   :topics: Unit5-Writing-Classes/Exercises
   :from_source: F
   :language: java

   Write the code for the class StepTracker below with the class name, the instance variables, and the constructor with a parameter for the minimum number of steps threshold for active days. Make sure it compiles.  
   Write the accessor methods activeDays which returns the number of active days.
   Write the mutator method addDailySteps which takes a parameter and adds it to the appropriate instance variable and changes other instance variables appropriately.
   Write the accessor method averageSteps which returns the average number of steps per day, calculated by dividing the total number of steps taken by the number of days tracked.
   ~~~~
   public class StepTracker
   {
      //instance variable declarations here


      //constructor with a parameter here

      //accessor method activeDays() here


      //mutator method addDailySteps here.
      // @param number of steps taken that day


      //accessor method averageSteps() here
      // @return average steps calculated by dividing the total number of steps taken by the number of days tracked (which should be instance variables).




      public static void main(String[] args)
      {
         StepTracker tr = new StepTracker(10000);
         System.out.println(tr.activeDays()); // returns 0. No data have been recorded yet.
         System.out.println(tr.averageSteps()); // returns 0.0. When no step data have been recorded, the averageSteps method returns 0.0.
         tr.addDailySteps(9000); // This is too few steps for the day to be considered active.
         tr.addDailySteps(5000); // This is too few steps for the day to be considered active.
         System.out.println(tr.activeDays()); // returns 0.  No day had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 7000.0 The average number of steps per day is (14000 / 2).
         tr.addDailySteps(13000); // This represents an active day.
         System.out.println(tr.activeDays());  // returns 1. Of the three days for which step data were entered, one day had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 9000.0. The average number of steps per day is (27000 / 3).
         tr.addDailySteps(23000); // This represents an active day.
         tr.addDailySteps(1111); // This is too few steps for the day to be considered active.
         System.out.println(tr.activeDays()); // returns 2. Of the five days for which step data were entered, two days had at least 10,000 steps.
         System.out.println(tr.averageSteps()); // returns 10222.2. The average number of steps per day is (51111 / 5).
      }
   }