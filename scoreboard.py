import turtle

ALIGNMENT = 'center'
FONT = ('Arial','20','normal')

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0,y=250)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',False,align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.home()
    #     self.write('GAME OVER',False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()
        