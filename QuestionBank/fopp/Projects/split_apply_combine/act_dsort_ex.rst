.. activecode:: act_dsort_ex
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: split_apply_combine
    :topics: Projects/split_apply_combine
    :from_source: T

    myd = {'c':5, 'a': 1, 'b': 10}
    print(sorted(myd))
    sorted_keys = sorted(myd, key=myd.get, reverse=True)
    print(sorted_keys)
    for k in sorted_keys:
        print(k, myd[k])