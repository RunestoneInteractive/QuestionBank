.. activecode:: lamda_function
   :author: bmiller
   :difficulty: 3.0
   :basecourse: httlads
   :chapter: PythonReview
   :subchapter: python_review_new
   :topics: PythonReview/python_review_new
   :from_source: T
   :coach:

   x = lambda a : a + 7 # Notice that this is a one line expression
   print (x(5))

   y = lambda a, b, c : a * b * c
   print (y(2,3,4))

   z = lambda a : a * 3
   print(z("Happy birthday to you!" + "\n"))