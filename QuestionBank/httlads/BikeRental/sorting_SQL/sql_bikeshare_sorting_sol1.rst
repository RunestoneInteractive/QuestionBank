.. activecode:: sql_bikeshare_sorting_sol1
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/sorting_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
    duration, start_station, end_station
    FROM
    trip_data
    WHERE
    duration >= 3600
    ORDER BY
    duration DESC
    LIMIT
    40