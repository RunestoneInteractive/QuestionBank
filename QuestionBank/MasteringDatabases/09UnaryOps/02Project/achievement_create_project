.. activecode:: achievement_create_project
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 02Project
   :topics: 09UnaryOps/02Project
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS achievement;
   CREATE TABLE achievement (
   achId              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   creatureId         INTEGER,
   skillCode          VARCHAR(3),
   proficiency        INTEGER,
   achDate            TEXT,
   test_townId VARCHAR(3) REFERENCES town(townId),     -- foreign key
   FOREIGN KEY (creatureId) REFERENCES creature (creatureId),
   FOREIGN KEY (skillCode) REFERENCES skill (skillCode)
   );

   -- Bannon floats in Anoka (where he aspired)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (1, 'A', 3, datetime('now'), 'a');

   -- Bannon swims in Duluth (he aspired in Bemidji)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (1, 'E', 3, datetime('2017-09-15 15:35'), 'd');
   -- Bannon floats in Anoka (where he aspired)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (1, 'A', 3, datetime('2018-07-14 14:00'), 'a');

   -- Bannon swims in Duluth (he aspired in Bemidji)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (1, 'E', 3, datetime('now'), 'd');
   -- Bannon doesn't gargle
   -- Mieska gargles in Tokyo (had no aspiration to)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (5, 'Z', 6, datetime('2016-04-12 15:42:30'), 't');

   -- Neff #3 gargles in Blue Earth (but not to his aspired proficiency)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (3, 'Z', 4, datetime('2018-07-15'), 'be');
   -- Neff #3 gargles in Blue Earth (but not to his aspired proficiency)
   -- on same day at same proficiency, signifying need for arbitrary id
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (3, 'Z', 4, datetime('2018-07-15'), 'be');

   -- Beckham achieves PK in London
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (11, 'PK', 10, datetime('1998-08-15'), 'le');
   -- Kane achieves PK in London
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (12, 'PK', 10, datetime('2016-05-24'), 'le');
   -- Rapinoe achieves PK in London
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (13, 'PK', 10, datetime('2012-08-06'), 'le');
   -- Godizilla achieves PK in Tokyo poorly with no date
   -- had not aspiration to do so- did it on a dare ;)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (8, 'PK', 1, NULL, 't');


   -- -------------------- -------------------- -------------------
   -- Thor achieves three-legged race in Metroville (with Elastigirl)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (9, 'THR', 10, datetime('2018-08-12 14:30'), 'mv');
   -- Elastigirl achieves three-legged race in Metroville (with Thor)
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (10, 'THR', 10, datetime('2018-08-12 14:30'), 'mv');

   -- Kermit 'pilots' 2-person bobsledding  (pilot goes into contribution)
   --       with Thor as brakeman (brakeman goes into contribution) in Duluth,
   --    achieve at 76% of maxProficiency
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (7, 'B2', 19, datetime('2017-01-10 16:30'), 'd');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (9, 'B2', 19, datetime('2017-01-10 16:30'), 'd');

   -- 4 people form track realy team in London:
   --   Neff #4, Mieska, Myers, Bannon
   --    achieve at 85% of maxProficiency
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (4, 'TR4', 85, datetime('2012-07-30'), 'le');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (5, 'TR4', 85, datetime('2012-07-30'), 'le');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (2, 'TR4', 85, datetime('2012-07-30'), 'le');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (1, 'TR4', 85, datetime('2012-07-30'), 'le');

   -- Thor, Rapinoe, and Kermit form debate team in Seattle, WA and
   -- achieve at 80% of maxProficiency
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (9, 'D3', 8, datetime('now', 'localtime'), 'sw');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (13, 'D3', 8, datetime('now', 'localtime'), 'sw');
   INSERT INTO achievement (creatureId, skillCode, proficiency,
                            achDate, test_townId)
                   VALUES (7, 'D3', 8, datetime('now', 'localtime'), 'sw');