.. parsonsprob:: find_function_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: find_function
   :topics: Chapter7/find_function
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Construct a block of code that correctly finds and prints where the first "B" is in the string. Declare ``city`` before ``index``.
   -----
   int main() {
   
      string city = "New Baltimore";
   
      string city = "New Baltimore" #distractor
   
      int index;
   
      index = city.find('B');
   
      index = city.find(B); #distractor
   
      index = city.find('b'); #distractor
   
      cout << index << endl;
   
   }