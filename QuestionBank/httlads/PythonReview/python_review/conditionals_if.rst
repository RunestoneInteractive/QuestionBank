.. activecode:: conditionals_if
   :author: bmiller
   :difficulty: 3.0
   :basecourse: httlads
   :chapter: PythonReview
   :subchapter: python_review
   :topics: PythonReview/python_review
   :from_source: T
   :coach:

   num = 5
   if type(num) == float:
      print("num is a float")

   elif type(num) == int:
      print("num is an int")

   elif type(num) == string:
      print("num is a string")

   else:
      print("num is not a float, int, or string")