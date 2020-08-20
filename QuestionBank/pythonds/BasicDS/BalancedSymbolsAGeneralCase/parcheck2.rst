.. activecode :: parcheck2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: BalancedSymbolsAGeneralCase
   :topics: BasicDS/BalancedSymbolsAGeneralCase
   :from_source: T
   :caption: Solving the General Balanced Symbol Problem
   :nocodelens:

   from pythonds.basic import Stack

   def parChecker(symbolString):
       s = Stack()
       balanced = True
       index = 0
       while index < len(symbolString) and balanced:
           symbol = symbolString[index]
           if symbol in "([{":
               s.push(symbol)
           else:
               if s.isEmpty():
                   balanced = False
               else:
                   top = s.pop()
                   if not matches(top,symbol):
                          balanced = False
           index = index + 1
       if balanced and s.isEmpty():
           return True
       else:
           return False

   def matches(open,close):
       opens = "([{"
       closers = ")]}"
       return opens.index(open) == closers.index(close)


   print(parChecker('{({([][])}())}'))
   print(parChecker('[{()]'))