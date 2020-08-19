.. activecode:: sql_bikeshare_agg_3
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/aggregation_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, start_station, count(*)
    FROM
      trip_data
    WHERE
      member_type = 'Casual'
    GROUP BY
      member_type, start_station
    ORDER BY
      COUNT(*) DESC
    LIMIT
      20