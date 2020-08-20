.. parsonsprob:: parsons_1
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: cpp4python
   :chapter: IntroCpp
   :subchapter: Exercises
   :topics: IntroCpp/Exercises
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


config values (conf.py):

- parsons_div_class - custom CSS class of the component's outermost div