.. mchoice:: LinkedListMChoice
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: LinearLinked
    :subchapter: ImplementinganOrderedList
    :topics: LinearLinked/ImplementinganOrderedList
    :from_source: T
    :answer_a: In a circular linked list, the head Node of the linked list contains a pointer to the last node in the list.
    :answer_b: In a circular linked list, the last Node of the linked list contains a pointer to the head node of the list rather than pointing to NULL.
    :answer_c: In a circular linked list, every node contains a pointer to the head of the list, making it possible to return back to the beginning of the list at any time.
    :answer_d: In a circular linked list, the head and final Node of the linked list point to each other, making it possible to traverse through the list in both directions.
    :correct: b
    :feedback_a: Wrong! the head Node of the list will only contain a pointer to the second Node.
    :feedback_b: Correct! the final Node of the linked list will contain a pointer to the first node so that it is possible to make "circles" around the list.
    :feedback_c: Wrong! None of the nodes in the middle of the list will ever point to the head node in a circular linked list.
    :feedback_d: Hint: This would be possible in a circular doubly linked list, but not a circular linked list.
    :pct_on_first: 0.725
    :total_students_attempting: 80
    :num_students_correct: 80
    :mean_clicks_to_correct: 1.4625

    After having read over unordered and ordered linked lists, what do you think a circular linked list would do differently from an ordered or unordered linked list? (Hint: think about the example from the beginning of the chapter.)