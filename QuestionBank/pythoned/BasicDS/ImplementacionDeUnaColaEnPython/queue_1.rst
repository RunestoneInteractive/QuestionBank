.. mchoice:: queue_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaColaEnPython
   :topics: BasicDS/ImplementacionDeUnaColaEnPython
   :from_source: None
   :correct: b
   :answer_a: 'hola', 'perro'
   :answer_b: 'perro', 3
   :answer_c: 'hola', 3
   :answer_d: 'hola', 'perro', 3
   :feedback_a: Recuerde que lo primero que se agrega a la cola es lo primero que se elimina. FIFO
   :feedback_b: S&iacute;, first-in-first-out significa que hola se ha eliminado
   :feedback_c: Colas y pilas son estructuras de datos en las que s&oacute;lo se puede acceder al primero y al &uacute;ltimo &iacute;tem.
   :feedback_d: Tal vez usted pas&oacute; por alto el llamado a avanzar al final

   Suponga que usted tiene la siguiente serie de operaciones para colas.

   ::

       c = Cola()
       c.agregar('hola')
       c.agregar('perro')
       c.agregar(3)
       c.avanzar()

   ¿Qué ítems quedan en la cola?