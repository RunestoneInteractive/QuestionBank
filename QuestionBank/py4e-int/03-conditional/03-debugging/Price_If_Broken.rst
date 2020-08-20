.. activeCode:: Price_If_Broken
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-debugging
    :topics: 03-conditional/03-debugging
    :from_source: T
    :caption: Using multiple if statements

    weight = 0.5
    if weight < 1:
        price = 1.45
    if weight > 1:
        price = 1.15
    total = weight * price
    print(weight)
    print(price)
    print(total)