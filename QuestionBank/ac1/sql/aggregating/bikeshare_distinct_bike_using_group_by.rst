.. activecode:: bikeshare_distinct_bike_using_group_by
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
     bike_number
   FROM
     trip_data
   GROUP BY
     bike_number