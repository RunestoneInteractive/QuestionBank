.. activecode:: bikeshare_count_trips_above_below_one_hour
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: ifs_and_cases
   :topics: sql/ifs_and_cases
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     IF(duration > 3600, TRUE, FALSE) AS is_over_one_hour,
     COUNT(*) AS n_trips
   FROM
     bikeshare_stations
   GROUP BY
     is_over_one_hour