.. activecode:: cond_rec_a5a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Below is one way to complete the program.
   ~~~~
   #include <iostream>
   using namespace std;

   bool guessTheWord (string correct) {
       cout << "Guess the word!";
       string guess;
       cin >> guess;
       if (guess == correct) {
           cout << "That's it!";
       }
       else {
           guessTheWord(correct);
       }
   }