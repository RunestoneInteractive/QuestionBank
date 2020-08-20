.. activecode:: brontosaurausexample
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionarycounters
   :topics: 09-dictionaries/09-dictionarycounters
   :from_source: T

   word = 'brontosaurus'
   d = dict()
   for c in word:
       if c not in d:
           d[c] = 1
       else:
           d[c] = d[c] + 1
   print(d)