.. parsonsprob:: CookieOrderA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: cookieOrderA
   :topics: Unit7-ArrayList/cookieOrderA
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.4877675841
   :total_students_attempting: 1308
   :num_students_correct: 1182.0
   :mean_clicks_to_correct: 2.2969543147

   The method getTotalBoxes below contains the correct code for one solution to this problem, but it is mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
   -----
   public int getTotalBoxes() {
   
   =====
       int sum = 0;
   =====
       for (CookieOrder co : this.orders) {
   =====
           sum += co.getNumBoxes();
   =====
       } // end for
   =====
       return sum;
   =====
   } // end method