.. activecode:: tdh1
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Enumerate
   :topics: Dictionaries/Enumerate
   :from_source: None

   actress = ("Julia", "Roberts", 1967, "Pretty Woman", 1990, "Atlanta", "Georgia")
   for tup in enumerate(actress): # entire tuple
       print(tup)

   for (index, ch) in enumerate("Crunchy Frog"): # unpack tuple
       print(index, ch)

   fruit = ["apple", "orange", "banana", "cherry"]
   for (i, f) in enumerate(fruit):
       fruit[i] = f.upper()

   print(fruit)