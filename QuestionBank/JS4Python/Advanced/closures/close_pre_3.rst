.. mchoice:: close_pre_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: Advanced
    :subchapter: closures
    :topics: Advanced/closures
    :from_source: T

    Consider the following code.  What is printed out by the final call to double?

    .. code-block:: javascript

        function parent() {
            let a = 10;

            let double = function() {
            a = a+a;
            console.log(a);
            };

            let square = function() {
            a = a*a;
            console.log(a);
            }

            return { double, square }
        }
        let { double, square } = parent();
        double();
        square();
        double();

    - 20

      - No, the change made to the value of a is 'permanent' because a is in the closure

    - 400

      - No, this is the value after square is called for the first time.

    - 10

      - No.  The value definitely changes over time.

    - 800

      + Very Good!  You must really understand closures, and you can do math!