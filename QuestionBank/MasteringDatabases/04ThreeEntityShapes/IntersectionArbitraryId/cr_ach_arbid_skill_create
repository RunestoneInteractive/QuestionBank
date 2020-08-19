.. activecode:: cr_ach_arbid_skill_create
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 04ThreeEntityShapes
   :subchapter: IntersectionArbitraryId
   :topics: 04ThreeEntityShapes/IntersectionArbitraryId
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS skill;

   CREATE TABLE skill (
   skillCode          VARCHAR(3)      NOT NULL PRIMARY KEY,
   skillDescription   VARCHAR(20)
   );

   DROP TABLE IF EXISTS creature;

   CREATE TABLE creature (
   creatureId          INTEGER      NOT NULL PRIMARY KEY,
   creatureName        VARCHAR(20),
   creatureType        VARCHAR(20),
   creatureResideTown  VARCHAR(20)
   );

   DROP TABLE IF EXISTS achievement;

   CREATE TABLE achievement (
   achId              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   creatureId         INTEGER,
   skillCode          VARCHAR(3),
   proficiency        INTEGER,
   achDate            TEXT,
   FOREIGN KEY (creatureId) REFERENCES creature (creatureId),
   FOREIGN KEY (skillCode) REFERENCES skill (skillCode)
   );