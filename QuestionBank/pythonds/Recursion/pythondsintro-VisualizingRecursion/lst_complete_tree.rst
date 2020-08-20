.. activecode:: lst_complete_tree
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: pythondsintro-VisualizingRecursion
    :topics: Recursion/pythondsintro-VisualizingRecursion
    :from_source: T
    :caption: Recursively Drawing a Tree
    :nocodelens:

    import turtle

    def tree(branchLen,t):
        if branchLen > 5:
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15,t)
            t.left(40)
            tree(branchLen-15,t)
            t.right(20)
            t.backward(branchLen)

    def main():
        t = turtle.Turtle()
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color("green")
        tree(75,t)
        myWin.exitonclick()

    main()