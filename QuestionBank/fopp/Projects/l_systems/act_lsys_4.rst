.. actex:: act_lsys_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: l_systems
    :topics: Projects/l_systems
    :from_source: T
    :nocodelens:

    Here are the rules for an L-system that creates something that resembles
    a common garden herb.  Implement the following rules and try it.  Use an
    angle of 25.7 degrees.

    ::

        H
        H --> HFX[+H][-H]
        X --> X[-FFF][+FFF]FX
    ~~~~