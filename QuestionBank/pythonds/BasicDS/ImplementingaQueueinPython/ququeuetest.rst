.. codelens:: ququeuetest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: ImplementingaQueueinPython
   :topics: BasicDS/ImplementingaQueueinPython
   :from_source: T
   :caption: Example Queue Operations

   class Queue:
       def __init__(self):
           self.items = []

       def isEmpty(self):
           return self.items == []

       def enqueue(self, item):
           self.items.insert(0,item)

       def dequeue(self):
           return self.items.pop()

       def size(self):
           return len(self.items)

   q=Queue()

   q.enqueue(4)
   q.enqueue('dog')
   q.enqueue(True)
   print(q.size())