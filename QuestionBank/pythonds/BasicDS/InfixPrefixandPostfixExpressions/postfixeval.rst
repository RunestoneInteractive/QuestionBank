.. activecode:: postfixeval
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: BasicDS
   :subchapter: InfixPrefixandPostfixExpressions
   :topics: BasicDS/InfixPrefixandPostfixExpressions
   :from_source: T
   :caption: Postfix Evaluation
   :nocodelens:

   from pythonds.basic import Stack

   def postfixEval(postfixExpr):
       operandStack = Stack()
       tokenList = postfixExpr.split()

       for token in tokenList:
           if token in "0123456789":
               operandStack.push(int(token))
           else:
               operand2 = operandStack.pop()
               operand1 = operandStack.pop()
               result = doMath(token,operand1,operand2)
               operandStack.push(result)
       return operandStack.pop()

   def doMath(op, op1, op2):
       if op == "*":
           return op1 * op2
       elif op == "/":
           return op1 / op2
       elif op == "+":
           return op1 + op2
       else:
           return op1 - op2

   print(postfixEval('7 8 + 3 2 + /'))