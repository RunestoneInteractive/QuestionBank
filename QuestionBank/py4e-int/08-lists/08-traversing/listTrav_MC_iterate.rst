.. mchoice:: listTrav_MC_iterate
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-traversing
    :topics: 08-lists/08-traversing
    :from_source: T
    :practice: T
    :answer_a: 8
    :answer_b: 9
    :answer_c: 15
    :answer_d: Error, the for statement needs to use the range function.
    :correct: b
    :feedback_a: Iteration by item will process once for each item in the sequence, even the empty list.
    :feedback_b: Yes, there are nine elements in the list so the for loop will iterate nine times.
    :feedback_c: Iteration by item will process once for each item in the sequence. Each string is viewed as a single item, even if you are able to iterate over a string itself.
    :feedback_d: The for statement can iterate over a sequence item by item.


    How many times will the for loop iterate in the following statements?

    ::

      p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
      for ch in p:
          print(ch)