.. activecode:: bikeshare_filter_and_group_by_different_columns
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
     SUM(duration) AS total_duration
   FROM
     trip_data
   WHERE
     end_station = 31111
   GROUP BY
     start_station