.. activecode:: sql_bikeshare_agg_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: aggregation_SQL
    :topics: PredictiveAnalytics/aggregation_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    SELECT
      member_type, COUNT(*)
    FROM
      trip_data
    GROUP BY
      member_type
    ORDER BY
      COUNT(*) DESC
    LIMIT
      10