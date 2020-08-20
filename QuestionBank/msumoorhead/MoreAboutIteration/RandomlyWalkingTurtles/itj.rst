.. activecode:: itj
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: RandomlyWalkingTurtles
    :topics: MoreAboutIteration/RandomlyWalkingTurtles
    :from_source: None
    :nocodelens:

    import random
    import turtle


    def isInScreen(w, t):
        if random.random() > 0.1:
            return True
        else:
            return False


    t = turtle.Turtle()
    wn = turtle.Screen()

    t.shape('turtle')
    while isInScreen(wn, t):
        coin = random.randrange(2)
        if coin == 0:              # heads
            t.left(90)
        else:                      # tails
            t.right(90)

        t.forward(50)

    wn.exitonclick()