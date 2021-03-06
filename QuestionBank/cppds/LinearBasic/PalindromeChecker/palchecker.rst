.. activecode:: palchecker
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: PalindromeChecker
   :topics: LinearBasic/PalindromeChecker
   :from_source: T
   :caption: A Palindrome Checker Using Deque
   :optional:

   #Program that detects palindromes.

   from pythonds.basic.deque import Deque

   def palchecker(aString):
       chardeque = Deque()

       for ch in aString:
           #pushes each char in the string to the deque.
           chardeque.addRear(ch)

       stillEqual = True

       while chardeque.size() > 1 and stillEqual:
           first = chardeque.removeFront()
           last = chardeque.removeRear()
           if first != last: #if the two opposite positions of the
                             #word is not the same, then it is not
                             #a palindrome.
               stillEqual = False

       return stillEqual

   def main():
       print(palchecker("lsdkjfskf"))
       print(palchecker("radar"))
   main()