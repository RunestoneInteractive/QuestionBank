.. activecode:: baseconvert
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: BasicDS
    :subchapter: ConvertingDecimalNumberstoBinaryNumbers
    :topics: BasicDS/ConvertingDecimalNumberstoBinaryNumbers
    :from_source: T
    :caption: Converting from Decimal to any Base
    :nocodelens:

    from pythonds.basic import Stack

    def baseConverter(decNumber,base):
        digits = "0123456789ABCDEF"

        remstack = Stack()

        while decNumber > 0:
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base

        newString = ""
        while not remstack.isEmpty():
            newString = newString + digits[remstack.pop()]

        return newString

    print(baseConverter(25,2))
    print(baseConverter(25,16))