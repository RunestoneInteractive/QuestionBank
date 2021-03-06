.. mchoice:: HASH_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: SortSearch
   :subchapter: Hashing
   :topics: SortSearch/Hashing
   :from_source: T
   :correct: b
   :answer_a: 100, __, __, 113, 114, 105, 116, 117, 97, 108, 99
   :answer_b: 99, 100, __, 113, 114, __, 116, 117, 105, 97, 108
   :answer_c: 100, 113, 117, 97, 14, 108, 116, 105, 99, __, __
   :answer_d: 117, 114, 108, 116, 105, 99, __, __, 97, 100, 113
   :feedback_a: It looks like you may have been doing modulo 2 arithmentic.  You need to use the hash table size as the modulo value.
   :feedback_b: Using modulo 11 arithmetic and linear probing gives these values
   :feedback_c: It looks like you are using modulo 10 arithmetic, use the table size.
   :feedback_d: Be careful to use modulo not integer division.
   :pct_on_first: 0.6636744464
   :total_students_attempting: 1671
   :num_students_correct: 1651.0
   :mean_clicks_to_correct: 1.5015142338

   Suppose you are given the following set of keys to insert into a hash table that holds exactly 11 values:  113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99 Which of the following best demonstrates the contents of the hash table after all the keys have been inserted using linear probing?