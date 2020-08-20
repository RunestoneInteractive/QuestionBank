.. activecode:: deco_counter2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Frameworks
    :subchapter: decorators
    :topics: Frameworks/decorators
    :from_source: T

    def call_counter(func):
       def wrap(*args, **kwargs):
           wrap.counter += 1
           return func(*args,**kwargs)
       wrap.counter = 0
       return wrap

    @call_counter
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    for i in range(20):
        print(fib(i), fib.counter)
        fib.counter = 0