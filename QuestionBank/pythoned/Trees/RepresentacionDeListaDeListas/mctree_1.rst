.. mchoice:: mctree_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Trees
   :subchapter: RepresentacionDeListaDeListas
   :topics: Trees/RepresentacionDeListaDeListas
   :from_source: None
   :correct: c
   :answer_a: ['a', ['b', [], []], ['c', [], ['d', [], []]]]
   :answer_b: ['a', ['c', [], ['d', ['e', [], []], []]], ['b', [], []]]
   :answer_c: ['a', ['b', [], []], ['c', [], ['d', ['e', [], []], []]]]
   :answer_d: ['a', ['b', [], ['d', ['e', [], []], []]], ['c', [], []]]
   :feedback_a: No es así, este árbol no tiene el nodo 'e'.
   :feedback_b: Esto está cerca, pero si usted mira cuidadosamente verá que los hijos izquierdo y derecho de la raíz están intercambiados.
   :feedback_c: Muy bien
   :feedback_d: Esto está cerca, pero los nombres de los hijos izquierdo y derecho han sido intercambiados junto con las estructuras subyacentes.

   Dadas las siguientes instrucciones:

   .. sourcecode:: python

       x = ArbolBinario('a')
       insertarIzquierdo(x,'b')
       insertarDerecho(x,'c')
       insertarDerecho(obtenerHijoDerecho(x),'d')
       insertarIzquierdo(obtenerHijoDerecho(obtenerHijoDerecho(x)),'e')

   ¿Cuál de las siguientes respuestas corresponde a la representación correcta del árbol?