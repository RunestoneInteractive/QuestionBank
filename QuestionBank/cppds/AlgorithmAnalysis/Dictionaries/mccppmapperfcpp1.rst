.. mchoice:: mccppmapperfcpp1
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: Dictionaries
    :topics: AlgorithmAnalysis/Dictionaries
    :from_source: F
    :answer_a: mymap.count('x')
    :answer_b: mymap.erase('x')
    :answer_c: mymap['x'] = 10;
    :answer_d: mymap['x'] = mymap['x'] + 1;
    :answer_e: all of the above are O(1)
    :correct: e
    :feedback_a: count is a constant operation for a hash table because you do not have to iterate but there is a better answer.
    :feedback_b: removing an element from a hash table is a constant operation but there is a better answer.
    :feedback_c: Assignment to a hash table key is constant but there is a better answer.
    :feedback_d: Re-assignment to a hash table key is constant but there is a better answer.
    :feedback_e: The only hash table operations that are not O(1) are those that require iteration.

    Which of the hash table operations shown below is O(1)?