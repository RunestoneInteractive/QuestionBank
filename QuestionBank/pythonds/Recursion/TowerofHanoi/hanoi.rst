.. activecode:: hanoi
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: TowerofHanoi
    :topics: Recursion/TowerofHanoi
    :from_source: T
    :caption: Solving Tower of Hanoi Recursively

    def moveTower(height,fromPole, toPole, withPole):
        if height >= 1:
            moveTower(height-1,fromPole,withPole,toPole)
            moveDisk(fromPole,toPole)
            moveTower(height-1,withPole,toPole,fromPole)

    def moveDisk(fp,tp):
        print("moving disk from",fp,"to",tp)

    moveTower(3,"A","B","C")