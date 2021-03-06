.. mchoice:: LLq1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: LinearLinked
    :subchapter: ImplementinganUnorderedListLinkedLists
    :topics: LinearLinked/ImplementinganUnorderedListLinkedLists
    :from_source: T
    :answer_a: Every Node is contained within the UnorderedList class object. Making access to every Node of the linked list possible.
    :answer_b: Every Node in the linked list is exactly one space in memory away from the next. Making it possible to find the next Node and traverse through the list.
    :answer_c: Every Node in the list is in various locations in memory, and those memory addresses are stored in an array inside of the UnorderedList object, which makes accessing each Node possible.
    :answer_d: Every Node in the list is in various locations in memory, and each Node contains a pointer to the next Node in the list without needing to be contained in the UnorderedList class.
    :correct: d
    :feedback_a: Wrong! An UnorderedList class object will only reference the first item of the linked list.
    :feedback_b: Wrong! A Node in a linked list can be in various locations in memory. This is very important to understand how linked lists operate.
    :feedback_c: Wrong! While every Node can and will likely be in various locations in memory, all those locations will not be contained in the UnorderedList class object.
    :feedback_d: Correct! An unordered linked list class object will have a pointer to the first Node of the list. That Node will contain a pointer to the second Node of the list, and so on.
    :pct_on_first: 0.5752212389
    :total_students_attempting: 113
    :num_students_correct: 112
    :mean_clicks_to_correct: 1.7410714286

    Select the correct statement below.