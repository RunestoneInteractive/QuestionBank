.. actex:: stack_stringrev
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaPilaEnPython
   :topics: BasicDS/ImplementacionDeUnaPilaEnPython
   :from_source: None
   :nocodelens:

   from test import testEqual

   class Pila:
        def __init__(self):
            self.items = []

        def estaVacia(self):
            return self.items == []

        def incluir(self, item):
            self.items.append(item)

        def extraer(self):
            return self.items.pop()

        def inspeccionar(self):
            return self.items[len(self.items)-1]

        def tamano(self):
            return len(self.items)


   def cadenaInversa(miCadena):
       # Escriba aquí su código

   testEqual(cadenaInversa('casa'),'asac')
   testEqual(cadenaInversa('x'),'x')
   testEqual(cadenaInversa('1234567890'),'0987654321')