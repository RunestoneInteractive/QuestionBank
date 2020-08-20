.. parsonsprob:: mixedupcode_question9_2
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

   Construct a block of code that prints a dictionary containing the amount of times a word appears in the given string.
   -----
   phrase = "Explore the NEW Wolverine Access"
   =====
   word_count = {}
   =====
   dictionary = dict() #distractor
   =====
   for word in phrase.split():
   =====
   for word in phrase: #distractor
   =====
    if word not in word_count:
   =====
    if word not in dictionary: #distractor
   =====
     word_count[word] = 0
   =====
    word_count[word] = 1 #distractor
   =====
    word_count[word] += 1
   =====
   print(word_count)