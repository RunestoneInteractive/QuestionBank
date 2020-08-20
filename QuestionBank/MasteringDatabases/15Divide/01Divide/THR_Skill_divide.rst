.. activecode:: THR_Skill_divide
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create, THR_Skill

  SELECT DISTINCT creatureId
  FROM Achievement AS IN1
  WHERE NOT EXISTS
      (SELECT *
         FROM ThreeLeggedRaceSkill
        WHERE NOT EXISTS
              (SELECT *
                 FROM Achievement AS IN2
                WHERE (IN1.creatureId = IN2.creatureId)
                  AND (IN2.skillCode = ThreeLeggedRaceSkill.skillCode)));