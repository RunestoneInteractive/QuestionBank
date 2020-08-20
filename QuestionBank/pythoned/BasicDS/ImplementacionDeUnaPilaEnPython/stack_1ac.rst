.. activecode:: stack_1ac
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaPilaEnPython
   :topics: BasicDS/ImplementacionDeUnaPilaEnPython
   :from_source: None
   :caption: Implementación de una clase Pila usando listas de Python
   :nocodelens:

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