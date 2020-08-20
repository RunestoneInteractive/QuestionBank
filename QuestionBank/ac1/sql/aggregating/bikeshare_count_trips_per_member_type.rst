.. activecode:: bikeshare_count_trips_per_member_type
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
     member_type,
     COUNT(*) AS n_trips
   FROM
     trip_data
   GROUP BY
     member_type