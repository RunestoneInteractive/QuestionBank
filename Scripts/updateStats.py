#%%
import directive
from pathlib import Path
import redis
import json

#%%

r = redis.Redis()


def update_one_course(basecourse, r):
    print(basecourse)
    p = Path("../QuestionBank")
    p = p / basecourse

    qlist = [q for q in p.glob("**/*") if q.is_file()]
    for q in qlist:
        with q.open(mode="r+") as qf:
            print(q)
            d = directive.Directive(qf.read())
            key = f"{basecourse}/{d.options['topics']}/{d.identifier}"
            stats = r.get(key)
            if stats:
                stats = json.loads(json.loads(stats))
                print(stats)
                for s in [
                    "pct_on_first",
                    "total_students_attempting",
                    "num_students_correct",
                    "mean_clicks_to_correct",
                    "difficulty",
                ]:
                    d.add_option(s, stats[s])

                qf.seek(0)
                qf.write(str(d))
                qf.truncate()


# %%
for basecourse in [
    "pythonds",
    "fopp",
    "thinkcspy",
    "cppds",
    "StudentCSP",
    "thinkcpp",
    "pythonds3",
    "haugrud",
    "cps110fall2018",
    "cps110spring2019",
    "csawesome",
    "csjava",
    "httlads",
    "webfundamentals",
    "MasteringDatabases",
]:

    update_one_course("fopp", r)

# %%
