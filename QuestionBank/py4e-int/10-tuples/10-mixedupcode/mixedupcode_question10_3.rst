.. parsonsprob:: mixedupcode_question10_3
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

   Construct a block of code that swaps the two second and fourth values of tuple t with one another.
   -----
   t = ('Apple', 'Banana', 'Grapefruit', 'Pear', 'Peach')
   =====
   a, b, c, d = t #distractor
   =====
   a, b, c, d, e = t
   =====
   t = a, c, b, e, d #distractor
   =====
   t = a, d, c, b, e