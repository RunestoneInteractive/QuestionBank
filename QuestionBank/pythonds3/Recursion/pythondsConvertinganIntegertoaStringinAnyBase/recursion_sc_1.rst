.. actex:: recursion_sc_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Recursion
   :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
   :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
   :from_source: T
   :nocodelens:

   from test import testEqual


   def reverse(s):
       return s

   testEqual(reverse("hello"), "olleh")
   testEqual(reverse("l"), "l")
   testEqual(reverse("follow"), "wollof")
   testEqual(reverse(""), "")