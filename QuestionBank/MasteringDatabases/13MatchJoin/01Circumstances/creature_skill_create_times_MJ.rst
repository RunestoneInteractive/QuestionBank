.. activecode:: creature_skill_create_times_MJ
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 13MatchJoin
   :subchapter: 01Circumstances
   :topics: 13MatchJoin/01Circumstances
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS creature;
   CREATE TABLE creature (
   creatureId          INTEGER      NOT NULL PRIMARY KEY,
   creatureName        VARCHAR(20),
   creatureType        VARCHAR(20),
   reside_townId VARCHAR(3) REFERENCES town(townId),     -- foreign key
   idol_creatureId     INTEGER,
   FOREIGN KEY(idol_creatureId) REFERENCES creature(creatureId)
   );

   INSERT INTO creature VALUES (1,'Bannon','person','p',10);
   INSERT INTO creature VALUES (2,'Myers','person','a',9);
   INSERT INTO creature VALUES (3,'Neff','person','be',NULL);
   INSERT INTO creature VALUES (4,'Neff','person','b',3);
   INSERT INTO creature VALUES (5,'Mieska','person','d', 10);
   INSERT INTO creature VALUES (6,'Carlis','person','p',9);
   INSERT INTO creature VALUES (7,'Kermit','frog','g',8);
   INSERT INTO creature VALUES (8,'Godzilla','monster','t',6);
   INSERT INTO creature VALUES (9,'Thor','superhero','as',NULL);
   INSERT INTO creature VALUES (10,'Elastigirl','superhero','mv',13);
   INSERT INTO creature VALUES (11,'David Beckham','person','le',9);
   INSERT INTO creature VALUES (12,'Harry Kane','person','le',11);
   INSERT INTO creature VALUES (13,'Megan Rapinoe','person','sw',10);

   DROP TABLE IF EXISTS skill;

   CREATE TABLE skill (
   skillCode          VARCHAR(3)      NOT NULL PRIMARY KEY,
   skillDescription   VARCHAR(40),
   maxProficiency     INTEGER,     -- max score that can be achieved for this skill
   minProficiency     INTEGER,     -- min score that can be achieved for this skill
   origin_townId      VARCHAR(3)     REFERENCES town(townId)     -- foreign key
   );

   INSERT INTO skill VALUES ('A', 'float', 10, -1,'b');
   INSERT INTO skill VALUES ('E', 'swim', 5, 0,'b');
   INSERT INTO skill VALUES ('O', 'sink', 10, -1,'b');
   INSERT INTO skill VALUES ('U', 'walk on water', 5, 1,'d');
   INSERT INTO skill VALUES ('Z', 'gargle', 5, 1,'a');
   INSERT INTO skill VALUES ('B2', '2-crew bobsledding', 25, 0,'d');
   INSERT INTO skill VALUES ('TR4', '4x100 meter track relay', 100, 0,'be');
   INSERT INTO skill VALUES ('C2', '2-person canoeing', 12, 1,'t');
   INSERT INTO skill VALUES ('THR', 'three-legged race', 10, 0,'g');
   INSERT INTO skill VALUES ('D3', 'Australasia debating', 10, 1,NULL);
   INSERT INTO skill VALUES ('PK', 'soccer penalty kick', 10, 1, 'le');