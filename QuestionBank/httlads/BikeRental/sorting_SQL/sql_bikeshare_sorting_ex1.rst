.. activecode:: sql_bikeshare_sorting_ex1
    :author: bmiller
    :difficulty: 3
    :basecourse: httlads
    :topics: BikeRental/sorting_SQL
    :from_source: T
    :language: sql
    :autograde: unittest
    :dburl: /runestone/books/published/httlads/_static/bikeshare.db
    :pct_on_first: 0.1111111111
    :total_students_attempting: 108
    :num_students_correct: 85
    :mean_clicks_to_correct: 9.2588235294

    Get the duration, start station ID, and end station ID for bike trips that are 60 minutes or longer, in the order of largest number of seconds first and display the top 40 results.
    ~~~~
    
    
    ====
    assert 39,0 == 84190
    assert 39,2 == 31018