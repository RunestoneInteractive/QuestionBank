.. activecode:: balcheck
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: BalancedSymbolsAGeneralCase
    :topics: BasicDS/BalancedSymbolsAGeneralCase
    :from_source: T
    :caption: Solving the General Balanced Symbol Problem
    :nocodelens:

    from pythonds3.basic import Stack


    def balance_checker(symbol_string):
        s = Stack()
        for symbol in symbol_string:
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.is_empty():
                    return False
                else:
                    if not matches(s.pop(), symbol):
                        return False

        return s.is_empty()

    def matches(sym_left, sym_right):
        all_lefts = "([{"
        all_rights = ")]}"
        return all_lefts.index(sym_left) == all_rights.index(sym_right)


    print(balance_checker('{({([][])}())}'))
    print(balance_checker('[{()]'))