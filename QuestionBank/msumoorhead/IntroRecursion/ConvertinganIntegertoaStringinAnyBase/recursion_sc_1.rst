.. actex:: recursion_sc_1
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: IntroRecursion
   :subchapter: ConvertinganIntegertoaStringinAnyBase
   :topics: IntroRecursion/ConvertinganIntegertoaStringinAnyBase
   :from_source: None

   from test import testEqual
   def reverse(s):
       return s

   testEqual(reverse("hello"),"olleh")
   testEqual(reverse("l"),"l")
   testEqual(reverse("follow"),"wollof")
   testEqual(reverse(""),"")