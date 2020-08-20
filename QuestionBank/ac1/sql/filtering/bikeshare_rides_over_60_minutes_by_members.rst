.. activecode:: bikeshare_rides_over_60_minutes_by_members
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: filtering
   :topics: sql/filtering
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     member_type,
     start_date,
     duration
   FROM
     trip_data
   WHERE
     duration >= 3600 AND
     member_type = 'Member'
   LIMIT
     10