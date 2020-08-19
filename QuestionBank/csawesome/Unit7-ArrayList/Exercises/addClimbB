.. parsonsprob:: addClimbB
   :author: Leonardo Alvarez
   :difficulty: 1.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: Exercises
   :topics: Unit7-ArrayList/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 11
   :num_students_correct: 10.0
   :mean_clicks_to_correct: 5.2

      /** Adds a new climb with name peakName and time climbTime to the list of climbs in order by name
     *
     * @param peakName the name of the mountain peak climbed
     * @param climbTime the number of minutes taken to complete the climb
     */
   -----
   public void addClimbB(String peakName, int climbTime)
    {
   
   =====
   int index = 0;
   =====
   while (index < climbList.size() && climbList.get(index).getName().compareTo(peakName) <= 0);
   =====
   {
     index++;
   }   
   =====
       climbList.add(index, new ClimbInfo(peakName, climbTime));
   }
   =====
     } // end while 
   =====
   } //end method