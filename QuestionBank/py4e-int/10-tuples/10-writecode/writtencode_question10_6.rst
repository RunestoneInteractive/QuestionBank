.. activecode:: writtencode_question10_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :nocodelens:

   list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

   updated_list = [tup[:-1] + (100,) for tup in list_of_tuples]