.. activecode:: skill_create_group
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 04Group
   :topics: 09UnaryOps/04Group
   :from_source: T
   :language: sql

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