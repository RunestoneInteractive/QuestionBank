.. mchoice:: stack_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaPilaEnPython
   :topics: BasicDS/ImplementacionDeUnaPilaEnPython
   :from_source: None
   :answer_a: 'x'
   :answer_b: 'y'
   :answer_c: 'z'
   :answer_d: La pila está vacía
   :correct: c
   :feedback_a: Recuerde que una pila se construye de abajo hacia arriba.
   :feedback_b: Recuerde que una pila se construye de abajo hacia arriba.
   :feedback_c: ¡Bien hecho!
   :feedback_d: Recuerde que una pila se construye de abajo hacia arriba.

   Dada la siguiente secuencia de operaciones de pila, ¿cuál es el ítem en el tope de la pila cuando se completa la secuencia?

   .. code-block:: python

    m = Pila()
    m.incluir('x')
    m.incluir('y')
    m.extraer()
    m.incluir('z')
    m.inspeccionar()