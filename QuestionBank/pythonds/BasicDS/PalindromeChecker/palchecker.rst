.. activecode:: palchecker
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: PalindromeChecker
   :topics: BasicDS/PalindromeChecker
   :from_source: T
   :caption: A Palindrome Checker Using Deque
   :nocodelens:

   from pythonds.basic import Deque

   def palchecker(aString):
       chardeque = Deque()

       for ch in aString:
           chardeque.addRear(ch)

       stillEqual = True

       while chardeque.size() > 1 and stillEqual:
           first = chardeque.removeFront()
           last = chardeque.removeRear()
           if first != last:
               stillEqual = False

       return stillEqual

   print(palchecker("lsdkjfskf"))
   print(palchecker("radar"))