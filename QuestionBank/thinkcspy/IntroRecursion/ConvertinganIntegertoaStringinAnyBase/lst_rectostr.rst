.. activecode:: lst_rectostr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: ConvertinganIntegertoaStringinAnyBase
    :topics: IntroRecursion/ConvertinganIntegertoaStringinAnyBase
    :from_source: T
    :caption: Recursively Converting from Integer to String
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 3.0

    def toStr(n,base):
       convertString = "0123456789ABCDEF"
       if n < base:
          return convertString[n]
       else:
          return toStr(n//base,base) + convertString[n%base]
    
    print(toStr(1453,16))