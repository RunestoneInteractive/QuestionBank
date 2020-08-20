.. parsonsprob:: aaa
   :author: Matthew Zuniga
   :difficulty: 3.3345724907
   :basecourse: fopp
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F
   :language: c++
   :pct_on_first: 0.4163568773
   :total_students_attempting: 269
   :num_students_correct: 192.0
   :mean_clicks_to_correct: 6.4010416667

   Construct a block of code that correctly implements the accumulator pattern.
   -----
   template < class InputIt, class T >
   T sum(InputIt first, InputIt last, T value)
   {
       while (first != last) {
          value = value + *first;
          ++first;
       }
       return value;
   }