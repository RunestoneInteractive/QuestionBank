.. actex:: SBlussenVraag4
   :author: Gilles Fiers
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F

   
   ~~~~
   import turtle
   wn = turtle.Screen()

   #Olga tekent een cirkel
   Olga = turtle.Turtle()
   Olga.penup()
   Olga.forward(150)
   Olga.left(90)
   Olga.pendown()
   Olga.circle(150)

   #Joe beweegt willekeurig
   Joe = turtle.Turtle()
   Joe.shape("turtle")