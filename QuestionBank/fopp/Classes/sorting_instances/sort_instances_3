.. activecode:: sort_instances_3
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

       def sort_priority(self):
           return self.price

   L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
   print("-----sorted by price, referencing a class method-----")
   for f in sorted(L, key=Fruit.sort_priority):
       print(f.name)

   print("---- one more way to do the same thing-----")
   for f in sorted(L, key=lambda x: x.sort_priority()):
       print(f.name)