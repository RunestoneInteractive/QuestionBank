.. mchoice:: HASH_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: SearchHash
   :subchapter: Hashing
   :topics: SearchHash/Hashing
   :from_source: T
   :correct: b
   :answer_a: 100, __, __, 113, 114, 105, 121, 117, 97, 108, 99
   :answer_b: 99, 100, 121, 113, 114, __, __, 117, 105, 97, 108
   :answer_c: 100, 113, 117, 97, 14, 108, 121, 105, 99, __, __
   :answer_d: 117, 114, 108, 121, 105, 99, __, __, 97, 100, 113
   :feedback_a: It looks like you may have been doing modulo 2 arithmentic.  You need to use the hash table size as the modulo value.
   :feedback_b: Using modulo 11 arithmetic and linear probing gives these values
   :feedback_c: It looks like you are using modulo 10 arithmetic, use the table size.
   :feedback_d: Be careful to use modulo not integer division.
   :pct_on_first: 0.5409836066
   :total_students_attempting: 122
   :num_students_correct: 121
   :mean_clicks_to_correct: 1.8016528926

   Suppose you are given the following set of keys to insert into a hash table that holds exactly 11 values:  113 , 117 , 97 , 100 , 114 , 108 , 121 , 105 , 99 Which of the following best demonstrates the contents of the hash table after all the keys have been inserted using linear probing?