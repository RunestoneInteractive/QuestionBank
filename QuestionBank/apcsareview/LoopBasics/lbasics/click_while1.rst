.. clickablearea:: click_while1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: LoopBasics
    :subchapter: lbasics
    :topics: LoopBasics/lbasics
    :from_source: T
    :question: Click on all the statements that are part of the body of the while loop.  If you make a mistake you can click on the statement again to unhighlight it.
    :iscode:
    :feedback: Remember, the body of a loop is all the statements between the { and } after the while keyword or single statement following the while if there are no {}.

    :click-incorrect:int x = 5;:endclick:
    :click-incorrect:while (x > 0):endclick:
    :click-incorrect:{:endclick:
        :click-correct:System.out.println(x);:endclick:
        :click-correct:x = x - 1;:endclick:
    :click-incorrect:}:endclick: