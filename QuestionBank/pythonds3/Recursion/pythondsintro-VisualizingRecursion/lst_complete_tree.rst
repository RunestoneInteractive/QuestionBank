.. activecode:: lst_complete_tree
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: pythondsintro-VisualizingRecursion
    :topics: Recursion/pythondsintro-VisualizingRecursion
    :from_source: T
    :caption: Recursively Drawing a Tree
    :nocodelens:

    import turtle


    def tree(branch_len, t):
        if branch_len > 5:
            t.forward(branch_len)
            t.right(20)
            tree(branch_len - 15, t)
            t.left(40)
            tree(branch_len - 15, t)
            t.right(20)
            t.backward(branch_len)

    def main():
        t = turtle.Turtle()
        my_win = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color("green")
        tree(75, t)
        my_win.exitonclick()

    main()