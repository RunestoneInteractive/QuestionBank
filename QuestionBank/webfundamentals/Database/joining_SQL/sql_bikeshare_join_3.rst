.. activecode:: sql_bikeshare_join_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Database
    :subchapter: joining_SQL
    :topics: Database/joining_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      *
    FROM
      trip_data, bikeshare_stations
    WHERE
      start_station = station_id
    LIMIT
      10