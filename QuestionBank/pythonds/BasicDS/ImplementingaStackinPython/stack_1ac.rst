.. activecode:: stack_1ac
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: ImplementingaStackinPython
   :topics: BasicDS/ImplementingaStackinPython
   :from_source: T
   :caption: Implementing a Stack class using Python lists
   :nocodelens:

   class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items)-1]

        def size(self):
            return len(self.items)