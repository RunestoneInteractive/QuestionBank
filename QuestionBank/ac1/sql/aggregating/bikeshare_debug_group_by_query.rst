.. activecode:: bikeshare_debug_group_by_query
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: aggregating
   :topics: sql/aggregating
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   Find and fix the error(s) in the following code, which is trying to calculate
   the mean trip duration for trips by member type Member.
   ~~~

   SELECT
     AVG(duration)
   FROM
     trip_data
   GROUP BY
     member_type
   ====
   assert 0,0 == 772.0053481492348