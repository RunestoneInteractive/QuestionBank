.. activecode:: hw7DE
   :author: Damon Ellingston
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F

   **HW 7**

   Write a script that accepts a single input: an integer,a float,a string separated by commas. Example input: <<5,2.99,broom>> all-on-one-line, not 3 separate inputs. Use the first line already printed below. Your code should detach the first item, convert it to an integer, and square it. Detach the second item, convert it to a float, and take its square root (use the math library = import math). Show only 2 decimal places, use round(). Detach the third item, convert it to ASCII and put it in the sentence “The ASCII code for <string> is ”. Here is an example of the output your code should produce: 

   ``The square of 5 is 25``

   ``The square root of 2.99 is 1.73``

   ``The ASCII code for broom is 98 114 111 111 109``

   Your code should work for any combination of int,float,string entered by the user.
   ~~~~
   x=input("Enter an int,a float,and a string separated by commas: ")