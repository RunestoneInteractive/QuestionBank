.. parsonsprob:: question9_2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionarycounters
   :topics: 09-dictionaries/09-dictionarycounters
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Construct a block of code that prints a dictionary containing the amount of times a letter appears in the string 'word'.
   -----
   word = "cheerful"
   =====
   d = dictionary() #distractor
   =====
   d = dict()
   =====
   for char in word:
   =====
   for char in d: #distractor
   =====
    if char in d: #distractor
   =====
    if char not in d:
   =====
     d[char] = 1
   =====
    else:
   =====
     d[char] += 1
   =====
   print(d)