.. mchoice:: queue_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: ImplementingaQueueinPython
   :topics: BasicDS/ImplementingaQueueinPython
   :from_source: T
   :correct: b
   :answer_a: 'hello', 'dog'
   :answer_b: 'dog', 3
   :answer_c: 'hello', 3
   :answer_d: 'hello', 'dog', 3
   :feedback_a: Remember the first thing added to the queue is the first thing removed.  FIFO
   :feedback_b: Yes, first in first out means that hello is gone
   :feedback_c: Queues, and Stacks are both data structures where you can only access the first and the last thing.
   :feedback_d: Ooops, maybe you missed the dequeue call at the end?
   :pct_on_first: 0.7342064715
   :total_students_attempting: 2596
   :num_students_correct: 2583.0
   :mean_clicks_to_correct: 1.3712737127

   Suppose you have the following series of queue operations.
   
   ::
   
       q = Queue()
       q.enqueue('hello')
       q.enqueue('dog')
       q.enqueue(3)
       q.dequeue()
   
   What items are left on the queue?