.. actex:: recursion_sc_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Recursion
   :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
   :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
   :from_source: T
   :nocodelens:

   from test import testEqual


   def remove_white(s):
       return s

   def is_pal(s):
       return False

   testEqual(is_pal(remove_white("x")), True)
   testEqual(is_pal(remove_white("radar")), True)
   testEqual(is_pal(remove_white("hello")), False)
   testEqual(is_pal(removeWremove_whitehite("")), True)
   testEqual(is_pal(remove_white("hannah")), True)
   testEqual(is_pal(remove_white("madam i'm adam")), True)