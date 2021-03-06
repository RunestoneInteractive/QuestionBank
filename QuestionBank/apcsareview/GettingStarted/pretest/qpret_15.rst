.. mchoice:: qpret_15
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: [1, 2, 3, 4, 5]
    :answer_b: [1, 2, 4, 5, 6]
    :answer_c: [1, 2, 5, 4, 6]
    :answer_d: [1, 5, 2, 4, 6]
    :answer_e: [1, 6, 2, 4, 5]
    :correct: c
    :feedback_a: The set replaces the 3 with the 4 so this can't be right
    :feedback_b: The add with an index of 2 and a value of 5 adds the 5 at index 2 not 3. Remember that the first index is 0.
    :feedback_c: The add method that takes just a value as a parameter adds that value to the end of the list. The set replaces the value at that index with the new value. The add with parameters of an index and a value puts the passed value at that index and moves any existing values by one index to the right (increments the index). So the list looks like: 1 // add 1 1 2 // add 2 1 2 3 // add 3 1 2 4 // set index 2 to 4 1 2 5 4 // add 5 to index 2 (move rest right) 1 2 5 4 6 // add 6 to end
    :feedback_d: The add with an index of 2 and a value of 5 adds the 5 at index 2 not 1. Remember that the first index is 0.
    :feedback_e: How did the 6 get in position 2?

    Given the following code segment, what will be printed when it is executed?

    .. code-block:: java

        List<Integer> list1 = new ArrayList<Integer>();
        list1.add(new Integer(1));
        list1.add(new Integer(2));
        list1.add(new Integer(3));
        list1.set(2, new Integer(4));
        list1.add(2, new Integer(5));
        list1.add(new Integer(6));
        System.out.println(list1);