.. activecode:: cond_rec_a5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Finish the code below so that the function will continue to
   ask for input until the user guesses the word correctly.
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
   }