.. activecode:: CS152_ch07_validation_exercise2
    :author: John Cigas
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: SentinelValuesAndValidation
    :topics: MoreAboutIteration/SentinelValuesAndValidation
    :from_source: F
    :timelimit: 60000

    Rewrite the function and calling code to ask for a positive integer. The function should return this positive integer.
    ~~~~
    def get_yes_or_no(message):
        valid_input = False
        while not valid_input:
            answer = input(message)
            answer = answer.upper() # convert to upper case
            if answer == 'Y' or answer == 'N':
                valid_input = True
            else:
                print('Please enter Y for yes or N for no.')
        return answer

    response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
    if response == 'Y':
        print('Great! They are very healthy.')
    else:
        print('Too bad. If cooked right, they are quite tasty.')