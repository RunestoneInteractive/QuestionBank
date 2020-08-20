.. codelens:: clens11_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionParameters
   :topics: Functions/FunctionParameters
   :from_source: T
   :python: py3

   def hello3(s, n):
      greeting = "Hello {} ".format(s)
      print(greeting*n)

   hello3("Wei", 4)
   hello3("", 1)
   hello3("Kitty", 11)