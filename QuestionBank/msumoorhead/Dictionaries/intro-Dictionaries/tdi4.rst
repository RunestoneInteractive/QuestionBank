.. activecode:: tdi4
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: intro-Dictionaries
   :topics: Dictionaries/intro-Dictionaries
   :from_source: None

   eng = ('one','two','three')
   sp = ('uno','dos','tres')
   eng2sp = {}

   for (e,s) in zip(eng,sp):
       print(e,s)


   print(eng2sp)