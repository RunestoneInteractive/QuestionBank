.. mchoice:: check_loops
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: datatypes
    :topics: TheBasics/datatypes
    :from_source: T
    :answer_a: ``for (let i in mylist) { writeln(i);}``
    :feedback_a: The for in loop iterates over the keys so this will print 0 ... 4.
    :answer_b: ``for (let i = 0; i < mylist.length; i++) { writeln(mylist[i])}``
    :feedback_b: i is the index variable and prints out the value stored at that index in the list
    :answer_c: ``for (let i of mylist) { writeln(i);}``
    :feedback_c: This is the closest example to python's ``for i in mylist:``
    :answer_d: ``for (let i in mylist) { writeln(mylist[i])}``
    :feedback_d: i is the index variable and prints out the value stored at that index in the list
    :correct: a

    Which of the above for loops will **not** print out the numbers 1 through 5 given the declarations below.

    .. code-block:: javascript

        let mylist = [1,2,3,4,5];