.. mchoice:: mce_6_9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter6
    :subchapter: Exercises
    :topics: Chapter6/Exercises
    :from_source: T
    :practice: T

    The super evil villian RePete wants to annoy the city by
    hacking into the city's helper robots and making them repeat
    everything they say 5 times. However, there's an error in his
    code and now the robots won't stop repeating! Can you find the
    error?

    .. code-block:: cpp

     void repeatBot (string input) {
       int n = 0;
       while (n < 5) {
         cout << input << " ";
         n--;
       }
     }

     int main() {
       repeatBot ("Hello, how may I help you?");
     }

    - ``repeatBot`` can only take one word as an argument.

      - A ``string`` is any number of characters or words surrounded by double quotes, not just one word.

    - Since ``n`` is declared to be 0, 0 is always less than 5, so the code loops infinitely.

      - The code doesn't loop infinitely because of the value ``n`` was declared to be.

    - Every time the ``while`` loop runs, ``n`` is reset to 0, so it will always be less than 5.

      - The initialization of ``n`` occurs outside the ``while`` loop, so the value of ``n`` does not get reset to 0.

    - Since ``n`` is declared to be 0 and we continuously decrement ``n``, it will always be less than 5, so the code loops infinitely.

      + Since ``n`` starts at 0 and gets smaller, the conditional for the ``while`` loop will always be true, and thus the code runs forever.