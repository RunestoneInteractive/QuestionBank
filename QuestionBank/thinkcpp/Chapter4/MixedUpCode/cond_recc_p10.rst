.. parsonsprob:: cond_recc_p10
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

   In the table of ASCII characters, the lowercase alphabet consists
   of characters 97-122.  The uppercase alphabet consists of characters
   65-90, which is a 32 character shift back from the lowercase.  Construct
   a recursive function that asks the user to input a LOWERCASE character,
   converts that character to UPPERCASE character and prints it.  If the user
   enters a character outside of the range of the LOWERCASE alphabet, prompt
   the user again.  Hint:  "||" means "or" when used between two conditional
   statements.
   -----
   void capitalize () {
   =====
    cout << "Input a lowercase character!";
   =====
    char let;
    cin >> let;
   =====
    if (int(let) < 97 || int(let) > 122) {
   =====
     capitalize (); }
   =====
    let = let - 32;
   =====
    cout << char(let);
   =====
   }