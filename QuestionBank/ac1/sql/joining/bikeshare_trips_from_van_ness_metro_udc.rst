.. activecode:: bikeshare_trips_from_van_ness_metro_udc
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
     trip_data AS trips
   INNER JOIN
     bikeshare_stations AS stations
   ON
     trips.start_station = stations.station_id
   WHERE
     stations.name = 'Van Ness Metro / UDC'