.. activecode:: tdb
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: TuplesandMutability
   :topics: Dictionaries/TuplesandMutability
   :from_source: None

   actress = ("Julia", "Roberts", 1967, "Pretty Woman", 1990, "Atlanta", "Georgia")
   print(actress[2])
   print(actress[2:6])

   actress = actress[:3] + ("Duplicity", 2009) + actress[5:]
   print(actress)