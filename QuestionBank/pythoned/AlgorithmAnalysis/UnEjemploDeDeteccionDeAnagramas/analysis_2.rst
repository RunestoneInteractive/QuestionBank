.. mchoice:: analysis_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: AlgorithmAnalysis
    :subchapter: UnEjemploDeDeteccionDeAnagramas
    :topics: AlgorithmAnalysis/UnEjemploDeDeteccionDeAnagramas
    :from_source: None
    :answer_a: O(n)
    :answer_b: O(n^2)
    :answer_c: O(log n)
    :answer_d: O(n^3)
    :correct: a
    :feedback_b: Tenga cuidado, al contar los ciclos usted debe asegurarse de que los ciclos están anidados.
    :feedback_d: Tenga cuidado, al contar los ciclos usted debe asegurarse de que los ciclos están anidados.
    :feedback_c: log n normalmente se indica cuando el problema se hace iterativamente más pequeño
    :feedback_a: Aunque hay dos ciclos, ellos no están anidados. Usted podría pensar en esto como O(2n) pero podemos ignorar la constante 2.

    Dado el siguiente fragmento de código, ¿cuál es su O-grande de tiempo de ejecución?

    .. code-block:: python

      prueba = 0
      for i in range(n):
         prueba = prueba + 1

      for j in range(n):
         prueba = prueba - 1