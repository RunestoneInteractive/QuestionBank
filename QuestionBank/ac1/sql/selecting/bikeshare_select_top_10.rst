.. activecode:: bikeshare_select_top_10
  :author: bmiller
  :difficulty: 3.0
  :basecourse: ac1
  :chapter: sql
  :subchapter: selecting
  :topics: sql/selecting
  :from_source: T
  :language: sql
  :dburl: /_static/bikeshare.db

  SELECT
    *
  FROM
    trip_data
  LIMIT
    10