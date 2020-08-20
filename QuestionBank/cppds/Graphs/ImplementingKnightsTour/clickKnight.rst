.. clickablearea:: clickKnight
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Graphs
    :subchapter: ImplementingKnightsTour
    :topics: Graphs/ImplementingKnightsTour
    :from_source: T
    :question: What line denotes the base case of the Knight's Tour function?
    :iscode: 
    :feedback: Remember, the base case is usually the first comparison in the function!
    :pct_on_first: 0.2352941176
    :total_students_attempting: 17
    :num_students_correct: 14
    :mean_clicks_to_correct: 2.0714285714

    :click-incorrect:def knightTour(n,path,u,limit)::endclick:
    :click-incorrect:u.setColor('gray'):endclick:
    :click-incorrect:path.append(u):endclick:
    :click-correct:if n < limit::endclick:
        :click-incorrect:nbrList = list(u.getConnections()):endclick:
        :click-incorrect:i = 0:endclick:
        :click-incorrect:done = False:endclick:
        :click-incorrect:while i < len(nbrList) and not done::endclick:
            :click-incorrect:if nbrList[i].getColor() == 'white'::endclick:
                :click-incorrect:done = knightTour(n+1, path, nbrList[i], limit):endclick:
            :click-incorrect:i = i + 1:endclick:
        :click-incorrect:if not done:  # prepare to backtrack:endclick:
            :click-incorrect:path.pop():endclick:
            :click-incorrect:u.setColor('white'):endclick:
    :click-incorrect:else::endclick:
        :click-incorrect:done = True:endclick:
    :click-incorrect:return done:endclick: