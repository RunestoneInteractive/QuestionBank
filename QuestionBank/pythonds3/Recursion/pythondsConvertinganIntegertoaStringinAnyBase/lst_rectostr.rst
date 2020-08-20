.. activecode:: lst_rectostr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
    :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
    :from_source: T
    :caption: Recursively Converting from Integer to String

    def to_str(n, base):
       convert_string = "0123456789ABCDEF"
       if n < base:
          return convert_string[n]
       else:
          return to_str(n // base, base) + convert_string[n % base]

    print(to_str(1453, 16))