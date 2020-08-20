.. mchoice:: mc_pntrhlp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: AtomicData
   :subchapter: AtomicData
   :topics: AtomicData/AtomicData
   :from_source: T
   :answer_a: varPntr: 9
   :answer_b: varPntr: 50
   :answer_c: varPntr: 150
   :answer_d: 0x7ffeb9ce053c
   :answer_e: none of the above
   :correct: b
   :feedback_a: Not quite, the variable varN no longer equals 100 past line 7!
   :feedback_b: Right!
   :feedback_c: No, the values do not add together!
   :feedback_d: We are dereferencing the pointer, so you would not get the address of varN. Try again!
   :feedback_e: One of the above is indeed correct.

   If the lines (varN = 50;) and  (cout << \*ptrN << endl;) were inserted into line 7-8, what would it cout?