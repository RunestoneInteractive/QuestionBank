.. activecode:: wvu_challenge_whiledictionaries
    :author: Brian Powell
    :difficulty: 4.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F

    Write code that asks users to the first name, last name, and age of members of their extended family. Users should be able to enter as many family members as they want. Figure out what format for having users enter data you think is best.

    The information should be stored in a two-level dictionary. The key of the top-level dictionary should be the last name. Its value should be another dictionary where the key is the first name and the value is the age. Your dictionary should look like this: ``{'Lastname': {'Firstname' : 35}}``

    For each last name, your code should print the number of people, the oldest person's name, and their average age.

    ~~~~