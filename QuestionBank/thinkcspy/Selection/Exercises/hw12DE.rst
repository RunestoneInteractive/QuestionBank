.. activecode:: hw12DE
   :author: Damon Ellingston
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F

   **Homework 12 - Bingo!**

    Write a program that allows the user to guess a random number from 1 to 50. It should include an enter() function, asking the user: n = int(input(“Guess?”)).

    First you will generate a random number from 1 to 50 using the random() module. Don’t tell the user what the random number is!

    Next you will call the function enter() five times = five guesses. For each guess, there are three possible responses::


     “Too high” followed by “Guess?” from the enter() function

     “Too low” followed by “Guess?” from the enter() function

     “Bingo!”` at which point it exits the program

    
    Write a simple for loop so that there will be 5 guesses. After 5 wrong guesses, the computer responds: “Sorry - the number was n”
   ~~~~