.. clickablearea:: rec_base1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit11-Recursion
    :subchapter: topic-11-1-recursion-day1
    :topics: Unit11-Recursion/topic-11-1-recursion-day1
    :from_source: T
    :question: Click on the line or lines that contain the test for the base case
    :iscode:
    :feedback: When a base case test is true a value is returned and the recursion stops.


    :click-incorrect:public static int factorial(int n):endclick:
    :click-incorrect:{:endclick:
        :click-correct:if (n == 0):endclick:
            :click-incorrect:return 1;:endclick:
        :click-incorrect:else:endclick:
            :click-incorrect:return n * factorial(n-1);:endclick:
    :click-incorrect:}:endclick: