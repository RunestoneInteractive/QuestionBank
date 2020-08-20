.. activecode:: dequecode_py
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: ImplementingaDequeCpp
   :topics: LinearBasic/ImplementingaDequeCpp
   :from_source: T
   :caption: Using Deque in Python
   :optional:

   #Example code of a deque.

   class Deque:
       def __init__(self):
           self.items = []

       def empty(self):
           return self.items == []

       def push_back(self, item):
           self.items.append(item)

       def push_front(self, item):
           self.items.insert(0,item)

       def pop_back(self):
           self.items.pop()

       def pop_front(self):
           self.items.pop(0)

       def back(self):
           return self.items[-1]

       def front(self):
           return self.items[0]

       def size(self):
           return len(self.items)

       def at(self, index):
           return self.items[index]

   def main():
       d = Deque()

       print("Deque Empty? ", d.empty())
       d.push_back("Zebra")
       print("Deque Empty? ", d.empty())

       d.push_front("Turtle") #pushes to the front of the deque.
       d.push_front("Panda")
       d.push_back("Catfish") #pushes to the back of the deque.
       d.push_back("Giraffe")

       print("Deque Size: ", d.size())
       print("Item at the front: ", d.front())
       print("Item at the back: ", d.back())

       print("\n")
       print("Items in the Deque: ")
       for i in range(d.size()):
           #prints each item in the deque.
           print(d.at(i), end=" ")
       print("\n")

       d.pop_back()
       d.pop_front()

       print("Item at the front: ", d.front())
       print("Item at the back: ", d.back())
       print("Deque Size: ", d.size())

       print("\n")
       print("Items in the Deque: ")
       for i in range(d.size()):
           #prints each item in the deque.
           print(d.at(i), end=" ")
       print("\n")
   main()