.. activecode:: alt_kiva_hist1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: graphing_with_altair
    :topics: Projects/graphing_with_altair
    :from_source: T
    :nocodelens:

    import altair

    movie_ratings = [6.1, 6.9, 6.8, 3.4, 7.7, 3.8, 5.8, 7, 7, 7.5, 8.4, 6.8, 7, 6.1, 2.5, 8.9, 8.1, 7, 5.6, 6.3, 8.4, 6.9, 7.1, 5.7, 3.2, 6, 7.7, 6.4, 7, 7.1, 7.4, 6.8, 5.4, 4.9, 7.6, 4.6, 6.6, 5.6, 5.7, 7.1, 6.7, 7.3, 5.9, 3.2, 7.4, 7.6, 3.7, 6.8, 8.2, 6.1, 5.8, 8.4, 8.6, 6.2, 6.4, 5.1, 5.6, 4.4, 5.6, 5.7, 8.1, 5.4, 7.3, 5, 7.7, 6.9, 8.4, 7.5, 7.1, 8.2, 6.6, 6.4, 3.3, 5.7, 8.2, 8.2, 5.8, 8, 3.4, 8.2, 3.2, 5, 4.8, 7.3, 6.1, 5, 5.6, 6.1, 7.2, 8.4, 7.8, 4.3, 6.8, 4.9, 6.2, 8.3, 6.2, 7.9, 7.1, 7.3]

    data = altair.Data(ratings=movie_ratings)
    chart = altair.Chart(data)
    mark = chart.mark_bar()
    X = altair.Axis('ratings:Q', bin=True)
    Y = altair.Axis('count()')
    enc = mark.encode(x=X,y=Y)
    enc.display()