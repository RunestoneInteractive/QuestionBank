.. activecode:: binconvert_py
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: LinearBasic
  :subchapter: ConvertingDecimalNumberstoBinaryNumbers
  :topics: LinearBasic/ConvertingDecimalNumberstoBinaryNumbers
  :from_source: T
  :caption: Converting Decimal to Binary
  :optional:

  #converts a given decimal number into binary.

  from pythonds.basic.stack import Stack
  def divideBy2(decNumber):
      #performs the conversion process.
      remstack = Stack()

      while decNumber > 0:
          #gets the remainder of division by 2
          #and adds the remainder to a stack.
          rem = decNumber % 2
          remstack.push(rem)
          decNumber = decNumber // 2

      binString = ""
      while not remstack.isEmpty():
          #adds the numbers in the stack to a string.
          binString = binString + str(remstack.pop())

      return binString

  def main():
      print(divideBy2(42))
  main()