.. shortanswer:: bikeshare_name_and_explain_if_query
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: ifs_and_cases
   :topics: sql/ifs_and_cases
   :from_source: T

   Give meaningful names to the columns in the following query and explain what
   question th query is trying to answer.

   .. code-block:: sql

      SELECT
        IF(duration > 0.5 * 3600, TRUE, FALSE) AS column_1,
        SUM(IF(start_station = 31111, 1, 0)) AS column_2
      FROM
        trip_data
      GROUP BY
        column_1