.. parsonsprob:: mixedupcode_question10_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-mixedupcode
   :topics: 10-tuples/10-mixedupcode
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Reorder the code blocks to put the words in a file into a dictionary, where the key is the word and the value is its length. Then sort this list in alphabetical order.
   -----
   with open(mbox-short.txt) as filename:
   =====
    lines = filename.readlines()
   =====
    dictionary_one = {}
   =====
    dictionary = {} #distractor
   =====
    for line in lines.split():
   =====
     for word in line:
   =====
      if word not in dictionary_one.keys():
   =====
      if word not in dictionary.keys(): #distractor
   =====
       dictionary_one[word] = len(word)
   =====
    dictionary_one.sort(key = lambda x: x[0]) #distractor
   =====
    dictionary_one.sort(key = lambda x: x[0][0])