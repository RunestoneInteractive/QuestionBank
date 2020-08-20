.. parsonsprob:: cond_recc_p9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: MixedUpCode
   :topics: Chapter4/MixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 7.0

   Construct a recursive function that tells the user to enter a positive
   number.  It should then output that number to the terminal.  If the user
   enters a negative number or zero, prompt the user again.
   -----
   void takeSum () {
   =====
    cout << "Input a positive number!";
   =====
    int num;
    cin >> num;
   =====
    if (num < 0) {
   =====
     takesum ();
   =====
    } // END "if"
   =====
    cout << num;
   =====
   } // END function