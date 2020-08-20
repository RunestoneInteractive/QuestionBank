.. activecode:: baseconvert
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: LinearBasic
    :subchapter: ConvertingDecimalNumberstoBinaryNumbers
    :topics: LinearBasic/ConvertingDecimalNumberstoBinaryNumbers
    :from_source: T
    :caption: Converting from Decimal to any Base
    :optional:

    #converts a decimal number into desired base 1-16.

    from pythonds.basic.stack import Stack

    def baseConverter(decNumber,base):
        #performs the conversion process.
        digits = "0123456789ABCDEF"

        remstack = Stack()

        while decNumber > 0:
            #adds the remainder after division of base, to the stack.
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base

        newString = ""
        while not remstack.isEmpty():
            #makes a string out of all the items in the stack.
            newString = newString + digits[remstack.pop()]

        return newString

    def main():
        imynum = 25
        print(baseConverter(imynum, 2))
        print(baseConverter(imynum, 16))
    main()