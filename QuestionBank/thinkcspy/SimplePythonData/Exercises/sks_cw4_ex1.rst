.. activecode:: sks_cw4_ex1
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F

   [30 pts] Write a program to play the "guess the number" game. 
   The computer will pick a magic number between 1 and 100 and the user will try to 
   guess the number in as few guesses as possible. The program will keep asking for a 
   guess until the magic number is entered by the user. The program will also give hints to the 
   user (hot or cold) based on whether the new guess is closer or further to the magic number compared to 
   the previous guess.  For the first guess, it will be assumed the "previous guess" is 50. The program will 
   output the number of guesses.
   
   Below is a sample run of how the program should proceed:

   ::

     I am thinking of a number between 1 and 100.
     Can you guess what the number is?
     Enter your guess:
     40
     Cold!
     Enter your guess:
     75
     Hot!
     Enter your guess:
     87
     Hot!
     Enter your guess:
     82
     You win!
     You solved it in 4 guesses.

   ~~~~
   # Write your code here

   ====