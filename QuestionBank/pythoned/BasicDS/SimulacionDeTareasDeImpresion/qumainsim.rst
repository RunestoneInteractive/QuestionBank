.. activecode:: qumainsim
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: SimulacionDeTareasDeImpresion
   :topics: BasicDS/SimulacionDeTareasDeImpresion
   :from_source: None
   :caption: Simulación de la cola de una impresora
   :nocodelens:

   from pythoned.basicas.cola import Cola

   import random

   class Impresora:
       def __init__(self, paginas):
           self.tasaPaginas = paginas
           self.tareaActual = None
           self.tiempoRestante = 0

       def tictac(self):
           if self.tareaActual != None:
               self.tiempoRestante = self.tiempoRestante - 1
               if self.tiempoRestante == 0:
                   self.tareaActual = None

       def ocupada(self):
           if self.tareaActual != None:
               return True
           else:
               return False

       def iniciarNueva(self,nuevaTarea):
           self.tareaActual = nuevaTarea
           self.tiempoRestante = nuevaTarea.obtenerPaginas() \
           * 60/self.tasaPaginas

   class Tarea:
       def __init__(self,tiempo):
           self.marcaTiempo = tiempo
           self.paginas = random.randrange(1,21)

       def obtenerMarca(self):
           return self.marcaTiempo

       def obtenerPaginas(self):
           return self.paginas

       def tiempoEspera(self, tiempoActual):
           return tiempoActual - self.marcaTiempo


   def simulacion(numeroSegundos, paginasPorMinuto):

       impresoraLaboratorio = Impresora(paginasPorMinuto)
       colaImpresion = Cola()
       tiemposEspera = []

       for segundoActual in range(numeroSegundos):

         if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

         if (not impresoraLaboratorio.ocupada()) and \
                   (not colaImpresion.estaVacia()):
           tareaSiguiente = colaImpresion.avanzar()
           tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
           impresoraLaboratorio.iniciarNueva(tareaSiguiente)

         impresoraLaboratorio.tictac()

       esperaPromedio=sum(tiemposEspera)/float(len(tiemposEspera))
       print("Tiempo de espera promedio%6.2f segundos %3d tareas restantes."%(esperaPromedio, colaImpresion.tamano()))


   def nuevaTareaImpresion():
       numero = random.randrange(1,181)
       if numero == 180:
           return True
       else:
           return False

   for i in range(10):
       simulacion(3600,5)