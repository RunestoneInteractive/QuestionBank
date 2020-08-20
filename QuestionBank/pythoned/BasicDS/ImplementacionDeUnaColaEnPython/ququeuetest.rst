.. codelens:: ququeuetest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaColaEnPython
   :topics: BasicDS/ImplementacionDeUnaColaEnPython
   :from_source: None
   :caption: Ejemplo de operaciones de Cola

   class Cola:
       def __init__(self):
           self.items = []

       def estaVacia(self):
           return self.items == []

       def agregar(self, item):
           self.items.insert(0,item)

       def avanzar(self):
           return self.items.pop()

       def tamano(self):
           return len(self.items)

   c=Cola()

   c.agregar(4)
   c.agregar('perro')
   c.agregar(True)
   print(c.tamano())