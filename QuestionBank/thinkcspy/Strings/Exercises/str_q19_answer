.. activecode:: str_q19_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: T

    def encrypt(message, cipher):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted = ''
        for char in message:
            if char == ' ':
                encrypted = encrypted + ' '
            else:
                pos = alphabet.index(char)
                encrypted = encrypted + cipher[pos]
        return encrypted

    def decrypt(encrypted, cipher):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decrypted = ''
        for char in encrypted:
            if char == ' ':
                decrypted = decrypted + ' '
            else:
                pos = cipher.index(char)
                decrypted = decrypted + alphabet[pos]
        return decrypted


    cipher = "badcfehgjilknmporqtsvuxwzy"

    encrypted = encrypt('hello world', cipher)
    print encrypted

    decrypted = decrypt(encrypted, cipher)
    print(decrypted)