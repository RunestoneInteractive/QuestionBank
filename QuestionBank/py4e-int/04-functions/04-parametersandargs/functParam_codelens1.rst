.. codelens:: functParam_codelens1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-parametersandargs
    :topics: 04-functions/04-parametersandargs
    :from_source: T
    :showoutput:

    import math

    def print_twice(bruce):
        print(bruce)
        print(bruce)

    print_twice('Spam')
    print_twice(17)
    print_twice(math.pi)