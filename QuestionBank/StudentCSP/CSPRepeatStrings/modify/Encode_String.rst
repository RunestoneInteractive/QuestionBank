.. codelens:: Encode_String
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatStrings
    :subchapter: modify
    :topics: CSPRepeatStrings/modify
    :from_source: T

    message = "meet me at midnight"
    str = "abcdefghijklmnopqrstuvwxyz. "
    eStr = "zyxwvutsrqponmlkjihgfedcba ."
    encodedMessage = ""
    for letter in message:
        pos = str.find(letter)
        encodedMessage = encodedMessage + eStr[pos:pos+1]
    print(encodedMessage)