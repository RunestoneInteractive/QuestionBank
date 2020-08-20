.. codelens:: Numbers_Product
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatNumbers
    :subchapter: list
    :topics: CSPRepeatNumbers/list
    :from_source: T

    product = 1  # Start out with nothing
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for number in numbers:
        product = product * number
    print(product)