.. parsonsprob:: var-mixed-hello
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 02-variables
   :subchapter: 02-MixedupCode
   :topics: 02-variables/02-MixedupCode
   :from_source: T
   :practice: T
   :numbered: left

   The following program segment should prompt the user for their name and say hello to them.
   But, the blocks have been mixed up and include extra blocks that aren't correct.
   -----
   name = input('What is your name?\n')
   =====
   name = "yourName" #distractor
   =====
   greeting = "Hello "
   =====
   print(greeting + name)
   =====
   print("Hello" name) #distractor