.. parsonsprob:: mixedupcode_question10_4
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

   Reorder the blocks of code to transform the dictionary 'd' into a list of tuples called tup_list, and sort it by the dictionary's values in descending order.
   -----
   d = {'a': 10, 'b': 2, 'c': 27, 'd': 15, 'e': 30, 'f': 3}
   =====
   tup_list = [d.items] #distractor
   =====
   tup_list = list(d.items())
   =====
   d.sort(reverse = True) #distractor
   =====
   tup_list.sort(reverse = True) #distractor
   =====
   tup_list.sort(key = lambda x: x[1], reverse = True)
   =====
   print(tup_list)