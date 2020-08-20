.. codelens:: listChange
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-aliasing
    :topics: 08-lists/08-aliasing
    :from_source: T
    :question: What is the value of a[0] after the line with the red arrow executes?
    :breakline: 4
    :feedback: Think about what it means that b is a.
    :correct: gobals.a[0]

    a = [1, 2, 3]
    b = a
    b[0] = 17
    print(a)