.. activecode:: bikeshare_mean_duration_for_casual_member_type
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: aggregating
   :topics: sql/aggregating
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     AVG(duration)
   FROM
     trip_data
   WHERE
     member_type = 'Casual'