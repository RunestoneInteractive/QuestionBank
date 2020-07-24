# Extract some statistics about questions that are autograded
# Chapter
# Subchapter
# name
# mean clicks to correct
# total clicks to correct
# num students correct
# num students correct on first try
# total attempts at question
# mean attempts at question
# mean total attempts
# total students attempting
# pct correct on first try
#
# Each report is for one base course
#
# TODO: get this working for autograded activecodes

#%%
import pandas as pd
from sqlalchemy import create_engine
import altair as alt
from os import environ


# %%
eng = create_engine(environ["DBTUNNEL"])


#%%


def count_ones(series):
    return len(series.where(lambda x: x == 1).dropna())


# %%


def get_all_attempts(basecourse, qtype):
    """
    Get all attempts on the question regardless of whether the student was
    ever correct or not.
        :param basecourse:
        :param qtype: Question type mchoice, fitb, etc
        :returns: Pandas DataFrame
    """
    df = pd.read_sql_query(
        f"""
    SELECT name, sid, count(*)
    FROM questions JOIN {qtype}_answers ON name = div_id
    JOIN courses on {qtype}_answers.course_name = courses.course_name
    AND courses.base_course = '{basecourse}'
    GROUP BY name, sid """,
        eng,
    )

    dfc = df.groupby(["name", "sid"]).agg(all_attempts=("count", "mean"))
    dfc = dfc.reset_index()
    all_mean = dfc.groupby("name").agg(
        total_attempts=("all_attempts", "sum"),
        mean_t_attempts=("all_attempts", "mean"),
        total_students_attempting=("all_attempts", "count"),
    )
    all_mean.reset_index()
    return all_mean


# %%
def get_all_click_data(basecourse, directive):
    """
    Get all the data for every student that got a corrrect answer
        :param: basecourse
        :param: directive question type mchoice, fitb, etc.
        :returns: Pandas DataFrame
    """
    return pd.read_sql_query(
        f"""
SELECT {directive}_answers.div_id, {directive}_answers.sid, {directive}_answers.timestamp, correct
FROM {directive}_answers JOIN
    (SELECT {directive}_answers.div_id, {directive}_answers.sid, min({directive}_answers.timestamp) first_correct
        FROM {directive}_answers JOIN questions on ({directive}_answers.div_id = name)
        JOIN courses ON {directive}_answers.course_name = courses.course_name and courses.base_course = '{basecourse}'
        WHERE  correct = 'T'
        GROUP BY {directive}_answers.div_id, {directive}_answers.sid ) AS T
    ON {directive}_answers.div_id = T.div_id and {directive}_answers.sid = T.sid and {directive}_answers.timestamp <= first_correct
    ORDER BY div_id, sid, timestamp""",
        con=eng,
    )


# %%
def get_correct_stats(basecourse, directive):
    """
    Get the statistics for students that got a correct answer:
        Mean number of clicks to get the correct answer
        Total number of clicks in getting the correct answer
        Number of students that got a correct answer

        :param: basecourse
        :param: directive - question type mchoice, fitb, etc
    """
    ctc = get_all_click_data(basecourse, directive)
    xxx = ctc.groupby(["div_id", "sid"]).agg(ctc=("timestamp", "count")).reset_index()
    mc_stats = xxx.groupby("div_id").agg(
        mean_clicks_to_correct=("ctc", "mean"),
        total_clicks_to_correct=("ctc", "sum"),
        num_students_correct=("ctc", "count"),
        num_first_try=("ctc", count_ones),
    )
    bc_qs = pd.read_sql_query(
        f"""select chapter, subchapter, name from questions where base_course='{basecourse}'""",
        eng,
    )
    mc_stats = mc_stats.reset_index()
    mc_stats = bc_qs.merge(mc_stats, right_on="div_id", left_on="name")[
        [
            "chapter",
            "subchapter",
            "name",
            "mean_clicks_to_correct",
            "total_clicks_to_correct",
            "num_students_correct",
            "num_first_try",
        ]
    ]
    return mc_stats.sort_values(
        ["mean_clicks_to_correct", "num_students_correct"], ascending=False
    )


# %%
def get_combined_stats(basecourse, qtype):
    """Combine the statistics

    Args:
        basecourse (str): course to gather statistics from
        qtype (str): question type - mchoice, fitb, etc

    Returns:
        DataFrame: A Pandas DataFrame containing the statistics
    """
    f = get_correct_stats(basecourse, qtype)
    all_mean = get_all_attempts(basecourse, qtype)
    mergedf = f.merge(all_mean, left_on="name", right_on="name", how="outer")
    mergedf["pct_on_first"] = mergedf.num_first_try / mergedf.total_students_attempting
    return mergedf


# %%
def get_combined_qtypes(basecourse):
    qtypes = ["mchoice", "fitb", "dragndrop", "parsons", "clickablearea"]
    flist = []
    for qtype in qtypes:
        print(f"getting stats for {qtype}")
        try:
            res = get_combined_stats(basecourse, qtype)
            res["question_type"] = qtype
            flist.append(res)
        except:
            print(f"No stats for {qtype}")
    return pd.concat(flist)


# %%
