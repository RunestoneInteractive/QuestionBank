.. activecode:: bikeshare_order_by_duration_with_where_clause
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
     member_type,
     start_date
     end_station
   FROM
     trip_data
   WHERE
     start_station = 31111
   ORDER BY
     duration DESC
   LIMIT
     10