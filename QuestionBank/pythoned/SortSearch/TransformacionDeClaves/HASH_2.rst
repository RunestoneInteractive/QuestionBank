.. mchoice:: HASH_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: SortSearch
   :subchapter: TransformacionDeClaves
   :topics: SortSearch/TransformacionDeClaves
   :from_source: None
   :correct: b
   :answer_a: 100, __, __, 113, 114, 105, 116, 117, 97, 108, 99
   :answer_b: 99, 100, __, 113, 114, __, 116, 117, 105, 97, 108
   :answer_c: 100, 113, 117, 97, 14, 108, 116, 105, 99, __, __
   :answer_d: 117, 114, 108, 116, 105, 99, __, __, 97, 100, 113
   :feedback_a:  Parece que usted puede haber estado aplicando aritmética módulo 2. Usted necesita utilizar el tamaño de la tabla hash como valor de la operación módulo.
   :feedback_b:  El uso de aritmética módulo 11 y de prueba lineal da estos valores
   :feedback_c: Parece que usted puede haber estado aplicando aritmética módulo 10, use el tamaño de la tabla.
   :feedback_d: Tenga cuidado en usar la operación módulo, no la división entera

   Supongamos que a usted se le da el siguiente conjunto de claves para insertar en una tabla hash que puede contener exactamente 11 valores: 113, 117, 97, 100, 114, 108, 116, 105, 99 ¿Cuál de las siguientes opciones demuestra mejor el contenido de la tabla hash después de que se han insertado todas las claves utilizando la prueba lineal?