.. activecode:: recursion_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: Recursion
   :topics: Chapter4/Recursion
   :from_source: T
   :language: cpp
   :caption: Guessing Game.

   You can have a little bit of fun with recursion.  Try this guessing game below!
   ~~~~
   #include <iostream>
   #include <cstdlib>
   #include <ctime>
   using namespace std;

   void guessTheNumber(int num) {
       cout << "Enter your guess!";
       int guess;
       cin >> guess;
       if (guess == num) {
           cout << "That's it!";
       }
       else if (guess > num) {
           cout << "Too high! ";
           guessTheNumber(num);
       }
       else {
           cout << "Too low! ";
           guessTheNumber(num);
       }
   }

   int main() {
       srand((unsigned) time(0));
       int randomNumber = (rand())%101;
       guessTheNumber(randomNumber);
   }