.. activecode:: sql_bikeshare_sorting_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: sorting_SQL
    :topics: PredictiveAnalytics/sorting_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, start_date, duration
    FROM
      trip_data
    ORDER BY
      duration
    LIMIT
      10