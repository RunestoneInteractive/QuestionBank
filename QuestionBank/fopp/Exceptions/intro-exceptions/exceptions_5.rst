.. activecode:: exceptions_5
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
   except Exception as e:
       print("got an error")
       print(e)

   print("continuing")