.. activecode:: sql_bikeshare_agg_4
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/aggregation_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db


    SELECT
      member_type, SUM(duration)
    FROM
      trip_data
    GROUP BY
      member_type
    LIMIT
      10