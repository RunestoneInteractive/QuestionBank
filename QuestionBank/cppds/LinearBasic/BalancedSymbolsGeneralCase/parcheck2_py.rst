.. activecode:: parcheck2_py
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: BalancedSymbolsGeneralCase
   :topics: LinearBasic/BalancedSymbolsGeneralCase
   :from_source: T
   :caption: Solving the General Balanced Symbol Problem
   :optional:

   #Program does the same as before, except with 2 extra symbols.

   from pythonds.basic.stack import Stack

   def parChecker(symbolString):
       s = Stack()
       balanced = True
       index = 0
       while index < len(symbolString) and balanced:
           symbol = symbolString[index]
           if symbol in "([{": #if the current symbol ==
                               #an open symbol.
               s.push(symbol)
           else:
               if s.isEmpty(): #if there is a closed symbol
                               #but no open symbol is pending.
                   balanced = False
               else:
                   top = s.pop()
                   if not matches(top,symbol): #if the current closed symbol
                                               #is a different type than the
                                               #pending open one.
                          balanced = False
           index = index + 1
       if balanced and s.isEmpty(): #if the string is completely analyzed with
                                    #no remaining open symbols.
           return True
       else:
           return False

   def matches(open,close):
       #Checks if the type of an open and closed symbol are the same.
       opens = "([{"
       closers = ")]}"
       return opens.index(open) == closers.index(close)

   def main():
       print(parChecker('{[([][])]()}'))
       print(parChecker('[{()]'))
   main()