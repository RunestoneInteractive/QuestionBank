.. activecode:: bikeshare_open_vs_closed_stations
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: joining
   :topics: sql/joining
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   Write a query to compare, in terms of number of trips and mean duration,
   stations that are listed as open and closed.
   ~~~~

   ====
   assert 0,0 == closed
   assert 1,0 == open
   assert 0,1 == 13440
   assert 1,1 == 395482