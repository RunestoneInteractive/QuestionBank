.. actex:: recursion_sc_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: IntroRecursion
   :subchapter: ConvertinganIntegertoaStringinAnyBase
   :topics: IntroRecursion/ConvertinganIntegertoaStringinAnyBase
   :from_source: T

   from test import testEqual
   def reverse(s):
       return s

   testEqual(reverse("hello"),"olleh")
   testEqual(reverse("l"),"l")
   testEqual(reverse("follow"),"wollof")
   testEqual(reverse(""),"")