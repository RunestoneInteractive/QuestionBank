.. mchoice:: stack_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ImplementacionDeUnaPilaEnPython
   :topics: BasicDS/ImplementacionDeUnaPilaEnPython
   :from_source: None
   :answer_a: 'x'
   :answer_b: la pila está vacía
   :answer_c: ocurrirá un error
   :answer_d: 'z'
   :correct: c
   :feedback_a: Quizás usted desee comprobar la documentación para estaVacia
   :feedback_b: Hay un número impar de cosas en la pila, pero cada vez a través del ciclo se extraen 2 cosas
   :feedback_c: ¡Bien hecho!
   :feedback_d: Quizás usted desee comprobar la documentación para estaVacia

   Dada la siguiente secuencia de operaciones de pila, ¿cuál es el ítem en el tope de la pila cuando se completa la secuencia?

   .. code-block:: python

     m = Pila()
     m.incluir('x')
     m.incluir('y')
     m.incluir('z')
     while not m.estaVacia():
        m.extraer()
        m.extraer()