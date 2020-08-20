.. activecode:: 05section6_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-loops
    :topics: 05-iterations/05-loops
    :from_source: T
    :coach:
    :caption: A simple version of the Python built-in min() function

    def min(values):
        smallest = None
        for value in values:
            if smallest is None or value < smallest:
                smallest = value
        return smallest

    nums = [1,2,3,4,5]
    print(min(nums))