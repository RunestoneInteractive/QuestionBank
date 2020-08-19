.. parsonsprob:: question11_1_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-regularexpressions
   :topics: 11-regex/11-regularexpressions
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Construct a block of code that sorts through a file and prints out any line starting with 'Wolverines'.
   -----
   import re
   =====
   hand = open('mbox-short.txt')
   =====
   for line in hand:
   =====
    line = line.split() #distractor
   =====
    line = line.rstrip()
   =====
    if re.search('Wolverines', line): #distractor
   =====
    if re.search('^Wolverines', line):
   =====
     print(line)