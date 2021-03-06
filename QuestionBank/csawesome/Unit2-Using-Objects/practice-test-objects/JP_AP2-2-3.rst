.. mchoice:: JP_AP2-2-3
   :author: John Pataracchia
   :difficulty: 2.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: practice-test-objects
   :topics: Unit2-Using-Objects/practice-test-objects
   :from_source: F
   :random: 
   :answer_a: I only
   :answer_b: I and II
   :answer_c: II and III
   :answer_d: II only
   :answer_e: I, II, and III
   :correct: c
   :feedback_a: I needs to initialize the object variable with a call to new BaseballLeague().
   :feedback_b: I needs to initialize the object variable with a call to new BaseballLeague().
   :feedback_c: Correct!
   :feedback_d: III  is also a correct answer.
   :feedback_e: I needs to initialize the object with a call to new BaseballLeague().
   :pct_on_first: 0.5
   :total_students_attempting: 46
   :num_students_correct: 42.0
   :mean_clicks_to_correct: 1.9523809524

    Which of the following code segments correctly creates an instance of a new BaseballLeague object?
   
    .. code-block:: java
   
        public class BaseballLeague
        {
            private int numTeams;
            private boolean refsHired;
   
            public BaseballLeague()
            {
                numTeams = 4;
                refsHired = false;
            }
   
            public BaseballLeague(int teams)
            {
                numTeams = teams;
                refsHired = false;
            }
        }
        I.   BaseballLeague myLeague;
        II.  int numOfTeams = 6;
             BaseballLeague yourTeam = new BaseballLeague(numOfTeams + 6);
        III. int teamCount = 16;
             BaseballLeague ourTeam = new BaseballLeague(teamCount);