.. mchoice:: mcpydictperf
  :author: bmiller
  :difficulty: 3.0
  :basecourse: pythoned
  :chapter: AlgorithmAnalysis
  :subchapter: Diccionarios
  :topics: AlgorithmAnalysis/Diccionarios
  :from_source: None
  :answer_a: 'x' in miDiccionario
  :answer_b: del miDiccionario['x']
  :answer_c: miDiccionario['x'] == 10
  :answer_d: miDiccionario['x'] = miDiccionario['x'] + 1
  :answer_e: todas las anteriores son O(1)
  :correct: e
  :feedback_a: ``in`` es una operación constante para un diccionario porque no tiene que iterar pero hay una respuesta mejor.
  :feedback_b: Borrar un elemento de un diccionario es una operación constante, pero hay una respuesta mejor.
  :feedback_c: La asignación a una clave de diccionario es constante pero hay una respuesta mejor.
  :feedback_d: La reasignación a una clave de diccionario es constante pero hay una respuesta mejor.
  :feedback_e: Las únicas operaciones de diccionario que no son O(1) son aquéllas que requieren iteración.

  ¿Cuál de las operaciones sobre diccionarios que se muestran a continuación es O(1)?