.. parsonsprob:: vars_types_p7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: mixedUpCode
   :topics: Chapter2/mixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Construct a block of code that outputs the volume of a cylinder
   with a radius of 3 and a height of 4.  There are many ways to do this using the
   choices below, but only the correct answer that uses the LEAST lines
   of code will be accepted.
   
   -----
   int main() {
   =====
    cout << 3.14 * 3 * 3 * 4;
   =====
    cout << 3.14 * 3 ^ 2 * 4; #distractor
   =====
    height = 4; #distractor
   =====
    base = 3.14 * 3 * 3; #distractor
   =====
    base = 3.14 * 3 ^ 2; #distractor
   =====
    cout << base * height; #distractor
   =====
    volume = base * height; #distractor
   =====
    cout << volume; #distractor
   =====
   }