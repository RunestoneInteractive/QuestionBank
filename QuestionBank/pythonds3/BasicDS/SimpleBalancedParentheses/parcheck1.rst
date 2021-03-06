.. activecode:: parcheck1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: SimpleBalancedParentheses
    :topics: BasicDS/SimpleBalancedParentheses
    :from_source: T
    :caption: Solving the Balanced Parentheses Problem
    :nocodelens:

    from pythonds3.basic import Stack


    def par_checker(symbol_string):
        s = Stack()
        for symbol in symbol_string:
            if symbol == "(":
                s.push(symbol)
            else:
                if s.is_empty():
                    return False
                else:
                    s.pop()

        return s.is_empty()


    print(par_checker("((()))"))  # expected True
    print(par_checker("((()()))"))  # expected True
    print(par_checker("(()"))  # expected False
    print(par_checker(")("))  # expected False