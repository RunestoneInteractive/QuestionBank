.. activecode:: hw3DE
   :author: Damon Ellingston
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F

   **Homework 3**

   Write a script that asks the user for three (3) inputs, we'll call them X, Y and Z. Output should be three separate statements:

   ``The square of [X] is [X^2]``

   ``The square of [Y] is [Y^2]``

   ``The square of [Z] is [Z^2]``

   where the user can input any three numbers they like and get correct answers. Unfortunately the Runestone Interactive textbook does not support the command::

   `X = eval(input("Enter your first number: "))`

   The first two lines written below will convert an input string into a float.
   ~~~~
   x = input("Enter your first number: ")
   x = float(x)