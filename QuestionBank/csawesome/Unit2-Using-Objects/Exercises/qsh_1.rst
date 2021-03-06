.. mchoice:: qsh_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: II and IV
   :answer_b: II, III, and IV
   :answer_c: I, II, III, IV
   :answer_d: II only
   :answer_e: IV only
   :correct: b
   :feedback_a: III is also correct.
   :feedback_b: String overrides equals to check if the two string objects have the same characters. The == operator checks if two object references refer to the same object. So II is correct since s1 and s2 have the same characters. Number II is correct since s3 and s1 are referencing the same string, so they will be ==. And s2 and s3 both refer to string that have the same characters so equals will be true in IV. The only one that will not be true is I, since s1 and s2 are two different objects (even though they have the same characters).
   :feedback_c: I is not correct since s1 and s2 are two different objects (even though they have the same characters). If s1 and s2 were both referring to literals, then I would be correct, but the new operator forces a new object to be created.
   :feedback_d: III and IV are also correct.
   :feedback_e: II and III are also correct.
   :pct_on_first: 0.3568189745
   :total_students_attempting: 2867
   :num_students_correct: 2819.0
   :mean_clicks_to_correct: 2.1426037602

   Given the following code segment, which of the following is true?
   
   .. code-block:: java
   
     String s1 = new String("Hi There");
     String s2 = new String("Hi There");
     String s3 = s1;
   
     I.   (s1 == s2)
     II.  (s1.equals(s2))
     III. (s1 == s3)
     IV.  (s2.equals(s3))