.. activecode:: sql_bikeshare_filter_sol1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: filtering_SQL
    :topics: PredictiveAnalytics/filtering_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    select * from trip_data where bike_number = 'W01274' and duration < 900