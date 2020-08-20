.. parsonsprob:: CookieOrderB
 :author: bmiller
 :difficulty: 3.0
 :basecourse: apcsareview
 :chapter: ListBasics
 :subchapter: cookieOrderB
 :topics: ListBasics/cookieOrderB
 :from_source: T
 :numbered: left
 :adaptive:

 The method removeVariety below contains the correct code for one solution to this problem, but it is mixed up and contains extra blocks that are not needed.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
 -----
 private int removeVariety(String cookieVar) {
  int numBoxesRemoved = 0;
 =====
  for (int i = this.orders.size() - 1; i >= 0; i--) {
  String thisOrder = this.orders.get(i);
 =====
    if(cookieVar.equals(thisOrder.getVariety())) {
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