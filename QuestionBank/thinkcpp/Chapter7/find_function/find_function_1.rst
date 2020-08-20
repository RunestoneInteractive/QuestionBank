.. clickablearea:: find_function_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: find_function
    :topics: Chapter7/find_function
    :from_source: T
    :question: Click on the name of each variable that had been initialized with the value of 0.
    :iscode: 
    :feedback: Remember that the index of a string begins at 0, not 1.
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    :click-incorrect:def main() {::endclick:
        :click-incorrect:string fruit = "apple";:endclick:
        int:click-incorrect: index_a :endclick:= fruit.find('e');
        int:click-correct: index_b :endclick:= fruit.find("app");
        int:click-correct: index_c :endclick:= fruit.find('a');
        int:click-incorrect: index_d :endclick:= fruit.find('l');
    }