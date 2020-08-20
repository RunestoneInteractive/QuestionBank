.. activecode:: exceptions_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: intro-exceptions
   :topics: Exceptions/intro-exceptions
   :from_source: T
   :nocanvas:

   try:
       items = ['a', 'b']
       third = items[2]
       print("This won't print")
   except IndexError:
       print("error 1")

   print("continuing")

   try:
       x = 5
       y = x/0
       print("This won't print, either")
   except IndexError:
       print("error 2")


   print("continuing again")