.. activecode:: bikeshare_where_with_aggregation
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
     COUNT(*) AS n_trips
   FROM
     trip_data
   WHERE
     COUNT(*) > 100
   GROUP BY
     start_station