.. activecode::  cndtnl-wc-weightq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T
    :nocodelens:

    weight = 0.5
    if weight < 1:
        price = 1.45
    if weight > 1:
        price = 1.15
    total = weight * price
    print(weight)
    print(price)
    print(total)