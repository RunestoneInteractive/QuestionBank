.. activecode:: tdv
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Sparsematrices
   :topics: Dictionaries/Sparsematrices
   :from_source: None

   matrix = {(3, 0): 1, (1, 2): 2, (3, 4): 3}

   x = int(input('x coordinate'))
   y = int(input('y coordinate'))
   print(matrix.get((x,y),0))