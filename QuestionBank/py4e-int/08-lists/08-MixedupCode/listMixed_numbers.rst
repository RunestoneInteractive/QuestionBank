.. parsonsprob:: listMixed_numbers
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-MixedupCode
    :topics: 08-lists/08-MixedupCode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:
    :noindent:

    The following program segment should swap the first and last values of the list "numbers" using
    indexing. But, the blocks have been mixed up and include an extra block that isn't needed in the
    solution. Drag the needed blocks from the left and put them in the correct order on the right.
    -----
    numbers = [3, 2, 1, 4]
    =====
    first = numbers[0]
    last = numbers[3]
    =====
    numbers[0] = last
    numbers[-1] = first
    =====
    first = numbers[1]
    last = numbers[4] #distractor