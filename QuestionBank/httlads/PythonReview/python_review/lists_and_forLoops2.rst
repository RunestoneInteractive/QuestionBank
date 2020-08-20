.. activecode:: lists_and_forLoops2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: httlads
   :chapter: PythonReview
   :subchapter: python_review
   :topics: PythonReview/python_review
   :from_source: T

   my_list = [3, 4, 64, 2, 45, 23, 12, 34, 146]
   total = 0
   for val in my_list:
       if val % 2 == 1:
           total += val
   print(total)