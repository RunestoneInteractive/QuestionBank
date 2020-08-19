.. activecode:: set_adv_creature_create
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 11SetOps
  :subchapter: 02UnionIntersectMinusAdvanced
  :topics: 11SetOps/02UnionIntersectMinusAdvanced
  :from_source: T
  :language: sql

  -- ------------------   town -- -------------------------------

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

  -- ------------------   creature -- -------------------------------
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

  -- ------------------   skill -- -------------------------------
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
  -- Note that no skill originates in Philly or Metroville or Asgaard

  -- ------------------  teamSkill  -- -------------------------------
  DROP TABLE IF EXISTS teamSkill;

  CREATE TABLE teamSkill (
  skillCode      VARCHAR(3)  NOT NULL PRIMARY KEY references skill (skillCode),
  teamSize       INTEGER
  );

  INSERT INTO teamSkill VALUES ('B2', 2);
  INSERT INTO teamSkill VALUES ('TR4', 4);
  INSERT INTO teamSkill VALUES ('C2', 2);
  INSERT INTO teamSkill VALUES ('THR', 2);
  INSERT INTO teamSkill VALUES ('D3', 3);

  -- ------------------  achievement  -- -------------------------------
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
  -- Godzilla achieves PK in Tokyo poorly with no date
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

  -- no 2-person canoeing achievements, but some have aspirations

  -- ------------------  aspiration  -- -------------------------------
  DROP TABLE IF EXISTS aspiration;

  CREATE TABLE aspiration
  ( -- foreign key
    creatureId    INTEGER     NOT NULL   REFERENCES creature(creatureId),
    -- foreign key
    skillCode     VARCHAR(3)  NOT NULL   REFERENCES skill(skillCode),
    aspiredProficiency INTEGER,
    desired_townId     VARCHAR(3) REFERENCES town(townId),     -- foreign key
    PRIMARY KEY (creatureId, skillCode)
  );


  -- Bannon aspires float in Anoka with proficiency of 3
  INSERT INTO aspiration VALUES (1,'A',3,'a');
  -- Bannon aspires swim in Bemidji with proficiency of 4
  INSERT INTO aspiration VALUES (1,'E',4,'b');
  -- Bannon aspires gargling in Blue Earth with proficiency of 3
  INSERT INTO aspiration VALUES (1,'Z',3,'be');
  -- Myers aspires float with proficiency of 3
  INSERT INTO aspiration VALUES (2,'A',3,NULL);
  -- Neff #3 aspires float in Bemidji with proficiency of 8
  INSERT INTO aspiration VALUES (3,'A',8,'b');
  -- Neff #3 aspires gargling in Blue Earth with proficiency of 5
  INSERT INTO aspiration VALUES (3,'Z',5,'be');
  -- Neff #4 aspires swim in Greenville with proficiency of 3
  INSERT INTO aspiration VALUES (4,'E',3,'g');
  -- Mieska aspires gargling in Duluth with proficiency of
  INSERT INTO aspiration VALUES (5,'Z',10,'d');
  -- Carlis aspires gargling in London with proficiency of
  INSERT INTO aspiration VALUES (6,'Z',3,'le');
  -- Kermit aspires swim in Bemidji with proficiency of
  INSERT INTO aspiration VALUES (7,'E',3,'b');
  -- Godzilla aspires sink in Tokyo with proficiency of
  INSERT INTO aspiration VALUES (8,'O',4,'t');

  -- Beckham, Kane, and Rapinoe aspire to achieve PK at maxProficiency in London
  INSERT INTO aspiration VALUES (11,'PK',10,'le');
  INSERT INTO aspiration VALUES (12,'PK',10,'le');
  INSERT INTO aspiration VALUES (13,'PK',10,'le');
  -- Kermit aspires to achieve 2-person bobsledding at proficiency 20 in Duluth
  INSERT INTO aspiration VALUES (7,'B2',20,'d');
  -- Bannon and Mieska aspire to achieve 4x100 meter track relay at
  -- proficiency of 85 in Seattle, WA.
  INSERT INTO aspiration VALUES (1,'TR4',85,'sw');
  INSERT INTO aspiration VALUES (5,'TR4',85,'sw');

  -- Thor, Rapinoe, and Kermit form debate team in Seattle, WA and
  -- asppire to achieve at 80% of maxProficiency
  INSERT INTO aspiration VALUES (9,'D3',8,'sw');
  INSERT INTO aspiration VALUES (13,'D3',8,'sw');
  INSERT INTO aspiration VALUES (7,'D3',8,'sw');

  -- no 2-person canoeing achievements, but some have aspirations

  -- Carlis and Bannon aspire to achieve 2-person canoeing in Bemidji
  -- with proficiency of 9
  INSERT INTO aspiration VALUES (6,'C2',9,'b');
  INSERT INTO aspiration VALUES (1,'C2',9,'b');

  -- Thor, Elastigirl do not aspire to anything

  -- ------------------  role  -- -------------------------------
  DROP TABLE IF EXISTS role;
  CREATE TABLE role
  (
    roleName VARCHAR(20)   NOT NULL PRIMARY KEY
  );

  INSERT INTO role VALUES ('first leg');   -- 4x100 track
  INSERT INTO role VALUES ('second leg');  -- 4x100 track
  INSERT INTO role VALUES ('third leg');   -- 4x100 track
  INSERT INTO role VALUES ('anchor leg');  -- 4x100 track
  INSERT INTO role VALUES ('pilot');       -- 2-crew bobsled
  INSERT INTO role VALUES ('brakeman');    -- 2-crew bobsled
  INSERT INTO role VALUES ('right leg');   -- 3-legged race
  INSERT INTO role VALUES ('left leg');    -- 3-legged race
  INSERT INTO role VALUES ('stern paddler'); -- 2-person canoeing
  INSERT INTO role VALUES ('bow paddler');   -- 2-person canoeing
  INSERT INTO role VALUES ('first speaker'); -- Australasia debating
  INSERT INTO role VALUES ('second speaker');-- Australasia debating
  INSERT INTO role VALUES ('team captain');  -- Australasia debating


  -- ------------------  contribution  -- -------------------------------
  DROP TABLE IF EXISTS contribution;
  CREATE TABLE contribution (
      creatureId         INTEGER     NOT NULL REFERENCES creature(creatureId),
      achId              INTEGER     NOT NULL REFERENCES achievement(achId),
      skillCode          VARCHAR(3)  NOT NULL REFERENCES skill(skillCode),
      roleName           VARCHAR(20) REFERENCES role(roleName),
      PRIMARY KEY (creatureId, achId)
  );

  -- Thor (right leg) achieves three-legged race in Metroville (with Elastigirl (left leg))
  INSERT INTO contribution VALUES (9, 12, 'THR', 'right leg');
  INSERT INTO contribution VALUES (10, 13, 'THR', 'left leg');
  -- Kermit 'pilots' 2-crew bobsledding
  --       with Thor as brakeman
  INSERT INTO contribution VALUES (7, 14, 'B2', 'pilot');
  INSERT INTO contribution VALUES (9, 15, 'B2', 'brakeman');
  --
  -- keep track relay, have 4 people:
  --   Neff #4 (first leg), Mieska(second leg), Myers (third leg), Bannon (anchor leg)
  INSERT INTO contribution VALUES (4, 16, 'TR4', 'first leg');
  INSERT INTO contribution VALUES (5, 17, 'TR4', 'second leg');
  INSERT INTO contribution VALUES (2, 18, 'TR4', 'third leg');
  INSERT INTO contribution VALUES (1, 19, 'TR4', 'anchor leg');
  -- Thor (second speaker), Rapinoe (team captain), and Kermit (first speaker) form debate team
  INSERT INTO contribution VALUES (7, 22, 'D3', 'first speaker');
  INSERT INTO contribution VALUES (9, 20, 'D3', 'second speaker');
  INSERT INTO contribution VALUES (13, 21, 'D3', 'team captain');

  --
  -- no 2-person canoeing contributions, but some have aspirations


  -- ------------------  aspiredContribution  -- -------------------------------
  DROP TABLE IF EXISTS aspiredContribution;
  CREATE TABLE aspiredContribution (
      creatureId         INTEGER     NOT NULL REFERENCES creature(creatureId),
      skillCode          VARCHAR(3)  NOT NULL REFERENCES skill(skillCode),
      roleName           VARCHAR(20) REFERENCES role(roleName),
      PRIMARY KEY (creatureId, skillCode)
  );


  -- no 2-person canoeing contributions, but Carlis and Bannon have aspirations
  INSERT INTO aspiredContribution VALUES (6, 'C2', 'stern paddler');
  INSERT INTO aspiredContribution VALUES (1, 'C2', 'bow paddler');

  -- Bannon and Mieska aspire to contribute to achieve 4x100 meter track relay
  -- Bannon contributed in his aspired to role, Mieska had a different
  -- aspired to role than he ultimately contributed to
  INSERT INTO aspiredContribution VALUES (1, 'TR4', 'anchor leg');
  INSERT INTO aspiredContribution VALUES (5, 'TR4', 'third leg');

  -- Kermit aspires to contribute to piloting bobsled
  INSERT INTO aspiredContribution VALUES (7, 'B2', 'pilot');

  -- Thor, Rapinoe and Kermit aspire to contribute to debate
  INSERT INTO aspiredContribution VALUES (7, 'D3', 'first speaker');
  INSERT INTO aspiredContribution VALUES (9, 'D3', 'second speaker');
  INSERT INTO aspiredContribution VALUES (13, 'D3', 'team captain');

  -- Elastigirl, others not aspiring to contribute to anything