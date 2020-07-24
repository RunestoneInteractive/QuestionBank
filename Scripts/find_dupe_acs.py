from pathlib import Path
from directive import Directive

p = Path("../QuestionBank/fopp")

flist = [x for x in p.glob("**/*") if x.is_file()]

activecodes = {}
for f in flist:
    with f.open() as df:
        try:
            d = Directive(df.read())
            if d.kind == "activecode":
                activecodes[f] = d
        except Exception as e:
            print(f"Error in {f} is {e}")


for q1 in activecodes.values():
    for q2 in activecodes.values():
        if q1 is not q2:
            if q1.instructions and q1.same_question(q2):
                if q1.starter_code == q2.starter_code:
                    print(f"{q1.identifier} and {q2.identifier} are the same")
                    if bool(q1.hidden_code) != bool(q2.hidden_code):
                        if q1.hidden_code:
                            print(f"{q1.identifier} has unit tests")
                        else:
                            print(f"{q2.identifier} has unit tests")
                            print(q2.hidden_code)
                else:
                    print(q1.starter_code)
                    print(q2.starter_code)

