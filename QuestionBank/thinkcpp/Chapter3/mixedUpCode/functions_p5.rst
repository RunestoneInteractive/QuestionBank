.. parsonsprob:: functions_p5
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
   :mean_clicks_to_correct: 3.0

   Suppose you have already defined a function called sumOfSquares which
   returns the sum of the squares of two numbers and root which returns the
   square root of a number.  Construct a function that calculates the hypotenuse
   of the right triangle and prints the three sidelengths.
   -----
   int main () {
   =====
    double s1 = 4.8;
    double s2 = 3.8;
   =====
    int s1 = 4.8; #paired
    int s2 = 3.6;
   =====
    double sqSum = sumOfSquares(s2, s1);
   =====
    sqSum = sumOfSquares(s1, s2); #paired
   =====
    double hyp = root(sqSum);
   =====
    double hyp = root(s1, s2); #paired
   =====
    cout << "The sides of the triangle are: " << s1 << ", " << s2 << ", " << hyp;
   =====
    cout << "The sides of the triangle are: " << s1 << ", " << s2 << ", " << s3; #paired
   =====
   }