.. parsonsprob:: mucp_8_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: mixed_up_code
   :topics: Chapter8/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Let's write the code for the ``printSong`` function. ``printSong``
   takes a ``Song`` as a parameter and prints out the instance variables
   in the following format: "title" by artist (album, year). Put the necessary blocks of
   code in the correct order.
   -----
   void printSong (Song s) {
   =====
   struct printSong (Song s) {  #paired
   =====
      cout << "\"" << s.title << "\" by " << s.artist;
   =====
      cout << " (" << s.album << ", " << s.year << ")" << endl;
   =====
      cout << title << artist << album << year;  #distractor
   =====
      cout << "\"" << title << "\" by " << artist;  #distractor
   =====
      cout << " (" << album << ", " << year << ")" << endl;  #distractor
   =====
   }