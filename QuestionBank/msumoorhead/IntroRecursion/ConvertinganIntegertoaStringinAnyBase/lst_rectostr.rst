.. activecode:: lst_rectostr
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: IntroRecursion
    :subchapter: ConvertinganIntegertoaStringinAnyBase
    :topics: IntroRecursion/ConvertinganIntegertoaStringinAnyBase
    :from_source: None
    :caption: Recursively Converting from Integer to String

    def toStr(n,base):
       convertString = "0123456789ABCDEF"
       if n < base:
          return convertString[n]
       else:
          return toStr(n//base,base) + convertString[n%base]

    print(toStr(1453,16))