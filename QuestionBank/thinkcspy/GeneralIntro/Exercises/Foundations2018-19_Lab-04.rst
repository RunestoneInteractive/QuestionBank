.. activecode:: Foundations2018-19_Lab-04
    :author: Max Garagnani
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
 

    ~~~~
    # A simple program illustrating the use of the "for" statement

    print("This function generates chaotic values")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)