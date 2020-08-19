.. activecode:: wof_ac_sleep
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: chapterProject
    :topics: Inheritance/chapterProject
    :from_source: T
    :autograde: unittest
    :language: python
    :nocodelens:

    This project will take you through the process of implementing a simplified version of the game **Wheel of Fortune**. Here are the rules of our game:

    * There are ``num_human`` human players and ``num_computer`` computer players.
        * Every player has *some* amount of money ($0 at the start of the game)
        * Every player has a set of prizes (none at the start of the game)
    * The goal is to **guess a phrase within a given category**. For example:
        * Category: **Artist & Song**
        * Phrase: **Whitney Houston's I Will Always Love You**
    * Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: ``_``):
        * Category: **Artist & Song**
        * Phrase: ``_______ _______'_ _ ____ ______ ____ ___``
    * Note that case (capitalization) does not matter
    * During their turn, every player spins the wheel to determine a prize amount and:
        * If the wheel lands on a **cash** square, players may do one of three actions:
            * **Guess any letter** that hasn't been guessed by typing a letter (a-z)
                * Vowels (a, e, i, o, u) cost $250 to guess and can't be guessed if the player doesn't have enough money. All other letters are "free" to guess
                * The player can guess any letter that hasn't been guessed and gets that cash amount for *every time* that letter appears in the phrase
                * If there is a prize, the user also gets that prize (in addition to any prizes they already had)
                * Example: The user lands on $500 and guesses 'W'
                    * There are three W's in the phrase, so the player wins $1500
            * **Guess the complete phrase** by typing a phrase (anything over one character that isn't `'pass'`)
                * If they are correct, they win the game
                * If they are incorrect, it is the next player's turn
            * **Pass** their turn by entering ``'pass'``
        * If the wheel lands on **"lose a turn"**, the player loses their turn and the game moves on to the next player
        * If the wheel lands on **"bankrupt"**, the player loses their turn *and* loses their money. However, they keep all of the prizes they have won so far.
    * The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

    First, let's learn about a few functions and methods that we'll use along the way to do this project. There are no questions to answer in these next few active code windows, they are just here to introduce or reintroduce you to some functions and methods that you may not be aware of. The active code window that starts with "Part A" is where you are first asked to complete code.

    The ``time.sleep(s)`` function (from the ``time`` module) delays execution of the next line of code for ``s`` seconds. You'll find that we can build a little suspense during gameplay with some well-placed delays. The game can also be easier for users to understand if not everything happens instantly.
    ~~~~
    import time

    for x in range(2, 6):
        print('Sleep {} seconds..'.format(x))
        time.sleep(x) # "Sleep" for x seconds
    print('Done!')