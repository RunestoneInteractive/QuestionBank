.. activecode:: survivor_missing
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create, survivor_input, survivor_times

  --------------------------------------------------------
  -- The minus to get missing survivor skills
  --
  drop table if exists creatureId_skillCode_missing_cr_sur_skill;

  -- This is how we demonstrated minus before in the book, using 'except'
  --
  -- create table creatureId_skillCode_missing_cr_sur_skill as
  -- SELECT creatureId, skillCode
  -- FROM achievingCr_survivorSkill_pair
  -- EXCEPT
  -- SELECT creatureId, skillCode FROM crId_s_code_of_Achievement
  -- ;

  -- However, not all systems have except, and to help match the
  -- nested query example, let's see how we do a minus with NOT EXISTS
  --

  create table creatureId_skillCode_missing_cr_sur_skill as
  SELECT creatureId, skillCode
  FROM achievingCr_survivorSkill_pair A
  WHERE NOT EXISTS (
    SELECT creatureId, skillCode
    FROM crId_s_code_of_Achievement B
    WHERE A.creatureId = B.creatureId
          and A.skillCode = B.skillCode
  )
  ;