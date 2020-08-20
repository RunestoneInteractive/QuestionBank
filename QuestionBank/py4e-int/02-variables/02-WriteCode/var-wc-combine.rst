.. activecode::  var-wc-combine
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: 02-WriteCode
    :topics: 02-variables/02-WriteCode
    :from_source: T
    :nocodelens:

    totalMinutes = 270
    numMinutes = totalMinutes % 60
    numHours = (totalMinutes - numMinutes) / 60
    print(numHours)
    print(numMinutes)