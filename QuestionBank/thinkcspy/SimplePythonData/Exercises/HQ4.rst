.. activecode:: HQ4
   :author: Harsha Madu
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :question: Write a program to add numbers.
   :coach:

   print("My first program adds a list of numbers")
   myList = [2, 4, 6, 8, 10]
   total = 0
   for num in myList:
       total = total + num
   print(total)