.. mchoice:: mctree_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Trees
   :subchapter: ListofListsRepresentation
   :topics: Trees/ListofListsRepresentation
   :from_source: T
   :correct: c
   :answer_a: ["a", ["b", [], []], ["c", [], ["d", [], []]]]
   :answer_b: ["a", ["c", [], ["d", ["e", [], []], []]], ["b", [], []]]
   :answer_c: ["a", ["b", [], []], ["c", [], ["d", ["e", [], []], []]]]
   :answer_d: ["a", ["b", [], ["d", ["e", [], []], []]], ["c", [], []]]
   :feedback_a: Not quite, this tree is missing the "e" node.
   :feedback_b: This is close, but if you carefully you will see that the left and right children of the root are swapped.
   :feedback_c: Very good
   :feedback_d: This is close, but the left and right child names have been swapped along with the underlying structures.
   :pct_on_first: 1.0
   :total_students_attempting: 3
   :num_students_correct: 3
   :mean_clicks_to_correct: 1.0

   Given the following statments:
   
   .. sourcecode:: python
   
       x = make_binary_tree("a")
       insert_left(x, "b")
       insert_right(x, "c")
       insert_right(get_right_child(x), "d")
       insert_left(get_right_child(get_right_child(x)), "e")
   
   Which of the answers is the correct representation of the tree?