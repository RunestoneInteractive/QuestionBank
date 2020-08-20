.. parsonsprob:: mt-copy-greater-or-equal
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: Exercises
   :topics: CSPRepeatNumbers/Exercises
   :from_source: F
   :numbered: left

   Solve my really cool parsons problem...if you can.
   -----
   def copyGreaterOrEqual(list, value):
   =====
   def copyGreaterOrEqual(self, list, value): #paired
   =====
       list2 = []
   =====
       list2 = 0 #paired
   =====
       for item in list:
   =====
           if item >= value:
   =====
           if item > value: #paired
   =====
               list2.append(item)
   =====
               list2.add(item) #paired
   =====
       return list2