#%%
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pathlib import Path
import re
from os import environ

# %%
eng = create_engine(environ["DBTUNNEL"])

# %%
df = pd.read_sql_query(
    """select name, chapter, subchapter, question, author, difficulty, from_source, base_course, topic from questions where question_type != 'page' and base_course != 'fcla'""",
    eng,
)


# %%
# import re

# qt = qt.lstrip()
# x = re.match(r"(\.\. \w+::\s+(.*?)\n(\s+))(:.*)", qt, flags=re.DOTALL)
# x.groups()


# %%
# print(
#     re.sub(
#         r"(\.\. \w+::\s+(.*?)\n(\s+))(:.*)",
#         f"\\1:author: {name}\n\\3\\4",
#         qt,
#         flags=re.DOTALL,
#     )
# )


# %%
def compute_indent(q):
    ql = q.split("\n")
    g = re.match(r"^(\s+):", ql[1])
    if g:
        return len(g.group(1))
    for i in range(2, 10):
        g = re.match(r"^(\s+)\S", ql[i])
        if g:
            return len(g.group(1))


# %%
def update_question(q, author, difficulty, from_source, topic, basecourse):
    if q[0:2] == "\\x":
        return
    q = q.strip()
    try:
        indent = compute_indent(q)
    except:
        indent = 4
    author = " " * indent + ":author: " + str(author)
    difficulty = " " * indent + ":difficulty: " + str(difficulty)
    from_source = " " * indent + ":from_source: " + str(from_source)
    topic = " " * indent + ":topic: " + str(topic)
    basecourse = " " * indent + ":basecourse: " + str(basecourse)
    qlist = q.split("\n")
    qlist.insert(1, from_source)
    qlist.insert(1, topic)
    qlist.insert(1, basecourse)
    qlist.insert(1, difficulty)
    qlist.insert(1, author)
    return "\n".join(qlist)


q = """
.. actex:: ex_5_7

    Write a fruitful function ``sumTo(n)`` that returns the sum of all integer numbers up to and
    including `n`.   So ``sumTo(10)`` would be ``1+2+3...+10`` which would return the value 55.  Use the
    equation  (n * (n + 1)) / 2.
    ~~~~

    def sumTo(n):
        # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertAlmostEqual(sumTo(15),120.0,0,"Tested sumTo on input 15")
            self.assertAlmostEqual(sumTo(0),0.0,0,"Tested sumTo on input 0")
            self.assertAlmostEqual(sumTo(25),325.0,0,"Tested sumTo on input 25")
            self.assertAlmostEqual(sumTo(7),28.0,0,"Tested sumTo on input 7")

    myTests().main()
"""

# update_question(q, "foo", "bar", "T", "foo/bar", "foo")
# exit()

# %%
for ix, row in df.iterrows():
    try:
        topic = row["chapter"] + "/" + row["subchapter"]
    except:
        topic = "not set"
    p = Path(topic)
    p = Path("../QuestionBank") / row["base_course"] / p
    p.mkdir(parents=True, exist_ok=True)
    p = p / row["name"].replace("/", "_-_")
    try:
        with p.open("w") as f:
            res = update_question(
                row["question"],
                row["author"],
                str(row["difficulty"]),
                row["from_source"],
                topic,
                row["base_course"],
            )
            if res is not None:
                f.write(res)
            else:
                print(f'Bad Encoding for {row["base_course"]} {row["name"]}')

    except Exception as e:
        print(f'Problem with {row["base_course"]} {row["name"]} - {e}')


# %%
