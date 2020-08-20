.. mchoice:: question_sort_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: SortSearch
   :subchapter: ElOrdenamientoPorMezcla
   :topics: SortSearch/ElOrdenamientoPorMezcla
   :from_source: None
   :correct: b
   :answer_a: [16, 49, 39, 27, 43, 34, 46, 40]
   :answer_b: [21,1]
   :answer_c: [21, 1, 26, 45]
   :answer_d: [21]
   :feedback_a: Ésta es la segunda mitad de la lista.
   :feedback_b: Sí, ordenamientoPorMezcla continuará moviéndose recursivamente hacia el inicio de la lista hasta que se tope con el caso base.
   :feedback_c: Recuerde que ordenamientoPorMezcla no opera sobre la mitad derecha de la lista sino hasta que la mitad derecha esté completamente ordenada.
   :feedback_d: Ésta es la lista después de 4 llamadas recursivas

   Dada la siguiente lista de números: [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] ¿Cuál de las siguientes respuestas corresponde a la lista que será ordenada después de 3 llamadas recursivas a ordenamientoPorMezcla?