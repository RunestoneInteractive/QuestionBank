.. parsonsprob:: mixedupcode_question10_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-mixedupcode
   :topics: 10-tuples/10-mixedupcode
   :from_source: T
   :numbered: left
   :adaptive:

   Reorder the blocks of code to create a list containing tuples of each word from word_list paired with their lengths. Then sort the words by length from highest to lowest.
   -----
   word_list = ['pen', 'skyscraper', 'post', 'computer', 'apple', 'Hollywood']
   =====
   tup_list = []
   =====
   for word in word_list:
   =====
   for word in tup_list: #distractor
   =====
    tup = word, len(word)
   =====
    tup_list.append(tup)
   =====
    word_list.append(tup) #distractor
   =====
   tup_list.sort(key = lambda x: x[1], reverse = True)
   =====
   tup_list.sort(x[1], reverse = True) #distractor