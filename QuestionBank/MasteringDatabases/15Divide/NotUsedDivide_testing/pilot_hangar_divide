.. activecode:: pilot_hangar_divide
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: NotUsedDivide_testing
   :topics: 15Divide/NotUsedDivide_testing
   :from_source: T
   :language: sql
   :include: pilot_hangar_create

   -- A method made popular by C. Date in his textbooks
   SELECT DISTINCT pilot_name
   FROM PilotSkills AS PS1
   WHERE NOT EXISTS
       (SELECT *
          FROM Hangar
         WHERE NOT EXISTS
               (SELECT *
                  FROM PilotSkills AS PS2
                 WHERE (PS1.pilot_name = PS2.pilot_name)
                   AND (PS2.plane_name = Hangar.plane_name)));