.. codelens:: clens_1_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: NestedData
    :subchapter: ListswithComplexItems
    :topics: NestedData/ListswithComplexItems
    :from_source: T
    :python: py3

    nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
    print(nested1[0])
    print(len(nested1))
    nested1.append(['i'])
    for L in nested1:
        print(L)