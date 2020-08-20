.. actex:: mctree_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Trees
   :subchapter: NodosYReferencias
   :topics: Trees/NodosYReferencias
   :from_source: None

   from test import testEqual

   def crearArbol():
       #Escriba su código aquí

   arbolDePrueba = crearArbol()

   testEqual(arbolDePrueba.obtenerHijoDerecho().obtenerValorRaiz(),'c')
   testEqual(arbolDePrueba.obtenerHijoIzquierdo().obtenerHijoDerecho().obtenerValorRaiz(),'d')
   testEqual(arbolDePrueba.obtenerHijoDerecho().obtenerHijoIzquierdo().obtenerValorRaiz(),'e')