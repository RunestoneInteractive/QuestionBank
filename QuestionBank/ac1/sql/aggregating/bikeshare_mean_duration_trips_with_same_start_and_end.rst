.. activecode:: bikeshare_mean_duration_trips_with_same_start_and_end
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: aggregating
   :topics: sql/aggregating
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   For the station with the most trips that started and ended at the same
   station, find the mean duration (in seconds) of all trips, rounded to the
   nearest whole number.
   ~~~~

   ====
   assert 0,0 == 31217
   assert 0,3 == 5164