.. activecode:: bikeshare_select_columns
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: selecting
   :topics: sql/selecting
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     member_type,
     start_date,
     duration
   FROM
     trip_data
   LIMIT
     10