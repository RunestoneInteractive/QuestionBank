.. shortanswer:: bikeshare_explain_join
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: joining
   :topics: sql/joining
   :from_source: T

   What question is the following query answering?

   .. code-block:: sql

      SELECT
        trips.start_station,
        AVG(duration) AS mean_duration
      FROM
        trips_data AS trips
      INNER JOIN
        bikeshare_stations AS stations
      ON
        trips.start_station = stations.station_id
      WHERE
        stations.status = 'closed'