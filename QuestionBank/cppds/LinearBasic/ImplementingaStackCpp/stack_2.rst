.. mchoice:: stack_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: ImplementingaStackCpp
   :topics: LinearBasic/ImplementingaStackCpp
   :from_source: T
   :answer_a: 37
   :answer_b: the stack is empty
   :answer_c: an error will occur
   :answer_d: 4
   :correct: c
   :feedback_a: You may want to check out the docs for
   :feedback_b: There is an odd number of things on the stack but each time through the loop 2 things are popped.
   :feedback_c: Good Job, this is true because the stack can not evenly pop off every item within itself, because there is an odd number of items.
   :feedback_d: You may want to check out the docs for isEmpty
   :pct_on_first: 0.3703703704
   :total_students_attempting: 162
   :num_students_correct: 162
   :mean_clicks_to_correct: 2.0679012346

   Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?
   
   .. code-block:: cpp
   
     stack<int> m;
     m.push(37);
     m.push(56);
     m.push(4);
     while (!m.empty()){
         m.pop();
         m.pop();
     }