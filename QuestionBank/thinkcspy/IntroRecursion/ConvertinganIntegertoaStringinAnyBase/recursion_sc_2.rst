.. actex:: recursion_sc_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: IntroRecursion
   :subchapter: ConvertinganIntegertoaStringinAnyBase
   :topics: IntroRecursion/ConvertinganIntegertoaStringinAnyBase
   :from_source: T

   from test import testEqual
   def removeWhite(s):
       return s

   def isPal(s):
       return False

   testEqual(isPal(removeWhite("x")),True)
   testEqual(isPal(removeWhite("radar")),True)
   testEqual(isPal(removeWhite("hello")),False)
   testEqual(isPal(removeWhite("")),True)
   testEqual(isPal(removeWhite("hannah")),True)
   testEqual(isPal(removeWhite("madam i'm adam")),True)