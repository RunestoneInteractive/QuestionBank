.. parsonsprob:: mixedupcode_question9_4
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

   Construct a block of code that correctly reads in a file, and counts the amount of times each word appears in the file.
   -----
   with open(words.txt, "r") as filename: #distractor
   =====
   with open("words.txt", "r") as filename:
   =====
    word_counter = {}
   =====
    lines = filename.read() #distractor
   =====
    lines = filename.readlines()
   =====
    for line in lines:
   =====
     for word in line.split():
   =====
     for word in line: #distractor
   =====
      if word not in word_counter.keys();
   =====
       word_counter[word] = 0
   =====
      word_counter[word] += 1