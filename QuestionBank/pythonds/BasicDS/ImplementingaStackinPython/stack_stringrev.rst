.. actex:: stack_stringrev
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: ImplementingaStackinPython
   :topics: BasicDS/ImplementingaStackinPython
   :from_source: T
   :nocodelens:

   from test import testEqual
   from pythonds.basic import Stack

   def revstring(mystr):
       # your code here

   testEqual(revstring('apple'),'elppa')
   testEqual(revstring('x'),'x')
   testEqual(revstring('1234567890'),'0987654321')