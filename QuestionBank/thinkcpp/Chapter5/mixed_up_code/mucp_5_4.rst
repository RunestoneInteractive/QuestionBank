.. parsonsprob:: mucp_5_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: mixed_up_code
   :topics: Chapter5/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Let's write the code for the ``triangleArea`` function. ``triangleArea``
   takes two ``double`` parameters, ``base`` and ``height``. It returns the
   area of the triangle using the formula 1/2 * base * height.
   Put the necessary blocks of code in the correct order.
   -----
   double triangleArea (double base, double height) {
   =====
   int triangleArea (double base, double height) {  #distractor
   =====
   void triangleArea (double base, double height) {  #distractor
   =====
   double triangleArea (base, height) {  #distractor
   =====
      double area;  #distractor
   =====
      return 0.5 * base * height;
   =====
      cout << 0.5 * base * height << endl;  #distractor
   =====
   }