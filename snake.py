from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  segments = []

  def __init__(self,):
    self.segments = []
    self.create_snake()

  def create_snake(self):
    for pos in STARTING_POSITIONS:
      self.add_segment(pos)
    self.segments[0].color('purple')


  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
    self.segments[0].forward(MOVE_DISTANCE)

  def add_segment(self, position):
    tim = Turtle(shape='square')
    tim.color('white')
    tim.penup()
    tim.goto(position)
    self.segments.append(tim)

  def reset(self):
    for seg in self.segments:
      seg.goto(1000,1000)
    self.segments.clear()
    self.create_snake()

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def up(self):
    if self.segments[0].heading() != DOWN:
      self.segments[0].setheading(UP)

  def down(self):
    if self.segments[0].heading() != UP:
      self.segments[0].setheading(DOWN)

  def left(self):
    if self.segments[0].heading() != RIGHT:
      self.segments[0].setheading(LEFT)

  def right(self):
    if self.segments[0].heading() != LEFT:
      self.segments[0].setheading(RIGHT)
