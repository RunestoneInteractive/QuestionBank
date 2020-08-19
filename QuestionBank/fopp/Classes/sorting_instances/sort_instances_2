.. activecode:: sort_instances_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Classes
   :subchapter: sorting_instances
   :topics: Classes/sorting_instances
   :from_source: T

   class Fruit():
       def __init__(self, name, price):
           self.name = name
           self.price = price

   L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
   for f in sorted(L, key=lambda x: x.price):
       print(f.name)