.. parsonsprob:: CookieOrderB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: cookieOrderB
   :topics: Unit8-ArrayList/cookieOrderB
   :from_source: T
   :numbered: left
   :adaptive:

   The method removeVariety below contains the correct code for one solution to this problem, but it is mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  There may be extra blocks that are not needed in a correct solution.
   -----
   private int removeVariety(String cookieVar) {
       int numBoxesRemoved = 0;
   =====
       for (int i = this.orders.size() - 1; i >= 0; i--) {
   =====
       for (int i = 0; i < this.orders.size(); i++) { #paired
   =====
           String thisOrder = this.orders.get(i);
   =====
           if(cookieVar.equals(thisOrder.getVariety())) {
   =====
           if(cookieVar == thisOrder.getVariety()) { #paired
   =====
               numBoxesRemoved += thisOrder.getNumBoxes();
               this.orders.remove(i);
   =====
           } // end if
   =====
       } // end for
   =====
       return numBoxesRemoved;
   =====
   } // end method