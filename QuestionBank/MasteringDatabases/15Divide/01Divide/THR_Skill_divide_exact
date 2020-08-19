.. activecode:: THR_Skill_divide_exact
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create, THR_Skill

    SELECT IN1.creatureId
      FROM Achievement AS IN1
           LEFT OUTER JOIN
           ThreeLeggedRaceSkill AS P1
           ON IN1.skillCode = P1.skillCode
      GROUP BY IN1.creatureId
    HAVING COUNT(IN1.skillCode) =
            (SELECT COUNT(skillCode) FROM ThreeLeggedRaceSkill)
       AND COUNT(P1.skillCode) =
            (SELECT COUNT(skillCode) FROM ThreeLeggedRaceSkill);