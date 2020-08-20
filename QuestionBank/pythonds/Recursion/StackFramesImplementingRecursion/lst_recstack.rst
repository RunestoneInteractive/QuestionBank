.. activecode:: lst_recstack
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: StackFramesImplementingRecursion
    :topics: Recursion/StackFramesImplementingRecursion
    :from_source: T
    :caption: Converting an Integer to a String Using a Stack
    :nocodelens:

    from pythonds.basic import Stack

    rStack = Stack()

    def toStr(n,base):
        convertString = "0123456789ABCDEF"
        while n > 0:
            if n < base:
                rStack.push(convertString[n])
            else:
                rStack.push(convertString[n % base])
            n = n // base
        res = ""
        while not rStack.isEmpty():
            res = res + str(rStack.pop())
        return res

    print(toStr(1453,16))