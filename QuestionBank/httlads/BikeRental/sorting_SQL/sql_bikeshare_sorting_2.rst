.. activecode:: sql_bikeshare_sorting_2
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/sorting_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, start_date, duration
    FROM
      trip_data
    ORDER BY
      duration DESC
    LIMIT
      10