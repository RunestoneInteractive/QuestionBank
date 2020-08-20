.. activecode:: creature_create_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 03TwoEntityShapes
   :subchapter: TwoEntityShapes
   :topics: 03TwoEntityShapes/TwoEntityShapes
   :from_source: T
   :language: sql
   :include: town_create

   DROP TABLE IF EXISTS creature;

   CREATE TABLE creature (
   creatureId          INTEGER      NOT NULL PRIMARY KEY,
   creatureName        VARCHAR(20),
   creatureType        VARCHAR(20),
   townId VARCHAR(3) REFERENCES town(townId)     -- foreign key
   );