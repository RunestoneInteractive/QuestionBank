.. activecode:: oj_count
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 14OuterJoin
   :subchapter: NotUsedOJTesting
   :topics: 14OuterJoin/NotUsedOJTesting
   :from_source: T
   :language: sql
   :include: oj_test_create

   DROP TABLE IF EXISTS OuterJoinStreetUser;

   CREATE TABLE OuterJoinStreetUser AS
   SELECT S.Name AS Street, U.*
   FROM Streets S
   LEFT OUTER JOIN Users U ON U.Streetid = S.Id;

   SELECT  Street, Count(Username) AS COUNT
   FROM OuterJoinStreetUser
   GROUP BY Street;