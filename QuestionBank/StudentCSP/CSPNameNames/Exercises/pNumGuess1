.. parsonsprob:: pNumGuess1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.2107843137
   :total_students_attempting: 204
   :num_students_correct: 183.0
   :mean_clicks_to_correct: 4.4644808743

   Put the code in order to define a NumberGuess class that will pick a random number from 1 to 100 in the __init__ method. Create a play method that loops while the current user guess is not equal to the game's pick.  The game will ask the user to pick a number from 1 to 100 and tell the user if the guess is too low, too high, or correct.
   -----
   import random
   class NumberGuess:
   =====
       def __init__(self):
   =====
           self.number = random.randrange(1, 101)
           self.guess = -1
   =====
       def play(self):
   =====
           while (self.number != self.guess):
   =====
               value = input("Guess a number from 1 to 100: ")
               self.guess = int(value)
   =====
               if (self.guess < self.number):
   =====
                   print("Too low")
   =====
               elif (self.guess > self.number):
   =====
                   print("Too high")
   =====
               else:
   =====
                   print("You guessed the number!")