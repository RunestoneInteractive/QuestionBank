.. parsonsprob:: CookieOrderA
 :author: bmiller
 :difficulty: 3.0
 :basecourse: apcsareview
 :chapter: ListBasics
 :subchapter: cookieOrderA
 :topics: ListBasics/cookieOrderA
 :from_source: T
 :numbered: left
 :adaptive:

 The method getTotalBoxes below contains the correct code for one solution to this problem, but it is mixed up and contains extra blocks that are not needed.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
 -----
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