.. actex:: recursion_sc_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Recursion
   :subchapter: pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
   :topics: Recursion/pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
   :from_source: None
   :nocodelens:

   from test import testEqual
   def invertir(s):
       return s

   testEqual(invertir("hola"),"aloh")
   testEqual(invertir("l"),"l")
   testEqual(invertir("seguir"),"riuges")
   testEqual(invertir(""),"")