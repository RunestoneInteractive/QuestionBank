.. codelens::  cl_powerof_bad
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: Variablesandparametersarelocal
    :topics: Functions/Variablesandparametersarelocal
    :from_source: None

    def powerof(x, p):
        power = p   # this power is a local variable
        y = x ** power
        return y

    power = 3
    result = powerof(10, 2)
    print(result)