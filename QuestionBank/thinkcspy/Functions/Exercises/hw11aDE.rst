.. activecode:: hw11aDE
   :author: Damon Ellingston
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F

   **Homework 11 part a**
  
    <--Indent = 4 spaces) Write a program ``scores()`` that accepts quiz scores from 0 to 20, separated by commas. Your program should allow the user to enter *as many scores as they like*.  It then averages those scores and prints out a grade as follows::

     18<= x <=20    "A"
     16<= x < 18    "B"
     14<= x < 16    "C"
     12<= x < 14    "D"
      x < 12       "F"


   Example: "Enter your scores "  ---> 15,19,15.5 /  avg  = 16.5   --->  prints out   "B". Hint: You may want to use the length command len(L) for counting the number of items on a list.
   ~~~~