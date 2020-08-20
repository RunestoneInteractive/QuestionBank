.. activecode:: sdw
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: None
   :nocanvas:

   print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
   print((2 ** 3) ** 2)   # use parentheses to force the order you want!