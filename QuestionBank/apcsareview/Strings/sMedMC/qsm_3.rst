.. mchoice:: qsm_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Strings
   :subchapter: sMedMC
   :topics: Strings/sMedMC
   :from_source: T
   :answer_a: null
   :answer_b: hi there
   :answer_c: HI THERE
   :answer_d: Hi There
   :answer_e: hI tHERE
   :correct: d
   :feedback_a: This would be true if we had s1 = s4 after s4 = null was executed. Strings are immutable and so any changes to a string returns a new string.
   :feedback_b: This would only be correct if we had s1 = s2 after s2.toLowerCaase() was executed. Strings are immutable and so any change to a string returns a new string.
   :feedback_c: This would be correct if we had s1 = s3 after s3.toUpperCase() was executed. String are immutable and so any change to a string returns a new string.
   :feedback_d: Strings are immutable meaning that any changes to a string creates and returns a new string, so the string referred to by s1 does not change.
   :feedback_e: Strings are immutable and so any changes to a string returns a new string.

   Given the following code segment, what is the value of s1 after the code executes?

   .. code-block:: java

     String s1 = "Hi There";
     String s2 = s1;
     String s3 = s2;
     String s4 = s1;
     s2 = s2.toLowerCase();
     s3 = s3.toUpperCase();
     s4 = null;