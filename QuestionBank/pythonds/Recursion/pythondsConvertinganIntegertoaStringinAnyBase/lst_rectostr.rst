.. activecode:: lst_rectostr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
    :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
    :from_source: T
    :caption: Recursively Converting from Integer to String

    def toStr(n,base):
       convertString = "0123456789ABCDEF"
       if n < base:
          return convertString[n]
       else:
          return toStr(n//base,base) + convertString[n%base]

    print(toStr(1453,16))