.. activecode:: bikeshare_subquery_mean_duration_open_stations
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: joining
   :topics: sql/joining
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   SELECT
     COUNT(*) AS n_trips
   FROM
     trip_data
   WHERE
     start_station IN (
       SELECT
         station_id
       FROM
         bikeshare_stations
       WHERE
         status = 'open'
     )