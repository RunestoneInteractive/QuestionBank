.. parsonsprob:: looping_counting_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: looping_and_counting
   :topics: Chapter7/looping_and_counting
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 5.0

   As an exercise, encapsulate this code in a function named
   ``countLetters``, and generalize it so that it accepts the string and
   the letter as arguments. In the function, declare length, count, and index in that order.
   Within the main function, declare city and letter in that order.
   -----
   int countLetter(string s, char letter) {
   =====
      int length = s.length();
   =====
      int count = 0;
   =====
      int index = 0;
   =====
      while (index < length) {
   =====
        if (s[index] == letter) {
   =====
          count = count + 1;
        }
   =====
        index = index + 1;
      }
   =====
      return count;
   }
   =====
   int main() {
   =====
      string city = "New Baltimore";
   =====
      char letter = "e";
   =====
      cout << countLetter(city, letter);
   }