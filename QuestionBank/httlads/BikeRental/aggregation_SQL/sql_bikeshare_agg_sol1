.. activecode:: sql_bikeshare_agg_sol1
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/aggregation_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
    start_station, AVG(duration)
    FROM
    trip_data
    GROUP BY
    start_station
    ORDER BY
    AVG(duration) DESC
    LIMIT
    10