.. activecode:: bikeshare_order_by_multiple_columns
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: sorting
   :topics: sql/sorting
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     start_station,
     end_station,
     duration
   FROM
     trip_data
   ORDER BY
     start_station ASC,
     end_station ASC,
     duration DESC
   LIMIT
     10