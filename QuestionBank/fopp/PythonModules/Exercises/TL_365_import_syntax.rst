.. mchoice:: TL_365_import_syntax
   :author: Tyler Luchko
   :difficulty: 2.9504643963
   :basecourse: fopp
   :chapter: PythonModules
   :subchapter: Exercises
   :topics: PythonModules/Exercises
   :from_source: F
   :random: 
   :answer_a: import math
   :answer_b: from math import exp
   :answer_c: from math import *
   :answer_d: import math as m
   :correct: a
   :feedback_a: Correct! This will make it obvious to anyone who reads your code when you use something from the ``math`` module.
   :feedback_b: This imports only the ``exp()`` function and puts it in the global namespace. This can make it difficult to tell where this function comes from.
   :feedback_c: This imports everything from ``math`` and puts it in the global namespace. This can make it difficult to tell when the ``math`` module is being used.
   :feedback_d: Don't change the names of modules unless it is the convention for that module. This makes your code harder to read.
   :pct_on_first: 0.5123839009
   :total_students_attempting: 646
   :num_students_correct: 639.0
   :mean_clicks_to_correct: 1.8090766823

   Which is the best way to import the ``math`` module so you can use the ``exp()`` function?