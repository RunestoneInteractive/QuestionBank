.. activecode:: bikeshare_count_distinct_bikes
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
     COUNT(DISTINCT bike_number) AS n_distinct_bikes
   FROM
     trip_data