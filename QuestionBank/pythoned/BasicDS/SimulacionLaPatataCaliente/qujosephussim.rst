.. activecode:: qujosephussim
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: SimulacionLaPatataCaliente
   :topics: BasicDS/SimulacionLaPatataCaliente
   :from_source: None
   :caption: Simulación de la patata caliente
   :nocodelens:

   from pythoned.basicas.cola import Cola

   def papaCaliente(listaNombres, N):
       colaSimulacion = Cola()
       for nombre in listaNombres:
           colaSimulacion.agregar(nombre)

       while colaSimulacion.tamano() > 1:
           for i in range(N):
               colaSimulacion.agregar(colaSimulacion.avanzar())

           colaSimulacion.avanzar()

       return colaSimulacion.avanzar()

   print(papaCaliente(["Bill","David","Susan","Jane","Kent","Brad"],7))