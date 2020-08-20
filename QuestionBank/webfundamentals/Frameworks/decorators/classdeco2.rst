.. activecode:: classdeco2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Frameworks
   :subchapter: decorators
   :topics: Frameworks/decorators
   :from_source: T

   class ccc:
       def __init__(self,start_val, current_time):
           self.counter = start_val
           self.define_time = current_time

       def __call__(self, func):
           def wrap(*args, **kwargs):
               self.counter += 1
               return func(*args, **kwargs)
           wrap.wrapper = self
           return wrap
   import time

   @ccc(0,time.time())
   def fib(n):
       if n <= 1:
           return 1
       else:
           return fib(n-1) + fib(n-2)

   print(fib(30))
   print(fib.wrapper.counter)
   print(fib.wrapper.define_time)