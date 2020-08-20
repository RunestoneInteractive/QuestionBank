.. parsonsprob:: faghodsiaghasihgoisagnboeiagn
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: IntroRecursion
   :subchapter: Exercises
   :topics: IntroRecursion/Exercises
   :from_source: F

   Solve my really cool parsons problem...if you can.
   -----
   def findmax(alist):
   =====
      if len(alist) == 0:
         return None
   =====
      curmax = alist[0]
      for item in alist:
   =====
         if item &gt; curmax:
   =====
            curmax = item
   =====
      return curmax