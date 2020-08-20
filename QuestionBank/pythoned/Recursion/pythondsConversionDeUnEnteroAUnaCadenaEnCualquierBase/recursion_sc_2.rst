.. actex:: recursion_sc_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Recursion
   :subchapter: pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
   :topics: Recursion/pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
   :from_source: None
   :nocodelens:

   from test import testEqual
   def eliminarEspacio(s):
       return s

   def esPalindromo(s):
       return False

   testEqual(esPalindromo(eliminarEspacio("x")),True)
   testEqual(esPalindromo(eliminarEspacio("radar")),True)
   testEqual(esPalindromo(eliminarEspacio("hola")),False)
   testEqual(esPalindromo(eliminarEspacio("")),True)
   testEqual(esPalindromo(eliminarEspacio("reconocer")),True)
   testEqual(esPalindromo(eliminarEspacio("luz azul")),True)