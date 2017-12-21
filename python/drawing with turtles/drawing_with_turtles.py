import turtle

def turtle_drawing_triagle(tmnt):
  tmnt.forward(100)
  for turn in range(2):
    tmnt.left(120)
    tmnt.forward(100)

def turtle_drawing_square(tmnt, edge_length):
  for turn in range(4):
    tmnt.forward(edge_length)
    tmnt.right(90)

def turtle_drawing_circle(tmnt):
  tmnt.circle(100)

def turtles_drawing_polygons():
  window = turtle.Screen()
  window.bgcolor("black")

  leo = turtle.Turtle()
  leo.shape("turtle")
  leo.color("blue")
  leo.turtlesize(8, 9, 7)
  leo.speed(4)
  turtle_drawing_square(leo, 200)

  raph = turtle.Turtle()
  raph.shape("turtle")
  raph.color("red")
  raph.turtlesize(6, 7, 5)
  raph.speed(4)
  turtle_drawing_circle(raph)

  mikey = turtle.Turtle()
  mikey.shape("turtle")
  mikey.color("orange")
  mikey.turtlesize(4, 4, 4)
  mikey.speed(4)
  turtle_drawing_triagle(mikey)

  window.exitonclick()

turtles_drawing_polygons()
