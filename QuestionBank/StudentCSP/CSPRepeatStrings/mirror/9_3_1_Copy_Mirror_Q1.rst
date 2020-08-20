.. mchoice:: 9_3_1_Copy_Mirror_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatStrings
   :subchapter: mirror
   :topics: CSPRepeatStrings/mirror
   :from_source: T
   :answer_a: Make the phrase <code>"Time to panic!"</code>
   :answer_b: Change the <code>newString</code> in line 1 to <code>"!"</code> instead of <cod>""</code>
   :answer_c: Change the right hand side of line 4 to <code>letter + "!" + newstring + letter</code>
   :answer_d: Change the right hand side of line 4 to <code>letter + newstring + "!" + letter</code>
   :correct: b
   :feedback_a: That would give us <code>!cinaP ot emiTTime to Panic!</code>.
   :feedback_b: We can start our accumulator with something in it.
   :feedback_c: That would give us <code>!!c!i!n!a!P! !o!t! !e!m!i!T!Time to Panic!</code> -- exclamation points between the letters in the first half of the mirror.
   :feedback_d: That would give us <code>!cinaP ot emiT!T!i!m!e! !t!o! !P!a!n!i!c!!</code> -- exclamation points between the letters in the second half of the mirror.
   :pct_on_first: 0.474916388
   :total_students_attempting: 897
   :num_students_correct: 894.0
   :mean_clicks_to_correct: 2.0648769575

   Change the mirroring program to mirror the phrase ``"Time to Panic"`` with a single exclamation point in the middle, to make the printed words look like this: ``cinaP ot emiT!Time to Panic``.  How do you do it?