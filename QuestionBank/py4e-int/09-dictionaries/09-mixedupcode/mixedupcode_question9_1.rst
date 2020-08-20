.. parsonsprob:: mixedupcode_question9_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-mixedupcode
   :topics: 09-dictionaries/09-mixedupcode
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Construct a block of code that prints a dictionary containing the amount of times a letter appears in the given string.
   -----
   phrase = "Explore the NEW Wolverine Access"
   =====
   d = dictionary() #distractor
   =====
   d = dict()
   =====
   for word in phrase:
   =====
   for word in d: #distractor
   =====
    for letter in word.lower():
   =====
     if letter in d: #distractor
   =====
     if letter not in d:
   =====
      d[letter] = 1
   =====
     else:
   =====
      d[letter] += 1
   =====
   print(d)