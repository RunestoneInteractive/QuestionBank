.. mchoice:: stack_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: BasicDS
   :subchapter: ImplementingaStackinPython
   :topics: BasicDS/ImplementingaStackinPython
   :from_source: T
   :answer_a: "x"
   :answer_b: "y"
   :answer_c: "z"
   :answer_d: The stack is empty
   :correct: c
   :feedback_a: Remember that a stack is built from the bottom up.
   :feedback_b: Remember that a stack is built from the bottom up.
   :feedback_c: Good job.
   :feedback_d: Remember that a stack is built from the bottom up.
   :pct_on_first: 0.8333333333
   :total_students_attempting: 18
   :num_students_correct: 18
   :mean_clicks_to_correct: 1.2222222222

   Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?
   
   .. code-block:: python
   
    m = Stack()
    m.push("x")
    m.push("y")
    m.pop()
    m.push("z")
    m.peek()