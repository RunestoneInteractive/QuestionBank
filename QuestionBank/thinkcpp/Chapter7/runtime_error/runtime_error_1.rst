.. clickablearea:: runtime_error_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: runtime_error
    :topics: Chapter7/runtime_error
    :from_source: T
    :question: Click on each spot that would cause a runtime error.
    :iscode: 
    :feedback: Remember, an index that is negative or greater than the length of the string - 1 will give a run-time error.
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    :click-incorrect:def main() {:endclick:
        :click-incorrect:string fruit = "apple";:endclick:
        char letter = :click-incorrect:fruit[0];:endclick:
        char letter = :click-correct:fruit[9];:endclick:
        :click-incorrect:cout << fruit << endl;:endclick:
        cout <<  :click-correct:fruit[-4]:endclick:  << endl;
        cout <<  :click-incorrect:fruit[4]:endclick:  << endl;
    }