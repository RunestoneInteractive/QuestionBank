.. activecode:: sql_bikeshare_filter_sol1
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/filtering_SQL
    :from_source: T
    :language: sql
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db

    select * from trip_data where bike_number = 'W01274' and duration < 900