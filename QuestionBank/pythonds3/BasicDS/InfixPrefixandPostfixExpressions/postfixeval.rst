.. activecode:: postfixeval
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: InfixPrefixandPostfixExpressions
    :topics: BasicDS/InfixPrefixandPostfixExpressions
    :from_source: T
    :caption: Postfix Evaluation
    :nocodelens:

    from pythonds3.basic import Stack

    def postfix_eval(postfix_expr):
        operand_stack = Stack()
        token_list = postfix_expr.split()

        for token in token_list:
            if token in "0123456789":
                operand_stack.push(int(token))
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token, operand1, operand2)
                operand_stack.push(result)
        return operand_stack.pop()


    def do_math(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2


    print(postfix_eval("7 8 + 3 2 + /"))