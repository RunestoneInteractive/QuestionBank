.. parsonsprob:: jktest2
   :author: Jerry Kearns
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :maxdist:
   :order:
   :language:
   :noindent:
   :adaptive:
   :numbered:
   :practice: T

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