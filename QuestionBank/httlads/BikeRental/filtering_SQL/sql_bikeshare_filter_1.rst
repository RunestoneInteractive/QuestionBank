.. activecode:: sql_bikeshare_filter_1
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/filtering_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, start_date, duration
    FROM
      trip_data
    WHERE
      duration >= 3600
    LIMIT
      10