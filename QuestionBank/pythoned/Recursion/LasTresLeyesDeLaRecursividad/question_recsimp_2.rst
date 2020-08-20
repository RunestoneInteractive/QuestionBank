.. mchoice:: question_recsimp_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Recursion
   :subchapter: LasTresLeyesDeLaRecursividad
   :topics: Recursion/LasTresLeyesDeLaRecursividad
   :from_source: None
   :correct: d
   :answer_a: n == 0
   :answer_b: n == 1
   :answer_c: n &gt;= 0
   :answer_d: n &lt;= 1
   :feedback_a:  Aunque esto funcionaría hay opciones mejores y un poco más eficientes. Dado que fact(1) y fact(0) valen lo mismo.
   :feedback_b: Una buena opción, pero ¿qué pasa si usted llama a fact(0)?
   :feedback_c: Este caso base sería verdadero para todos los números mayores que cero, así que el factorial de cualquier número positivo sería 1.
   :feedback_d: Bien, éste es el más eficiente, e incluso previene que su programa colapse si se intenta calcular el factorial de un número negativo.

   Suponga que usted va a escribir una función recusiva para calcular el factorial de un número. fact(n) devuelve n * n-1 * n-2 * ... , donde el factorial de cero está definido como 1. ¿Cuál sería el caso base más apropiado?