.. codelens:: clens11_2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionInvocation
   :topics: Functions/FunctionInvocation
   :from_source: T
   :python: py3

   def hello():
      print("Hello")
      print("Glad to meet you")

   print(type(hello))
   print(type("hello"))

   hello()
   print("Hey, that just printed two lines with one line of code!")
   hello()  # do it again, just because we can...