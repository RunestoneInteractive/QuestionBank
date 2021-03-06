.. activecode:: orderedlistclass
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaListaOrdenada
   :topics: BasicDS/ImplementacionDeUnaListaOrdenada
   :from_source: None
   :caption: Clase ListaOrdenada hasta ahora
   :hidecode:
   :nocodelens:

   class Nodo:
       def __init__(self,datoInicial):
           self.dato = datoInicial
           self.siguiente = None

       def obtenerDato(self):
           return self.dato

       def obtenerSiguiente(self):
           return self.siguiente

       def asignarDato(self,nuevodato):
           self.dato = nuevodato

       def asignarSiguiente(self,nuevosiguiente):
           self.siguiente = nuevosiguiente


   class ListaOrdenada:
       def __init__(self):
           self.cabeza = None

       def buscar(self,item):
           actual = self.cabeza
           encontrado = False
           detenerse = False
           while actual != None and not encontrado and not detenerse:
               if actual.obtenerDato() == item:
                   encontrado = True
               else:
                   if actual.obtenerDato() > item:
                       detenerse = True
                   else:
                       actual = actual.obtenerSiguiente()

           return encontrado

       def agregar(self,item):
           actual = self.cabeza
           previo = None
           detenerse = False
           while actual != None and not detenerse:
               if actual.obtenerDato() > item:
                   detenerse = True
               else:
                   previo = actual
                   actual = actual.obtenerSiguiente()

           temp = Nodo(item)
           if previo == None:
               temp.asignarSiguiente(self.cabeza)
               self.cabeza = temp
           else:
               temp.asignarSiguiente(actual)
               previo.asignarSiguiente(temp)

       def estaVacia(self):
           return self.cabeza == None

       def tamano(self):
           actual = self.cabeza
           contador = 0
           while actual != None:
               contador = contador + 1
               actual = actual.obtenerSiguiente()

           return contador


   milista = ListaOrdenada()
   milista.agregar(31)
   milista.agregar(77)
   milista.agregar(17)
   milista.agregar(93)
   milista.agregar(26)
   milista.agregar(54)

   print(milista.tamano())
   print(milista.buscar(93))
   print(milista.buscar(100))