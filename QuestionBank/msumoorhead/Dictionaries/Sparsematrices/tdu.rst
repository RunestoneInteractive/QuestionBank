.. activecode:: tdu
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Sparsematrices
   :topics: Dictionaries/Sparsematrices
   :from_source: None

   matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

   print(matrix[0,3])
   print(matrix.get((0,3)))
   print(matrix.get((0,3), 'key not found'))
   print(matrix.get((1,2)))
   print(matrix[1,2])