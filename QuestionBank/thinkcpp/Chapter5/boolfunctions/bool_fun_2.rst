.. parsonsprob:: bool_fun_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: boolfunctions
   :topics: Chapter5/boolfunctions
   :from_source: T
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 8.5

   Construct a block of code that first checks if a number is positive,
   then checks if it's even, and then prints out a message to classify
   the number.  It prints "both" if the number is both positive and even,
   "even" if the number is only even, and finally "positive" if the number
   is only positive.
   -----
   bool positiveFlag = (x > 0);
   =====
   bool positiveFlag = (x < 0); #distractor
   =====
   bool evenFlag = (n%2 == 0);
   =====
   bool evenFlag = (n%2 == 1); #distractor
   =====
   if (evenFlag && positiveFlag) {
   =====
   if (evenFlag || positiveFlag) {  #distractor
   =====
    cout << "both"; }
   =====
   else if (evenFlag) {
   =====
    cout << "even"; }
   =====
   else {
   =====
    cout << "positive"; }