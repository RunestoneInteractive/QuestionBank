.. activecode:: bikeshare_min_and_max_trip_duration_by_start_station
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
     start_station,
     MIN(duration) AS minimum_duration,
     MAX(duration) AS maximum_duration
   FROM
     trip_data
   GROUP BY
     start_station