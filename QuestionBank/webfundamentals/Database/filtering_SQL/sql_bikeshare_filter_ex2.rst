.. activecode:: sql_bikeshare_filter_ex2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Database
    :subchapter: filtering_SQL
    :topics: Database/filtering_SQL
    :from_source: T
    :language: sql
    :autograde: unittest
    :dburl: /runestone/books/published/webfundamentals/_static/bikeshare.db
    :pct_on_first: 0.4957983193
    :total_students_attempting: 119
    :num_students_correct: 115
    :mean_clicks_to_correct: 2.7739130435

    Get the ending station and the duration of all of the bike trips originating at station ``31111`` that lasted 8 hours or more.
    ~~~~
    
    
    ====
    assert 20,0 == 31100
    assert 20,1 == 40733
    assert 0,0 == 31202
    assert 0,1 == 45722