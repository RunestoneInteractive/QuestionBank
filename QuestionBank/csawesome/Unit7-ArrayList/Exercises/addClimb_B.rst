.. parsonsprob:: addClimb_B
   :author: Leonardo Alvarez
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: Exercises
   :topics: Unit7-ArrayList/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0833333333
   :total_students_attempting: 12
   :num_students_correct: 11.0
   :mean_clicks_to_correct: 6.0

   Write an implementation of the ClimbingClub method addClimb 
    that stores the elements of climbList in alphabetical order by name 
    (as determined by the compareTo method of the String class). This
    implementation of addClimb should create a new ClimbInfo object
    with the given name and time and then insert the object into 
    the appropriate position in climbList.
   -----
   public void addClimb(String peakName, int climbTime) {
   =====
   for (int i = 0; i < this.climbList.size(); i++) { 
   =====
   if (peakName.compareTo(this.climbList.get(i).getName()) <= 0) { 
   =====
   this.climbList.add(i, new ClimbInfo(peakName, climbTime)); 
      return;            
   =====
   } // end if statement 
   =====
   } // end for loop 
   =====
   this.climbList.add(new ClimbInfo(peakName, climbTime));
   =====
   } //end method