.. activecode:: alt_kiva_bar2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: graphing_with_altair
    :topics: Projects/graphing_with_altair
    :from_source: T
    :nocodelens:

    import altair

    data = altair.Data(customer=['Alice', 'Bob', 'Claire', 'Drake', 'Emma','Alice', 'Emma', 'Ginger'],
        cakes=[5,9,7,10,82,70,42,64],
        flavor=['chocolate', 'vanilla', 'strawberry','chocolate','vanilla','strawberry','chocolate','strawberry'])
    chart = altair.Chart(data)
    mark = chart.mark_bar()
    enc = mark.encode(x='customer:N',y='cakes',color='flavor:N')
    enc.display()