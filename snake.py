import turtle
WEST = 180
EAST = 0
NORTH = 90
SOUTH = 270
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)
    
    
    def add_body(self,position):
        body_part = turtle.Turtle()
        body_part.shape('square')
        body_part.color('white')
        body_part.penup()
        body_part.goto(position)
        self.body.append(body_part)


    def extend(self):
        self.add_body(self.body[-1].position())


    def move(self):
        for i in range(len(self.body)-1,-1,-1):
            self.body[i].penup()
            if i == 0:
                self.body[i].forward(20)              
            else:
                self.body[i].goto(self.body[i-1].position())       
            #print(str(i),body[i].position())           


    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)


    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)


    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

            
    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def reset(self):
        for i in self.body:
            i.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]