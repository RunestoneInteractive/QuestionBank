.. activecode:: pilot_hangar_divide_exact
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: NotUsedDivide_testing
   :topics: 15Divide/NotUsedDivide_testing
   :from_source: T
   :language: sql
   :include: pilot_hangar_create

    SELECT PS1.pilot_name
      FROM PilotSkills AS PS1
           LEFT OUTER JOIN
           Hangar AS H1
           ON PS1.plane_name = H1.plane_name
      GROUP BY PS1.pilot_name
    HAVING COUNT(PS1.plane_name) = (SELECT COUNT(plane_name) FROM Hangar)
       AND COUNT(H1.plane_name) = (SELECT COUNT(plane_name) FROM Hangar);