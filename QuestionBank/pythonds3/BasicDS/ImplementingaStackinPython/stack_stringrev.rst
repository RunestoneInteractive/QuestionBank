.. actex:: stack_stringrev
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: BasicDS
   :subchapter: ImplementingaStackinPython
   :topics: BasicDS/ImplementingaStackinPython
   :from_source: T
   :nocodelens:

   from test import testEqual
   from pythonds3.basic import Stack

   def rev_string(my_str):
       # your code here

   testEqual(rev_string("apple"), "elppa")
   testEqual(rev_string("x"), "x")
   testEqual(rev_string("1234567890"), "0987654321")