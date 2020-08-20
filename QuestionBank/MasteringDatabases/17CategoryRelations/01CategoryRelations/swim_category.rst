.. activecode:: swim_category
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 17CategoryRelations
   :subchapter: 01CategoryRelations
   :topics: 17CategoryRelations/01CategoryRelations
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS swim_category;

   CREATE TABLE swim_category (
   skillCode          VARCHAR(3)      NOT NULL,
   category           VARCHAR(20)     NOT NULL,
   lowProfVal         INTEGER         NOT NULL,
   highProfVal        INTEGER         NOT NULL
   );

   INSERT INTO swim_category VALUES ('E', 'poor', 0, 1);
   INSERT INTO swim_category VALUES ('E', 'fair', 2, 3);
   INSERT INTO swim_category VALUES ('E', 'good', 4, 5);