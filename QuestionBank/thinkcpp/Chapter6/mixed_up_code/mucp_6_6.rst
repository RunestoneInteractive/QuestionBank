.. parsonsprob:: mucp_6_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: mixed_up_code
   :topics: Chapter6/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:

   We can further generalize ``repeatString`` so that it repeats a given string a given number of times.
   Let's write the code for the new ``repeatString`` function, which is a void function that takes
   a string input and an int x as parameters and uses a while loop to print out the string x number of times.
   -----
   void repeatString (string input, int x) {
   =====
   void repeatString (string input, string x) {                         #paired
   =====
      int n = 0;
   =====
      int n = x;                       #paired
   =====
      while (n < x) {
   =====
      while (x < n) {                        #paired
   =====
         cout << input << endl;
   =====
         n++;
      }
   }
   =====
         x++;                       #paired
      }
   }