.. activecode:: FunDef1
        :author: bmiller
        :difficulty: 3.0
        :basecourse: TeacherCSP
        :chapter: CSPNameNames
        :subchapter: noteFunDefVsCall
        :topics: CSPNameNames/noteFunDefVsCall
        :from_source: T

        def greetJohn():  # procedure definition: body not executed yet!
            name = "John"
            print("Good day, " + name + "!")

        greetJohn()       # procedure call: body is executed at this point