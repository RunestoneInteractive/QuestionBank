.. activecode:: bikeshare_mean_duration_by_station_name
   :author: bmiller
   :difficulty: 3.0
   :basecourse: ac1
   :chapter: sql
   :subchapter: joining
   :topics: sql/joining
   :from_source: T
   :language: sql
   :dburl: /runestone/books/published/ac1/_static/bikeshare.db

   Write a query to display the mean duration of trip for each start station
   name. For example, one row could read as ``White House Station | 12345``.
   sort the result by the average duration in ascending order.
   ~~~~

   ====
   assert 0,0 == 15th St & Massachusetts Ave SE
   assert 0,1 == 446.11764705882354