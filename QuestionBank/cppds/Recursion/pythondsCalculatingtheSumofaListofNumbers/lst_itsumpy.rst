.. activecode:: lst_itsumpy
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: pythondsCalculatingtheSumofaListofNumbers
   :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
   :from_source: T
   :caption: Iterative Summation Python
   :optional:

   #Example of summing up a list without using recursion.

   def listsum(numList):
       theSum = 0

       for i in numList:
           theSum = theSum + i

       return theSum

   def main():
       print(listsum([1, 3, 5, 7, 9]))

   main()