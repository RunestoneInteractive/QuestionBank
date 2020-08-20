.. parsonsprob:: listMixed_instructions
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-MixedupCode
    :topics: 08-lists/08-MixedupCode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    The following program segment should first print out the program's instructions. Next it should
    continuously ask the user if it wants to add a word to a list <i>vocabulary</i> and then append it
    to the end the list IF the word is not already in the list. The blocks have been mixed up and
    include extra blocks that aren't needed in the solution.
    -----
    print("Enter a word to add it to the vocabulary list or type in 'quit' to end the program.")
    response = 0
    vocabulary = []
    =====
    while response != "quit":
    =====
    while response == "quit": #distractor
    =====
        response = input("Enter a vocabulary word:")
    =====
        if response not in vocabulary:
    =====
            vocabulary.append(response)