.. activecode:: Foundations2017-18_Lab_05
    :author: Max Garagnani
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
 

    ~~~~
    # A simple program illustrating chaotic behaviour

    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)