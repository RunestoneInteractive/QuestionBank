.. shortanswer:: bikeshare_explain_group_by_query
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: aggregating
   :topics: sql/aggregating
   :from_source: T

   Explain what the following query will return.

   .. code-block:: sql

      SELECT
        start_station,
        AVG(duration) AS mean_duration
      FROM
        trip_data
      WHERE
        duration >= 3600
      GROUP BY
        start_station
      ORDER BY
        AVG(duration) DESC