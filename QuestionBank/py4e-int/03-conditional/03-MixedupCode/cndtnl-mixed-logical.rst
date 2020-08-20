.. parsonsprob:: cndtnl-mixed-logical
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-MixedupCode
    :topics: 03-conditional/03-MixedupCode
    :from_source: T
    :practice: T
    :adaptive:
    :numbered: left

    Arrange the following code so that after x and y are defined, they are compared and if the value of x
    and y are the same object it prints ``"x and y are the same"``; if x and y have the same value it
    prints ``"x and y have the same value"``; and prints ``"x and y are not similar"`` if x and y do not
    fit the other conditionals. Be sure to indent correctly!
    -----
    x = 12
    =====
    y = x
    =====
    if x is y:
    =====
        print("x and y are the same")
    =====
    elif x == y:
    =====
        print("x and y have the same value")
    =====
    else:
    =====
        print("x and y have different values")