.. mchoice:: queue_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: ImplementingaQueueCpp
   :topics: LinearBasic/ImplementingaQueueCpp
   :from_source: T
   :correct: b
   :answer_a: 10, 20
   :answer_b: 20, 30
   :answer_c: 10, 30
   :answer_d: 10, 20, 30
   :feedback_a: Remember the first item added to the queue is the first item removed. Remember FIFO.
   :feedback_b: Yes, first in first out means that the 10 is now gone.
   :feedback_c: Queues and stacks are both data structures where you can only access the first or the last items.
   :feedback_d: Oops, maybe you missed the pop call at the end?
   :pct_on_first: 0.6558441558
   :total_students_attempting: 154
   :num_students_correct: 154
   :mean_clicks_to_correct: 1.4155844156

   Suppose you have the following series of queue operations.
   
   ::
   
       queue<int> q;
       q.push(10);
       q.push(20);
       q.push(30);
       q.pop();
   
   What items are left on the queue?