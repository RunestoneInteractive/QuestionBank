.. activecode:: dec_callable
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Frameworks
   :subchapter: decorators
   :topics: Frameworks/decorators
   :from_source: T

   class MyClass:
       def __init__(self, name ):
           self.ivar1 = name

       def __call__(self, x, y):
           print("Hello: {0}".format(self.ivar1))
           sum = x+y
           print("the sum is {0}".format(sum))
           return sum

   foo = MyClass('brad')

   foo(2,9)