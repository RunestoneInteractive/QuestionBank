.. activecode:: creature_town
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 03TwoEntityShapes
   :subchapter: AllInOne
   :topics: 03TwoEntityShapes/AllInOne
   :from_source: T
   :language: sql
   :enabledownload:

   DROP TABLE IF EXISTS town;

   CREATE TABLE town (
   townId          VARCHAR(3)      NOT NULL PRIMARY KEY,
   townName        VARCHAR(20),
   State           VARCHAR(20),
   Country         VARCHAR(20),
   townNickname    VARCHAR(80),
   townMotto       VARCHAR(80)
   );

   INSERT INTO town VALUES ('p', 'Philadelphia', 'PA', 'United States', 'Philly', 'Let brotherly love endure');
   INSERT INTO town VALUES ('a', 'Anoka', 'MN', 'United States', 'Halloween Capital of the world', NULL);
   INSERT INTO town VALUES ('be', 'Blue Earth', 'MN', 'United States', 'Beyond the Valley of the Jolly Grean Giant', 'Earth so rich the city grows!');
   INSERT INTO town VALUES ('b', 'Bemidji', 'MN', 'United States', 'B-town', 'The first city on the Mississippi');
   INSERT INTO town VALUES ('d', 'Duluth', 'MN', 'United States', 'Zenith City', NULL);
   INSERT INTO town VALUES ('g', 'Greenville', 'MS', 'United States', 'The Heart & Soul of the Delta', 'The Best Food, Shopping, & Entertainment In The South');
   INSERT INTO town VALUES ('t', 'Tokyo', 'Kanto', 'Japan', NULL, NULL);
   INSERT INTO town VALUES ('as', 'Asgard', NULL, NULL, 'Home of Odin''s vault', 'Where magic and science are one in the same');

   CREATE TABLE creature (
   creatureId          INTEGER      NOT NULL PRIMARY KEY,
   creatureName        VARCHAR(20),
   creatureType        VARCHAR(20),
   townId VARCHAR(3) REFERENCES town(townId)     -- foreign key
   );

   INSERT INTO creature VALUES (1,'Bannon','person','p');
   INSERT INTO creature VALUES (2,'Myers','person','a');
   INSERT INTO creature VALUES (3,'Neff','person','be');
   INSERT INTO creature VALUES (4,'Neff','person','b');
   INSERT INTO creature VALUES (5,'Mieska','person','d');
   INSERT INTO creature VALUES (6,'Carlis','person','p');
   INSERT INTO creature VALUES (7,'Kermit','frog','g');
   INSERT INTO creature VALUES (8,'Godzilla','monster','t');
   INSERT INTO creature VALUES (9,'Thor','superhero','as');
   INSERT INTO creature VALUES (10,'Iron Man','superhero','z');