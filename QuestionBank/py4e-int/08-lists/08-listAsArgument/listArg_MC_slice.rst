.. mchoice:: listArg_MC_slice
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listAsArgument
    :topics: 08-lists/08-listAsArgument
    :from_source: T
    :practice: T
    :answer_a: True
    :answer_b: False
    :correct: a
    :feedback_a: The slice operator creates a new list called "t", but that will not affect the list it was passed.
    :feedback_b: The slice operator creates a new list called "t", so it will not modify the original list.

    True or False. The following code block will not remove the first element from the list argument.

    ::

      def deleting_first(lst):
          lst = lst[1:]