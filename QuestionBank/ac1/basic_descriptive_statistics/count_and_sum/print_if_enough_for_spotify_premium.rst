.. fillintheblank:: print_if_enough_for_spotify_premium
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: basic_descriptive_statistics
   :subchapter: count_and_sum
   :topics: basic_descriptive_statistics/count_and_sum
   :from_source: T

   Suppose cell B1 contains the amount of money between you and your friends.
   Write a formula to check if this amount is enough for Spotify Premium. If it
   is enough, the result should evaluate ``TRUE``, otherwise ``FALSE``.

   - :=IF\(B1>=15, TRUE, FALSE\): Correct
     :=IF\(B1>15, TRUE, FALSE\): Incorrect: Remember to print ``TRUE`` if B1=15.
     :IF\(B1>=15, TRUE, FALSE\): Incorrect: Formulas must start with ``=``.
     :x: Incorrect