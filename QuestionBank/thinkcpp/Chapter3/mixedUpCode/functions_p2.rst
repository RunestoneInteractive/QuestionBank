.. parsonsprob:: functions_p2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: mixedUpCode
   :topics: Chapter3/mixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 5.0

   Your final grade is determined by a midterm component (each midterm
   is worth 20% of the grade) and a final component. In order to avoid
   any discrepancies with students who's grades are on the fence, your
   teacher follows this strict grading scale: [0,60) = F, [60, 70) = D,
   [70, 80) = C, [80, 90) = B and [90, 100] = A. He does not round until
   the very end.
   Construct a function that determines a student's final grade according
   to this grading scheme and prints the result.
   -----
   void finalGrade (double m1, double m2, double f) {
   =====
   void finalGrade (double m1, m2, f) { #paired
   =====
    double m_comp = m1 * 0.2 + m2 * 0.2;
    double f_comp = f * 0.06;
   =====
    int m_comp = m1 * 0.2 + m2 * 0.2; #paired
    int f_comp = f * 0.06;
   =====
    double final_grade = m_comp + f_comp;
   =====
    cout << int(final_grade);
   =====
    cout << int(final_grade) + 1; #paired
   =====
    cout << final_grade; #paired
   =====
   }