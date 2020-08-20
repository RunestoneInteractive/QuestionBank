.. activecode:: cr_ach_skill_populate
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 04ThreeEntityShapes
  :subchapter: IntersectionShape
  :topics: 04ThreeEntityShapes/IntersectionShape
  :from_source: T
  :language: sql
  :include: cr_ach_skill_create

  INSERT INTO creature VALUES (1,'Bannon','person','Philly');
  INSERT INTO creature VALUES (3,'Neff','person','Blue Earth');
  INSERT INTO creature VALUES (5,'Mieska','person','Duluth');

  INSERT INTO skill VALUES ('A', 'float');
  INSERT INTO skill VALUES ('E', 'swim');
  INSERT INTO skill VALUES ('O', 'sink');
  INSERT INTO skill VALUES ('U', 'walk on water');
  INSERT INTO skill VALUES ('Z', 'gargle');

  INSERT INTO achievement VALUES (1, 'A', 1);
  INSERT INTO achievement VALUES (1, 'E', 3);
  INSERT INTO achievement VALUES (5, 'Z', 3);
  INSERT INTO achievement VALUES (3, 'Z', 1);

  -- display to screen
  SELECT *
  FROM creature natural join achievement natural join skill;