.. activecode:: town_create_reduce
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 03Reduce
   :topics: 09UnaryOps/03Reduce
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS town;

   CREATE TABLE town (
   townId          VARCHAR(3)      NOT NULL PRIMARY KEY,
   townName        VARCHAR(20),
   State           VARCHAR(20),
   Country         VARCHAR(20),
   townNickname    VARCHAR(80),
   townMotto       VARCHAR(80)
   );

   -- order matches table creation:
   -- id    name          state   country
   -- nickname   motto
   INSERT INTO town VALUES ('p', 'Philadelphia', 'PA', 'United States',
                            'Philly', 'Let brotherly love endure');
   INSERT INTO town VALUES ('a', 'Anoka', 'MN', 'United States',
                            'Halloween Capital of the world', NULL);
   INSERT INTO town VALUES ('be', 'Blue Earth', 'MN', 'United States',
                            'Beyond the Valley of the Jolly Green Giant',
                            'Earth so rich the city grows!');
   INSERT INTO town VALUES ('b', 'Bemidji', 'MN', 'United States',
                            'B-town', 'The first city on the Mississippi');
   INSERT INTO town VALUES ('d', 'Duluth', 'MN', 'United States',
                           'Zenith City', NULL);
   INSERT INTO town VALUES ('g', 'Greenville', 'MS', 'United States',
                            'The Heart & Soul of the Delta',
                            'The Best Food, Shopping, & Entertainment In The South');
   INSERT INTO town VALUES ('t', 'Tokyo', 'Kanto', 'Japan', NULL, NULL);
   INSERT INTO town VALUES ('as', 'Asgard', NULL, NULL,
                            'Home of Odin''s vault',
                            'Where magic and science are one in the same');
   INSERT INTO town VALUES ('mv', 'Metroville', NULL, NULL,
                           'Home of the Incredibles',
                           'Still Standing');
   INSERT INTO town VALUES ('le', 'London', 'England', 'United Kingdom',
                           'The Smoke',
                           'Domine dirige nos');
   INSERT INTO town VALUES ('sw', 'Seattle', 'Washington', 'United States',
                           'The Emerald City',
                           'The City of Goodwill');