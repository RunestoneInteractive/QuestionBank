.. activecode:: sql_bikeshare_join_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: joining_SQL
    :topics: PredictiveAnalytics/joining_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      COUNT(*)
    FROM
      trip_data, bikeshare_stations
    WHERE
      start_station = station_id