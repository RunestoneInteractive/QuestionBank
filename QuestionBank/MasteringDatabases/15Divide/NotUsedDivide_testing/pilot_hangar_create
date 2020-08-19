.. activecode:: pilot_hangar_create
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: NotUsedDivide_testing
   :topics: 15Divide/NotUsedDivide_testing
   :from_source: T
   :language: sql

    DROP TABLE IF EXISTS PilotSkills;

    CREATE TABLE PilotSkills
    (pilot_name CHAR(15) NOT NULL,
    plane_name CHAR(15) NOT NULL,
    PRIMARY KEY (pilot_name, plane_name));

    DROP TABLE IF EXISTS Hangar;
    CREATE TABLE Hangar
    (plane_name CHAR(15) NOT NULL PRIMARY KEY);

    INSERT INTO PilotSkills VALUES ('Celko',    'Piper Cub');
    INSERT INTO PilotSkills VALUES ('Higgins',  'B-52 Bomber');
    INSERT INTO PilotSkills VALUES ('Higgins',  'F-14 Fighter');
    INSERT INTO PilotSkills VALUES ('Higgins',  'Piper Cub');
    INSERT INTO PilotSkills VALUES ('Jones',    'B-52 Bomber');
    INSERT INTO PilotSkills VALUES ('Jones',    'F-14 Fighter');
    INSERT INTO PilotSkills VALUES ('Smith',    'B-1 Bomber');
    INSERT INTO PilotSkills VALUES ('Smith',    'B-52 Bomber');
    INSERT INTO PilotSkills VALUES ('Smith',    'F-14 Fighter');
    INSERT INTO PilotSkills VALUES ('Wilson',   'B-1 Bomber');
    INSERT INTO PilotSkills VALUES ('Wilson',   'B-52 Bomber');
    INSERT INTO PilotSkills VALUES ('Wilson',   'F-14 Fighter');
    INSERT INTO PilotSkills VALUES ('Wilson',   'F-17 Fighter');

    INSERT INTO Hangar VALUES ('B-1 Bomber');
    INSERT INTO Hangar VALUES ('B-52 Bomber');
    INSERT INTO Hangar VALUES ('F-14 Fighter');