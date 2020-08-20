.. clickablearea:: values2.0
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter2
    :subchapter: Values
    :topics: Chapter2/Values
    :from_source: T
    :question: Click on all integer VALUES.
    :iscode: 
    :feedback: Try again!
    :pct_on_first: 0.3333333333
    :total_students_attempting: 3
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 2.0

    :click-incorrect:int main() {:endclick:
        :click-incorrect:int x:endclick: = :click-correct:7:endclick:;
        :click-incorrect:char c:endclick: = :click-incorrect:'8':endclick:;
        while (:click-incorrect:x:endclick: < :click-correct:10:endclick:) {
            cout << :click-incorrect:c:endclick: << endl;
            :click-incorrect:x:endclick:++;
        }
        :click-incorrect:c:endclick: = :click-incorrect:'9':endclick:;
        cout << ":click-incorrect:It's the year:endclick: :click-incorrect:3000:endclick:!";
        cout << :click-incorrect:"Just kidding, it's ":endclick: << :click-correct:2020:endclick: << "!";
    }