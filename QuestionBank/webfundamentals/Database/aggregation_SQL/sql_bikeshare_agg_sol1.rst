.. activecode:: sql_bikeshare_agg_sol1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Database
    :subchapter: aggregation_SQL
    :topics: Database/aggregation_SQL
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