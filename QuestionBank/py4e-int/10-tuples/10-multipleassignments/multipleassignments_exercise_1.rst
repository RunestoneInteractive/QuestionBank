.. activecode:: multipleassignments_exercise_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-multipleassignments
   :topics: 10-tuples/10-multipleassignments
   :from_source: T
   :nocodelens:

   d = {'a':10, 'b':1, 'c':22}
   l = list()
   for key, val in d.items():
       l.append((val, key))
   print(l) #should print [(10, 'a'), (1, 'b'), (22, 'c')]
   l.sort(reverse=True)
   print(l) #should print [(22, 'c'), (10, 'a'), (1, 'b')]