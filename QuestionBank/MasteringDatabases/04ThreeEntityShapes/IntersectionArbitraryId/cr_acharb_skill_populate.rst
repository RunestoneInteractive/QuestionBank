.. activecode:: cr_acharb_skill_populate
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 04ThreeEntityShapes
  :subchapter: IntersectionArbitraryId
  :topics: 04ThreeEntityShapes/IntersectionArbitraryId
  :from_source: T
  :language: sql
  :include: cr_ach_arbid_skill_create

  INSERT INTO creature VALUES (1,'Bannon','person','Philly');
  INSERT INTO creature VALUES (3,'Neff','person','Blue Earth');
  INSERT INTO creature VALUES (5,'Mieska','person','Duluth');

  INSERT INTO skill VALUES ('A', 'float');
  INSERT INTO skill VALUES ('E', 'swim');
  INSERT INTO skill VALUES ('O', 'sink');
  INSERT INTO skill VALUES ('U', 'walk on water');
  INSERT INTO skill VALUES ('Z', 'gargle');

  INSERT INTO achievement (creatureId, skillCode, proficiency, achDate)
                  VALUES (1, 'A', 1, datetime('now'));
  INSERT INTO achievement (creatureId, skillCode, proficiency, achDate)
                  VALUES (1, 'E', 3, datetime('2019-09-15 15:35'));
  INSERT INTO achievement (creatureId, skillCode, proficiency, achDate)
                  VALUES (5, 'Z', 3, datetime('2019-09-15 15:42:30'));
  INSERT INTO achievement (creatureId, skillCode, proficiency, achDate)
                  VALUES (3, 'Z', 1, datetime('now', 'localtime'));

  -- display to screen
  SELECT *
  FROM creature natural join achievement natural join skill;