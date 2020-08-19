.. parsonsprob:: functions_p8
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

   In Michigan, the probability that it snows on any given day
   in the winter is about 14%.  The probability of having a snow day
   on any given day in the winter is about 4%.  The probability that
   is snows and you have a snow day is 8%.  Construct and call a
   function that calculates the probability of a having a snow day,
   given the fact that it will snow tonight.
   -----
   void conditionalProb (double B, double union) {
   =====
   void conditionalProb (double B, union) { #paired
   =====
    double prob = union / B;
   =====
    double prob = B / union; #paired
   =====
    cout << prob;
   =====
   } //conditionalProb
   =====
   int main () {
   =====
    double pSnow = 0.14;
    double pSnowday = 0.04;
    double pBoth = 0.08;
   =====
    conditionalProb(pSnow, pBoth);
   =====
    conditionalProb(pSnowday, pBoth); #paired
   =====
    conditionalProb(pSnowday, pSnow); #paired
   =====
   } //main