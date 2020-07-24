import re


def compute_indent(ql: list) -> int:
    if g := re.match(r"^(\s+):", ql[1]):
        return len(g.group(1))
    for i in range(2, 10):
        if g := re.match(r"^(\s+)\S", ql[i]):
            return len(g.group(1))


def find_end_of_options(ql: list) -> int:
    for i in range(1, len(ql)):
        if g := re.match(r"^(\s*)$", ql[i]):
            return i
    return i


testq = """
.. mchoice:: question11_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :topic: Functions/FunctionParameters
   :from_source: T
   :answer_a: def print_many(x, y):
   :answer_b: print_many
   :answer_c: print_many(x, y)
   :answer_d: Print out string x, y times.
   :correct: b
   :feedback_a: This line is the complete function header (except for the semi-colon) which includes the name as well as several other components.
   :feedback_b: Yes, the name of the function is given after the keyword def and before the list of parameters.
   :feedback_c: This includes the function name and its parameters
   :feedback_d: This is a comment stating what the function does.

   What is the name of the following function?

   .. code-block:: python

     def print_many(x, y):
         for i in range(y):
             print(x)
"""
testq = testq.strip()

test2 = """
.. actex:: ac11_14_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :topic: Functions/Exercises
   :from_source: T

   Write a function to count how many odd numbers are in a list.
   ~~~~
   def countOdd(lst):
       # your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(countOdd([1,3,5,7,9]),5,"Tested countOdd on input [1,3,5,7,9]")
           self.assertEqual(countOdd([1,2,3,4,5]),3,"Tested countOdd on input [-1,-2,-3,-4,-5]")
           self.assertEqual(countOdd([2,4,6,8,10]),0,"Tested countOdd on input [2,4,6,8,10]")
           self.assertEqual(countOdd([0,-1,12,-33]),2,"Tested countOdd on input [0,-1,12,-33]")

   myTests().main()
"""
test2 = test2.strip()


class Directive:
    def __init__(self, dstring):
        dstring = dstring.strip()
        dstring_list = dstring.split("\n")
        self.dline = dstring_list[0]
        self.identifier = self.dline.split("::")[1].strip()
        self.kind = self.dline.split("::")[0].strip().split()[1]
        if self.kind == "actex":
            self.kind = "activecode"
        self.indent = compute_indent(dstring)
        end_opt = find_end_of_options(dstring_list)
        self.indent = compute_indent(dstring_list)
        options = dstring_list[1:end_opt]
        # remove the indent from content
        self.content = [x[self.indent :] for x in dstring_list[end_opt + 1 :]]
        self.options = {}
        for opt in options:
            opt_parts = opt.strip().split(maxsplit=1)
            key = opt_parts[0].strip(":")
            if len(opt_parts) > 1:
                value = opt_parts[1]
            else:
                value = ""
            self.options[key] = value
        if self.kind == "activecode" or self.kind == "actex":
            if "~~~~" in self.content:
                end_instructions = self.content.index("~~~~")
                self.instructions = self.content[:end_instructions]
            else:
                end_instructions = 0
                self.instructions = []
            if "====" in self.content:
                start_hidden = self.content.index("====")
                self.starter_code = self.content[end_instructions + 1 : start_hidden]
                self.hidden_code = self.content[start_hidden + 1 :]
            else:
                self.hidden_code = []
                self.starter_code = self.content[end_instructions + 1 :]

    def same_question(self, other):
        """Compare the question part of two directives

        Args:
            other (Directive): The directive to compare against
        """
        if self.kind == "activecode" and other.kind == self.kind:
            return self.instructions == other.instructions
        else:
            return False

    def add_option(self, key: str, value: str) -> None:
        self.options[key] = value

    def __str__(self) -> str:
        rlist = [self.dline]
        ind = " " * self.indent
        for key, val in self.options.items():
            key = f":{key}:"
            rlist.append(f"{ind}{key} {val}")
        rlist.append("")
        rlist = rlist + [ind + x for x in self.content]
        return "\n".join(rlist)


if __name__ == "__main__":
    d = Directive(testq)
    e = Directive(test2)
    print(e.instructions)
    print(e.hidden_code)
    print(e.starter_code)
    f = Directive(test2)
