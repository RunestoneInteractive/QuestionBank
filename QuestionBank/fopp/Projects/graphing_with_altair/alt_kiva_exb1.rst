.. activecode:: alt_kiva_exb1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: graphing_with_altair
    :topics: Projects/graphing_with_altair
    :from_source: T
    :nocodelens:

    import altair

    data = altair.Data(customer=['Alice', 'Bob', 'Claire'], cakes=[5,9,7], flavor=['chocolate', 'vanilla', 'strawberry'])
    print(data)