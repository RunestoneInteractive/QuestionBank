.. mchoice:: listString_MC_poe
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listsAndStrings
    :topics: 08-lists/08-listsAndStrings
    :from_source: T
    :practice: T
    :answer_a: Poe
    :answer_b: EdgarAllanPoe
    :answer_c: EAP
    :answer_d: William Shakespeare
    :correct: c
    :feedback_a: Three characters but not the right ones.  namelist is the list of names.
    :feedback_b: Too many characters in this case.  There should be a single letter from each name.
    :feedback_c: Yes, split creates a list of the three names.  The for loop iterates through the names and creates a string from the first characters.
    :feedback_d: That does not make any sense.

    What is printed by the following statements?

    ::

      myname = "Edgar Allan Poe"
      namelist = myname.split()
      init = ""
      for aname in namelist:
          init = init + aname[0]
      print(init)