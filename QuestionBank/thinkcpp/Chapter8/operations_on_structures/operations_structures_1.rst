.. clickablearea:: operations_structures_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: operations_on_structures
    :topics: Chapter8/operations_on_structures
    :from_source: T
    :question: Click on all incorrect statements.
    :iscode: 
    :feedback: Remember, this syntax can be used only in an initialization, not in an assignment statement.
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.5

    :click-incorrect:int main() {:endclick:
        :click-incorrect:Point blank = { 3.0, 4.0 };:endclick:
        :click-incorrect:Point hello;:endclick:
        :click-correct:hello = { 3.0, 4.0 };:endclick:
        :click-incorrect:Point new;:endclick:
        :click-incorrect:new = (Point){3.0, 4.0};:endclick:
        :click-correct:new = {3.0, 4.0};:endclick:
    }