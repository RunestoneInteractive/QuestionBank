.. activecode:: bikeshare_count_star
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
     COUNT(*) AS n_rows
   FROM
     trip_data