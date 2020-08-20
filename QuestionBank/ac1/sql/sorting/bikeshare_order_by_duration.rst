.. activecode:: bikeshare_order_by_duration
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
     *
   FROM
     trip_data
   ORDER BY
     duration DESC
   LIMIT
     10