.. parsonsprob:: mixedupcode_question10_8
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

   Construct a block of code that takes the longest item in each tuple, and adds it to the list 'longest_words'.
   -----
   list_o_tuples = [('twice', 'for', 'apples'), ('regular', 'combining'), ('one', 'five', 'twenty', 'twenty-four'), ('tmobile', 'sprint', 'at&t')]
   =====
   lst = []
   =====
   for tup in list_o_tuples:
   =====
    longest_word = ''
   =====
    longest_word = 0 #distractor
   =====
    for item in tup:
   =====
     if len(item) > len(longest_word):
   =====
      longest_word = item
   =====
     longest_word = len(item) #distractor
   =====
    lst.append(longest_word)