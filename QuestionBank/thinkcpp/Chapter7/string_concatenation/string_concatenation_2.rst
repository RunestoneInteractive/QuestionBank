.. parsonsprob:: string_concatenation_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: string_concatenation
   :topics: Chapter7/string_concatenation
   :from_source: T
   :numbered: left
   :adaptive:

   As an exercise, put together the code below so that it prints ``C++ is so fun!""
   -----
   int main() {
   =====
      string language = "C++";
      string action = " is so ";
      string adjective = "fun!";
   =====
      string language = "C++"; #distractor
      string action = "is so";
      string adjective = "fun!";
   =====
      cout << language + action + adjective << endl;
   =====
      cout << "language" + "action" + "adjective" << endl; #distractor
   =====
   }