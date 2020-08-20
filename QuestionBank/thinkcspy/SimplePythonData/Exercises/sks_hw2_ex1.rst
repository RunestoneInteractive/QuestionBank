.. activecode:: sks_hw2_ex1
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F

   [50 pts] Write a program that computes and prints the 1000th prime number.

   To help you get started, here is a rough outline of the stages you should probably follow in writing your code: 

   ::

     a.	Initialize some state variables 
     b.	Generate all (odd) integers > 1 as candidates to be prime 
     c.	For each candidate integer, test whether it is prime 
        i.	One easy way to do this is to test whether any other integer > 1 evenly divides the candidate with 0 remainder. To do this, you can use modular arithmetic, for example, the expression a%b returns the remainder after dividing the integer a by the integer b. 
        ii.	You might think about which integers you need to check as divisors – certainly you don’t need to go beyond the candidate you are checking, but how much sooner can you stop checking? 
     d.	If the candidate is prime, print out some information so you know where you are in the computation, and update the state variables 
     e.	Stop when you reach some appropriate end condition. In formulating this condition, don’t forget that your program did not generate the first prime (2). 

   ~~~~
   # Write your code here

   ====