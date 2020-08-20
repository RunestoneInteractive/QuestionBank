.. activecode:: tdg2
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Composability
   :topics: Dictionaries/Composability
   :from_source: None

   actress = ( ("Julia", "Roberts"), (8, "October", 1967),
               [ ("Duplicity", 2009),
                 ("Notting Hill", 1999),
                 ("Pretty Woman", 1990),
                 ("Erin Brockovich", 2000),
                 ("Eat Pray Love", 2010),
                 ("Mona Lisa Smile", 2003) ],
               ("Atlanta", "Georgia") )

   print(type(actress[1]))
   print(actress[1])