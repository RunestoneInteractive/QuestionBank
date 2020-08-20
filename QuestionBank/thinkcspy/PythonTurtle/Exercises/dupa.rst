.. activecode:: dupa
    :author: Marta Rutkowska
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    ========================
Nasz pierwszy szlaczek!
========================

Poniżej znajdziesz kod za pomocą którego narysujemy poniższy szlaczek:   

.. image:: C:/Users/Lenovo/Documents/moodle/Pierwszy_Szlaczek_1.png

Zmodyfikuj ten kod, tak aby szlaczek składał się z siedmiu powtarzających się odcinków. 
Skopiuj   
----------

.. activecode:: codeexample1
   :coach:
   :caption: This is a caption

   from turtle import *

   for i in range(2):
	right(90)
	fd(40)
	left(90)
	fd(30)
	left(90)
	fd(40)
	right(90)
	fd(30)