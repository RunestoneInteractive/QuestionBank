.. mchoice:: JP_AP2-5-4
    :author: John Pataracchia
    :difficulty: 0.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: practice-test-objects
    :topics: Unit2-Using-Objects/practice-test-objects
    :from_source: F
    :random: 
    :answer_a: int x = oneThing(2, 10) + anotherThing(5, 2);
    :answer_b: int x = oneThing(10, 2) + anotherThing(2, 5);
    :answer_c: int x = oneThing(2, 10) + anotherThing(3, 2);
    :answer_d: int x = oneThing(6, 3) + anotherThing(2, 10);
    :answer_e: int x = oneThing(0, 2) + anotherThing(20, 1);
    :correct: a
    :feedback_a: oneThing(2,10) returns 2*10 = 20 and anotherThing(5,2) returns 5/2 = 2.5 truncated to 2 with integer division, which adds up to 22.
    :feedback_b: This would return 20 + 0 (which is 0.4 truncated) = 20.
    :feedback_c: This would return 20 + 1 (which is 1.5 truncated) = 21.
    :feedback_d: This would return 18 + 0 = 18.
    :feedback_e: This would return (0 * 2 = 0) + (20/1 = 20) = 20.
    :pct_on_first: 0.3714285714
    :total_students_attempting: 35
    :num_students_correct: 33.0
    :mean_clicks_to_correct: 2.4545454545

    Consider the following methods, which appear in the same class.
    
    .. code-block:: java
    
        public int oneThing(int i, int j)
        {
            return i * j;
        }
    
        public int anotherThing(int i, int j)
        {
            return i / j;
        }
    
    Which of the following statements, if located in a method in the same class, will initialize the variable x to 22?