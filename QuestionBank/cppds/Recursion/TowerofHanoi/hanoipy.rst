.. activecode:: hanoipy
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: TowerofHanoi
   :topics: Recursion/TowerofHanoi
   :from_source: T
   :caption: Solving Tower of Hanoi Recursively Python
   :optional:

   #Simulation of the tower of hanoi.

   def moveTower(height,fromPole, toPole, withPole):
       if height >= 1:
           moveTower(height-1,fromPole,withPole,toPole) #Recursive call
           moveDisk(fromPole,toPole)
           moveTower(height-1,withPole,toPole,fromPole) #Recursive call

   def moveDisk(fp,tp):
       print("moving disk from",fp,"to",tp)

   def main():
       moveTower(3,"A","B","C")

   main()