.. activecode:: gargling_category
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 17CategoryRelations
  :subchapter: 01CategoryRelations
  :topics: 17CategoryRelations/01CategoryRelations
  :from_source: T
  :language: sql
  :include: all_creature_create

  DROP TABLE IF EXISTS gargling_category;

  CREATE TABLE gargling_category (
  skillCode          VARCHAR(3)      NOT NULL,
  category           VARCHAR(20)     NOT NULL,
  lowProfVal         INTEGER         NOT NULL,
  highProfVal        INTEGER         NOT NULL
  );

  INSERT INTO gargling_category VALUES ('Z', 'poor', 0, 1);
  INSERT INTO gargling_category VALUES ('Z', 'fair', 2, 3);
  INSERT INTO gargling_category VALUES ('Z', 'good', 4, 5);