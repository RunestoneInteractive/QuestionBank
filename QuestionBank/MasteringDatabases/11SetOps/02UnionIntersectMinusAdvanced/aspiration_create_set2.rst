.. activecode:: aspiration_create_set2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 11SetOps
   :subchapter: 02UnionIntersectMinusAdvanced
   :topics: 11SetOps/02UnionIntersectMinusAdvanced
   :from_source: T
   :language: sql

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