.. activecode:: act_xkcd_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: xkcd_pass
    :topics: Projects/xkcd_pass
    :from_source: T

    import random
    import sys
    sys.setExecutionLimit(60000) # 60 seconds
    my_password = "abcd"
    guess_num = 0
    done = False
    while not done:

        guessed_pw = ""
        # your code here

        if guessed_pw == my_password:
            print("found it after ", guess_num, " tries")
            done = True