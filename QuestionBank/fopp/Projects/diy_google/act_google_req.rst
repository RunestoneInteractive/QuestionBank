.. activecode:: act_google_req
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: diy_google
    :topics: Projects/diy_google
    :from_source: T

    import requests

    res = requests.get("/runestone/static/fopp/_static/home.html")

    page_text = res.text
    # Now the whole page is just one big string!

    print(page_text)