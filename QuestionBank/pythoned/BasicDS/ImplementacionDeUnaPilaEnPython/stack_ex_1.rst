.. activecode:: stack_ex_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaPilaEnPython
   :topics: BasicDS/ImplementacionDeUnaPilaEnPython
   :from_source: None
   :nocodelens:

   from pythoned.basicas.pila import Pila

   p=Pila()

   print(p.estaVacia())
   p.incluir(4)
   p.incluir('perro')
   print(p.inspeccionar())
   p.incluir(True)
   print(p.tamano())
   print(p.estaVacia())
   p.incluir(8.4)
   print(p.extraer())
   print(p.extraer())
   print(p.tamano())