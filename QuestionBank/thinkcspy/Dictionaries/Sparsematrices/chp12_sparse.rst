.. activecode:: chp12_sparse
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Sparsematrices
   :topics: Dictionaries/Sparsematrices
   :from_source: T

   matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
   print(matrix.get((0,3)))

   print(matrix.get((1, 3), 0))