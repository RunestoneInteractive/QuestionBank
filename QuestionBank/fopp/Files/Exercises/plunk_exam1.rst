.. activecode:: plunk_exam1
    :author: Laura Plunkett
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Files
    :subchapter: Exercises
    :topics: Files/Exercises
    :from_source: F
   

    The code below creates a deck of cards, and a list with 5 cards in it. Write at least two functions that test for any of the following in a hand of cards: all cards having the same suit i.e. all hearts or all clubs, two cards with the same face value i.e. two sevens or two queens, three cards with the same face value i.e. three sevens or three queens, four cards with the same face value i.e. four sevens or four queens, two pairs, or other poker hands of value such as straights or straight flushes, full house, etc.  
    ~~~~
    import random

    # make a deck
    list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    list_suits = ["diamond", "club", "heart", "spade"]

    deck = []
    for suit in list_suits:
        for value in list_values:
            card = [suit, value]
            deck.append(card)

    # get 5 random cards without replacement
    hand = random.sample(deck,5)
    # to get the value and suit of the first card:
    print(hand[0][0])
    print(hand[0][1])

    # Your test functions here


    ====
    
config values (conf.py):

- activecode_div_class - custom CSS class of the component's outermost div
- activecode_hide_load_history - if True, hide the load history button
- wasm_uri - Path or Full URL to folder containing WASM files for SQL. /_static is default