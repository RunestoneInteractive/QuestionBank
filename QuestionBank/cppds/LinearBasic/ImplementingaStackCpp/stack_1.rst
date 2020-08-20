.. mchoice:: stack_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: ImplementingaStackCpp
   :topics: LinearBasic/ImplementingaStackCpp
   :from_source: T
   :answer_a: 5
   :answer_b: 12
   :answer_c: 27
   :answer_d: The stack is empty
   :correct: c
   :feedback_a: Remember that a stack is built from the bottom up.
   :feedback_b: pay attention to the line that says m.pop();.
   :feedback_c: Good job. This is correct because the 12 was poped of from the end and the 27 was pushed.
   :feedback_d: This would mean everyting is removed from the stack, when does that happen?
   :pct_on_first: 0.8650306748
   :total_students_attempting: 163
   :num_students_correct: 163
   :mean_clicks_to_correct: 1.1595092025

   Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?
   
   .. code-block:: cpp
   
    stack<int> m;
    m.push(5);
    m.push(12);
    m.pop();
    m.push(27);
    cout << m.top();