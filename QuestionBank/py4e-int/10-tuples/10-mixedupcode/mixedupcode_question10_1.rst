.. parsonsprob:: mixedupcode_question10_1
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

   Construct a block of code that sorts the string 'txt' into a list of tuples (first element is the length of the word, the second being the word). Sort the list in terms of word length from longest to shortest.
   -----
   txt = 'but soft what light in yonder window breaks'
   =====
   words = txt.split()
   =====
   t = []
   =====
   for word in words.split(): #distractor
   =====
   for word in words:
   =====
    t.append((len(word), word))
   =====
    t.append(len(word)) #distractor
   =====
   t.sort(reverse = False) #distractor
   =====
   t.sort(reverse = True)