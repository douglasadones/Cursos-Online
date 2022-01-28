from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # esse atributo foi adicionado para simplificar a notação.

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        peace_of_body = Turtle("square")
        peace_of_body.color("white")
        peace_of_body.penup()
        peace_of_body.goto(position)
        self.segments.append(peace_of_body)

    def extend(self):
        # adiciona um novo segmento para a cobra na mesma posição do último segmento
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Isso vai garantir que se a cabeça for para um lado,
            new_x = self.segments[seg_num - 1].xcor()   # o corpo irá segui-la. Aqui o movimento da cobra foi invertido,
            new_y = self.segments[seg_num - 1].ycor()   # Fazendo com que o corpo anterior assuma a posição do seguinte.
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.seth(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.seth(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.seth(RIGHT)
