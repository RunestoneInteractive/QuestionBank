.. codelens:: cl_change_parm
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: Variablesandparametersarelocal
    :topics: Functions/Variablesandparametersarelocal
    :from_source: None
    :question: What is the value of x when the line with the red arrow executes?
    :breakline: 8
    :feedback: x in the square function is a local variable.
    :correct: globals.x

    def square(x):
        y = x * x
        x = 0       # assign a new value to the parameter x
        return y

    x = 2
    z = square(x)
    print(z, 'is the square of', x)