.. activecode:: sql_bikeshare_intro_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: bike_data_starter
    :topics: PredictiveAnalytics/bike_data_starter
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, start_date, duration
    FROM
      trip_data
    LIMIT
      10