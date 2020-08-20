.. clickablearea:: rectangles_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: rectangles
    :topics: Chapter8/rectangles
    :from_source: T
    :question: Click on the legal ways to create a Point and Rectangle structure, assuming that the Point and Rectangle structures are declared above the main function in the same way as in the active code above.
    :iscode: 
    :feedback: Re-read the text above and try again.
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 7.0

    :click-incorrect:def main() {:endclick:
        :click-incorrect:Point corner = { 0.0, 0.0 );:endclick:
        :click-incorrect:Rectangle box = { ( 0.0, 0.0 ), 100.0, 200.0 }:endclick:
        :click-correct:Rectangle box = { { 0.0, 0.0 }, 100.0, 200.0 };:endclick:
        :click-correct:Point corner = { 0.0, 0.0 };:endclick:
        :click-correct:Rectangle box = { corner, 100.0, 200.0 };:endclick:
    }