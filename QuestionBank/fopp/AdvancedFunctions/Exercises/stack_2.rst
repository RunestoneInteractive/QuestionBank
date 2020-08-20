.. mchoice:: stack_2
    :author: Andrew McDonald
    :difficulty: 1.0
    :basecourse: fopp
    :chapter: AdvancedFunctions
    :subchapter: Exercises
    :topics: AdvancedFunctions/Exercises
    :from_source: F
    :answer_a: 'x'
    :answer_b: the stack is empty
    :answer_c: an error will occur
    :answer_d: 'z'
    :correct: c
    :feedback_a: You may want to check out the docs for isEmpty
    :feedback_b: There is an odd number of things on the stack but each time through the loop 2 things are popped.
    :feedback_c: Good Job.
    :feedback_d: You may want to check out the docs for isEmpty
    :pct_on_first: 0.2173913043
    :total_students_attempting: 23
    :num_students_correct: 22.0
    :mean_clicks_to_correct: 2.4090909091

    Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?
    
    .. code-block:: python
    
        m = Stack()
        m.push('x')
        m.push('y')
        m.push('z')
        while not m.isEmpty():
            m.pop()
            m.pop()