.. activecode:: skill_be_create
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 03TwoEntityShapes
   :subchapter: be-be_Shapes
   :topics: 03TwoEntityShapes/be-be_Shapes
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS skill;

   CREATE TABLE skill (
   skillCode          VARCHAR(3)      NOT NULL PRIMARY KEY,
   skillDescription   VARCHAR(20)
   );

   Drop TABLE IF EXISTS TeamSkill;

   CREATE TABLE teamSkill (
   skillCode      VARCHAR(3)  NOT NULL PRIMARY KEY references skill (skillCode),
   teamSize       INTEGER
   );

   INSERT INTO skill VALUES ('A', 'float');
   INSERT INTO skill VALUES ('E', 'swim');
   INSERT INTO skill VALUES ('O', 'sink');
   INSERT INTO skill VALUES ('U', 'walk on water');
   INSERT INTO skill VALUES ('Z', 'gargle');
   INSERT INTO skill VALUES ('B4', '4-person bobsledding');
   INSERT INTO skill VALUES ('TR4', '400 meter track relay');
   INSERT INTO skill VALUES ('C2', '2-person canoeing');
   INSERT INTO skill VALUES ('THR', 'three-legged race');
   INSERT INTO skill VALUES ('D3', 'debate');

   INSERT INTO teamSkill VALUES ('B4', 4);
   INSERT INTO teamSkill VALUES ('TR4', 4);
   INSERT INTO teamSkill VALUES ('C2', 2);
   INSERT INTO teamSkill VALUES ('THR', 2);
   INSERT INTO teamSkill VALUES ('D3', 3);

   -- show the team skills
   SELECT * from teamSkill;