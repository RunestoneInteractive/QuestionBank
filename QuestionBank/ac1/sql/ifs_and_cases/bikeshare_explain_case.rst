.. shortanswer:: bikeshare_explain_case
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: ifs_and_cases
   :topics: sql/ifs_and_cases
   :from_source: T

   Explain what the following query is returning.

   .. code-block:: sql

      SELECT
        CASE
          WHEN member_type = 'Casual' AND start_station = end_station THEN "casual_same_station"
          WHEN start_station = end_station THEN "member_same_station"
          WHEN member_type = 'Casual' THEN "casual_different_station"
          ELSE "member_different_station"
        END AS ride_classification,
        AVG(IF(duration > 3600, 1, 0)) AS proportion_trips_over_one_hour
      FROM
        trip_data
      WHERE
        member_type IN ('Casual', 'Member')
      GROUP BY
        ride_classification