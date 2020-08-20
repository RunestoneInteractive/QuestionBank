.. activecode:: qujosephussim
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: SimulationHotPotato
   :topics: BasicDS/SimulationHotPotato
   :from_source: T
   :caption: Hot Potato Simulation
   :nocodelens:

   from pythonds.basic import Queue

   def hotPotato(namelist, num):
       simqueue = Queue()
       for name in namelist:
           simqueue.enqueue(name)

       while simqueue.size() > 1:
           for i in range(num):
               simqueue.enqueue(simqueue.dequeue())

           simqueue.dequeue()

       return simqueue.dequeue()

   print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))