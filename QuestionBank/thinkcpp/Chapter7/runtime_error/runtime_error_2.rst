.. parsonsprob:: runtime_error_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: runtime_error
   :topics: Chapter7/runtime_error
   :from_source: T
   :numbered: left
   :adaptive:

   Construct a block of code that correctly changes the string to say "cat in the hat" instead of "cat on the mat", then print it.
   -----
   int main() {

      string sentence = "cat on the mat";

      sentence[4] = "i";

      sentence[5] = "i"; #distractor

      sentence[3] = "i"; #distractor

      sentence[11] = "h";

      sentence [12] = "h"; #distractor

      sentence[11] = "h" #distractor

      cout << sentence << endl;

   }