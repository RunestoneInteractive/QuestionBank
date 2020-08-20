.. parsonsprob:: vars_types_p5
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

   Construct a block of code that takes the volume of the rectangular
   prism defined by length, width, and height and prints
   the result to the terminal.
   
   -----
   int main() {
   =====
    int length = 2;
    int width = 3;
    int height = 4;
   =====
    length = 2; #paired
    width = 3;
    height = 4;
   =====
    int volume;
   =====
    volume = height * width * length;
   =====
    int volume = length * width * height #distractor
   =====
    cout << volume;
   =====
    print(volume) #distractor
   =====
    return volume; #distractor
   =====
   }