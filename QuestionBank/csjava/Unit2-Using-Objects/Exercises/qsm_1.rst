.. mchoice:: qsm_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: F
   :practice: T
   :answer_a: I, II, III
   :answer_b: I only
   :answer_c: II only
   :answer_d: III only
   :answer_e: II and III only
   :correct: a
   :feedback_a: The "equals" operation on strings returns true when the strings have the same characters.  The == operator returns true when they refer to the same object.  In this case all three references actually refer to the same object so both == and equals will be true.
   :feedback_b: This is true, since s1 and s3 contain the same characters since s1 and s3 actually refer to the same string object. But, it isn't the only thing that is true.
   :feedback_c: This is true since s2 == s1.  But, it isn't the only thing that is true.
   :feedback_d: This is true since s3 == s2, and s2 == s1 so it follows that s1 == s3.  But, it isn't the only thing that is true.
   :feedback_e: This is true since they all refer to the same string object.  But, they also contain the same characters so equals is also true.

   After the following code is executed, which of I, II and/or III will evaluate to true?

   .. code-block:: java

     String s1 = "xyz";
     String s2 = s1;
     String s3 = s2;

     I.   s1.equals(s3)
     II.  s1 == s2
     III. s1 == s3