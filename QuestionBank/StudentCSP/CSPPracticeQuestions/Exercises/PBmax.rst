.. parsonsprob:: PBmax
    :author: Renske Weeda
    :difficulty: 0.0
    :basecourse: StudentCSP
    :chapter: CSPPracticeQuestions
    :subchapter: Exercises
    :topics: CSPPracticeQuestions/Exercises
    :from_source: F
    :numbered: left
    :language: java
    :pct_on_first: 0.0
    :total_students_attempting: 19
    :num_students_correct: 7.0
    :mean_clicks_to_correct: 15.7142857143

    The following program segment should count and print the highest value in the array. Rearrange the blocks into the correct order and complete the program.
    -----
    int[] l = {20,24,23,35,30,35};
    =====
    int b=l[0];
    =====
    for( int i=0; i < l.length; i++ ){
    =====
       if( l[i] > b ){
    =====
          b=l[i];
    =====
       }
    =====
    }
    =====
    System.out.println(b);
    =====