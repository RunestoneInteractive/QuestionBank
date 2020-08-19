.. activecode:: q21_answer
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F

    def rot13(mess):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypted = ''
        for char in mess:
            if char == ' ':
                encrypted = encrypted + ' '
            else:
                rotated_index = alphabet.index(char) + 13
                if rotated_index < 26:
                    encrypted = encrypted + alphabet[rotated_index]
                else:
                    encrypted = encrypted + alphabet[rotated_index % 26]
        return encrypted

    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))